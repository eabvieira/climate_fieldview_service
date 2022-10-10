from pydantic import BaseModel
from typing import List


class ParceirosNegocioClimate_FieldviewResponse(BaseModel):

    codigo_parceiro_negocio: str
    nome_razao_social: str
