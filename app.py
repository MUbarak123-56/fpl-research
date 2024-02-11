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

st.set_page_config(layout='wide', page_title = "FPL Soccer Intelligence", page_icon="⚽")

from st_pages import Page, add_page_title, show_pages

show_pages(
    [
        Page("app.py", name="Home",icon= "🏠"),
        # Can use :<icon-name>: or the actual icon
        Page("pages/business_intelligence.py",name= "Business Intelligence", icon="📰"),
        # The pages appear in the order you pass them
        Page("pages/fpl_analyst.py", name="FPL Analyst", icon="🤖"),
    ]
)

#add_page_title(layout="wide")

from st_pages import show_pages_from_config

show_pages_from_config()
#if st.button("Home"):
#    st.switch_page("app.py")
#if st.button("Business Inelligence"):
#    st.switch_page("pages/business_intelligence.py")
#if st.button("Fantasy League Analyst"):
#    st.switch_page("pages/fpl_analyst.py")

with open("style.css")as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html = True)
        
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

st.markdown("<h1 style='text-align: center;'>⚽ FPL Soccer Intelligence</h1>", unsafe_allow_html=True)
st.markdown("<h5 style='text-align: center;'>Authors: Mubarak Ganiyu, Nitipon 'Tony' Trimaitreepituk</h5>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: red;'>For a great viewing experience, please use dark mode to view this app.</h6>", unsafe_allow_html=True)
st.markdown("<h6 style='text-align: center; color: red;'>Use the sidebar to navigate to other pages.</h6>", unsafe_allow_html=True)

st.header("Introduction")
st.write("""
    Welcome to "FPL Soccer Intelligence," a comprehensive analysis project that delves deep into the heart of English Premier League soccer. Our journey begins with the vibrant and competitive spirit of the league, where every game is a story, and every player, a potential maestro orchestrating moments of magic on the pitch. This project is born out of a passion for the beautiful game and a curiosity to understand the dynamics that govern team performances and player contributions through data-driven insights.
    
    The Premier League, known for its intensity and unpredictability, offers a rich dataset for analysis. By examining data from the latest seasons, including the ongoing 2023-2024 season, our goal is to explore trends that lie beneath the surface. We leverage data from lesague outcomes and the Fantasy Premier League (FPL) app, a platform that scores player performances weekly, to draw comparisons and contrasts that reveal more than just the scoreline.
    
    Our project seeks to provide fans, analysts, and enthusiasts with insights that enhance their understanding and appreciation of the league. Whether you're a die-hard supporter, a fantasy league competitor, or simply a lover of soccer, "FPL Soccer Intelligence" invites you to explore the numbers behind the drama, the strategies, and the sheer unpredictability that make the Premier League one of the most exciting sports leagues in the world.
    
    Our app has two focus areas: Business Intelligence and Chatbot Development.
    """)
#st.subheader("Analyzing Premier League Outcomes and FPL Data")

st.header("FPL Business Intelligence Reporting")
st.write("""
         We use Tableau, a business intelligence platform to visualize players' performance points according to the Fantasy Premier League app 
         and the overall team performance represented by the actual Premier League table. 
         It is divided into three parts as followed:
         """)

# FPL Timeline Analysis
st.subheader("1. FPL performance points Timeline Analysis")
st.write("""
         This section is a dynamic line graph that represents the progress of accumulative performance points of all premier league players in a season.
         There is a slider for the users to inspect the total performance points at any specific time.
         The graph contains data across 4 seasons from 2020 to the current season; they are separated into four graphs that you can select from the drop-down menu.
         There is also another drop-down menu that allows users to select only some positions to compare the performance of players in specific positions: 
         Defenders (DEF), Forwards (FWD), Goalkeepers (GK), and Midfielders (MID). The visualization highlights trends, 
         patterns, and anomalies over time, providing insights into player performance and consistency.
         """)

# FPL Ranking Insights
st.subheader("2. FPL Ranking Insights")
st.write("""
         The FPL Ranking tab offers a current-season snapshot of individual player rankings within the FPL. 
         It showcases a bar chart listing players by their accrued FPL points, revealing the standout performers. 
         The interface includes club logos, suggesting interactive elements that allow users to filter rankings by team. 
         This real-time leaderboard is instrumental for identifying top players in the particular Premier League season.
         There is a slider, a drop-down menu to select the season, and a filter to select interested positions that work similarly to the ones in the Timeline Analysis.
         """)

# FPL and Premier League Comparison
st.subheader("3. FPL and Premier League Comparison")
st.write("""
         In our third section, we investigate the correlation between total FPL points of all the players in the team and the actual Premier League team performance. 
         Using a scatter plot juxtaposed with team badges against their league positions, we analyze whether FPL points are 
         indicative of a team's capacity to excel in the Premier League. This analysis underscores the complexity of football 
         performance metrics, showing that FPL points, while reflective of individual prowess, do not always correspond to a 
         team's league success. It is also possible that some teams with high total FPL points, but with low Premier League ranking perform inconsistently.
         """)

# Add your Tableau embed code or Streamlit components to display the visualizations
# For example:
# st.tableau_chart("https://public.tableau.com/views/YourVizName/DashboardName")

# Ensure you replace 'YourVizName/DashboardName' with the actual path to your Tableau visualization


st.header("FPL Analyst Chatbot")
st.write("""FPL Analyst is a specialized version of ChatGPT designed to assist users in selecting players for their Fantasy Premier League (FPL) teams. It operates by providing recommendations for player selection based on a detailed analysis of historical performance data and the most recent trade information within and outside the Premier League. Utilizing a custom dataset, FPL Analyst offers personalized advice by examining patterns, player statistics, match outcomes from previous games, and the latest transfer activities. This enables users to make informed decisions for their fantasy teams.
            FPL Analyst guides users in understanding player strengths, weaknesses, overall impact on past matches, and implications of recent transfers. It ensures users have the insights needed to select the most effective players for their fantasy teams. The advice provided by FPL Analyst is grounded in detailed data analysis, focusing on helping users optimize their FPL strategies and improve their standings in the league.""")

# References Section
st.header("References")
st.markdown("""
    The insights presented in this project are based on data sourced from:
    - Premier League game and player performance data: [Excel For Soccer](https://www.excel4soccer.com/download/)
    - Fantasy Premier League data and analysis: [Fantasy-Premier-League on GitHub](https://github.com/vaastav/Fantasy-Premier-League)
    """)
#new_data = data_load()
#st.dataframe(df.head())

st.write("For more information, click the link below 👇 to check our GitHub repo.")
st.link_button("GitHub Repo", "https://github.com/MUbarak123-56/fpl-research")
    

#if __name__ == '__main__':
#    run()
