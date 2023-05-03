import os

from fastapi import FastAPI, Depends, HTTPException, Request
from fastapi.security import APIKeyHeader
from dotenv import load_dotenv

from chat.chat_interactor import create_answer, get_user_prompt
from constants import PROMPT_TEMPLATE
from app.pydantic_models import Message

load_dotenv()
api_key_header = APIKeyHeader(name="X-API-KEY")


app = FastAPI()

API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise Exception("API_KEY not set in environment")


@app.get("/chat")
def chat(api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    response = get_user_prompt()
    return {"message": response}


@app.post("/chat")
def chat(data: Message, api_key: str = Depends(api_key_header)):
    if api_key != API_KEY:
        raise HTTPException(status_code=403, detail="Invalid API Key")
    prompt = PROMPT_TEMPLATE.format(data.message)
    response = create_answer(prompt)
    if 'Unknown' in response:
        return {"message": "I don't know, please contact support by email support@nifty-bridge.com"}
    return {"message": response}
