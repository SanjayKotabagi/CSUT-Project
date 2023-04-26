import streamlit as st
import utils as utl
from views import log, nmapgui, urlscanner, aip, home, misc, reg
from logic import login_register as lr



st.set_page_config(layout="wide")
utl.inject_custom_css()
utl.navbar_component()
lrobj = lr.Log_Reg()


def navigation():
    route = utl.get_current_route()
    if route == "home":
        home.load_view(lrobj)
    elif route == "nmapgui":
        nmapgui.load_view(lrobj)
    elif route == "urlscanner":
        urlscanner.load_view(lrobj)
    elif route == "misc":
        misc.load_view(lrobj)
    elif route == "aip":
        aip.load_view(lrobj)
    elif route == "login":
        log.load_view(lrobj)
    elif route == "reg":
        reg.load_view(lrobj)
    elif route == None:
        home.load_view(lrobj)
        
navigation()