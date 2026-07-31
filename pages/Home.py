import streamlit as st
def home_page():
    st.title("LinkMind AI ⭐")
    st.write("Your intelligent memory for the web")
    user = st.session_state.user
    st.subheader(
        f"Welcome back, {user['name']} 👋"
    )
    st.divider()
    st.image(
    "assets/bookmark.png",
    use_container_width=True
    )
    st.write(
        """
        Bookmarks are digital references that allow users to save and revisit important web pages without needing to remember or search for the URLs again. They help organize online resources such as articles, tutorials, research papers, documentation, blogs, and videos for future use. As users browse the internet, the number of saved bookmarks often grows rapidly, making it difficult to locate relevant information later. Traditional browser bookmarks only store the page title and URL, providing limited organization and search capabilities. An AI-powered bookmark management system addresses this challenge by automatically analyzing the content of each webpage using Natural Language Processing (NLP) and Large Language Models (LLMs). The system extracts meaningful information, identifies keywords and named entities, classifies the webpage into relevant categories, generates concise summaries, and stores the processed data in a MongoDB database. Users can then search, filter, and retrieve bookmarks efficiently based on their content rather than relying solely on page titles or URLs. This intelligent approach transforms conventional bookmarking into a smart knowledge management system, enabling faster access to valuable information while improving productivity and organization.

        """
    )

