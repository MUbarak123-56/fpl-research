import streamlit as st
import pandas as pd
from langchain.chat_models import ChatOpenAI
from langchain.agents import create_pandas_dataframe_agent
from langchain.agents.agent_types import AgentType

st.set_page_config(page_title='FPL Data Analyst')
st.markdown("<h1 style='text-align: center;'>Welcome to the FPL Data Analyst</h1>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center;'>Hey There, Soccer Friends. Click the link below to chat with our FPL Data Analyst.</h6>", unsafe_allow_html=True)

st.link_button("Click here to be redirected to a new page.", "https://chat.openai.com/g/g-OxrmR8wbw-fantasy-league-analyst")
