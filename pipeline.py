from agents import build_reader_agent, build_search_agent,writer_chain,critic_chain

def run_research_pipeline(topic: str) -> dict:
    state = {}
    #seacrh agent working 
    