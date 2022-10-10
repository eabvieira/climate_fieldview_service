from typing import List
from fastapi import APIRouter, Depends

from app.models.schemas.dominios.culturas import CulturasClimate_FieldviewResponse
from app.models.schemas.dominios.culturas_modalidades import CulturasModalidadesClimate_FieldviewResponse
from app.models.schemas.dominios.cultivares import CultivaresClimate_FieldviewResponse
from app.models.schemas.dominios.parceiros_negocio import ParceirosNegocioClimate_FieldviewResponse
from app.models.schemas.dominios.cotacao_auxiliar import CotacaoAuxiliarClimate_FieldviewResponse
from app.models.schemas.dominios.culturas_anteriores import CulturasAnterioresClimate_FieldviewResponse
from app.models.schemas.dominios.bancos import BancosResponse

from app.dependencies.dominios.culturas import culturas
from app.dependencies.dominios.culturas_modalidades import cultura_modalidades
from app.dependencies.dominios.cultivares import cultivares
from app.dependencies.dominios.parceiros_negocio import parceiros_negocio
from app.dependencies.dominios.cotacao_auxiliar import cotacao_auxiliar
from app.dependencies.dominios.culturas_anteriores import culturas_anteriores
from app.dependencies.dominios.bancos import bancos

router = APIRouter()


@router.get(
    "/culturas",
    response_model=List[CulturasClimate_FieldviewResponse],
    name="Climate_Fieldview: Lista de culturas da seguradora",
    tags=['dominios']
)
async def _culturas(
    culturas: List[CulturasClimate_FieldviewResponse] = Depends(culturas)
) -> List[CulturasClimate_FieldviewResponse]:

    return culturas


@router.get(
    "/cultura/modalidades",
    response_model=List[CulturasModalidadesClimate_FieldviewResponse],
    name="Climate_Fieldview: Lista de culturas da seguradora",
    tags=['dominios']
)
async def _cultura_modalidades(
    modalidade_cultura: List[CulturasModalidadesClimate_FieldviewResponse] = Depends(
        cultura_modalidades)
) -> List[CulturasModalidadesClimate_FieldviewResponse]:

    return modalidade_cultura


@router.post(
    "/cultivares",
    response_model=List[CultivaresClimate_FieldviewResponse],
    name="Climate_Fieldview: Lista de culturas da seguradora",
    tags=['dominios']
)
async def _cultivares(
    cultivares: List[CultivaresClimate_FieldviewResponse] = Depends(cultivares)
) -> List[CultivaresClimate_FieldviewResponse]:

    return cultivares


@router.get(
    "/parceiros_negocio",
    response_model=List[ParceirosNegocioClimate_FieldviewResponse],
    name="Climate_Fieldview: Lista de culturas da seguradora",
    tags=['dominios']
)
async def _parceiros_negocio(
    parceiros_negocio: List[ParceirosNegocioClimate_FieldviewResponse] = Depends(
        parceiros_negocio)
) -> List[ParceirosNegocioClimate_FieldviewResponse]:

    return parceiros_negocio


@router.post(
    "/cotacao_auxiliar",
    response_model=CotacaoAuxiliarClimate_FieldviewResponse,
    name="Climate_Fieldview: Retorna informações básicas e necessárias para simulacao",
    tags=['dominios']
)
async def _cotacao_auxiliar(
    cotacao_auxiliar: CotacaoAuxiliarClimate_FieldviewResponse = Depends(
        cotacao_auxiliar)
) -> CotacaoAuxiliarClimate_FieldviewResponse:

    return cotacao_auxiliar


@router.get(
    "/culturas_anteriores",
    response_model=List[CulturasAnterioresClimate_FieldviewResponse],
    name="Climate_Fieldview: Retorna as culturas anteriores",
    tags=['dominios']
)
async def _culturas_anteriores(
    culturas_anteriores: List[CulturasAnterioresClimate_FieldviewResponse] = Depends(
        culturas_anteriores)
) -> List[CulturasAnterioresClimate_FieldviewResponse]:

    return culturas_anteriores


@router.get(
    "/bancos",
    response_model=List[BancosResponse],
    name="Climate_Fieldview: Retorna a lista de bancos aceitos",
    tags=['dominios']
)
async def _bancos(
    bancos: List[BancosResponse] = Depends(bancos)
) -> List[BancosResponse]:

    return bancos
