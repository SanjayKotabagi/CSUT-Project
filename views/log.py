import streamlit as st
from views import home


def load_view(lrobj):
    # if lrobj.login == True:
    #     home.load_view(lrobj)
    st.header("Login :-")
    user = st.text_input("Username")
    pw = st.text_input("Enter Password")
    if st.button("Login Now"):
        if lrobj.login(user,pw) == True:
            home.load_view(lrobj)
        else:
            st.write("Login Failed")
    
    
        
