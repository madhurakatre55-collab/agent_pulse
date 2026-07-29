from agents import build_reader_agent, build_search_agent,writer_chain,critic_chain

def run_research_pipeline(topic: str) -> dict:
    state = {}
    #seacrh agent working 
    search_agent = build_search_agent()
    search_result =search_agent.invoke({
        "messages" : [("user",f"Find recent,reliable and detailed information about:{topic}" )]
    })
    state["search_result"] = search_result['messages'][-1].ContentDispositionHeader
    print("Search Result:", state["search_result"])
    # reader agent
    reader_agent = build_reader_agent()
    reader_result = reader_agent.invoke({
        "messages" : [{'user',
               f"Based on the following search results about '{topic}',"
               f"pick the most revlent URL and scrape it for deeper content.\n\n"
               f"Search Results:\n{state['search_result']}"}
    }]
    })
    state["scraped_content"] = reader_result['messages'][-1].content
    print("Scraped Content:", state["scraped_content"])

    research_combined = (
    f"SEARCH RESULTS :\n {state['search_result']}\n\n"
    f"DETAILED SCRAPED CONTENT :\n {state['scraped_content']}"
    )
    state["report"] = writer_chain.invoke({
    "topic" : topic,    
    "research" : research_combined
    })
    state["feedback"] = critic_chain.invoke({
        "report" : state["report"]
    })
    print("\n critic report \n",state['feedback'])
    return state
if__name__ =="__main__":
    topic = input("\n Enter a topic to research: Enter a research topic:")
    run_research_pipeline(topic)