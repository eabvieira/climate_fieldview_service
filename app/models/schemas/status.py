from pydantic import BaseModel
from typing import List


class StatusClimate_FieldviewResponse(BaseModel):

    codigo: int = None
    descricao: str = ''
    ramo: int = None
    apolice: int = None
