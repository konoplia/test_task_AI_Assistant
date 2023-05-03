from pydantic import BaseModel, Field

from constants import MAX_TOKENS_USER

class Message(BaseModel):
    message: str=Field(max_length=MAX_TOKENS_USER)
