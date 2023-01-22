from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends

from .container import Container
from .schemas import TextRequest, TextResponse
from .services import ITextOperationService

router = APIRouter()


@router.post("/capitalize", response_model=TextResponse, summary="capitalize text")
@inject
def capitalize(
    text_request: TextRequest,
    service: ITextOperationService = Depends(Provide[Container.text_operation_service]),
) -> TextResponse:
    capitalized_text = service.capitalize(text_request.text)
    return TextResponse(text=capitalized_text)
