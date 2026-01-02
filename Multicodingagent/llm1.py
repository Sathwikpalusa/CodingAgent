from langchain_ollama import ChatOllama
def getllm():
    llm1=ChatOllama(model="tinyllama",temperature=0)
    return llm1