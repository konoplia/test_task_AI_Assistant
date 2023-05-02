from pydantic import BaseModel, Field


class Message(BaseModel):
    message: str=Field(max_length=1000)
