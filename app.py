import streamlit as st
import openai

# Streamlit App Configuration
st.set_page_config(
    page_title="AI YouTube Learning Guide",
    page_icon="🎥",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Function to call GPT-4o API
def call_gpt4o(api_key, system_prompt, user_message):
    """Calls GPT-4o API using OpenAI's updated client API."""
    client = openai.Client(api_key=api_key)
    try:
        response = client.chat.completions.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_message},
            ]
        )
        return response.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

# Function to display YouTube search results
def display_video_summaries(video_data):
    with st.expander("📺 Recommended YouTube Videos", expanded=True):
        for video in video_data:
            st.markdown(f"### [{video['title']}]({video['url']})")
            st.write(video['summary'])

# Main function
def main():
    if "video_results" not in st.session_state:
        st.session_state.video_results = []
        st.session_state.qa_pairs = []
        st.session_state.videos_loaded = False

    st.title("🎥 AI YouTube Learning Guide")
    st.markdown("""
        <div style='background-color: #004d99; padding: 1rem; border-radius: 0.5rem; margin-bottom: 2rem; color: white;'>
        Discover top educational YouTube videos and get AI-generated summaries and insights.
        Ask questions about the content for deeper learning.
        </div>
    """, unsafe_allow_html=True)

    # Sidebar: API Configuration
    with st.sidebar:
        st.header("🔑 API Configuration")
        openai_api_key = st.text_input("OpenAI API Key", type="password", help="Enter your OpenAI API key")

        if not openai_api_key:
            st.warning("⚠️ Please enter your OpenAI API Key to proceed")
            return
        st.success("API Key accepted!")

    # Video Search Section
    if openai_api_key:
        st.header("🔍 Search for Educational Videos")
        search_query = st.text_input("Enter a topic to learn about:")

        if st.button("🔎 Find Videos"):
            with st.spinner("Searching for the best educational videos..."):
                try:
                    search_prompt = "Find the top 3 educational YouTube videos related to: " + search_query
                    video_response = call_gpt4o(openai_api_key, "You are a helpful assistant that provides video recommendations.", search_prompt)
                    
                    video_results = []
                    video_lines = video_response.split("\n")
                    for line in video_lines:
                        if " - " in line:
                            title, url = line.split(" - ", 1)
                            summary_prompt = f"Summarize the key insights from this video: {url}"
                            summary = call_gpt4o(openai_api_key, "You are an AI that summarizes YouTube videos.", summary_prompt)
                            video_results.append({"title": title, "url": url, "summary": summary})

                    st.session_state.video_results = video_results
                    st.session_state.videos_loaded = True

                    display_video_summaries(video_results)
                except Exception as e:
                    st.error(f"❌ An error occurred: {e}")

        # Q&A Section
        if st.session_state.videos_loaded:
            st.header("❓ Ask AI About the Videos")
            question_input = st.text_input("Ask a question about these videos:")

            if st.button("Get Answer"):
                if question_input:
                    with st.spinner("Analyzing video content..."):
                        context = "\n".join([f"{vid['title']}: {vid['summary']}" for vid in st.session_state.video_results])
                        answer = call_gpt4o(openai_api_key, "You are an AI tutor answering questions based on video content.", f"{context}\nUser Question: {question_input}")
                        st.session_state.qa_pairs.append((question_input, answer))
                        st.markdown(f"**Q:** {question_input}")
                        st.markdown(f"**A:** {answer}")

if __name__ == "__main__":
    main()
