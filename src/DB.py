import chromadb
import google.generativeai as palm
from conf.Articles import articles
from conf.Models import embedding_model
from chromadb.api.types import Documents, Embeddings
from chromadb import Collection, QueryResult


# Set up the database and create embeddings from the files
def init():
    db = create_chroma_db(articles, "laws")
    return db


# Function to create embeddings for given documents using palm's embedding model
def embed_function(texts: Documents) -> Embeddings:
    # Embed the documents using any supported method
    return [
        palm.generate_embeddings(model=embedding_model, text=text)["embedding"]
        for text in texts
    ]


# Function to create a chroma client and collection to create the database.
def create_chroma_db(documents: Documents, name: str):
    chroma_client = chromadb.Client()
    db = chroma_client.create_collection(name=name, embedding_function=embed_function)
    add_to_collection(documents, db)
    return db


# Function to add to the chroma database collection after the database is setup given the documents array and database
def add_to_collection(documents: Documents, db: Collection, startID: int = 1):
    for i, d in enumerate(documents, start=startID):
        db.add(documents=d, ids=str(i))
        print(f"Added embedding with ID: {i}")
    print("Finished adding embeddings")


# Funtion to query the database with a question and get the top one document
def get_relevant_passage(query: str, db: Collection):
    passage = db.query(query_texts=[query], n_results=1)["documents"][0][0]
    return passage
