from unittest import result
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
    out = []
    
    for r in results['result']:
        out.append(
            f"Title: {r['title']}\nURL: {r['url']}\nSnippet:{r['content'][:300]}\n"
            )
    return "\n---\n".join(out)
print(web_search.invoke("what are the recent news of war?"))

@tool
def scrape_url(url:str) -> str:
    """scrape the content of the url and return the text"""
    try:
        resp = requests.get(url,timeout=8,headers={'User-Agent': 'Mozilla/5.0'})
        soup = BeautifulSoup(resp.text, "html.parser")
        for tag in soup(["script","style","nav","footer"]):
            tag.decompose()
        return soup.get_text(separator="\n",strip=True)[:3000]
    except Exception as e:
        return f"Could not scrape URL: {str(e)}"
print(scrape_url.invoke("url"))
        