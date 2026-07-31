import streamlit as st

from database.bookmark_db import (
    get_user_bookmarks,
    search_bookmarks,
    delete_bookmark
)

from ai.recommend import recommend_bookmarks


def view_bookmarks_page():

    st.title("📚 My Bookmarks")

    st.write(
        "Search, filter and manage your saved AI bookmarks."
    )

    st.divider()

    # -----------------------------
    # Login Check
    # -----------------------------

    if "user_id" not in st.session_state:

        st.warning("Please login first.")

        return

    user_id = st.session_state["user_id"]

    # -----------------------------
    # Search
    # -----------------------------

    search_text = st.text_input(
        "🔍 Search Bookmarks",
        placeholder="Title, URL, Category..."
    )

    if search_text:

        bookmarks = search_bookmarks(
            user_id,
            search_text
        )

    else:

        bookmarks = get_user_bookmarks(
            user_id
        )

    if len(bookmarks) == 0:

        st.info("No bookmarks found.")

        return

    st.metric(
        "Total Bookmarks",
        len(bookmarks)
    )

    st.divider()

    # -----------------------------
    # Category Filter
    # -----------------------------

    categories = sorted(

        list(

            set(

                bookmark.get(
                    "category",
                    "Others"
                )

                for bookmark in bookmarks

            )

        )

    )

    selected_category = st.selectbox(

        "Filter by Category",

        ["All"] + categories

    )

    st.divider()

    # -----------------------------
    # Display
    # -----------------------------

    for bookmark in bookmarks:

        if selected_category != "All":

            if bookmark.get(
                "category"
            ) != selected_category:

                continue

        with st.container(border=True):

            st.subheader(
                bookmark.get(
                    "title",
                    "No Title"
                )
            )

            st.write(
                bookmark.get(
                    "url",
                    ""
                )
            )

            st.caption(
                bookmark.get(
                    "domain",
                    ""
                )
            )

            col1, col2, col3 = st.columns(3)

            with col1:

                st.metric(
                    "Category",
                    bookmark.get(
                        "category",
                        "Others"
                    )
                )

            with col2:

                st.metric(
                    "Reading Time",
                    f"{bookmark.get('reading_time',0)} min"
                )

            with col3:

                st.metric(
                    "Confidence",
                    f"{bookmark.get('confidence',0)}%"
                )

            st.write("### 📝 Summary")

            st.write(
                bookmark.get(
                    "summary",
                    "No Summary Available"
                )
            )

            st.write("### 🔑 Keywords")

            keywords = bookmark.get(
                "keywords",
                []
            )

            if keywords:

                st.write(
                    ", ".join(keywords)
                )

            else:

                st.info(
                    "No keywords available."
                )

            st.write("### 🏷 AI Tags")

            tags = bookmark.get(
                "ai_tags",
                []
            )

            if tags:

                st.write(
                    ", ".join(tags)
                )

            else:

                st.info(
                    "No AI Tags."
                )

            with st.expander(
                "🏷 Named Entities"
            ):

                entities = bookmark.get(
                    "entities",
                    []
                )

                if entities:

                    for entity in entities:

                        st.write(

                            f"• {entity['text']} ({entity['label']})"

                        )

                else:

                    st.info(
                        "No entities found."
                    )

            with st.expander(
                "📄 Extracted Content"
            ):

                st.write(
                    bookmark.get(
                        "content",
                        ""
                    )
                )

            # -------------------------------------
            # AI Recommendation
            # -------------------------------------

            recommendations = recommend_bookmarks(
                bookmark,
                bookmarks
            )

            st.subheader(
                "🤖 Similar Bookmarks"
            )

            if recommendations:

                for item in recommendations:

                    rec = item["bookmark"]

                    st.write(
                        f"📌 {rec['title']}"
                    )

            else:

                st.info(
                    "No recommendations available."
                )

            col1, col2 = st.columns(2)

            with col1:

                if st.button(

                    "🗑 Delete Bookmark",

                    key=str(bookmark["_id"])

                ):

                    success = delete_bookmark(

                        str(bookmark["_id"])

                    )

                    if success:

                        st.success(
                            "Bookmark Deleted."
                        )

                        st.rerun()

                    else:

                        st.error(
                            "Delete Failed."
                        )

            with col2:

                st.caption(

                    f"Saved On : {bookmark.get('created_at','')}"

                )

            st.divider()