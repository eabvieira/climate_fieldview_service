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

def test_health_check():
    response = client.get("/climate_fieldview_service/health")
    assert response.status_code == 200


def test_get_simulacao():

    payload = {
        #"numero_cotacao_proposta": "",
        "tipo_seguro": "N",
        "codigo_corretor": "49792",
        "codigo_parceiro_negocio": "66",
        "numero_cpf_corretor": "04698999804",
        "subvencao_estadual": False,
        "subvencao_federal": False,
        "codigo_produto": 103,
        "numero_cpf_cnpj": "11395512302",
        "tipo_segurado": "F",
        "nome_segurado": "JOAO DA SILVA",
        "nome_propriedade": "FAZENDA UM",
        "cep_propriedade": "19800001",
        #"endereco_propriedade": "",
        #"numero_endereco_propriedade": "",
        #"complemento_propriedade": "",
        #"bairro_propriedade": "",
        #"nome_municipio_propriedade": "",
        #"uf_propriedade": "",
        #"nome_uf_propriedade": "",
        "codigo_modalidade": 95, #produtividade
        "codigo_cultura": 166,
        "valor_area_total": 90.0,
        "itens_cotacao": [
            {
                "numero_item": 0,
                "codigo_cultura_anterior": 0,
                "valor_area_segurada": 90,
                #"valor_custo_estimado": "",
                "valor_produtividade_esperada": 2712.0,
                "valor_unidade": 93.00,
                "percentual_nivel_cobertura": 65,
                #"percentual_franquia": None,
                #"numero_pes_planta": None,
                #"valor_distancia_planta_x": None,
                #"valor_distancia_planta_y": None,
                "idade_planta": None,
                "codigo_tipo_solo": 2,
                "codigo_pacote_tecnologico": "",
                "codigo_tipo_maquinario": "",
                "irrigado": False,
                "codigo_cultivar_variedade": 99553,
                "valor_produtividade_kilo_planta": None,
                "valor_produtividade_real_kilo": None,
                "percentual_comissao": 10,
                "percentual_desconto_geral": 0,
                "percentual_agravo_geral": 0,
                "premio_financiavel": False,
                "data_prevista_fim_colheita": "30/04/2022",
                "coberturas": [
                    {"codigo": "2006"},
                    {"codigo": "2002"},
                    {"codigo": "2005"},
                    {"codigo": "2010"},
                    {"codigo": "2011"},
                    {"codigo": "2019"},
                    {"codigo": "2022"},
                    {"codigo": "2024"},
                    {"codigo": "2025"},
                    {"codigo": "2026"}
                ]
            }
        ],
        "id_forma_regulacao_sinistro": 1
        }

    response = client.post("/climate_fieldview_service/v1/simulacao", headers=headers, data=json.dumps(payload))

    assert response.status_code == 200
