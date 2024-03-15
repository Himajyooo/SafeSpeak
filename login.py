import streamlit as st
# Function to display login page

def display_login_page():
    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check if email and password are correct (dummy check)
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True
            st.experimental_rerun()
        else:
            st.error("Invalid email or password")