from langchain_core.tools import tool
import requests
from bs4 import BeautifulSoup
from tavily import TavilyClient
import os
from dotenv import load_dotenv
from rich import print 
load_dotenv()

tavily = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
@tool
def web_search(query:str) -> str:
    """"  search for top 3 website srachpers on web related to top 5 toritrest places in india .return titles,urls """
    results = tavily.search(query=query,max_results=3)
    return results
print(web_search.invoke("what are the recent news of war?"))