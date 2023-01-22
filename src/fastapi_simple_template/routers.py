from dependency_injector.wiring import Provide, inject
from fastapi import APIRouter, Depends
from .schemas import TextRequest, TextResponse
from .services import ITextOperationService
from .container import Container

router = APIRouter()


@router.post("/capitalize", response_class=TextResponse, summary="capitalize text")
@inject
def capitalize(
    text_request: TextRequest, service: ITextOperationService = Depends(Provide[Container.text_operation_service])
) -> TextResponse:
    capitalized_text = service.capitalize(text_request.text)
    return TextResponse(text=capitalized_text)
