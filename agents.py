from langchain.agents import create_agent 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptsTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_serch, scrape_url
from dotenv import

load_dotenv()

llm = ChatOpenAI(model = "",temperature=0)

def build_search_agents():
    return create_agent(
        
        
    )