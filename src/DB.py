import chromadb
from chromadb.api.types import Documents, Embeddings
import google.generativeai as palm
from dotenv import load_dotenv
import os

load_dotenv()
api_key = os.environ.get("PALM_API_KEY")
palm.configure(api_key=api_key)

embedding_model = [
    m for m in palm.list_models() if "embedText" in m.supported_generation_methods
][0]


def embed_function(texts: Documents) -> Embeddings:
    # Embed the documents using any supported method
    return [
        palm.generate_embeddings(model=embedding_model, text=text)["embedding"]
        for text in texts
    ]


def create_chroma_db(documents, name):
    chroma_client = chromadb.Client()
    db = chroma_client.create_collection(name=name, embedding_function=embed_function)
    for i, d in enumerate(documents, start=1):
        db.add(documents=d, ids=str(i))
    return db
