from dotenv import load_dotenv
from langchain_groq import ChatGroq
load_dotenv() #.env should be in the same directory


llm = ChatGroq(
    model="llama-3.1-8b-instant",
    temperature=2,
    max_tokens=None,
    timeout=None,
    max_retries=2,
    # other params...
)

def get_answer(question):
    answer = llm.invoke(question)
    return answer.content



