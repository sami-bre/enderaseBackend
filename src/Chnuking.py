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
