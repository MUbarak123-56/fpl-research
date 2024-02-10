from matplotlib import pyplot
import streamlit as st
import streamlit.components.v1 as components
import PIL
import io
import numpy as np
#import pathlib
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(rc={'axes.facecolor':(0,0,0,0), 'figure.facecolor':(0,0,0,0)})
import pandas as pd

import time

st.image("fpl_icon.png", width = 200)
#@st.cache_data()
#def data_load():
#@st.cache_data()
df = pd.read_excel("data/fpl_data/full_df.xlsx")
 #   return df


st.set_page_config(layout='wide', page_title = "Soccer Maestros in England")
st.markdown("<h1 style='text-align: center; color: white;'>Soccer Maestros in England</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Authors: Mubarak Ganiyu, Nitipon 'Tony' Trimaitreepituk</h5>", unsafe_allow_html=True)
st.header("Introduction")
st.markdown("<h5 style='text-align: left; color: white;'>Our project analyzes data from the English Premier League Soccer. We used both actual teams results and"
    + "the data from the fantasy premier league app(FPL).</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: white;'>We analyzed team results to make prediction on the outcome of future games. We used the players' scores"
    " from the fantasy premier league app to visualize the ability of each player from the start to the end of each season (2021-2024).</h5>", unsafe_allow_html=True)
#new_data = data_load()
st.dataframe(df.head())
    

#if __name__ == '__main__':
#    run()
