#AM I PAWNED ?
from logic import pawned
import streamlit as st

def load_view(lrobj):
    st.header("AM I PAWNED ? ")

    password = st.text_input("Enter Password")
    res = pawned.get_pawned_password(password)
    if st.button("Check"):
        st.markdown(f"<h6>{res}</h6>",unsafe_allow_html=True)
