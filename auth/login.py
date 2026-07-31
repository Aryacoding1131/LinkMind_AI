import streamlit as st
from auth.auth_utils import login_user


def login_page():
    st.title("LinkMind AI ⭐")
    st.write("Your intelligent memory for the web")

    
    left, center, right = st.columns([1, 2, 1])

    with center:

        st.subheader(
            "🔐 Login",
            text_alignment="center"
        )

        email = st.text_input("Email")

        password = st.text_input(
            "Password",
            type="password"
        )

        # Center the button
        btn_col1, btn_col2, btn_col3 = st.columns([1, 1, 1])

        with btn_col2:
            login_clicked = st.button("Login")

        if login_clicked:

            success, user = login_user(
                email,
                password
            )

            if success:

                st.session_state.logged_in = True
                st.session_state.user = user
                st.session_state.user_id = str(user["_id"])
                st.session_state.username = user["name"]

                st.success("Login Successful")

                st.rerun()

            else:
                st.error(user)