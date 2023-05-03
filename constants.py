import os
import dotenv

dotenv.load_dotenv()

# Description: This file contains all the constants used in the project

# pdf file name
PDF_FILE= os.getenv("PDF_FILE")

# template using for prompt in app/main.py
PROMPT_TEMPLATE = "NiftyBridge AI assistant: {} If the answer is not in the context, say the word Unknown"

# path to pdf file
PATH_TO_PDF = "Untitled 5.pdf"

# max tokens which can produce OpenAI API
MAX_TOKENS = 1000

# template using for prompt in chat/chat_interactor.py
TEMPLATE = """You are a NiftyBridge AI assistant.
            If the question is not about the company Nifty Bridge you should not answer.
            Question: {question}
            Answer: 
            """

# error message if file not found
FILE_NOT_FOUND = "PDF File not found, please check the path to the file"

# max tokens which can input user
MAX_TOKENS_USER = 1000

# prompts for user
USER_PROMPTS = {
        "Qestion related to the company Nifty Bridge": {
            "Question": "What is Nifty Bridge?",
            "Answer": "Nifty Bridge is a company that provides services for the development of artificial intelligence.",
            "Question_1": "What services does Nifty Bridge provide?",
            "Answer_1": "Nifty Bridge provides services for the development of artificial intelligence."
        },
        "Questions which not related to the company Nifty Bridge": {

            "Question": "Who is Jimmy Page?",
            "Answer": "I don't know, please contact support by email support@nifty-bridge.com",

            "Question_1": "What is the capital of France?",
            "Answer_1": "I don't know, please contact support by email support@nifty-bridge.com"
        }
    }
