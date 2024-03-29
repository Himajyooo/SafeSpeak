import streamlit as st
import mysql.connector
from user_page import display_user_page
from login import display_login_page
from discussion_page import display_discussion_page
from signup import display_signup_page

# def create_connection():
#     #Used to connect Python with MySQL
#     con = mysql.connector.connect(\
#           host = "localhost",\
#           user = "root",
#           password = "may@2023")
#     cur = con.cursor()
#     strSQL = "show databases"
#     cur.execute(strSQL)
#     r = cur.fetchall()
#     if ("safespeak",) in r:
#         pass
#     else:  #Till here
#         strSQL = "create database safespeak;"
#         cur.execute(strSQL)
#     strSQL = "select database();"
#     cur.execute(strSQL)
#     r = cur.fetchall()
#     if r in ("safespeak",):
#         pass
#     else:
#         strSQL = "use safespeak;"
#         cur.execute(strSQL)
#     strSQL = "show tables;"
#     cur.execute(strSQL)
#     r = cur.fetchall()
#     if ("login",) in r:
#         pass
#     else:
#         strSQL = "create table login("\
#                 "userid int(5) primary key,username varchar(20),pass varchar(20),email varchar(20));"
#         cur.execute(strSQL)
#         strSQL="insert into login values(001,'user','password','user@email.com');"
#         cur.execute(strSQL)
#         con.commit()
#     # if ("item",) in r:
#     #     pass
#     # else:
#     #     strSQL = "create table item("\
#     #             "barcode varchar(20) primary key,name varchar(20),"\
#     #             "category varchar(20),price float(20),"\
#     #             "stock int);"
#     #     cur.execute(strSQL)
#     return con, cur

def main():
    # Initialize session state if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "selected_discussion" not in st.session_state:
        st.session_state.selected_discussion = None

    if "page" not in st.session_state:
        st.session_state.page = "user"
    
    if "signup" not in st.session_state:
        st.session_state.signup = False

    # Check if user is logged in
    if not st.session_state.logged_in:
        display_login_page()
    else:
        if st.session_state.selected_discussion:
            display_discussion_page()
        # elif st.session_state.page:
        #     display_user_page()
        elif st.session_state.signup:
            display_signup_page()
        else:
            display_user_page()

if __name__ == "__main__":
    main()
