from langchain_core.documents import Document
from services.scraper_client import get_crawl_client

def map_scrapes_to_document(doc):
    return Document(
        page_content=doc.markdown, 
        metadata={
            "source": doc.metadata.url,
            "title": doc.metadata.title, 
            "language": doc.metadata.language,
            "description": doc.metadata.description
        }
    )

def scrape_urls(urls) -> list[Document]:
    result: list[Document] = []   
    for url in urls:
        try:
            client = get_crawl_client()
            for url in urls:
                doc = client.scrape(url, formats=["markdown", "summary"])
                result.append(doc)

        except Exception as e:
            print(f"Error: {str(e)}")
    return result