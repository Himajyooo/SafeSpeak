import streamlit as st
import mysql.connector
from login import create_connection
from email_validator import validate_email, EmailNotValidError
# Function to check if the username is unique
def is_username_unique(username, cursor):
    sql = "SELECT COUNT(*) FROM login WHERE username = %s"
    cursor.execute(sql, (username,))
    result = cursor.fetchone()
    return result[0] == 0
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
    # Check if all fields are filled
        if not username or not password1 or not email:
            st.error("Please fill in all fields.")
        else:
            L = (username,password1,email)
            con,cur=create_connection()
            # Check if the email format is valid
            try:
                # Validate the email using email-validator library
                valid = validate_email(email)
                if not valid:
                    st.error("Invalid email format. Please enter a valid email address.")
                else:
                    con, cur = create_connection()
                    # Check if the username is unique
                    if is_username_unique(username, cur):
                        # Insert user into database
                        sql = "INSERT INTO login (username, pass, email) VALUES (%s, %s, %s)"
                        data = (username, password1, email)
                        cur.execute(sql, data)
                        con.commit()
                        con.close()
                        st.success(f"Sign up successful! Username: {username}, Email: {email}, Password: {password1}")
                    else:
                        st.error("Username already exists. Please choose a different username.")
            except EmailNotValidError as e:
                st.error("Invalid email format. Please enter a valid email address.")

        
        
        # Redirect to login page
    if st.button("Go back"):
        st.session_state.logged_in = False
        #st.session_state.page = "user"
        st.session_state.signup = False
        st.rerun()
    
