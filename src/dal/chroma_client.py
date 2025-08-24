import chromadb
import os

from dotenv import load_dotenv

def get_chroma_client():
    load_dotenv()
    return chromadb.HttpClient(
        host=os.getenv("CHROMADB_HOST"),
        port=os.getenv("CHROMADB_PORT")
    )