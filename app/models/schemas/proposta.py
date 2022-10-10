from pydantic import BaseModel
from typing import List, Any


class PropostaClimate_FieldviewRequest(BaseModel):

    class Items(BaseModel):

        class Poligonos(BaseModel):
            ordem: int
            latitude: float
            longitude: float
            altitude: float = None

        numero_item: str
        codigo_cultura_anterior: str
        data_prevista_plantio: str
        data_provavel_colheita: str
        beneficiarios: List[dict]  # TODO ver os campos corretos
        poligonos: List[Poligonos]

    class Propriedade(BaseModel):
        numero_grau_latitude: str
        numero_minuto_latitude: str
        numero_segundo_latitude: str
        descricao_sigla_latitude: str
        numero_grau_longitude: str
        numero_minuto_longitude: str
        numero_segundo_longitude: str
        descricao_sigla_longitude: str
        descricao_roteiro_acesso: str
        nome_propriedade: str
        endereco_propriedade: str
        numero_endereco_propriedade: str
        complemento_propriedade: str
        bairro_propriedade: str

    class Segurado(BaseModel):
        tipo_sexo: int
        data_nascimento: str
        estado_civil: str
        patrimonio_declarado: int = 1
        renda: int = 1
        estrangeiro: str = None
        segurado_pep: str = None
        possui_rne: str = None
        numero_rne: str = None
        numero_rg: str
        numero_passaporte: str = None
        pais: str = None
        data_expedicao: str
        nome_orgao_expedidor: str
        profissao: int = 0
        capital_social: int = 8
        faturamento_presumido: int = 1
        cep: str
        logradouro: str
        numero: str
        complemento: str
        bairro: str = "Não informado"
        cidade: str
        estado: str
        telefone: str
        celular: str
        email: str
        codigo_produtor_rural: str = ""

    class Pagamento(BaseModel):
        numero_banco: int = 33
        numero_agencia_debito: str = ''
        numero_conta_corrente_debito: str = ''
        numero_digito_conta_corrente_debito: str = ''
        data_vencimento_parcela: str = None

    class ModoEnvio(BaseModel):
        forma_envio: int
        destino_correspondencia: int
        email_corretor: List[str]
        envio_segurado: bool = False

    numero_cotacao_proposta: str
    sequencial_opcao_parcelamento: str
    numero_cpf_corretor: str
    itens: List[Items]
    propriedade: Propriedade
    segurado: Segurado
    modo_envio: ModoEnvio
    pagamento: Pagamento
    codigo_corretor: str

    class Config:
        schema_extra = {
            "example": {
                "numero_cotacao_proposta": "3794333",
                "sequencial_opcao_parcelamento": "142042684",
                "numero_cpf_corretor": "04698999804",
                "itens": [
                    {
                        "numero_item": "1",
                        "codigo_cultura_anterior": "1",
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
                    "numero_agencia_debito": "0001",
                    "numero_conta_corrente_debito": "977199",
                    "numero_digito_conta_corrente_debito": "0",
                    "data_vencimento_parcela": None
                }
            }
        }


class PropostaClimate_FieldviewResponse(BaseModel):

    boleto: Any = ''
    mensagem: str = ''
