import streamlit as st
import mysql.connector
from user_page import display_user_page
from login import display_login_page
from discussion_page import display_discussion_page
from signup import display_signup_page

def main():
    # Initialize session state if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False
        st.session_state.user_id = None
        st.session_state.username = None

    if "selected_discussion" not in st.session_state:
        st.session_state.selected_discussion = None
        st.session_state.d_id = None

    if "page" not in st.session_state:
        st.session_state.page = "user"
    
    if "signup" not in st.session_state:
        st.session_state.signup = False

    # Check if user is logged in
    if not st.session_state.logged_in:
        display_login_page()
    else:

        if st.session_state.selected_discussion:
            
            display_discussion_page()
        # elif st.session_state.page:
        #     display_user_page()
        elif st.session_state.signup:
            display_signup_page()
        else:
            display_user_page()

if __name__ == "__main__":
    main()
