import streamlit as st
from discussion_page import display_discussion_page

# Function to display user page
def display_user_page():
    st.title("Welcome")
    # Row for the logout button
    col1, col2 = st.columns([7, 1])
    with col2:
        if st.button("Logout", key="logout_button"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()
    # Load custom CSS
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.write(f"Welcome, user")

    
    # Display different discussions
    st.header("Discussions")
    if st.button("Discussion 1"):
        st.session_state.selected_discussion = "Discussion 1"
        st.session_state.page = "discussion"
        st.rerun()

    if st.button("Discussion 2"):
        st.session_state.selected_discussion = "Discussion 2"
        st.session_state.page = "discussion"
        st.rerun()

    if st.button("Discussion 3"):
        st.session_state.selected_discussion = "Discussion 3"
        st.session_state.page = "discussion"
        st.rerun()