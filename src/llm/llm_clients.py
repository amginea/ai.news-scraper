import os

from langchain_openai import AzureChatOpenAI
from langchain_openai import AzureOpenAIEmbeddings
from dotenv import load_dotenv

load_dotenv()
AZURE_ENDPOINT=os.getenv("AZURE_OPENAI_ENDPOINT")
AZURE_CHAT_DEPLOYMENT_NAME=os.getenv("AZURE_OPENAI_DEPLOYMENT_NAME")
AZURE_EMBEDDINGS_DEPLOYMENT_NAME=os.getenv("AZURE_OPENAI_EMBEDDING_MODEL")
OPENAI_API_VERSION=os.getenv("AZURE_OPENAI_API_VERSION")

def get_chat_client():
    return AzureChatOpenAI(
        azure_endpoint=AZURE_ENDPOINT,
        azure_deployment=AZURE_CHAT_DEPLOYMENT_NAME,
        openai_api_version=OPENAI_API_VERSION
    )
    
def get_embedding_client(): 
    return AzureOpenAIEmbeddings(
        azure_endpoint=AZURE_ENDPOINT,
        azure_deployment=AZURE_EMBEDDINGS_DEPLOYMENT_NAME,
        openai_api_version=OPENAI_API_VERSION
    )
