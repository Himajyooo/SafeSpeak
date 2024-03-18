import streamlit as st
from discussion_page import display_discussion_page

# Function to display user page
def display_user_page():
    st.title("User Page")
    st.write(f"Welcome, user")
    #{st.session_state.username}!")
    # Logout button in the top right corner
    col1, col2 = st.columns([1, 10])
    with col2:
        if st.button("Logout", key="logout_button"):
            st.session_state.logged_in = False
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
