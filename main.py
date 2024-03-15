import streamlit as st
from user_page import display_user_page
from login import display_login_page

# Streamlit app
def main():
    st.title("Discussion Forum")

    # Check if user is logged in
    if not st.session_state.get("logged_in"):
        display_login_page()
    else:
        display_user_page()



if __name__ == "__main__":
    main()
