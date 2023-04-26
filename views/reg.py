import streamlit as st
from views import home


def load_view(lrobj):
    st.header("Register")
    username = st.text_input("Enter Username for Reg")
    password = st.text_input("Enter Strong Password")
    mail = st.text_input("Enter Mail")
    if st.button("Register Now"):
        regres = lrobj.register(username,password,mail)
        if regres == True:
            st.write("Registration Success")
        else:
            st.write(regres)