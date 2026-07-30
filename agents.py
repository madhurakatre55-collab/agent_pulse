from langchain.agents import create_agent 
from langchain_openai import ChatOpenAI
from langchain_core.prompts import ChatPromptsTemplate
from langchain_core.output_parsers import StrOutputParser
from tools import web_serch, scrape_url
from dotenv import load_dotenv

load_dotenv()

llm = ChatOpenAI(model = "",temperature=0)

#agent1
def build_search_agents():
    return create_agent(
        model = llm,
        tools = [web_serch],
    )
    
#agent2
def build_reader_agent():
    return create_agent(
        model = llm,
        tools =[scrape_url],
    )    
# chain writer report 
writer_prompt = ChatPromptsTemplate([
     ("system","You are expert research writer.Write clear,structured and insightful report"),
     ("human","""Write a detailed research report on the topic below.
      Topic: {topic}
      Research Gathered:
      {research}
      Structure the report as:
      -Introduction
      -Key Finding (minimum 3 well-explained points)
      -Conclusion
      -Sources(list all URLs found in the research)
      Be detailed,factual and professional.
      """),
    ])
writer_chain = writer_prompt | llm | StrOutputParser()

#critic chain

critic_prompt = ChatPromptsTemplate([
    ("system","You are a sharp and constructive research critic.Be honest and specific."),
    ("human","""Review the research report below and evaluate it strictly.
    Report:{report}
    Respond in this exact format:
    Score: X/10
    Strengths:
    -
    -
    
    Area to Improve:
    -
    -
    One line verdict:
    -
    -
    -"""),
    ])
critic_chain =critic_prompt | llm | StrOutputParser()
