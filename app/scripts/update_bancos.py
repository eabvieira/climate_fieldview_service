#!/usr/bin/env python3
import os
from slugify import slugify
import asyncio

from app.db.mongo import dominios_collection
from agristamp_common.utils.services import service_get


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_NAME = 'bancos'


async def main():

    def get_bancos():

        print('Obtendo bancos na API da Climate_Fieldview')

        bancos_response = service_get(
            'climate_fieldview_service', 'v1/bancos', headers=HEADERS)

        return bancos_response

    def parse_bancos(json_payload):
        print(f'Parse dos bancos {json_payload}')

        documents = []
        for item in json_payload:

            documents.append({
                "dominio": DOMAIN_NAME,
                "internal_id": 0,
                "integration_id": int(item['codigo']),
                "slug": slugify(item['descricao']),
                "label": item['descricao'],
                "forma_pagamento_id": item['forma_pagamento']
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
    bancos_payload = get_bancos()

    documents = parse_bancos(bancos_payload.json())

    novas_culturas = await update_mongo_db(documents)


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
