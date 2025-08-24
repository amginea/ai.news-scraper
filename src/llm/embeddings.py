from llm.llm_clients import get_embedding_client

def get_embedding(text: str):
    return get_embedding_client().embed_query(text)