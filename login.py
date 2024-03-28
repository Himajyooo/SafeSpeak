import streamlit as st
from admin_page import display_admin_page

# Function to display login page
def display_login_page():
    # Custom CSS for background color and styles
    custom_css = """
    <style>
        body {
            background-color: #dbe9f7; /* pastel blue */
        }
        .stApp {
            background-color: #dbe9f7; /* pastel blue */
        }
        .stTextInput>div>div>input {
            background-color: #f0f3f5; /* lighter shade */
        }
        .stButton>button {
            background-color: #001f3f; /* dark navy blue */
            color: white;
            border-radius: 5px;
            padding: 0.5rem 1rem;
            border: none;
            transition: background-color 0.3s;
        }
        .stButton>button:hover {
            background-color: #003366; /* slightly darker navy blue on hover */
        }
        .st-error {
            color: #dc3545; /* error message color */
        }
    </style>
    """
    st.markdown(custom_css, unsafe_allow_html=True)

    st.title("Login")

    email = st.text_input("Email")
    password = st.text_input("Password", type="password")

    if st.button("Login"):
        # Check if email and password are correct (dummy check)
        if email == "user@example.com" and password == "password":
            st.session_state.logged_in = True
            st.session_state.page = "user"
            st.experimental_rerun()
            
        elif email == "admin@gmail.com" and password == "admin":
            display_admin_page()
        else:
            st.error("Invalid email or password")

# Call the function to display login page
display_login_page()
