from fastapi import FastAPI, Request
from pydantic import BaseModel
from rag.retriever import Retriever
from rag.generator import Generator
from rag.pipeline import run_pipeline
from utils.helpers import load_knowledge_base, create_vector_store, preprocess_text
import uvicorn

app = FastAPI()

class QueryRequest(BaseModel):
    query: str

retriever = Retriever()
generator = Generator()

@app.post("/ask")
async def ask(request: QueryRequest):
    user_query = request.query
    if not user_query:
        return {"error": "No query provided"}
    response = run_pipeline(user_query, retriever, generator)
    return {"response": response}

def main():
    kb_path = "src/data/knowledge_base.txt"
    kb_text = load_knowledge_base(kb_path)
    vector_store = create_vector_store(kb_text)

    print("Chatbot RAG sobre Trading. Digite 'sair' para encerrar.")
    while True:
        query = input("\nPergunta: ")
        if query.lower() == "sair":
            break
        query_proc = preprocess_text(query)
        docs = vector_store.similarity_search(query_proc, k=2)
        print("\nResposta baseada na base de conhecimento:")
        for doc in docs:
            print("-", doc.page_content.strip())

if __name__ == "__main__":
    import sys
    if len(sys.argv) > 1 and sys.argv[1] == "terminal":
        main()
    else:
        uvicorn.run("src.app:app", host="0.0.0.0", port=8000, reload=True)