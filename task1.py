#registration and login form...whenever someone registers,store that details in database then whenever you login,check the details with database 
import streamlit as st
import pymysql
#database connection
conn=pymysql.connect(
    host="localhost",
    user="root",
    password="Shruvan@3",
    database="student_db"
)
#create table 
cursor=conn.cursor()
cursor.execute("CREATE TABLE IF NOT EXISTS users (username VARCHAR(50) PRIMARY KEY, password VARCHAR(50))")

st.sidebar.title("User Authentication App")
menu=st.sidebar.radio("",["🔓Login","🔑Register"])

if menu=="🔑Register":
    st.header("Create New Account")
    with st.form("Register"):
        username=st.text_input("Username:")
        password=st.text_input("Password:",type='password')
        submit=st.form_submit_button("Register")
        res=cursor.execute("SELECT * FROM users WHERE username=%s",(username,))
        if res:
            st.error("username already exists")
        else:
            if submit:
                cursor.execute("INSERT INTO users (username, password) VALUES (%s, %s)", (username, password))
                conn.commit()
                st.success("Account created successfully")
elif menu=="🔓Login":
    st.header("Login To Your Account")
    with st.form("Login"):
        username=st.text_input("Username:")
        password=st.text_input("Password:",type='password')
        submit=st.form_submit_button("Login")
        if submit:
            res=cursor.execute("SELECT * FROM users WHERE username=%s AND password=%s",(username,password))
            if res:
                st.success(f"Welcome,{username}")
                st.snow()
            else:
                st.error("Invalid username or password")
    