import streamlit as st
from discussion_page import display_discussion_page

# Function to display user page
def display_user_page():
    st.title("User Page")
    st.write(f"Welcome, user")
    #{st.session_state.username}!")

    # Display different discussions
    st.header("Discussions")
    if st.button("Discussion 1"):
        display_discussion_page("Discussion 1")

    if st.button("Discussion 2"):
        display_discussion_page("Discussion 2")

    if st.button("Discussion 3"):
        display_discussion_page("Discussion 3")
