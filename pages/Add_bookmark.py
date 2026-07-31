import streamlit as st

from ai.workflow import run_pipeline

from utils.validator import validate_url

from database.bookmark_db import save_bookmark



def add_bookmark_page():

    st.title("➕ Add New Bookmark")


    st.write(
        """
        Paste any website URL.
        AI will automatically analyze,
        classify and summarize it.
        """
    )


    st.divider()


    url = st.text_input(
        "Enter Website URL",
        placeholder="https://example.com"
    )


    # ==================================================
    # RUN AI PIPELINE
    # ==================================================

    if st.button("Analyze Website"):


        if not url:

            st.error(
                "Please enter a URL"
            )

            return



        if not validate_url(url):

            st.error(
                "Invalid URL"
            )

            return



        with st.spinner(
            "Running AI Pipeline..."
        ):


            try:

                bookmark = run_pipeline(url)


            except Exception as e:

                st.error(
                    f"Pipeline Error: {e}"
                )

                return



        if not bookmark:

            st.error(
                "Pipeline failed"
            )

            return



        # Store result

        st.session_state[
            "temp_bookmark"
        ] = bookmark



        st.success(
            "Website analyzed successfully!"
        )



    # ==================================================
    # DISPLAY RESULT
    # ==================================================


    if "temp_bookmark" not in st.session_state:

        return



    bookmark = st.session_state[
        "temp_bookmark"
    ]



    st.divider()



    # ==================================================
    # WEBSITE INFORMATION
    # ==================================================

    st.subheader(
        "🌐 Website Information"
    )


    st.write(
        "**Title**"
    )

    st.write(
        bookmark.get(
            "title",
            "No title"
        )
    )



    st.write(
        "**Description**"
    )

    st.write(
        bookmark.get(
            "description",
            "No description"
        )
    )



    st.write(
        "**Domain**"
    )

    st.write(
        bookmark.get(
            "domain",
            ""
        )
    )



    st.write(
        "**Word Count**"
    )

    st.write(
        bookmark.get(
            "word_count",
            0
        )
    )



    with st.expander(
        "📄 Extracted Content"
    ):

        st.write(
            bookmark.get(
                "content",
                ""
            )[:3000]
        )



    with st.expander(
        "📌 Headings"
    ):


        for heading in bookmark.get(
            "headings",
            []
        ):

            st.write(
                "•",
                heading
            )



    # ==================================================
    # NLP
    # ==================================================

    st.divider()


    st.subheader(
        "🧠 NLP Analysis"
    )


    col1, col2 = st.columns(2)



    with col1:

        st.metric(

            "Reading Time",

            f"{bookmark.get('reading_time',0)} min"

        )



    with col2:

        st.metric(

            "Processed Words",

            bookmark.get(
                "word_count",
                0
            )

        )



    st.subheader(
        "🔑 Keywords"
    )


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
            "No keywords found"
        )



    st.subheader(
        "🏷 Named Entities"
    )


    entities = bookmark.get(
        "entities",
        []
    )


    if entities:


        for entity in entities:


            st.write(

                f"• {entity['text']} "
                f"({entity['label']})"

            )


    else:

        st.info(
            "No entities detected"
        )



    # ==================================================
    # OLLAMA CLASSIFICATION
    # ==================================================

    st.divider()


    st.subheader(
        "🤖 AI Classification"
    )


    col1, col2 = st.columns(2)



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

            "Confidence",

            f"{bookmark.get('confidence',0)}%"

        )



    st.subheader(
        "AI Tags"
    )


    tags = bookmark.get(
        "ai_tags",
        []
    )


    if tags:


        for tag in tags:

            st.write(
                f"🔹 {tag}"
            )


    else:

        st.info(
            "No AI tags generated"
        )



    # ==================================================
    # GROQ SUMMARY
    # ==================================================

    st.divider()


    st.subheader(
        "📝 AI Summary"
    )



    st.write(

        bookmark.get(
            "summary",
            "No summary"
        )

    )



    st.subheader(
        "📌 Key Points"
    )


    points = bookmark.get(
        "key_points",
        []
    )


    if points:


        for point in points:

            st.write(
                "•",
                point
            )

    else:

        st.info(
            "No key points available"
        )



    col1, col2 = st.columns(2)



    with col1:

        st.metric(

            "Difficulty",

            bookmark.get(
                "difficulty",
                "Unknown"
            )

        )



    with col2:

        st.metric(

            "Audience",

            bookmark.get(
                "audience",
                "Unknown"
            )

        )



    # ==================================================
    # SAVE TO MONGODB
    # ==================================================

    st.divider()


    st.subheader(
        "💾 Save Bookmark"
    )


    logged_in = st.session_state.get(
        "logged_in",
        False 
    )

    user_id = st.session_state.get(
        "user_id",
        None
    )

    if not logged_in:
        st.warning("Please log in to save Bookmarks!")

    else:
        if st.button("Saved to My Collections"):
            try:
                bookmark_id = save_bookmark(
                    user_id=user_id,
                    bookmark=bookmark
                )
                st.success("Bookmark saved successfully!")
            except Exception as e:
                st.error(
                    f"Database Error: {e}"
                )
