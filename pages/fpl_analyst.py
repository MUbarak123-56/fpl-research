import streamlit as st
import pandas as pd
import base64

st.set_page_config(page_title='FPL Analyst')
st.markdown("<h1 style='text-align: center;'>📈 🤖 Welcome to the FPL Analyst</h1>", unsafe_allow_html=True)

st.write("Our chatbot was built using GPT Builder by ingesting FPL data for it to understand while drawing insights from current trends in the Premier League and soccer world. It is designed to assist users with having the best FPL experience by recommending how they can craft their team. This apps focuses heavily on historical performance for recommendation. It is still in its beta testing phase and might not be fully accurate.")
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

st.markdown("<h6 style='text-align: center;'>Hey There, Soccer Friends. Click the link below to chat with our FPL Data Analyst.</h6>", unsafe_allow_html=True)
st.link_button("Click here to interact with FPL Analyst.", "https://chat.openai.com/g/g-OxrmR8wbw-fpl-analyst")
