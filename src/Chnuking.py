from docx import Document
from src.DB import *


def is_heading(paragraph):
    # Define your heading criteria here, e.g., based on font size or style
    return paragraph.style.name.startswith("Heading")


def chunk_articles(paragraphs):
    articles = []
    current_article = ""

    for paragraph in paragraphs:
        if is_heading(paragraph):
            if current_article:
                articles.append(current_article.strip())
                current_article = ""
        current_article += paragraph.text + "\n"

    if current_article:
        articles.append(current_article.strip())

    return articles


# Function to stro
def read_document(filepath: str):
    document: str = ""

    if filepath.endswith(".docx"):
        doc = Document(filepath)

        for paragraph in doc.paragraphs:
            document += paragraph.text + "\n"

    else:
        with open(filepath, "r") as file:
            document = file.read()

    documents = document.split("*****")

    if ("Proclamation" in filepath) and documents:
        procNum = documents[0].strip()

        documents = documents[1:]
        cited_docs = []
        for document in documents:
            document = f"{procNum} : \n {document} "
            cited_docs.append(document)

        documents = cited_docs

        # This is only for debugging purpose only
        # with open("temp.txt", "+a") as file:
        #     for document in documents:
        #         file.write(f"{document} \n\n*****\n\n")

    # print(len(documents))  # For debugging only
    return documents
