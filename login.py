import streamlit as st
from admin_page import display_admin_page
import mysql.connector
from user_page import display_user_page
from discussion_page import display_discussion_page
#from signup import display_signup_page

def create_connection():
    #Used to connect Python with MySQL
    con = mysql.connector.connect(\
          host = "localhost",\
          user = "root",
          password = "may@2023")
    cur = con.cursor()
    strSQL = "show databases"
    cur.execute(strSQL)
    r = cur.fetchall()
    if ("safespeak",) in r:
        pass
    else:  #Till here
        strSQL = "create database safespeak;"
        cur.execute(strSQL)
    strSQL = "select database();"
    cur.execute(strSQL)
    r = cur.fetchall()
    if r in ("safespeak",):
        pass
    else:
        strSQL = "use safespeak;"
        cur.execute(strSQL)
    strSQL = "show tables;"
    cur.execute(strSQL)
    r = cur.fetchall()
    if ("login",) in r:
        pass
    else:
        strSQL = "create table login("\
                "userid int(5) primary key,username varchar(20),pass varchar(20),email varchar(20));"
        cur.execute(strSQL)
        strSQL="insert into login values(001,'user','password','user@email.com');"
        cur.execute(strSQL)
        con.commit()
    # if ("item",) in r:
    #     pass
    # else:
    #     strSQL = "create table item("\
    #             "barcode varchar(20) primary key,name varchar(20),"\
    #             "category varchar(20),price float(20),"\
    #             "stock int);"
    #     cur.execute(strSQL)
    return con, cur
# Function to display login page
def display_login_page():
    create_connection()
    # Streamlit app
    st.title("SafeSpeak: Express Your Views")
    # Load custom CSS
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.title("Login")

    user = st.text_input("User Name")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        con,cur=create_connection()
        q="select * from login where username=%s and pass=%s;"
        cur.execute(q,(user,password))
        r=cur.fetchone()
        # Check if email and password are correct (dummy check)
            
        if user == "admin@gmail.com" and password == "admin":
            display_admin_page()
        elif r is not None:
            st.session_state.logged_in = True
            st.session_state.page = "user"
            st.rerun()
        else:
            st.error("Invalid email or password")
        con.close()
    elif st.button("No account?\nSign Up"):
        st.session_state.logged_in = True
        st.session_state.signup = True
        st.rerun()
        #display_signup_page()
            

# Call the function to display login page
#display_login_page()   
