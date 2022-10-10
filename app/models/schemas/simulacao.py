from logging import warning
from pydantic import BaseModel
from enum import Enum
from typing import List


class SimulacaoClimate_FieldviewRequest(BaseModel):

    class TipoSegurado(str, Enum):
        PF = 'F'
        PJ = 'J'

    class RegulacaoSinistro(int, Enum):
        media_geral = 1
        talhonado = 2

    class ItemCotacao(BaseModel):

        class Coberturas(BaseModel):
            codigo: str

        numero_item: int = 0
        codigo_cultura_anterior: int
        valor_area_segurada: float
        valor_custo_estimado: str = None
        valor_produtividade_esperada: float
        valor_unidade: float
        percentual_nivel_cobertura: float
        percentual_franquia: str = None
        numero_pes_planta: str = None
        valor_distancia_planta_x: str = None
        valor_distancia_planta_y: str = None
        idade_planta: str = None
        codigo_tipo_solo: int
        codigo_pacote_tecnologico: str = ''  # Não informado
        codigo_tipo_maquinario: str = ''  # Não informado
        irrigado: str = ''  # Não informado
        codigo_cultivar_variedade: str
        valor_produtividade_kilo_planta: str = None
        valor_produtividade_real_kilo: str = None
        percentual_comissao: float = 10
        percentual_desconto_geral: float = 0
        percentual_agravo_geral: float = 0
        premio_financiavel: bool = False
        data_prevista_fim_colheita: str
        coberturas: List[Coberturas]

    numero_cotacao_proposta: str = None
    tipo_seguro: str = 'N'
    codigo_corretor: int
    codigo_parceiro_negocio: str = None
    numero_cpf_corretor: str
    subvencao_estadual: bool
    subvencao_federal: bool
    codigo_produto: str
    numero_cpf_cnpj: str
    tipo_segurado: TipoSegurado
    nome_segurado: str
    nome_propriedade: str = None
    cep_propriedade: str
    endereco_propriedade: str = None
    numero_endereco_propriedade: str = None
    complemento_propriedade: str = None
    bairro_propriedade: str = None
    nome_municipio_propriedade: str = None
    uf_propriedade: str = None
    nome_uf_propriedade: str = None
    codigo_modalidade: int
    codigo_cultura: str
    valor_area_total: float
    itens_cotacao: List[ItemCotacao]
    id_forma_regulacao_sinistro: RegulacaoSinistro

    class Config:
        schema_extra = {
            "example": {
                "numero_cotacao_proposta": "",
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
                "endereco_propriedade": "",
                "numero_endereco_propriedade": "",
                "complemento_propriedade": "",
                "bairro_propriedade": "",
                "nome_municipio_propriedade": "",
                "uf_propriedade": "",
                "nome_uf_propriedade": "",
                "codigo_modalidade": 95,
                "codigo_cultura": 166,
                "valor_area_total": 90.0,
                "itens_cotacao": [
                    {
                        "numero_item": 0,
                        "codigo_cultura_anterior": 0,
                        "valor_area_segurada": 90,
                        "valor_custo_estimado": "",
                        "valor_produtividade_esperada": 2712.0,
                        "valor_unidade": 93.00,
                        "percentual_nivel_cobertura": 65,
                        "percentual_franquia": None,
                        "numero_pes_planta": None,
                        "valor_distancia_planta_x": None,
                        "valor_distancia_planta_y": None,
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
        }


class SimulacaoClimate_FieldviewResponse(BaseModel):

    class FormasPagamento(BaseModel):
        codigo: int
        descricao: str

    class Parcelamento(BaseModel):
        sequencial_opcao_parcelamento: int
        descricao_forma_parcelamento: str
        descricao_forma_pagamento: str
        valor_primeira_parcela: float
        valor_demais_parcela: float
        valor_premio_total_proponente: float
        valor_premio_total: float
        codigo_forma_pagamento: int
        valor_premio_liquido: float
        valor_parcela_subvencao_federal: float
        valor_parcela_subvencao_estadual: float

    class DetalhePremio(BaseModel):
        item: int
        cobertura: str
        valor_importancia_segurada: float
        valor_premio: float
        franquia: str

    class Items(BaseModel):
        numero_item: int
        valor_custo_estimado: float = None
        valor_produtividade_esperada: float = None
        valor_produtividade_garantida: float
        valor_produtividade_garantida_unidade: float
        valor_produtividade_esperada_saca_hectare: float
        valor_lmi_hectare: float
        valor_lmi_item: float
        valor_lmi_utilizado: float = None
        warnings: dict = None

    numero_cotacao_proposta: int = None
    descricao_cultura: str
    descricao_modalidade: str
    descricao_produto: str
    subvencao_federal: str
    subvencao_estadual: str
    data_cotacao: str
    data_validade_cotacao: str
    formas_pagamento: List[FormasPagamento]
    parcelamento: List[Parcelamento]
    detalhe_premio: List[DetalhePremio]
    itens: List[Items]
    warnings: dict
