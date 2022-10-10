#!/usr/bin/env python3
import os
from slugify import slugify
import asyncio

from app.db.mongo import dominios_collection
from app.scripts.utils import get_culturas_climate_fieldview



HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_NAME = 'culturas'

async def main():


    def parse_culturas(json_payload):
        print(f'Parse das culturas {json_payload}')

        culturas_agristamp_dict = {
            'milho-1a-safra': 'milho',
            'milho-2a-safra': 'milho-safrinha',
            'trigo': 'trigo-multirisco'
        }

        documents = []
        for item in json_payload:

            cultura_slug = slugify(item['descricao'])

            if cultura_slug in culturas_agristamp_dict:
                cultura_slug = culturas_agristamp_dict[cultura_slug]

            documents.append({
                "dominio": DOMAIN_NAME,
                "internal_id": 0,
                "integration_id": item['codigo'],
                "slug": cultura_slug,
                "label": item['descricao']
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
    culturas_payload = get_culturas_climate_fieldview()

    if culturas_payload:
        documents = parse_culturas(culturas_payload)

        novas_culturas = await update_mongo_db(documents)


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
