import streamlit as st
from user_page import display_user_page
from login import display_login_page
from discussion_page import display_discussion_page

# Streamlit app
def main():
    st.title("SafeSpeak: Express Your Views")

    # Initialize session state if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "selected_discussion" not in st.session_state:
        st.session_state.selected_discussion = None

    if "page" not in st.session_state:
        st.session_state.page = "user"

    # Check if user is logged in
    if not st.session_state.logged_in:
        display_login_page()
    else:
        if st.session_state.selected_discussion:
            display_discussion_page()
        else:
            display_user_page()

if __name__ == "__main__":
    main()
