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

if st.button("Home"):
    st.switch_page("app.py")
if st.button("Business Inelligence"):
    st.switch_page("pages/business_intelligence.py")
if st.button("Fantasy League Analyst"):
    st.switch_page("pages/fpl_analyst.py")
 
st.image("fpl_icon.png", width = 200)
#@st.cache_data()
#def data_load():
#@st.cache_data()
#df = pd.read_excel("data/fpl_data/full_df.xlsx")
 #   return df

st.markdown("<h1 style='text-align: center; color: white;'>Soccer Maestros in England</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center; color: white;'>Authors: Mubarak Ganiyu, Nitipon 'Tony' Trimaitreepituk</h5>", unsafe_allow_html=True)
st.header("Introduction")
st.write("""
    Welcome to "Soccer Maestros in England," a comprehensive analysis project that delves deep into the heart of English Premier League soccer. Our journey begins with the vibrant and competitive spirit of the league, where every game is a story, and every player, a potential maestro orchestrating moments of magic on the pitch. This project is born out of a passion for the beautiful game and a curiosity to understand the dynamics that govern team performances and player contributions through data-driven insights.
    
    The Premier League, known for its intensity and unpredictability, offers a rich dataset for analysis. By examining data from the latest seasons, including the ongoing 2023-2024 season, our goal is to uncover patterns, trends, and anomalies that lie beneath the surface. We leverage data from actual match outcomes and the Fantasy Premier League (FPL) app, a platform that scores player performances weekly, to draw comparisons and contrasts that reveal more than just the scoreline.
    
    From analyzing team forms and expected goals to exploring the intricate relationship between real match results and FPL performance scores, our project seeks to provide fans, analysts, and enthusiasts with insights that enhance their understanding and appreciation of the league. Whether you're a die-hard supporter, a fantasy league competitor, or simply a lover of soccer, "Soccer Maestros in England" invites you to explore the numbers behind the drama, the strategies, and the sheer unpredictability that make the Premier League one of the most exciting sports leagues in the world.
    """)
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
st.markdown("""
    The data used in this analysis were sourced from the following:
    - Premier League game and player performance data: [Excel For Soccer](https://www.excel4soccer.com/download/)
    - Fantasy Premier League data and analysis: [Fantasy-Premier-League on GitHub](https://github.com/vaastav/Fantasy-Premier-League)
    """)
st.markdown("<h5 style='text-align: left; color: white;'>Our project analyzes data from the English Premier League Soccer. We used both actual teams results and"
    + "the data from the fantasy premier league app(FPL).</h5>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: left; color: white;'>We analyzed team results to make prediction on the outcome of future games. We used the players' scores"
    " from the fantasy premier league app to visualize the ability of each player from the start to the end of each season (2021-2024).</h5>", unsafe_allow_html=True)

#new_data = data_load()
#st.dataframe(df.head())
    

#if __name__ == '__main__':
#    run()
