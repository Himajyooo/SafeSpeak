import streamlit as st

# Function to display user page
def display_admin_page():
    st.title("Admin Page")
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    st.write(f"Welcome, Admin")

    # Display different discussions
    st.header("Reports")
    if st.button("View Reports"):
        st.write(f"Detailed report of users")

    col1, col2 = st.columns([7, 1])
    with col2:
        if st.sidebar.button("Logout", key="logout_button"):
            st.session_state.logged_in = False
            st.session_state.admin = False
            st.rerun()
