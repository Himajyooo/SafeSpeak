import streamlit as st
from database import create_connection
# Function to display discussion page
def display_comments(con, cur):
    sql = "SELECT l.username, c.comment_desc FROM comment c JOIN login l ON c.userid = l.userid JOIN discussion d ON c.discussion_id = d.discussion_id WHERE d.d_name ='discussion1'"
    cur.execute(sql)
    q=cur.fetchall()
    print(q)
    if len(q)==0:
        st.write("No comments posted yet")
    else:
        i=0
        for comments in q:
            st.write(f" {q[i][0]} :  {q[i][1]}")
            i+=1
                
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

    if d_name:
        #st.write("Here is the content of the selected discussion.")
        st.header("Comments")
        display_comments(con,cur)
        
        new_comment = st.text_area("Write your comment here")
        if st.button("Post Comment"):
            # Placeholder for submitting the comment to your database
            user_name = st.session_state.username
            cur.execute("insert into comment (discussion_id,comment_desc,userid) values (%s,%s,%s)",(d_id,new_comment,user_id))
            con.commit()
            st.success("Comment posted successfully")

            st.rerun() 
        if st.button("Back"):
            st.session_state.selected_discussion = None
            st.session_state.page = "user"
            st.rerun()
    else:
        st.error("Discussion not selected")
