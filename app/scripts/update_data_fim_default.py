#!/usr/bin/env python3
import os
from slugify import slugify
import asyncio

from app.db.mongo import dominios_collection
from app.scripts.utils import get_culturas_climate_fieldview


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_NAME = 'data_prevista_fim_default'

async def main():



    # cotacao_auxiliar
    #data_limite_prevista_fim_colheita

    def parse_dominios():

        documents = [
            {
                "dominio": "data_prevista_fim_default",
                "internal_id": 0,
                "integration_id": 1,
                "slug": "soja",
                "label": "Soja",
                "default": "30/04/2022"
            },
            {
                "dominio": "data_prevista_fim_default",
                "internal_id": 0,
                "integration_id": 1,
                "slug": "milho-safrinha",
                "label": "Milho Safrinha",
                "default": "30/10/2022"
            },
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
