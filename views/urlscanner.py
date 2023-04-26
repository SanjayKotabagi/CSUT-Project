import streamlit as st
from logic import urlscan



# 439c27d55859d6e3cbeec33776ef8729d62af602660f8d4b2c6c6cc97d590eb4

def load_view(lrobj):
    st.header("URL Scanner")
    url = st.text_input("Enter URL")
    if st.button("Get report"):
        res = urlscan.get_url_report(url)
        if res != False:
            st.table(res)
        else:
            st.write("Submit the request first. check out this [link](https://pulsedive.com/api/)")
        
