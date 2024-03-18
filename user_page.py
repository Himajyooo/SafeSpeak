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
        st.experimental_set_query_params(selected_discussion="Discussion 1")
        st.experimental_rerun()

    if st.button("Discussion 2"):
        st.experimental_set_query_params(selected_discussion="Discussion 2")
        st.experimental_rerun()

    if st.button("Discussion 3"):
        st.experimental_set_query_params(selected_discussion="Discussion 3")
        st.experimental_rerun()
"""import streamlit as st

# Function to display user page
def display_user_page():
    st.title("User Page")
    st.write(f"Welcome,User")# {st.session_state.username}!")

    # Display different discussions
    st.header("Discussions")
    if st.button("Discussion 1"):
        redirect_to_discussion("Discussion 1")

    if st.button("Discussion 2"):
        redirect_to_discussion("Discussion 2")

    if st.button("Discussion 3"):
        redirect_to_discussion("Discussion 3")

# Function to redirect to discussion page
def redirect_to_discussion(discussion):
    st.session_state.selected_discussion = discussion
    # st.session_state.page = "discussion"
    display_discussion()

# Function to display discussion page
def display_discussion():
    selected_discussion = st.session_state.selected_discussion
    st.title(f"{selected_discussion}")
    st.write("Here is the content of the selected discussion.")"""
