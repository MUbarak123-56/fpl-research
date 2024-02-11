import streamlit.components.v1 as components
import streamlit as st

st.set_page_config(layout='wide')
st.markdown("<h2 style='text-align: center;'>📰 FPL Business Intelligence Report</h2>", unsafe_allow_html=True)

def add_bg(image_file):
        with open(image_file, "rb") as image_file:
            encoded_string = base64.b64encode(image_file.read())
        st.markdown(
        f"""
        <style>
        .stApp {{
            background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
            background-size: cover;}}
         }}
         </style>
         """,
         unsafe_allow_html=True
         )
add_bg("new_pattern.jpg") 

#st.header("FPL Business Intelligence Report")
#st.set_page_config(theme="light")
HtmlFile = open("fpl.html", 'r', encoding='utf-8')
source_code = HtmlFile.read() 
print(source_code)
components.html(source_code, width = 1500, height = 900)
