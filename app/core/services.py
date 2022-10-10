import requests
import json
import os
from fastapi import HTTPException

from app.core import config
from agristamp_common.utils.logs import logger
from agristamp_common.utils.const import TIMEOUT_ERROR
from app.errors.exceptions import ErroSeguradoraParser


def get_climate_fieldview_token():
    auth_url = f"{config.CLIMATE_FIELDVIEW_AUTH_URL}"
    payload = {'username': f'{config.CLIMATE_FIELDVIEW_API_USER_EMAIL}',
               'password': f'{config.CLIMATE_FIELDVIEW_API_USER_PASSWORD}',
               'rememberMe': 'true'}

    headers = {'Content-Type': 'application/json'}

    response = requests.request(
        "POST", auth_url, headers=headers, json=payload)

    response_token = response.headers['Authorization']

    # se o token atual for diferente do ambiente, ele é atualizado
    if(response_token != config.CLIMATE_FIELDVIEW_TOKEN):
        # remove variavel de ambiente
        os.unsetenv('CLIMATE_FIELDVIEW_TOKEN')

        # recria a variavel com o novo token
        os.environ['CLIMATE_FIELDVIEW_TOKEN'] = response.headers['Authorization']


def climate_fieldview_auth():
    get_climate_fieldview_token()
    headers = {
        'Content-Type': 'application/json;charset=UTF-8',
        'Authorization': str(config.CLIMATE_FIELDVIEW_TOKEN)
    }

    return headers


async def climate_fieldview_get(endpoint, params: dict = {}, ):

    headers = climate_fieldview_auth()

    endpoint_url = f"{config.CLIMATE_FIELDVIEW_API_URL}{endpoint}"

    try:
        climate_fieldview_request = requests.get(
            url=endpoint_url, params=params, headers=headers, timeout=config.CLIMATE_FIELDVIEW_TIMEOUT)

    except requests.exceptions.ReadTimeout:
        logger.error(f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}',
                     extra={'data': params, 'error_type': TIMEOUT_ERROR})
        raise HTTPException(
            500, f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}')

    # Log
    logger.info(f'Disparado GET {endpoint_url}', extra={
                'data': json.dumps(params), })

    if climate_fieldview_request.status_code == 200:
        logger.info(f'RESPONSE GET {endpoint_url}', extra={
                    'data': climate_fieldview_request.json(), })
        if not 'error' in climate_fieldview_request.json():
            return climate_fieldview_request.json()
        else:
            raise HTTPException(500, climate_fieldview_request.text)
    else:
        logger.info(f'RESPONSE GET {endpoint_url}', extra={
                    'data': climate_fieldview_request.text, })
        await climate_fieldview_error_messages(climate_fieldview_request)


def climate_fieldview_post(payload, endpoint):

    headers = climate_fieldview_auth()

    endpoint_url = f"{config.CLIMATE_FIELDVIEW_API_URL}{endpoint}"

    try:
        climate_fieldview_request = requests.post(url=endpoint_url, data=json.dumps(
            payload), headers=headers, timeout=config.CLIMATE_FIELDVIEW_TIMEOUT)

    except requests.exceptions.ReadTimeout:
        logger.error(f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}',
                     extra={'data': payload, 'error_type': TIMEOUT_ERROR})
        raise HTTPException(
            500, f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}')

    # Log
    logger.info(f'Disparado POST {endpoint_url}', extra={
                'data': payload, })

    if climate_fieldview_request.status_code in [200, 201]:
        logger.info(f'RESPONSE POST {endpoint_url}', extra={
                    'data': climate_fieldview_request.json(), })
        if not 'error' in climate_fieldview_request.json():
            return climate_fieldview_request.json()
        else:
            raise HTTPException(500, climate_fieldview_request.text)
    else:
        logger.info(f'RESPONSE POST {endpoint_url}', extra={
                    'data': climate_fieldview_request.text, })
        climate_fieldview_error_messages(climate_fieldview_request)


