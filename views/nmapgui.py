import streamlit as st
from logic import nmaplogic

def load_view(lrobj):
    st.header("NMAP Network Scanner Tool")

    #Take input from user for target address 
    target = st.text_input("Enter Target Address or IP")
    port_option = st.selectbox('Port Selection',('1-1024', 'Most Common', 'Enter Manually'))
    if port_option == '1-1024':
        ports = 'All'
    elif port_option == 'Most Common':
        ports = 'Common'
    elif port_option == 'Enter Manually':
        ports = 'Manual'

    if ports == 'Manual':
        ports_user = []
        ports_user = st.text_input("Enter Ports seprated by commas Eg : 20,80,81")
        try:
            ports = ports_user.split(',')
            ports = [int(x) for x in ports]
            if len(ports) == 1:
                ports = ports[0]
        except:
            st.write("Enter Ports")
            
    elif ports == 'Common':
        ports = [20,21,80,81]
    else:
        ports = 1024


    if st.button("Get Details"):
        res = nmaplogic.get_ports(target,ports)
        st.table(res)

        # if st.button("Save File"):
        #     filename = st.text_input("Enter file Name")
        #     f = open(filename, "w")
        #     f.write(res)
        #     f.close()
