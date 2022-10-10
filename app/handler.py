import asyncio
from app.main import api_gateway_handler
from app.sqs_handler import sqs_handler

print('Loading function')

def lambda_handler(event, context):

    if 'requestContext' in event:
        print('Chamando via API GATEWAY')
        return api_gateway_handler(event, context)

    elif 'Records' in event:
        print('Chamando via SQS')
        return sqs_handler(event, context)
