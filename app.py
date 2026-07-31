import streamlit as st
from auth.login import login_page
from auth.signup import signup_page
from pages.View_Bookmark import view_bookmarks_page
from pages.Home import home_page
from pages.Add_bookmark import add_bookmark_page
from pages.View_Bookmark import view_bookmarks_page

from pages.Recommendations import recommendation_page


st.set_page_config(
    page_title="LinkMind AI",
    page_icon="⭐",
    layout="wide"
)



# Session

if "logged_in" not in st.session_state:

    st.session_state.logged_in = False



if "user" not in st.session_state:

    st.session_state.user = None




# --------------------------
# Logged In User
# --------------------------

if st.session_state.logged_in:

    

    st.sidebar.title("LinkMind AI ⭐")


    st.sidebar.write(
        f"👤 {st.session_state.user['name']}"
    )

    menu = st.sidebar.radio(

        "Navigation",

        [
            "Home",
            "Add Bookmark",
            "View Bookmarks",
        ]

    )


    st.sidebar.divider()


    if st.sidebar.button("Logout"):


        st.session_state.logged_in = False

        st.session_state.user = None

        st.rerun()



    # Page Routing


    if menu == "Home":

        home_page()



    elif menu == "Add Bookmark":

        add_bookmark_page()



    elif menu == "View Bookmarks":

        view_bookmarks_page()






# --------------------------
# Login
# --------------------------

else:


    option = st.sidebar.radio(

        "Account",

        [
            "Login",
            "Signup"
        ]

    )


    if option == "Login":

        login_page()


    else:

        signup_page()

