import chromadb
from chromadb.api.types import Documents, Embeddings
import google.generativeai as palm
from conf.Models import embedding_model
from conf.Articles import articles
from conf.Models import text_model


# Set up the database and create embeddings from the files
def init():
    db = create_chroma_db(articles, "laws")
    return db, text_model


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


def add_to_collection(documents, db):
    for i, d in enumerate(documents, start=11):
        db.add(documents=d, ids=str(i))
        print(f"Added embedding with ID: {i}")
    print("Finished adding embeddings")


def get_relevant_passage(query, db):
    passage = db.query(query_texts=[query], n_results=1)["documents"][0][0]
    return passage
