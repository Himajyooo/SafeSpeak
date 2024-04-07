import streamlit as st
from database import create_connection
import time
# Function to display discussion page
def display_comments(con, cur,d_name):
    print(d_name)
    with open("css/comment.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    sql = "SELECT l.username, c.comment_desc FROM comment c JOIN login l ON c.userid = l.userid JOIN discussion d ON c.discussion_id = d.discussion_id WHERE d.d_name =%s"
    cur.execute(sql,(d_name,))
    q = cur.fetchall()
    if len(q) == 0:
        st.write("No comments posted yet")
    else:
        for i, comments in enumerate(q):
            # Apply different background colors based on comment index
            if i % 3 == 0:
                comment_class = "light-blue-bg"
            elif i % 3 == 1:
                comment_class = "medium-blue-bg"
            else:
                comment_class = "dark-blue-bg"
            st.write(f'<div class="comment-container {comment_class}"><span class="comment-text">{comments[0]}: {comments[1]}</span></div>', unsafe_allow_html=True)

def display_discussion_page():
    con,cur =  create_connection()
    d_name=st.session_state.selected_discussion
    d_id =st.session_state.d_id
    user_id=st.session_state.user_id

    st.title(f"Discussion:{d_name}")
    # Load custom CSS
    with open("css/styles.css", "r") as f:
        css = f.read()
    st.markdown(f"<style>{css}</style>", unsafe_allow_html=True)
    
    if d_name:
        #st.write("Here is the content of the selected discussion.")
        st.header("Comments")
        display_comments(con,cur,d_name)
        
        new_comment = st.text_area("Write your comment here")
        if st.button("Post Comment"):
            # Placeholder for submitting the comment to your database
            user_name = st.session_state.username
            cur.execute("insert into comment (discussion_id,comment_desc,userid) values (%s,%s,%s)",(d_id,new_comment,user_id))
            con.commit()
            st.success("Comment posted successfully")
            time.sleep(1)
            st.rerun()
             
        if st.button("Back"):
            st.session_state.selected_discussion = None
            st.session_state.page = "user"
            st.rerun()
    else:
        st.error("Discussion not selected")