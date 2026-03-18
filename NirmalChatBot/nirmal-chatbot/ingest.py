import os
from dotenv import load_dotenv

from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import Chroma
from langchain_huggingface import HuggingFaceEmbeddings

load_dotenv()

PDF_PATH = "data/nirmal_kumar_profile.pdf"
CHROMA_PATH = "chroma_db"

def ingest(): 

    print("Loading PDF...")

    loader = PyPDFLoader(PDF_PATH)
    documents = loader.load()

    print("Splitting text...")

    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=500,
        chunk_overlap=100
    )

    docs = text_splitter.split_documents(documents)

    print("Creating embeddings...")

    embeddings = HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

    print("Storing in ChromaDB...")

    db = Chroma.from_documents(
        docs,
        embedding=embeddings,
        persist_directory=CHROMA_PATH
    )

    db.persist()

    print("Ingestion Completed")

if __name__ == "__main__":
    ingest()