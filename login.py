import streamlit as st
from admin_page import display_admin_page
from database import create_connection
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
            cur.execute("SELECT userid FROM login WHERE username = %s AND pass = %s", (user, password))
            user_id = cur.fetchone()[0]
            user_name = user
            st.session_state.user_id=user_id
            st.session_state.username=user_name
            st.rerun()
        else:
            st.error("Incorrect username or password")
        con.close()
    elif st.button("No account?\nSign Up"):
        st.session_state.logged_in = True
        st.session_state.signup = True
        st.rerun()
  
