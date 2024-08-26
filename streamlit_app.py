import streamlit as st

# Define functions for each page
def page1():
    st.title("Page 1")
    st.write("This is the content of page 1.")

def page2():
    st.title("Page 2")
    st.write("This is the content of page 2.")

def page3():
    st.title("Page 3")
    st.write("This is the content of page 3.")

# Create a sidebar for navigation
page = st.sidebar.selectbox("Choose your page", ["Page 1", "Page 2", "Page 3"])

# Display the selected page
if page == "Page 1":
    page1()
elif page == "Page 2":
    page2()
else:
    page3()
