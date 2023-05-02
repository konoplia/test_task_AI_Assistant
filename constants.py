# Description: This file contains all the constants used in the project

# template using for prompt in app/main.py
PROMPT_TEMPLATE = "NiftyBridge AI assistant: {} If the answer is not in the context, say the word Unknown"

# path to pdf file
PATH_TO_PDF = "Untitled5.pdf"

# max tokens which can produce OpenAI API
MAX_TOKENS = 1000

# template using for prompt in chat/chat_interactor.py
TEMPLATE = """You are a NiftyBridge AI assistant.
            If the question is not about the company Nifty Bridge you should not answer.
            Question: {question}
            Answer: 
            """
