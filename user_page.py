import streamlit as st
from discussion_page import display_discussion_page
from database import create_connection

# Function to display user page
def display_user_page():
    con,cur=create_connection()
    user_id=st.session_state.user_id
    user_name=st.session_state.username
    st.title(f"Welcome {user_name}")
    # Row for the logout button
    col1, col2 = st.columns([7, 1])
    with col2:
        if st.sidebar.button("Logout", key="logout_button"):
            st.session_state.logged_in = False
            st.session_state.page = "login"
            st.rerun()
    # Load custom CSS
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.write(f"Welcome, user")

    # Display different discussions
    # Add a button in the sidebar to add new discussion
    # if st.sidebar.button("+ Add Discussion"):
    #     user_input = st.text_input("Enter new discussion")
    #     cur.execute("insert into discussion (d_name) values (%s)",(user_input,))
    #     con.commit()
    st.header("Discussions")
    if st.button("Discussion 1"):
        cur.execute("select discussion_id from discussion where d_name ='discussion1'")
        d_id= cur.fetchone()[0]
        st.session_state.selected_discussion = "discussion1"
        st.session_state.d_id = d_id
        st.session_state.page = "discussion"
        st.rerun()

    if st.button("Discussion 2"):
        cur.execute("select discussion_id from discussion where d_name ='discussion2'")
        d_id= cur.fetchone()[0]
        st.session_state.selected_discussion = "discussion2"
        st.session_state.d_id = d_id
        st.session_state.page = "discussion"
        st.rerun()

    if st.button("Discussion 3"):
        cur.execute("select discussion_id from discussion where d_name ='discussion3'")
        d_id= cur.fetchone()[0]
        st.session_state.selected_discussion = "discussion3"
        st.session_state.d_id = d_id
        st.session_state.page = "discussion"
        st.rerun()