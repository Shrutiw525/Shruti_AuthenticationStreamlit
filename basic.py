import streamlit as st
#title of the app
st.title("Hello,I am Shruti Tiwari")
st.title("This is a title and welcome to anurag uni")

st.divider()

#header of the app
st.header("This is a header")
st.subheader("This is a subheader")

st.divider()

#to display information
st.text("This is a plain text")

st.divider()

#for lines or stars or something
st.markdown("-----------------") 
st.markdown("### this is markdown")
st.markdown("### :red[this is red text]")
st.markdown("**This is bold text**")
st.markdown("*This is italic text*")
st.markdown(" - This is a bullet point \n - this is second one")
st.markdown("<h3 style='color:pink'>Pink Text</h3>",unsafe_allow_html=True)

st.divider()

#for different types of messages(list,numbers,dicts)
st.write(123)
st.write([1,2,3,4,5])
st.write({"name":"shruti","age":20})
st.write("This is a write statement")

st.divider()

# to add captions
st.caption("This is a caption")

st.divider()

#to add code
st.code("print(('hello world'))")
st.code("""
        def hello(a,b):
            return a+b
        """,language='python')

st.divider()

#to add latex--for mathematical expressions
st.latex(r'''a^2+b^2=c^2''')

st.divider()

#divider--visual horizontal line separator
st.divider()

#button 
if st.button("Click Me"):
    st.write("Button Clicked!")
    st.success("Success Message!")
    st.balloons()

st.divider()

#user input
name=st.text_input("Enter your name:")
st.code(f"Hello,{name}!")
if name=="":
    st.warning("Please enter your name")
elif name.replace(" ","").isalpha()==False:
    st.error("Name should only contain alphabets")
else:
    st.success("Valid name entered")

st.divider()

#multitext
comments=st.text_area("Enter your comments:")
st.write("Your comments:",comments)

st.divider()

#checkbox
if st.checkbox("I agree with terms and conditions"):
    st.write("Checkbox is checked")

st.divider()

#radio button
gender=st.radio("Select your gender:",("Male","Female"))
st.write("You are:",gender)

st.divider()

#selectbox
country=st.selectbox("Select your country:",["USA","CANADA","INDIA","UK"])
st.write("You are from:",country)

st.divider()

#multiselect
skills=st.multiselect("Select your skills:",["Python","Java","C++","HTML","AI","Deep learning","ML"])
st.write("Your skills are:",skills)

st.divider()

#slider
age=st.slider("Select your age:",0,100,25)
st.write("Your age is:",age)

st.divider()

#file uploader
up=st.file_uploader("upload your file:")
if up is not None:
    st.success("File uploaded successfully")
    st.write("File name:",up.name)

st.divider()

#forms
with st.form("My_form"): #role of with is--for a block of code inside the form orelse one button gets clicked and it is ended
    fname=st.text_input("Enter your first name:")
    lname=st.text_input("Enter your last name:")
    submit=st.form_submit_button("Submit")
    if submit:
        st.success("form submitted")

with st.form("Login"):
    user=st.text_input("Username:")
    pwd=st.text_input("Password:",type='password')
    login=st.form_submit_button("Login")
    if login:
        st.success(f"Welcome,{user}")
st.divider()
#column--to create columns
col1,col2,col3=st.columns(3)
with col1:
    st.header("col1")
    st.button("col1 button")
with col2:
    st.header("col2")
    st.button("col2 button")
with col3:
    st.header("col3")
    st.button("col3 button")

st.divider()

#container--to group elements together
with st.container():
    st.header("This is inside container")
    st.button("Container button")   
    st.text_input("Container text input")
    st.write("form inside container")
    with st.form("container_form"):
        c_name=st.text_input("Container name:")
        c_submit=st.form_submit_button("Container submit")
        if c_submit:
            st.success(f"Hello,{c_name} from container form")   

st.divider()

#table
data = {
    'Name': ['Anurag', 'Sumit', 'Rohit'],
    'Age': [21, 22, 20],
    'Course': ['B.Tech', 'M.Tech', 'BBA']
}
st.table(data)

st.divider()

#sidebar
st.sidebar.header("This is sidebar")
option=st.sidebar.selectbox("Select an option:",["home","about","contact"])
st.sidebar.write("You selected:",option)

st.divider()

#cache data
@st.cache_data
def load_data():
    return [1,2,3,4]
data=load_data()
st.write("Cached data:",data)