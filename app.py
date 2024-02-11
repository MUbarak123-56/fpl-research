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
from io import BytesIO
import base64
import time

st.set_page_config(layout='wide', page_title = "Soccer Maestros in England")

#if st.button("Home"):
#    st.switch_page("app.py")
#if st.button("Business Inelligence"):
#    st.switch_page("pages/business_intelligence.py")
#if st.button("Fantasy League Analyst"):
#    st.switch_page("pages/fpl_analyst.py")
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

 
#st.image("fpl_icon.png", width = 200)
#@st.cache_data()
#def data_load():
#@st.cache_data()
#df = pd.read_excel("data/fpl_data/full_df.xlsx")
 #   return df

st.markdown("<h1 style='text-align: center;'>⚽ Soccer Maestros in England</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Authors: Mubarak Ganiyu, Nitipon 'Tony' Trimaitreepituk</h5>", unsafe_allow_html=True)
st.header("Introduction")
st.write("""
    Welcome to "Soccer Maestros in England," a comprehensive analysis project that delves deep into the heart of English Premier League soccer. Our journey begins with the vibrant and competitive spirit of the league, where every game is a story, and every player, a potential maestro orchestrating moments of magic on the pitch. This project is born out of a passion for the beautiful game and a curiosity to understand the dynamics that govern team performances and player contributions through data-driven insights.
    
    The Premier League, known for its intensity and unpredictability, offers a rich dataset for analysis. By examining data from the latest seasons, including the ongoing 2023-2024 season, our goal is to explore trends that lie beneath the surface. We leverage data from lesague outcomes and the Fantasy Premier League (FPL) app, a platform that scores player performances weekly, to draw comparisons and contrasts that reveal more than just the scoreline.
    
    Our project seeks to provide fans, analysts, and enthusiasts with insights that enhance their understanding and appreciation of the league. Whether you're a die-hard supporter, a fantasy league competitor, or simply a lover of soccer, "Soccer Maestros in England" invites you to explore the numbers behind the drama, the strategies, and the sheer unpredictability that make the Premier League one of the most exciting sports leagues in the world.
    """)
#st.subheader("Analyzing Premier League Outcomes and FPL Data")
    
    # Data Preparation and Analysis
st.header("Data Preparation and Analysis")
st.write("""For our analysis, we compiled data from various sources, focusing on team performance metrics and individual player scores from the FPL. This involved cleaning the data, handling missing values, and preparing features to understand the dynamics of the game outcomes and player performances.
""")
    

#st.header("FPL Performance Analysis")
#st.write("""We compared the real match outcomes with the performance scores assigned by the FPL app, identifying discrepancies and patterns. This analysis helps in understanding how individual player performances correlate with the overall team success in the league.
#""")
    
# Weekly FPL Points Animation (Placeholder)
st.header("Weekly FPL Points Animation")
st.write("Here, we showcase an animation of the accumulative points from the FPL app received by each player, updated Oon a game to game basis. This visualization highlights the top-performing players throughout the season.")

# References Section
st.header("References")
st.markdown("""
    The insights presented in this project are based on data sourced from:
    - Premier League game and player performance data: [Excel For Soccer](https://www.excel4soccer.com/download/)
    - Fantasy Premier League data and analysis: [Fantasy-Premier-League on GitHub](https://github.com/vaastav/Fantasy-Premier-League)
    """)
#new_data = data_load()
#st.dataframe(df.head())
    

#if __name__ == '__main__':
#    run()
