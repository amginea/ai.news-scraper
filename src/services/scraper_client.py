import os

from firecrawl import Firecrawl
from dotenv import load_dotenv

load_dotenv()

def get_crawl_client() -> Firecrawl:
    return Firecrawl(
        api_key=os.getenv("FIRECRAWL_API_KEY")
    )