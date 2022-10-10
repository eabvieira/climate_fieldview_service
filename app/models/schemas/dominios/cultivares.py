from pydantic import BaseModel
from typing import List


class CultivaresClimate_FieldviewRequest(BaseModel):
    codigo_cultura: int
    uf: str
    codigo_fabricante: int = None


class CultivaresClimate_FieldviewResponse(BaseModel):

    codigo: int = None
    descricao: str
    fabricante: str = None
    uf: str
    grupo_cultivar: int
