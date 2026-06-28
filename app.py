import streamlit as st
from pipeline import run_research_pipeline

st.set_page_config(
    page_title="AI Research Agent",
    page_icon="🔎",
    layout="wide"
)

st.title("🔎 AI Research Agent")
st.write("Enter a topic and generate a complete research report using your search agent, reader agent, writer chain, and critic chain.")

with st.sidebar:
    st.header("About")
    st.write(
        """
        This app uses:
        - Search Agent
        - Reader/Scraper Agent
        - Writer Chain
        - Critic Chain
        """
    )

    st.markdown("---")
    # st.warning("Make sure your `.env` file contains `GOOGLE_API_KEY` and `TAVILY_API_KEY`.")

topic = st.text_input(
    "Enter research topic",
    placeholder="Example: Impact of AI on healthcare in 2026"
)

run_button = st.button("Generate Research Report", type="primary")

if run_button:
    if not topic.strip():
        st.error("Please enter a research topic.")
    else:
        with st.spinner("Running research pipeline... This may take some time."):
            try:
                result = run_research_pipeline(topic)

                st.success("Research report generated successfully!")

                tab1, tab2, tab3, tab4 = st.tabs(
                    [
                        "Final Report",
                        "Critic Feedback",
                        "Search Results",
                        "Scraped Content"
                    ]
                )

                with tab1:
                    st.subheader("Final Research Report")
                    st.markdown(result.get("report", "No report generated."))

                    st.download_button(
                        label="Download Report",
                        data=result.get("report", ""),
                        file_name=f"{topic.replace(' ', '_')}_research_report.txt",
                        mime="text/plain"
                    )

                with tab2:
                    st.subheader("Critic Feedback")
                    st.markdown(result.get("feedback", "No feedback generated."))

                with tab3:
                    st.subheader("Search Results")
                    st.text_area(
                        label="Search Output",
                        value=result.get("search_results", "No search results found."),
                        height=350
                    )

                with tab4:
                    st.subheader("Scraped Content")
                    st.text_area(
                        label="Scraped Output",
                        value=result.get("scraped_content", "No scraped content found."),
                        height=350
                    )

            except Exception as e:
                st.error("Something went wrong while running the pipeline.")
                st.exception(e)