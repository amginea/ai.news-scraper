from langchain.chains.combine_documents import create_stuff_documents_chain
from langchain.chains import create_retrieval_chain
from llm.llm_clients import get_chat_client
from llm.gpt import semantic_search_prompt
from dal.chroma import load_from_collection


def search_info(query, collection_name="markdowns") -> str:
   
    (docs, retriever) = load_from_collection(collection_name, query)
    print(docs)
    print(docs.__len__())
    question_answer_chain = create_stuff_documents_chain(
        llm=get_chat_client(),
        prompt=semantic_search_prompt(),
    )    
    print(semantic_search_prompt())
    rag_chain = create_retrieval_chain(retriever, question_answer_chain)
    response = rag_chain.invoke({"input": query})
    return response["answer"]