# AI YouTube Guide

## Project Overview
The **AI YouTube Guide** is a sophisticated web application designed to enhance educational experiences by leveraging artificial intelligence to discover, summarize, and explain YouTube video content. This project empowers users to find top educational videos on various topics and receive AI-generated summaries and insights. It also allows users to ask questions about the video's content, providing a deeper understanding of the subject matter.

**Purpose:**  
- Enables learners to quickly find quality educational YouTube videos.
- Provides concise AI-generated summaries to save time.
- Facilitates interactive learning by allowing users to ask AI-driven questions about video content.

**Target Audience:**  
- Students and educators seeking efficient learning resources.
- Lifelong learners and professionals looking to expand their knowledge.

## Key Features
- **Search YouTube for Educational Videos:** Discover top educational videos based on user input topics.
- **AI-Generated Summaries:** Receive clear summaries of each video’s key insights powered by OpenAI's GPT-4o.
- **Interactive Q&A Section:** Ask questions about the video content and receive AI-generated answers.
- **Streamlined User Interface:** A user-friendly design that guides users through video search and Q&A functionalities.

## Installation & Setup Guide

1. **Clone the Repository:**
   ```bash
   git clone https://github.com/yourusername/ai-youtube-guide.git
   cd ai-youtube-guide
   ```
   
2. **Set Up a Virtual Environment:**
   ```bash
   python3 -m venv venv
   source venv/bin/activate   # On Windows use `venv\Scripts\activate`
   ```
   
3. **Install Dependencies:**
   Create a `requirements.txt` file with the necessary dependencies:
   ```text
   streamlit
   openai
   ```
   Then, run:
   ```bash
   pip install -r requirements.txt
   ```

4. **Configuration:**
   - Acquire an OpenAI API Key from [OpenAI's website](https://openai.com/).
   - (Optional) Set your OpenAI API Key in an environment variable for secure access.

## Usage Instructions

1. **Running the App:**
   To start the Streamlit app, run:
   ```bash
   streamlit run app.py
   ```

2. **Walkthrough:**
   - **API Configuration Section:**  
     Enter your OpenAI API key in the sidebar; this is required to access AI functionalities.
   - **Search for Videos:**  
     Input a topic you're interested in learning about then click "Find Videos" to get recommendations.
   - **Review Video Summaries:**  
     View summarized insights for each video suggestion provided by AI.
   - **Q&A Interaction:**  
     Type a question related to the video content, click "Get Answer" to receive detailed insights from AI.

## Technology Stack
- **Languages:** Python
- **Framework:** Streamlit for the user interface
- **APIs:** OpenAI API for AI-powered content summarization and Q&A

## Additional Notes
- **Configuration:** Ensure your OpenAI API key is stored securely and not exposed in the source code.
- **Limitations:** The efficiency of video recommendations and summaries relies on the accuracy of GPT-4o's API responses.
- **Future Improvements:** 
  - Implementation of more advanced filtering for video recommendations.
  - Exploration of additional video sources beyond YouTube.

This project demonstrates a practical approach to integrating AI with educational tools, providing a modern solution for effective learning and content understanding.