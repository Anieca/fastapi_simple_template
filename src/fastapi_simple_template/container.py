from dependency_injector import containers, providers

from fastapi_simple_template.services import TextOperationService


class Container(containers.DeclarativeContainer):
    wiring_config = containers.WiringConfiguration(modules=[".routers"])

    text_operation_service = providers.Factory(TextOperationService)
