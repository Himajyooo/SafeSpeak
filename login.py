import streamlit as st
from admin_page import display_admin_page
from user_page import display_user_page
from discussion_page import display_discussion_page

# Function to display login page
def display_login_page():
    # Streamlit app
    st.title("SafeSpeak: Express Your Views")
    # Load custom CSS
    with open("styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.title("Login")

    user = st.text_input("User Name")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check if email and password are correct (dummy check)
        if user == "user" and password == "password":
            st.session_state.logged_in = True
            st.session_state.page = "user"
            st.rerun()
            
        elif user == "admin@gmail.com" and password == "admin":
            display_admin_page()
        else:
            st.error("Invalid email or password")

# Call the function to display login page
#display_login_page()   
