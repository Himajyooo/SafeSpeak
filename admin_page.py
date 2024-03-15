import streamlit as st

# Function to display user page
def display_admin_page():
    st.title("Admin Page")
    st.write(f"Welcome, Admin")

    # Display different discussions
    st.header("Reports")
    if st.button("View Reports"):
        st.write(f"Detailed report of users")

