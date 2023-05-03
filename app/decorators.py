import os

from fastapi.security import APIKeyHeader
from dotenv import load_dotenv
from functools import wraps
from fastapi import HTTPException

load_dotenv()

api_key_header = APIKeyHeader(name="X-API-KEY")



API_KEY = os.getenv("OPENAI_API_KEY")
if not API_KEY:
    raise Exception("API_KEY not set in environment")

def auth_required(func):
    @wraps(func)
    def wrapper(*args, **kwargs):
        api_key = kwargs.get('api_key')
        if api_key != API_KEY:
            raise HTTPException(status_code=403, detail="Invalid API Key")
        return func(*args, **kwargs)

    return wrapper
