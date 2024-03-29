import streamlit as st
import mysql.connector
from login import create_connection

def display_signup_page():
    st.title("Sign Up")
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    # Input fields for username, email, and password
    username = st.text_input("Username")
    email = st.text_input("Email")
    password1 = st.text_input("Password", type="password")
    #create_connection()
    # Sign up button
    if st.button("Sign Up"):
        L = (username,password1,email)
        con,cur=create_connection()
        strsql="insert into login (username,pass,email) values(%s,%s,%s)"
        cur.execute(strsql,L)
        con.commit()
        con.close()
        
        st.success(f"Sign up successful! Username: {username}, Email: {email}, Password: {password1}")

        # Redirect to login page
    if st.button("Go back"):
        st.session_state.logged_in = False
        #st.session_state.page = "user"
        st.session_state.signup = False
        st.rerun()
    
