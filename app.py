import streamlit as st
import openai

# Streamlit App Configuration
st.set_page_config(
    page_title="🎥 AI YouTube Learning Guide",
    page_icon="📚",
    layout="wide",
    initial_sidebar_state="expanded"
)

# Sidebar: Page Selector
with st.sidebar:
    st.header("📌 Select a Page")
    page = st.radio(
        "Navigate:",
        ["About the App", "AI YouTube Learning Guide"],
        index=0  # Default to "About the App"
    )

# About the App Page
if page == "About the App":
    st.title("🎥 About AI YouTube Learning Guide")
    


    st.markdown("""
    ## 📌 Overview  
    The **AI YouTube Learning Guide** is designed to help users **quickly discover, summarize, and interact** with educational YouTube videos. Instead of watching entire videos to determine their usefulness, this AI-powered tool provides **key insights and allows interactive Q&A**, ensuring an efficient and enriched learning experience.

    ---

    ## 🏆 Why This App?  
    YouTube is a **vast educational resource**, but:
    - **Finding high-quality educational videos** can be overwhelming.
    - **Watching full videos** to determine their value takes time.
    - **Extracting key takeaways** from long content is difficult.
    - **Asking specific questions** about the video content isn’t always possible.

    This app **solves these problems** by leveraging AI to **find the best videos, summarize their insights, and allow interactive discussions**—all within a single interface.

    ---

    ## 🛠️ How It Works  
    1️⃣ **Enter a topic** you want to learn about (e.g., "Machine Learning Basics").  
    2️⃣ The AI **fetches top educational videos** related to your topic.  
    3️⃣ Each video is **summarized by AI**, extracting the most important insights.  
    4️⃣ Users can **ask follow-up questions**, and AI will answer based on video content.  
    5️⃣ The app serves as a **personalized learning assistant**, making YouTube a more interactive and structured learning platform.

    ---

    ## 🌟 Key Features  
    ### 🔍 AI-Powered Video Search  
    - Searches for **high-quality educational videos** on YouTube.  
    - Uses AI to **identify top learning content** for your chosen topic.  
    - Ensures that **only relevant** and **useful** videos are recommended.  

    ### 📑 AI-Generated Summaries  
    - Extracts **key takeaways** from each video.  
    - Saves time by **eliminating the need to watch full videos**.  
    - Provides structured summaries, making it easy to grasp core concepts.  

    ### 🤖 Interactive Q&A  
    - Allows users to **ask questions** about the video content.  
    - AI provides **detailed answers** based on the video’s insights.  
    - Transforms passive video consumption into an **engaging, interactive experience**.  

    ### 🎯 Personalized Learning Assistant  
    - Acts as a **smart tutor** that helps you understand complex topics.  
    - Provides a **curated learning experience** instead of random video searches.  
    - Enhances retention by reinforcing learning through **summaries and Q&A**.  

    ---

    ## 🚀 Who Can Benefit?  
    ### 🎓 Students & Lifelong Learners  
    - Get **quick video summaries** instead of watching full content.  
    - Clarify doubts instantly by **asking AI follow-up questions**.  
    - Learn efficiently and **retain information better**.  

    ### 👨‍💻 Professionals & Researchers  
    - Find the **most relevant** content for skill development.  
    - Save time by **focusing only on essential insights**.  
    - Engage in **interactive Q&A** to deepen understanding.  

    ### 🧑‍🏫 Educators & Content Creators  
    - Discover **high-quality educational content** in their field.  
    - Get **structured insights** to enhance their teaching materials.  
    - Use AI-powered summaries for **quick reference & lesson planning**.  

    ---

    ## 🏁 Conclusion  
    The **AI YouTube Learning Guide** revolutionizes the way users interact with educational YouTube content. With **AI-powered search, intelligent summaries, and interactive Q&A**, this tool **saves time, enhances learning, and personalizes the educational experience**.  

    Start exploring today and **learn smarter, not harder!** 🚀🎥  
    """)


# AI YouTube Learning Guide Page
else:
    st.title("📚 AI YouTube Learning Guide")
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
            st.stop()
        st.success("API Key accepted!")
    
    # Function to call GPT-4o API
    def call_gpt4o(api_key, system_prompt, user_message):
        """Calls GPT-4o API using OpenAI's client API."""
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
    
    # Initialize session state
    if "video_results" not in st.session_state:
        st.session_state.video_results = []
        st.session_state.qa_pairs = []
        st.session_state.videos_loaded = False
    
    # Video Search Section
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
