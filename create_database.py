import os
from dotenv import load_dotenv, find_dotenv
import shutil

from langchain_community.document_loaders import DirectoryLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain.schema import Document
from langchain_openai import OpenAIEmbeddings
from langchain_community.vectorstores import Chroma # Chroma in an open-source embedding database

_ = load_dotenv(find_dotenv()) # read local .env file
my_api_key = os.environ['OPENAI_API_KEY']
CHROMA_PATH = "chroma"
DATA_PATH = "data/aws_ec2_documentation"

def generate_data_store():
    documents = load_documents()
    chunks = split_text(documents)
    save_to_chroma(chunks)

def load_documents():
    loader = DirectoryLoader(DATA_PATH, glob="*.md")
    documents = loader.load()
    return documents

def split_text(documents):
    """This function will split the documents into chunks."""
    text_splitter = RecursiveCharacterTextSplitter(
        chunk_size=1000,
        chunk_overlap=500,
        length_function=len,
        add_start_index=True
    )

    chunks = text_splitter.split_documents(documents)
    print(f"Split {len(documents)} documents into {len(chunks)} chunks.")
    document = chunks[20]
    print(document.page_content)
    print(document.metadata)
    
    return chunks

def save_to_chroma(chunks: list[Document]):
    # Clear out the database directory first
    if os.path.exists(CHROMA_PATH):
        shutil.rmtree(CHROMA_PATH) # Deletes all files and subdirectories within the specified path.
        
    # Create a vector database from the documents
    db = Chroma.from_documents(chunks, OpenAIEmbeddings(openai_api_key=my_api_key), persist_directory=CHROMA_PATH)
    db.persist() # Saves the database to disk as a SQLite3 file
    print(f"Saved {len(chunks)} chunks to database in {CHROMA_PATH}.")

if __name__ == "__main__":
    generate_data_store()