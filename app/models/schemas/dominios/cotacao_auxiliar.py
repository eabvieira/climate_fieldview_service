from typing import Any, List
from pydantic import BaseModel


class CotacaoAuxiliarClimate_FieldviewRequest(BaseModel):

    codigo_produto: int
    codigo_cultura: int
    codigo_modalidade: int
    cep_propriedade: int
    subvencao_sp: bool
    subvencao_federal: bool
    data_cotacao: str
    id_forma_regulacao_sinistro: int

    class Config:
        schema_extra = {
            "example": {
                "codigo_produto": 103,
                "codigo_cultura": 166,
                "codigo_modalidade": 95,
                "cep_propriedade": 19800001,
                "subvencao_sp": False,
                "subvencao_federal": False,
                "data_cotacao": "10/09/2021",
                "id_forma_regulacao_sinistro": 1
            }
        }


class CotacaoAuxiliarClimate_FieldviewResponse(BaseModel):

    class RegulacaoSinistro(BaseModel):
        quantidade_minima_itens: int
        quantidade_maxima_itens: int
        valor_minimo_area_por_hectare: float

    class CodigoDescricaoDefault(BaseModel):
        codigo: int
        descricao: str

    valor_custo: float
    valor_unidade: float
    unidade_medida: str
    valor_unidade_maxima: float
    valor_unidade_minima: float
    valor_produtividade: float
    valor_lmi_por_hectar: float = None
    data_limite_prevista_inicio_plantio: str
    data_limite_prevista_fim_plantio: str
    data_limite_prevista_inicio_colheita: str
    data_limite_prevista_fim_colheita: str
    data_termino_vigencia: str
    codigo_regiao_blaze: int
    codigo_municipo_bacen: int
    codigo_atividade_bacen: int = None
    codigo_cultura_bacen: int = None
    codigo_municipo_ibge: int
    id_zoneamento_agricola: str = None
    id_programa_subvencao: int = None
    niveis_cobertura: List[float]
    franquias: List[float] = None
    pacotes_tecnologicos: List[CodigoDescricaoDefault]
    tipos_de_solo: List[CodigoDescricaoDefault]
    maquinarios: List[CodigoDescricaoDefault]
    coberturas: List[CodigoDescricaoDefault]
    regulacao_sinistro: Any = None
    raw_climate_fieldview_cotacao_auxiliar: dict
