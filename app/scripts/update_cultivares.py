#!/usr/bin/env python3
import os
import json
from slugify import slugify
import asyncio

from agristamp_common.utils.services import service_post
from app.db.mongo import dominios_collection
from app.scripts.utils import LISTA_UFS


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_CULTIVARES = 'cultivares'
CULTURAS_HABILITADAS = ['soja',
                        'milho-safrinha',
                        'milho-braquiaria',
                        'sorgo-inverno',
                        'trigo-multirisco']  # TODO pegar da conf


async def main():

    async def get_culturas_climate_fieldview():

        culturas = await dominios_collection.find({'dominio': 'culturas'}, {"_id": 0}).to_list(None)

        return culturas

    def get_cultivares_climate_fieldview(cultura_id, uf, cultura_slug):

        if cultura_slug not in CULTURAS_HABILITADAS:
            return None

        print(
            f'Obtendo cultivares na API da Climate_Fieldview [cultura {cultura_id} - {cultura_slug} | {uf}]')

        params = {'codigo_cultura': cultura_id, 'uf': uf.upper()}

        cultivares_response = service_post(
            'climate_fieldview_service', 'v1/cultivares', headers=HEADERS, payload=json.dumps(params))

        if cultivares_response.status_code == 200:

            # Adiciona o id da cultura no retorno
            cultivares_payload = cultivares_response.json()
            for index, _ in enumerate(cultivares_payload):
                cultivares_payload[index].update({"cultura_id": cultura_id,
                                                  "cultura_slug": cultura_slug,
                                                  })

            return cultivares_payload
        else:
            return None

    def parse_cultivares(json_payload):

        def _int_to_roman(int_value):

            roman_values = {
                0: '0',
                1: 'I',
                2: 'II',
                3: 'III',
                4: 'IV',
                5: 'V',
                6: 'VI'
            }

            return roman_values[int_value]

        documents = []
        for item in json_payload:

            if item:
                list_uf = set()
                for estado in item:
                    if estado:
                        for cultivar in estado:

                            grupo_roman = _int_to_roman(
                                cultivar['grupo_cultivar'])

                            if (cultivar) and (slugify(cultivar['descricao']) != 'nao-informado'):
                                document = {
                                    "dominio": DOMAIN_CULTIVARES,
                                    "internal_id": 0,
                                    "integration_id": cultivar['codigo'],
                                    "slug": slugify(cultivar['descricao']),
                                    "label": cultivar['descricao'].strip(),
                                    "fabricante": cultivar['fabricante'].strip() if cultivar['fabricante'] else '',
                                    "grupo_id": cultivar['grupo_cultivar'],
                                    "grupo_label": f'GRUPO {grupo_roman}',
                                    "cultura_id": cultivar['cultura_id'],
                                    "cultura_slug": cultivar['cultura_slug'],
                                    "uf_slug": cultivar['uf'].lower(),
                                }

                                # Adiciona um cultivar default por estado/uf
                                if cultivar['uf'] not in list_uf:
                                    document_default = document.copy()
                                    document_default["dominio"] = f'{DOMAIN_CULTIVARES}_defaults'
                                    documents.append(document_default)
                                    list_uf.add(cultivar['uf'])

                                documents.append(document)
        return documents

    async def update_mongo_db(documents, dominio):
        print(f'Atualizado no Mongo')

        # Limpa base
        await dominios_collection.delete_many({'dominio': dominio})
        await dominios_collection.delete_many({'dominio': f'{dominio}_defaults'})

        # Adiciona os novos
        adicionados = await dominios_collection.insert_many(documents)

        return adicionados

    # Fluxo
    culturas_payload = await get_culturas_climate_fieldview()

    cultivares_payload = []
    for uf in LISTA_UFS:

        cultivares_payload.append([get_cultivares_climate_fieldview(cultura['integration_id'], uf, slugify(cultura['slug']))
                                   for cultura in culturas_payload])

    # Atualiza modalidades x culturas
    documents = parse_cultivares(cultivares_payload)

    if documents:
        novos_cultivares = await update_mongo_db(documents, DOMAIN_CULTIVARES)
    else:
        print("Sem documentos a atualizar")


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
