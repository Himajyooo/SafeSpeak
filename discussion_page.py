import streamlit as st

# Function to display discussion page
def display_discussion_page():
    st.title(f"Discussion:")# {selected_discussion}")
    
    selected_discussion = st.session_state.selected_discussion
    # Display comments for the selected discussion (you can retrieve comments from your database)
    if selected_discussion:
        st.write("Here is the content of the selected discussion.")
        st.header("Comments")
        # Placeholder for displaying comments

        # Comment submission form
        st.header("Post a Comment")
        new_comment = st.text_area("Write your comment here")
        if st.button("Post Comment"):
            # Placeholder for submitting the comment to your database
            st.success("Comment posted successfully")
        if st.button("Back"):
            st.session_state.selected_discussion = None
            st.session_state.page = "user"
            st.experimental_rerun()
    else:
        st.error("Discussion not selected")
    