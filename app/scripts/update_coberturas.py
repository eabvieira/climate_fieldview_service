#!/usr/bin/env python3
import os
import json
from datetime import datetime
from slugify import slugify
import asyncio

from app.db.mongo import dominios_collection
from app.scripts.utils import get_culturas_climate_fieldview
from agristamp_common.utils.services import service_post


HEADERS = {'Authorization': f"Bearer {os.getenv('AGRISTAMP_KEY')}"}
DOMAIN_NAME = 'coberturas'

async def main():


    async def get_culturas_climate_fieldview():

        culturas = await dominios_collection.find({'dominio': 'culturas'}, {"_id": 0}).to_list(None)

        return culturas


    def get_cotacao_auxiliar(cultura_slug, cultura_id_climate_fieldview):

        ceps_default_dict = {
            'soja': '19800001',
            'milho': '19800001',
            'milho-safrinha': '19800001',
            'sorgo-inverno': '75980000',
            'trigo-multirisco': '83750000'
        }

        try:
            cep_default = ceps_default_dict[cultura_slug]

        except KeyError as ke:
            print(f'Cultura sem cep default: {cultura_slug}')
            return None


        data_hoje = datetime.now().strftime('%d/%m/%Y')

        payload = {
            "codigo_produto": 103,
            "codigo_cultura": cultura_id_climate_fieldview,
            "codigo_modalidade": 95,
            "cep_propriedade": cep_default,
            "subvencao_sp": False,
            "subvencao_federal": False,
            "data_cotacao": data_hoje,
            "id_forma_regulacao_sinistro": 1
        }

        request_cotacao_auxiliar = service_post('climate_fieldview_service', 'v1/cotacao_auxiliar', HEADERS, json.dumps(payload))

        if request_cotacao_auxiliar.status_code == 200:
            cotacao_auxiliar = request_cotacao_auxiliar.json()

            return cotacao_auxiliar

        else:

            return None


    def parse_dominios(cotacao_auxiliar, cultura_slug):

        documents = []
        for cobertura in cotacao_auxiliar['coberturas']:

            documents.append(
                {
                    "dominio": DOMAIN_NAME,
                    "internal_id": 0,
                    "integration_id": int(cobertura['codigo']),
                    "slug": slugify(cobertura['descricao']),
                    "label": cobertura['descricao'],
                    "cultura_slug": cultura_slug
                }
            )

        return documents


    async def update_mongo_db(documents, cultura_slug):
        print(f'Atualizado no Mongo: {documents}')

        # Limpa base
        await dominios_collection.delete_many({'dominio': DOMAIN_NAME, 'cultura_slug': cultura_slug})

        # Adiciona os novos
        adicionados = await dominios_collection.insert_many(documents)

        return adicionados

    # Fluxo
    culturas = await get_culturas_climate_fieldview()
    for cultura in culturas:
        cotacao_auxiliar = get_cotacao_auxiliar(cultura['slug'], cultura['integration_id'])

        if cotacao_auxiliar:
            documents = parse_dominios(cotacao_auxiliar, cultura['slug'])
            novos_dominios = await update_mongo_db(documents, cultura['slug'])


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
