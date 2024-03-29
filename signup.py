import streamlit as st

def display_signup_page():
    st.title("Sign Up")
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    # Input fields for username, email, and password
    username = st.text_input("Username")
    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    # Sign up button
    if st.button("Sign Up"):
        
        st.success(f"Sign up successful! Username: {username}, Email: {email}, Password: {password}")

        # Redirect to login page
        st.session_state.logged_in = False
        #st.session_state.page = "user"
        st.rerun()
display_signup_page() 