def climate_fieldview_put(payload, endpoint, id):
    headers = climate_fieldview_auth()

    endpoint_url = f"{config.CLIMATE_FIELDVIEW_API_URL}{endpoint}{id}"

    try:
        climate_fieldview_request = requests.put(url=endpoint_url, data=json.dumps(
            payload), headers=headers, timeout=config.CLIMATE_FIELDVIEW_TIMEOUT)

    except requests.exceptions.ReadTimeout:
        logger.error(f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}',
                     extra={'data': payload, 'error_type': TIMEOUT_ERROR})
        raise HTTPException(
            500, f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}')

    # Log
    logger.info(f'Disparado PUT {endpoint_url}', extra={
                'data': payload, })

    if climate_fieldview_request.status_code in [200, 201]:
        logger.info(f'RESPONSE PUT {endpoint_url}', extra={
                    'data': climate_fieldview_request.json(), })
        if not 'error' in climate_fieldview_request.json():
            return climate_fieldview_request.json()
        else:
            raise HTTPException(500, climate_fieldview_request.text)
    else:
        logger.info(f'RESPONSE PUT {endpoint_url}', extra={
                    'data': climate_fieldview_request.text, })
        climate_fieldview_error_messages(climate_fieldview_request)


def climate_fieldview_patch(payload, endpoint, id):
    headers = climate_fieldview_auth()

    endpoint_url = f"{config.CLIMATE_FIELDVIEW_API_URL}{endpoint}{id}"

    try:
        climate_fieldview_request = requests.patch(url=endpoint_url, data=json.dumps(
            payload), headers=headers, timeout=config.CLIMATE_FIELDVIEW_TIMEOUT)

    except requests.exceptions.ReadTimeout:
        logger.error(f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}',
                     extra={'data': payload, 'error_type': TIMEOUT_ERROR})
        raise HTTPException(
            500, f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}')

    # Log
    logger.info(f'Disparado PATCH {endpoint_url}', extra={
                'data': payload, })

    if climate_fieldview_request.status_code in [200, 201]:
        logger.info(f'RESPONSE PATCH {endpoint_url}', extra={
                    'data': climate_fieldview_request.json(), })
        if not 'error' in climate_fieldview_request.json():
            return climate_fieldview_request.json()
        else:
            raise HTTPException(500, climate_fieldview_request.text)
    else:
        logger.info(f'RESPONSE PATCH {endpoint_url}', extra={
                    'data': climate_fieldview_request.text, })
        climate_fieldview_error_messages(climate_fieldview_request)


def climate_fieldview_delete(endpoint, id):
    headers = climate_fieldview_auth()

    endpoint_url = f"{config.CLIMATE_FIELDVIEW_API_URL}{endpoint}{id}"

    try:
        climate_fieldview_request = requests.delete(
            url=endpoint_url, headers=headers, timeout=config.CLIMATE_FIELDVIEW_TIMEOUT)

    except requests.exceptions.ReadTimeout:
        logger.error(f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}',
                     extra={'error_type': TIMEOUT_ERROR})
        raise HTTPException(
            500, f'Timeout {config.CLIMATE_FIELDVIEW_TIMEOUT} ao enviar para API da Climate_Fieldview {endpoint_url}')

    if climate_fieldview_request.status_code == 200:
        logger.info(f'RESPONSE DELETE {endpoint_url}', extra={
                    'data': climate_fieldview_request.json(), })
        if not 'error' in climate_fieldview_request.json():
            return climate_fieldview_request.json()
        else:
            raise HTTPException(500, climate_fieldview_request.text)
    else:
        logger.info(f'RESPONSE DELETE {endpoint_url}', extra={
                    'data': climate_fieldview_request.text, })
        climate_fieldview_error_messages(climate_fieldview_request)


def climate_fieldview_error_messages(climate_fieldview_request):

    error_response = climate_fieldview_request.json()

    if 'violations' in error_response:

        violations_messages = []
        for _, key in enumerate(error_response['violations']):
            violation = error_response['violations'][key]
            violations_messages.append(violation)

        parsed_error = ErroSeguradoraParser(violations_messages)
        raise HTTPException(parsed_error.code,
                            parsed_error.errors, parsed_error.error_code)

    else:

        if 'message' in error_response:
            parsed_error = ErroSeguradoraParser(error_response['message'])
            raise HTTPException(parsed_error.code,
                                parsed_error.errors, parsed_error.error_code)

        else:
            raise HTTPException(
                climate_fieldview_request.status_code, climate_fieldview_request.text)
