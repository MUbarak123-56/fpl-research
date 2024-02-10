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

st.set_page_config(layout='wide', page_title = "Soccer Maestros in England")
st.image("fpl_icon.png", width = 200)
#@st.cache_data()
#def data_load():
#@st.cache_data()
#df = pd.read_excel("data/fpl_data/full_df.xlsx")
 #   return df

st.markdown("<h1 style='text-align: center; color: white;'>Soccer Maestros in England</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Authors: Mubarak Ganiyu, Nitipon 'Tony' Trimaitreepituk</h5>", unsafe_allow_html=True)
st.header("Introduction")
st.subheader("Analyzing Premier League Outcomes and FPL Data")
    
    # Introduction
st.write("""Our project analyzes Premier League games, focusing on data from both sides' last 5 games, including form, expected goals scored, and expected goals conceded. We delve into data from previous seasons (2021-2024), comparing real match results with Fantasy Premier League (FPL) app performance scores. Our findings highlight a correlation between real results and FPL scores, albeit not perfect, showcasing that some teams perform differently in reality compared to their FPL metrics.
""")
    
    # Data Preparation and Analysis
st.header("Data Preparation and Analysis")
st.write("""For our analysis, we compiled data from various sources, focusing on team performance metrics and individual player scores from the FPL. This involved cleaning the data, handling missing values, and preparing features to understand the dynamics of the game outcomes and player performances.
""")
    
# FPL Performance Analysis
st.header("FPL Performance Analysis")
st.write("""We compared the real match outcomes with the performance scores assigned by the FPL app, identifying discrepancies and patterns. This analysis helps in understanding how individual player performances correlate with the overall team success in the league.
""")
    
# Weekly FPL Points Animation (Placeholder)
st.header("Weekly FPL Points Animation")
st.write("Here, we showcase an animation of the accumulative points from the FPL app received by each player, updated weekly. This visualization highlights the top-performing players throughout the season.")

# References Section
st.header("References")
st.markdown("""The data used in this analysis were sourced from the following:
- Premier League game and player performance data: [Excel For Soccer](https://www.excel4soccer.com/download/)""")
st.markdown("<h5 style='text-align: left; color: white;'>Our project analyzes data from the English Premier League Soccer. We used both actual teams results and"
    + "the data from the fantasy premier league app(FPL).</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: white;'>We analyzed team results to make prediction on the outcome of future games. We used the players' scores"
    " from the fantasy premier league app to visualize the ability of each player from the start to the end of each season (2021-2024).</h5>", unsafe_allow_html=True)

#new_data = data_load()
#st.dataframe(df.head())
    

#if __name__ == '__main__':
#    run()
