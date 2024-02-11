import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(layout='wide')
st.header("FPL Business Intelligence Report")
#st.set_page_config(theme="light")
HtmlFile = open("fpl.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, width = 1400, height = 900)
