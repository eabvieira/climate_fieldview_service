#!/usr/bin/env python3
import os
from slugify import slugify
import asyncio

from agristamp_common.utils.services import service_get, service_post
from app.db.mongo import dominios_collection
from app.scripts.utils import get_culturas_climate_fieldview


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_MODALIDADES = 'modalidades'
DOMAIN_MODALIDADES_CULTURA = 'modalidades_cultura'


async def main():

    def get_cultura_modalidades_climate_fieldview(cultura_id):
        print(
            f'Obtendo modalidades na API da Climate_Fieldview [cultura {cultura_id}]')

        params = {'codigo_cultura': cultura_id}

        modalidades_response = service_get(
            'climate_fieldview_service', 'v1/cultura/modalidades', headers=HEADERS, query=params)

        if modalidades_response.status_code == 200:

            # Adiciona o id da cultura no retorno
            modalidades_payload = modalidades_response.json()
            for index, _ in enumerate(modalidades_payload):
                modalidades_payload[index].update({"cultura_id": cultura_id})

            return modalidades_payload
        else:
            return None

    def parse_modalidades(json_payload):
        print(f'Parse das modalidades {json_payload}')

        # modalidades
        # Filtra todas as modalidades
        documents_modalidades = []
        for item in json_payload:
            for modalidade in item:
                if modalidade not in documents_modalidades:
                    documents_modalidades.append(modalidade)

        documents = []
        for modalidade in item:

            documents.append({
                "dominio": DOMAIN_MODALIDADES,
                "internal_id": 0,
                "integration_id": modalidade['codigo'],
                "slug": slugify(modalidade['descricao']),
                "label": modalidade['descricao']
            })

        return documents

    def parse_modalidades_x_culturas(json_payload):

        # modalidades_x_cultura
        documents = []
        for item in json_payload:

            if item:
                for modalidade in item:

                    documents.append({
                        "dominio": DOMAIN_MODALIDADES_CULTURA,
                        "internal_id": 0,
                        "integration_id": modalidade['codigo'],
                        "slug": slugify(modalidade['descricao']),
                        "cultura_id": modalidade['cultura_id'],
                        "label": modalidade['descricao']
                    })
        return documents

    async def update_mongo_db(documents, dominio):
        print(f'Atualizado no Mongo')

        # Limpa base
        await dominios_collection.delete_many({'dominio': dominio})

        # Adiciona os novos
        adicionados = await dominios_collection.insert_many(documents)

        return adicionados

    # Fluxo
    culturas_payload = get_culturas_climate_fieldview()

    culturas_ids = [cultura['codigo'] for cultura in culturas_payload]

    if culturas_ids:

        culturas_modalidades_payload = [get_cultura_modalidades_climate_fieldview(cultura_id)
                                        for cultura_id in culturas_ids]

        # Atualiza opcoes de modalidades
        documents = parse_modalidades(culturas_modalidades_payload)

        if documents:
            novas_modalidades = await update_mongo_db(documents, DOMAIN_MODALIDADES)
        else:
            print("Sem documentos a atualizar")

        # Atualiza modalidades x culturas
        documents = parse_modalidades_x_culturas(culturas_modalidades_payload)

        if documents:
            novas_modalidades = await update_mongo_db(documents, DOMAIN_MODALIDADES_CULTURA)
        else:
            print("Sem documentos a atualizar")


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
