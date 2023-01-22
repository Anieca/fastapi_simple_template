from pydantic import BaseModel, Field


class TextRequest(BaseModel):
    text: str = Field(..., title="input text")

    class Config:
        schema_extra = {"examples": {"text": "abcxyz"}}


class TextResponse(BaseModel):
    text: str = Field(..., title="output text")

    class Config:
        schema_extra = {"examples": {"text": "ABCXYZ"}}
