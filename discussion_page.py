import streamlit as st
from database import create_connection
# Function to display discussion page
def display_discussion_page():
    con,cur =  create_connection()
    d_name=st.session_state.selected_discussion
    d_id =st.session_state.d_id
    st.title(f"Discussion:{d_name}")# {selected_discussion}")
    # Load custom CSS
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    user_id=st.session_state.user_id


    # Display comments for the selected discussion (you can retrieve comments from your database)
    #print(selected_discussion)
    if d_name:
        #st.write("Here is the content of the selected discussion.")
        st.header("Comments")
        d_name=tuple(d_name)
        #cur.execute("select username, comment_desc from comment where discussion_id=%s",d_name)
        

        # Placeholder for displaying comments
        # comments = []  # List to store comments, assuming comments are retrieved from a database
        # # Display existing comments
        # for comment in comments:
        #     st.write(comment)
        # # Comment submission form
        
        new_comment = st.text_area("Write your comment here")
        if st.button("Post Comment"):
            # Placeholder for submitting the comment to your database
            cur.execute("insert into comment (discussion_id,comment_desc,userid) values (%s,%s,%s)",(d_id,new_comment,user_id))
            con.commit()
            st.success("Comment posted successfully")
            #comments.append(new_comment)    
        if st.button("Back"):
            st.session_state.selected_discussion = None
            st.session_state.page = "user"
            st.rerun()
    else:
        st.error("Discussion not selected")
