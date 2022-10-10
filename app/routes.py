from fastapi import APIRouter, Depends
from starlette.status import HTTP_201_CREATED

from app.models.schemas.simulacao import SimulacaoClimate_FieldviewResponse
from app.models.schemas.proposta import PropostaClimate_FieldviewResponse
from app.models.schemas.status import StatusClimate_FieldviewResponse
from app.models.schemas.documentos import DocumentosClimate_FieldviewResponse

from app.dependencies.simulacao import simulacao
from app.dependencies.proposta import proposta
from app.dependencies.status import status
from app.dependencies.documentos import documentos


router = APIRouter()


@router.post(
    "/simulacao",
    response_model=SimulacaoClimate_FieldviewResponse,
    name="Climate_Fieldview: Cria nova cotacao",
    tags=['api v1']
)
async def _simulacao(
    cotacao: SimulacaoClimate_FieldviewResponse = Depends(simulacao),
) -> SimulacaoClimate_FieldviewResponse:

    return cotacao


@router.post(
    "/proposta",
    status_code=HTTP_201_CREATED,
    response_model=PropostaClimate_FieldviewResponse,
    name="Climate_Fieldview: Cria nova proposta",
    tags=['api v1']
)
async def _proposta(
    proposta: PropostaClimate_FieldviewResponse = Depends(proposta),
) -> PropostaClimate_FieldviewResponse:

    return proposta


@router.get(
    "/status_proposta",
    response_model=StatusClimate_FieldviewResponse,
    name="Climate_Fieldview:Obter os detalhes das etapas da emissão solicitada.",
    tags=['api v1']
)
async def _status(
    status: StatusClimate_FieldviewResponse = Depends(status)
) -> StatusClimate_FieldviewResponse:

    return status


@router.get(
    "/documentos",
    response_model=DocumentosClimate_FieldviewResponse,
    name="Climate_Fieldview:Obter os documentos do tipo/item solicitado",
    tags=['api v1']
)
async def _documentos(
    documentos: DocumentosClimate_FieldviewResponse = Depends(documentos)
) -> DocumentosClimate_FieldviewResponse:

    return documentos
