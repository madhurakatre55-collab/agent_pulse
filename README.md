**AgentPulse **

An agentic research workflow built with LangChain, where a team of specialized AI agents collaborate to search the web, gather content, write a structured research report, and critique it — all automatically.

Overview

AgentPulse breaks the "research a topic" task into a pipeline of cooperating agents, each with a single responsibility:

1.Search Agent — searches the web for relevant sources on a given topic.
2.Reader Agent — scrapes and extracts content from the URLs the Search Agent finds.
3.Writer Chain — synthesizes the gathered research into a clear, structured report (Introduction, Key Findings, Conclusion, Sources).
4.Critic Chain — reviews the report, scores it out of 10, and lists strengths, areas to improve, and a one-line verdict.

Project Structure
agent_pulse/
├── agents.py          
├── pipeline.py         
├── tools.py
├── requirements.txt
├── .gitignore
└── README.md

