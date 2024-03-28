import streamlit as st
from user_page import display_user_page
from login import display_login_page
from discussion_page import display_discussion_page

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
#     if ("mkmartdb",) in r:
#         pass
#     else:  #Till here
#         strSQL = "create database mkmartdb;"
#         cur.execute(strSQL)
#     strSQL = "select database();"
#     cur.execute(strSQL)
#     r = cur.fetchall()
#     if r in ("mkmartdb",):
#         pass
#     else:
#         strSQL = "use mkmartdb;"
#         cur.execute(strSQL)
#     strSQL = "show tables;"
#     cur.execute(strSQL)
#     r = cur.fetchall()
#     if ("employee",) in r:
#         pass
#     else:
#         strSQL = "create table employee("\
#                 "empid int(5) primary key,name varchar(20),pass varchar(20),"\
#                 "admin varchar(10) default 'no',salary float(20),"\
#                 "phone_no varchar(50),city varchar(20),department varchar(20));"
#         cur.execute(strSQL)
#         strSQL="insert into employee values(007,null,'000','yes',null,null,null,null);"
#         cur.execute(strSQL)
#         con.commit()
#     if ("item",) in r:
#         pass
#     else:
#         strSQL = "create table item("\
#                 "barcode varchar(20) primary key,name varchar(20),"\
#                 "category varchar(20),price float(20),"\
#                 "stock int);"
#         cur.execute(strSQL)
#     return con, cur

def main():
    # Initialize session state if not already initialized
    if "logged_in" not in st.session_state:
        st.session_state.logged_in = False

    if "selected_discussion" not in st.session_state:
        st.session_state.selected_discussion = None

    if "page" not in st.session_state:
        st.session_state.page = "user"

    # Check if user is logged in
    if not st.session_state.logged_in:
        display_login_page()
    else:
        if st.session_state.selected_discussion:
            display_discussion_page()
        else:
            display_user_page()

if __name__ == "__main__":
    main()
