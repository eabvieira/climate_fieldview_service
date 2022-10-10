from pydantic import BaseModel


class BancosResponse(BaseModel):

    codigo: str
    descricao: str
    forma_pagamento: int
