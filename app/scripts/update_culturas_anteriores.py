#!/usr/bin/env python3
import os
from slugify import slugify
import asyncio

from app.db.mongo import dominios_collection
from app.core.config import CLIMATE_FIELDVIEW_CODIGO_PRODUTO

from agristamp_common.utils.services import service_get


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_NAME = 'cultura_anterior'
CULTURAS_HABILITADAS = ['soja',
                        'milho-safrinha',
                        'milho-braquiaria',
                        'trigo-multirisco',
                        'sorgo-inverno']  # TODO pegar da conf


async def main():

    async def get_culturas_climate_fieldview_mongo():

        culturas = await dominios_collection.find({'dominio': 'culturas'}, {"_id": 0}).to_list(None)

        return culturas

    def get_cultura_modalidades_climate_fieldview(cultura_id, cultura_slug):

        if cultura_slug not in CULTURAS_HABILITADAS:
            return None

        print(
            f'Obtendo modalidades na API da Climate_Fieldview [cultura {cultura_id}]')

        params = {'codigo_cultura': cultura_id}

        modalidades_response = service_get(
            'climate_fieldview_service', 'v1/cultura/modalidades', headers=HEADERS, query=params)

        if modalidades_response.status_code == 200:

            # Adiciona o id da cultura no retorno
            modalidades_payload = modalidades_response.json()
            for index, _ in enumerate(modalidades_payload):
                modalidades_payload[index].update({"cultura_id": cultura_id,
                                                  "cultura_slug": cultura_slug,
                                                   })

            return modalidades_payload
        else:
            return None

    def get_culturas_anteriores(cultura_id, modalidade_id, cultura_slug, modalidade_slug, codigo_produto_climate_fieldview):

        if cultura_slug not in CULTURAS_HABILITADAS:
            return None

        print(
            f'Obtendo culturas anteriores da API da Climate_Fieldview [cultura {cultura_id} - {cultura_slug} - {modalidade_id}]')

        params = {
            "codigo_produto": codigo_produto_climate_fieldview,
            "cultura": cultura_id,
            "modalidade": modalidade_id
        }

        anteriores_response = service_get(
            'climate_fieldview_service', 'v1/culturas_anteriores', headers=HEADERS, query=params)

        if anteriores_response.status_code == 200:

            # Adiciona o id da cultura no retorno
            anteriores_payload = anteriores_response.json()
            for index, _ in enumerate(anteriores_payload):
                anteriores_payload[index].update({"cultura_id": cultura_id,
                                                  "cultura_slug": cultura_slug,
                                                  "modalidade_id": modalidade_id,
                                                  "modalidade_slug": modalidade_slug
                                                  })

            return anteriores_payload
        else:
            return None

    def parse_culturas_anteriores(json_payload):
        print(f'Parse das culturas anteriores{json_payload}')

        documents = []
        for item in json_payload:

            if item:
                for cultura in item:

                    documents.append({
                        "dominio": DOMAIN_NAME,
                        "internal_id": 0,
                        "integration_id": cultura['codigo'],
                        "slug": slugify(cultura['descricao']),
                        "label": cultura['descricao'],
                        "cultura_id": cultura['cultura_id'],
                        "cultura_slug": cultura['cultura_slug'],
                        "modalidade_id": cultura['modalidade_id'],
                        "modalidade_slug": cultura['modalidade_slug'],
                    })

        return documents

    async def update_mongo_db(documents):
        print(f'Atualizado no Mongo')

        # Limpa base
        await dominios_collection.delete_many({'dominio': DOMAIN_NAME})

        # Adiciona os novos
        adicionados = await dominios_collection.insert_many(documents)

        return adicionados

    # Fluxo
    culturas_payload = await get_culturas_climate_fieldview_mongo()
    codigo_produto_climate_fieldview = CLIMATE_FIELDVIEW_CODIGO_PRODUTO

    if culturas_payload:

        # busca as modalidades das culturas
        modalidades = [get_cultura_modalidades_climate_fieldview(
            cultura['integration_id'], cultura['slug']) for cultura in culturas_payload]

        culturas_anteriores = []
        for item in modalidades:

            # Busca as culturas anteriores
            if item:
                for cultura in item:
                    culturas_anteriores.append(get_culturas_anteriores(cultura['cultura_id'],
                                                                       cultura['codigo'],
                                                                       cultura['cultura_slug'],
                                                                       slugify(
                                                                           cultura['descricao']),
                                                                       codigo_produto_climate_fieldview,
                                                                       )
                                               )

        documents = parse_culturas_anteriores(culturas_anteriores)

        novas_culturas_anteriores = await update_mongo_db(documents)


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
