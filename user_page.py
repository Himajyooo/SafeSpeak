import streamlit as st
from discussion_page import display_discussion_page

# Function to display user page
def display_user_page():
    st.title("User Page")
    st.write(f"Welcome, user")

    # Logout button in the top right corner
    if st.button("Logout", key="logout_button"):
        st.session_state.logged_in = False
        st.session_state.page = "login"
        st.experimental_rerun()
    
    # Display different discussions
    st.header("Discussions")
    if st.button("Discussion 1"):
        st.session_state.selected_discussion = "Discussion 1"
        st.session_state.page = "discussion"
        st.experimental_rerun()

    if st.button("Discussion 2"):
        st.session_state.selected_discussion = "Discussion 2"
        st.session_state.page = "discussion"
        st.experimental_rerun()

    if st.button("Discussion 3"):
        st.session_state.selected_discussion = "Discussion 3"
        st.session_state.page = "discussion"
        st.experimental_rerun()

    # Display back button only when on a discussion page
    if st.session_state.page == "discussion":
        if st.button("Back"):
            st.session_state.selected_discussion = None
            st.session_state.page = "user"
            #st.experimental_rerun()
