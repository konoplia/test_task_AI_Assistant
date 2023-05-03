from fastapi import FastAPI, Depends

from chat.chat_interactor import create_answer, get_user_prompt
from constants import PROMPT_TEMPLATE
from app.pydantic_models import Message
from app.decorators import auth_required, api_key_header


app = FastAPI()


@app.get("/chat")
@auth_required
def chat(api_key: str = Depends(api_key_header)):
    response = get_user_prompt()
    return {"message": response}


@app.post("/chat")
@auth_required
def chat(data: Message, api_key: str = Depends(api_key_header)):
    prompt = PROMPT_TEMPLATE.format(data.message)
    response = create_answer(prompt)
    if 'Unknown' in response:
        return {"message": "I don't know, please contact support by email support@nifty-bridge.com"}
    return {"message": response}

