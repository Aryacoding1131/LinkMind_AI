import streamlit as st
from auth.auth_utils import signup_user

def signup_page():
    st.title("LinkMind AI ⭐")
    st.write("Your intelligent memory for the web")
    st.subheader("Create Account")

    name = st.text_input("Full Name")

    email = st.text_input("Email")

    password = st.text_input(
        "Password",
        type="password"
    )

    confirm = st.text_input(
        "Confirm Password",
        type="password"
    )

    if st.button("Sign Up"):

        if name == "" or email == "" or password == "":
            st.error("All fields are required")
            return

        if password != confirm:
            st.error("Passwords do not match")
            return

        success, message = signup_user(
            name,
            email,
            password
        )

        if success:
            st.success(message)
        else:
            st.error(message)