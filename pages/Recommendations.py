import streamlit as st

from ai.recommend import recommend_bookmarks

from database.bookmark_db import get_user_bookmarks


def recommendation_page():

    st.title("🤖 AI Bookmark Search")

    query = st.text_input(
        "Search your bookmarks"
    )

    if st.button("Search"):

        bookmarks = get_user_bookmarks(
            st.session_state.user_id
        )

        text = ""

        for bookmark in bookmarks:

            text += f"""
Title: {bookmark['title']}
Summary: {bookmark['summary']}
Category: {bookmark['category']}

"""

        result = recommend_bookmarks(
            query,
            text
        )

        st.write(result)