import boto3
import debugpy
import logging
import json
from app.core.config import (QUEUE_URL_PROPOSTAS_PUB_SERVICE,
                             DEV,
                             AWS_DEFAULT_REGION,
                             AWS_ACCESS_KEY_ID,
                             AWS_SECRET_ACCESS_KEY
                             )


def set_trace():
    debugpy.listen(("0.0.0.0", 5678))


def trueround(number, places=0, rounding=None):
    from decimal import Decimal as dec
    from decimal import ROUND_HALF_UP
    from decimal import ROUND_CEILING
    from decimal import ROUND_DOWN
    from decimal import ROUND_FLOOR
    from decimal import ROUND_HALF_DOWN
    from decimal import ROUND_HALF_EVEN
    from decimal import ROUND_UP
    from decimal import ROUND_05UP
    original = number
    if type(number) == type(float()):
        number = str(number)
    if rounding == None:
        rounding = ROUND_HALF_UP
    place = '1.'
    for i in range(places):
        place = ''.join([place, '0'])
    number = float(dec(number).quantize(dec(place), rounding=rounding))
    print("trueround: {} -> {}".format(original, number))
    return number


log = logging.getLogger()


def sqs_send(payload):

    queue_url = QUEUE_URL_PROPOSTAS_PUB_SERVICE

    def sqs_send_prod(payload):

        client = boto3.client(service_name='sqs',
                              region_name=AWS_DEFAULT_REGION,
                              aws_access_key_id=AWS_ACCESS_KEY_ID,
                              aws_secret_access_key=AWS_SECRET_ACCESS_KEY,
                              endpoint_url=queue_url)

        result = client.send_message(QueueUrl=queue_url,
                                     MessageBody=json.dumps(payload))

        return result

    def sqs_send_dev(payload):

        def send_rabbitmq(payload):

            import pika

            connection = pika.BlockingConnection(
                pika.ConnectionParameters(host='172.17.0.1'))
            channel = connection.channel()

            channel.queue_declare(queue=queue_url)

            channel.basic_publish(
                exchange='', routing_key=queue_url, body=json.dumps(payload))
            print(f" [x] Sent: {payload}")
            connection.close()

        lambda_trigger_payload = {
            "Records": [
                {
                    "MessageId": "dev-19dd0b57-b21e-4ac1-bd88-01bbb068cb78",
                    "receiptHandle": "MessageReceiptHandle",
                    "body": payload,
                    "attributes": {
                        "ApproximateReceiveCount": "1",
                        "SentTimestamp": "1523232000000",
                        "SenderId": "123456789012",
                        "ApproximateFirstReceiveTimestamp": "1523232000001"
                    },
                    "messageAttributes": {},
                    "md5OfBody": "{{{md5_of_body}}}",
                    "eventSource": "aws:sqs",
                    "eventSourceARN": "arn:aws:sqs:us-east-1:123456789012:MyQueue",
                    "awsRegion": "us-east-1"
                }
            ]
        }

        # Chama o propostas_sub async
        send_rabbitmq(lambda_trigger_payload)
        return {'MessageId': 'Send via RabbitMQ'}

    # Trata envio de fila em dev(rabbitMQ) e prod(AWS Sqs)
    if (DEV == '1') or (DEV == 1):
        print('Enviando proposta via RabbitMQ (DEV)')
        return sqs_send_dev(payload)
    else:
        print(f'Enviando proposta via SQS - [{queue_url}]')
        return sqs_send_prod(payload)


def send_status_sqs(new_status, status_detail, mongo_id, environment):
    sqs_payload = {
        "slug": 'climate_fieldview',
        "_id": mongo_id,
        "type": "status",
        "payload": status_detail,
        "new_status": new_status,
        "environment": environment
    }

    sqs_result = sqs_send(sqs_payload)

    return sqs_result['MessageId']
