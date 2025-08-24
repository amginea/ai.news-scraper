from langchain_core.documents import Document
from langchain_chroma import Chroma
from dal.chroma_client import get_chroma_client
from llm.llm_clients import get_embedding_client
from langchain_text_splitters import RecursiveCharacterTextSplitter
from llm.embeddings import get_embedding

def create_or_update_collection(collection_name: str, documents: list[Document]) -> None:
    Chroma.from_documents(
        client=get_chroma_client(),
        documents=documents,
        embedding=get_embedding_client(), 
        collection_name=collection_name
    )
        
def extract_metadata(metadata):
    return {
        "source": metadata.url,
        "title": metadata.title, 
        "language": metadata.language,
        "description": metadata.description
    }
    
def upload_from_documents(documents: list[Document]):
    text_splitter = RecursiveCharacterTextSplitter(
        # Set a really small chunk size, just to show.
        chunk_size=100,
        chunk_overlap=20,
        length_function=len,
        is_separator_regex=False,
    )
    
    for doc in documents:
        metadata = extract_metadata(doc.metadata)
        create_or_update_collection("markdowns", text_splitter.split_documents(documents=[Document(page_content=doc.markdown, metadata=metadata)]))
        create_or_update_collection("summaries", text_splitter.split_documents(documents=[Document(page_content=doc.summary, metadata=metadata)]))
        
def load_from_collection(collection_name: str, query: str):
    retriever = Chroma(
        client=get_chroma_client(),
        embedding_function=get_embedding_client(),
        collection_name=collection_name
    )
    
    return (retriever.similarity_search_by_vector(get_embedding(query), k=10), retriever.as_retriever())