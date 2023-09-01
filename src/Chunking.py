import os
from docx import Document
from docx.text.paragraph import Paragraph


# This function is used to group a file that has a proper headaing and paragraph style to separate chunks and returns them as an array
def chunk_articles(paragraphs: [Paragraph]):
    # Function to determin a heading or not
    def is_heading(paragraph: Paragraph):
        # Define your heading criteria here, e.g., based on font size or style
        return paragraph.style.name.startswith("Heading")

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


# Function to read a document into an array of documents.
# It treats '.docx' and '.txt' files separately.
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

    return documents


# Get all the articles stored in the docs directory and return them as an array
def chunk_all_articles(docsPath: str = "docs"):
    laws = []

    # Navigating to the docs folder to get the files stored in there
    current_dir = os.path.dirname(os.path.abspath(__file__))
    parent_dir = os.path.join(current_dir, "..")
    os.chdir(parent_dir)
    docs_folder = os.path.join(parent_dir, docsPath)

    # Iterating through each file in the docs folder and storing the chunked version in an array
    for root, _, files in os.walk(docs_folder):
        for file in files:
            documents = read_document(os.path.join(root, file))
            laws.extend(documents)

    return laws
