from matplotlib import pyplot
import streamlit as st
import streamlit.components.v1 as components
import PIL
import io
import numpy as np
#import pathlib
import matplotlib.pyplot as plt
import seaborn as sns; sns.set(rc={'axes.facecolor':(0,0,0,0), 'figure.facecolor':(0,0,0,0)})

import time


def run():
    st.set_page_config(layout='wide', page_title = "Soccer Maestros in England")
    
    st.markdown("<h1 style='text-align: center; color: white;'>Soccer Maestros in England</h1>", unsafe_allow_html=True)
    st.markdown("<h5 style='text-align: center; color: white;'>Authors: Mubarak Ganiyu, Nitipon 'Tony' Trimaitreepituk</h5>", unsafe_allow_html=True)
    st.header("Introduction")
    st.write("Hello World")
    

if __name__ == '__main__':
    run()
