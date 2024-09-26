from fastapi import FastAPI
from langchain_ollama.llms import OllamaLLM
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.output_parsers import StrOutputParser
from langserve import add_routes

# Define the Ollama LLM
llm = OllamaLLM(model="qwen2.5:0.5b")

# Create prompt template
system_template = "Translate the following into {language}:"
prompt_template = ChatPromptTemplate.from_messages([
    ('system', system_template),
    ('user', '{text}')
])

# Create parser
parser = StrOutputParser()

# Create chain
chain = prompt_template | llm | parser

# Define FastAPI app
app = FastAPI(
    title="LangChain with Ollama",
    version="1.0",
    description="A LangChain service using Ollama"
)

# Add chain route
add_routes(app, chain, path="/chain")

if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="0.0.0.0", port=8000)