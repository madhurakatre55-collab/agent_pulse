from agents import build_reader_agent, build_search_agent,writer_chain,critic_chain

def run_research_pipeline(topic: str) -> dict:
    state = {}
    #seacrh agent working 
    search_agent = build_search_agent()
    search_result =search_agent.invoke({
        "messages" : [("user",f"Find recent,reliable and detailed information about:{topic}" )]
    })
    state["search_result"] = search_result['messages'][-1].ContentDispositionHeader
    
    