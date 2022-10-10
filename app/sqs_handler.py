from __future__ import print_function

from app.dependencies.proposta import proposta
from app.dependencies.status import status

from app.models.schemas.proposta import PropostaClimate_FieldviewRequest

from app.sqs_parser import sqs_payload


def sqs_handler(event, context):

    for record in event['Records']:
        raw_sqs_payload_body = record["body"]

        # payload do sqs
        event, slug, payload, proposta_id, documento_id, environment = sqs_payload(
            raw_sqs_payload_body)

        try:
            if event == "proposta":
                return proposta(PropostaClimate_FieldviewRequest(**payload), proposta_id, environment)

            elif event == "status":
                return status(payload, environment)

            else:
                raise Exception(f"Evento invalido: {event}")

        except Exception as e:
            print(f'Erro ao executar {str(e)}')
