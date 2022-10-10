#!/usr/bin/env python3
import os
from slugify import slugify
import asyncio

from app.db.mongo import dominios_collection
from app.scripts.utils import get_culturas_climate_fieldview


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_NAME = 'tipos_solo'

async def main():


    def parse_dominios():

        documents = [
            {
                "dominio": "tipos_solo",
                "internal_id": 0,
                "integration_id": 1,
                "slug": "tipo-1",
                "label": "Tipo 1"
            },
            {
                "dominio": "tipos_solo",
                "internal_id": 0,
                "integration_id": 2,
                "slug": "tipo-2",
                "label": "Tipo 2"
            },
            {
                "dominio": "tipos_solo",
                "internal_id": 0,
                "integration_id": 3,
                "slug": "tipo-3",
                "label": "Tipo 3"
            }
        ]

        return documents

    async def update_mongo_db(documents):
        print(f'Atualizado no Mongo')

        # Limpa base
        await dominios_collection.delete_many({'dominio': DOMAIN_NAME})

        # Adiciona os novos
        adicionados = await dominios_collection.insert_many(documents)

        return adicionados

    # Fluxo
    documents = parse_dominios()

    novos_dominios = await update_mongo_db(documents)


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
