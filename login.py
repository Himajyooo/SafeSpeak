import streamlit as st
from admin_page import display_admin_page
# Function to display login page

def display_login_page():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check if email and password are correct (dummy check)
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True
            st.session_state.page = "user"
            st.experimental_rerun()
            
        if email == "admin@gmail.com" and password == "admin":
            display_admin_page()
        else:
            st.error("Invalid email or password")