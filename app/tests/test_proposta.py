import os
import json
from dotenv import load_dotenv

load_dotenv()

from fastapi.testclient import TestClient
from app.main import app

client = TestClient(app)

headers = {
    'Authorization': 'Bearer '+os.getenv('AGRISTAMP_KEY')
}


def test_post_proposta():

    payload = {
            "numero_cotacao_proposta": "3794353",
            "sequencial_opcao_parcelamento": "142042998",
            "numero_cpf_corretor": "04698999804",
            "itens": [
                {
                    "numero_item": "1",
                    "codigo_cultura_anterior": 0,
                    "data_prevista_plantio": "12/11/2021",
                    "data_provavel_colheita": "30/04/2022",
                    "beneficiarios": [],
                    "poligonos": [
                        {
                            "ordem": 1,
                            "latitude": -22.67852,
                            "longitude": -50.39584,
                            "altitude": None
                        },
                        {
                            "ordem": 2,
                            "latitude": -22.68779,
                            "longitude": -50.39206,
                            "altitude": None
                        },
                        {
                            "ordem": 3,
                            "latitude": -22.69064,
                            "longitude": -50.3997,
                            "altitude": None
                        },
                        {
                            "ordem": 4,
                            "latitude": -22.68177,
                            "longitude": -50.40331,
                            "altitude": None
                        }
                    ]
                }
            ],
            "propriedade": {
                "numero_grau_latitude": "22",
                "numero_minuto_latitude": "40",
                "numero_segundo_latitude": "42",
                "descricao_sigla_latitude": "S",
                "numero_grau_longitude": "50",
                "numero_minuto_longitude": "23",
                "numero_segundo_longitude": "45",
                "descricao_sigla_longitude": "W",
                "descricao_roteiro_acesso": "N\u00e3o informado",
                "nome_propriedade": "FAZENDA UM",
                "endereco_propriedade": "RUA DA FAZENDA",
                "numero_endereco_propriedade": 1,
                "complemento_propriedade": "",
                "bairro_propriedade": "NAO INFORMADO"
            },
            "segurado": {
                "tipo_sexo": 2,
                "data_nascimento": "25/10/1989",
                "estado_civil": "C",
                "patrimonio_declarado": 1,
                "renda": 1,
                "estrangeiro": None,
                "segurado_pep": None,
                "possui_rne": None,
                "numero_rne": None,
                "numero_rg": "5039282728",
                "numero_passaporte": None,
                "pais": None,
                "data_expedicao": "01/01/2021",
                "nome_orgao_expedidor": "SJS",
                "profissao": 0,
                "capital_social": 8,
                "faturamento_presumido": 1,
                "cep": "91450-120",
                "logradouro": "RUA DO RECREIO",
                "numero": "499",
                "complemento": "",
                "bairro": "N\u00e3o informado",
                "cidade": "Porto Alegre",
                "estado": "RS",
                "telefone": "5152521512",
                "celular": "51252151253",
                "email": "teste@gmail.com",
                "codigo_produtor_rural": ""
            },
            "modo_envio": {
                "forma_envio": 1,
                "destino_correspondencia": 1,
                "email_corretor": [
                    "katia.veiga@propostaseguros.com.br",
                    "climate_fieldview@agristamp.com.br"
                ],
                "envio_segurado": False
            },
            "pagamento": {
                "numero_banco": 33,
                "data_vencimento_parcela": None
            }
        }

        
    response = client.post("/climate_fieldview_service/v1/proposta", headers=headers, data=json.dumps(payload))

    assert response.status_code in [200, 201]
