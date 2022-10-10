#!/usr/bin/env python3
import asyncio

from app.db.mongo import error_codes_collection


DOMAIN_NAME = "error_codes"

async def main():


    async def parse_error_codes():

        documents = []

        """error_dict = Dicionario para tradução de erros seguradora -> agristamp
        formato:
            error_dict = {
                '<Trecho da string original da seguradora>': (<codigo numerico unico>, <Mensagem a exibir no sistema>)
            }

        """
        error_dict = {
            'Cultura atingiu o limite máximo de contratação': (10, 'Limite máximo de contratações pra Cultura/Município atingido'),
            'Valor ultrapassou o máximo estabelecido para LMR': (11, 'Valor ultrapassou o máximo estabelecido para a seguradora'),
            'Foram encontradas restrições para este CPF/CNPJ': (12, 'Seguradora informou restrições referentes ao CPF/CNPJ informado'),
            'Nome/Razão Social inválido, informar nome completo': (13, 'Revise Nome e Sobrenome do segurado')
        }

        for index, key in enumerate(error_dict):
            documents.append({
                "dominio": DOMAIN_NAME,
                "error_code": error_dict.get(key)[0],
                "original_message": key,
                "label": error_dict.get(key)[1],
            })

        return documents

    async def update_mongo_db(documents):
        print(f'Atualizado no Mongo')

        # Limpa base
        await error_codes_collection.delete_many({'dominio': DOMAIN_NAME})

        # Adiciona os novos
        adicionados = await error_codes_collection.insert_many(documents)

        return adicionados

    # Fluxo
    documents = await parse_error_codes()

    novos_dominios = await update_mongo_db(documents)


loop = asyncio.get_event_loop()
forecast = loop.run_until_complete(main())
loop.close()
