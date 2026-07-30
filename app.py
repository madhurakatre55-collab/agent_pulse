import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="AgentPulse — AI Research Assistant",
    page_icon="🔎",
    layout="wide",
)

st.title("🔎 AgentPulse")
st.caption("A multi-agent research workflow powered by LangChain")

with st.sidebar:
    st.header("How it works")
    st.markdown(
        """
        1. **Search Agent** — finds relevant sources on the web
        2. **Reader Agent** — scrapes the most relevant source
        3. **Writer Chain** — writes a structured research report
        4. **Critic Chain** — scores and critiques the report
        """
    )
    st.divider()
    st.caption("Make sure your `.env` file has the required API key set before running the app.")

topic = st.text_input(
    "Enter a research topic",
    placeholder="e.g. Impact of AI on renewable energy",
)
run_clicked = st.button("🚀 Run Research", type="primary", use_container_width=True)

if run_clicked:
    if not topic.strip():
        st.warning("Please enter a topic first.")
    else:
        with st.spinner("Running the research pipeline... this can take a minute."):
            try:
                result = run_research_pipeline(topic)
                st.session_state["result"] = result
                st.session_state["topic"] = topic
                st.session_state["error"] = None
            except Exception as e:
                st.session_state["error"] = str(e)
                st.session_state.pop("result", None)

if st.session_state.get("error"):
    st.error(f"Something went wrong while running the pipeline:\n\n{st.session_state['error']}")

if "result" in st.session_state:
    result = st.session_state["result"]
    st.success(f"Research complete for: **{st.session_state['topic']}**")

    tab_report, tab_feedback, tab_search, tab_scraped = st.tabs(
        ["📄 Report", "🧐 Critic Feedback", "🔍 Search Results", "📰 Scraped Content"]
    )

    with tab_report:
        st.markdown(result.get("report", "No report generated."))
        st.download_button(
            "Download report as Markdown",
            data=result.get("report", ""),
            file_name=f"{st.session_state['topic'].replace(' ', '_')}_report.md",
            mime="text/markdown",
        )

    with tab_feedback:
        st.markdown(result.get("feedback", "No feedback generated."))

    with tab_search:
        st.text(result.get("search_result", "No search results."))

    with tab_scraped:
        st.text(result.get("scraped_content", "No scraped content."))
        