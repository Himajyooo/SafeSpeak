import streamlit as st
from admin_page import display_admin_page
from user_page import display_user_page
from discussion_page import display_discussion_page

# Function to display login page
def display_login_page():
    # Streamlit app
    st.title("SafeSpeak: Express Your Views")
    # Custom CSS for background color and styles
    # Custom CSS for background color and styles
    custom_css = """
    <style>
        body {
            background-image: url('https://wallpaperboat.com/wp-content/uploads/2019/10/free-website-background-21.jpg'); /* URL of your background image */
            background-size: cover;
            background-repeat: no-repeat;
            background-attachment: fixed;
            background-position: center;
        }
        .stApp {
            background-color: transparent; /* Set app background color as transparent */
            padding: 0; /* Remove padding */
        }
        .stTextInput>div>div>input {
            background-color: #f0f3f5; /* lighter shade */
            color: #001F3F;
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
