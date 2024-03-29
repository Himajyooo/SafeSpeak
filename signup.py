import streamlit as st
import mysql.connector
from login import create_connection
from email_validator import validate_email, EmailNotValidError

def display_signup_page():
    st.title("Sign Up")
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    # Input fields for username, email, and password
    username = st.text_input("Username")
    email = st.text_input("Email")
    password1 = st.text_input("Password", type="password")
    
    # Sign up button
    if st.button("Sign Up"):
        L = (username,password1,email)
        con,cur=create_connection()
        # Check if the email format is valid
        try:
            # Validate the email using email-validator library
            valid = validate_email(email)
            strsql="insert into login (username,pass,email) values(%s,%s,%s)"
            #st.success("Valid email format!")
            cur.execute(strsql,L)
            con.commit()
            con.close()
            
            st.success(f"Sign up successful! Username: {username}, Email: {email}, Password: {password1}")

        except EmailNotValidError as e:
            st.error("Invalid email format. Please enter a valid email address.")
        
        
        # Redirect to login page
    if st.button("Go back"):
        st.session_state.logged_in = False
        #st.session_state.page = "user"
        st.session_state.signup = False
        st.rerun()
    
