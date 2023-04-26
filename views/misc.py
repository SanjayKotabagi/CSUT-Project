import streamlit as st
from logic import misclogic

def load_view(lrobj):
    st.header("Miscellaneous")

    st.markdown("<h6>Check Email Reputation : ",unsafe_allow_html=True)
    email = st.text_input("Enter Email Address")
    if st.button("Get Info"):
        res = misclogic.getmailinfo(email)
        if res == 429:
            st.write("Limit Expired")
        else:
            st.table(res)
    
    st.markdown("<h6>Generate Strong Password : ",unsafe_allow_html=True)
    passlen = st.text_input("Enter Password Length")
    try:
        passlen = int(passlen)
    except:
        st.write("Enter Pass Len in numbers")
    if st.button("Get Password"):
        respass = misclogic.genpassword(passlen)
        st.markdown(f"<h6>Password : {respass}",unsafe_allow_html=True)

    st.markdown("<h6>Check Strong Password : ",unsafe_allow_html=True)
    password = st.text_input("Enter Password")
    if st.button("Check Strength"):
        passstrength = misclogic.checkpassword(password)
        st.markdown(f"<h6>{passstrength}. You can use this password.",unsafe_allow_html=True)
