from typing import Protocol


class ITextOperationService(Protocol):
    @staticmethod
    def capitalize(text: str) -> str:
        ...


class TextOperationService:
    @staticmethod
    def capitalize(text: str) -> str:
        return text.capitalize()
