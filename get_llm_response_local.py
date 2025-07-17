from langchain_ollama import ChatOllama

llm = ChatOllama(
    model = "phi:latest",
    temperature=0
)

def get_answer(question):
    answer = llm.invoke(question)
    return answer.content