import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import io 
import requests 
import openpyxl
import streamlit as st 


header = st.beta_container()
user_input = st.beta_container()
output_graphs = st.beta_container()
author_credits = st.beta_container()

with header:
    st.title("Testefjes")
    st.markdown("""
    
    """)

# Fetch Dataset from the New York Times Github Repository
url = 'https://github.com/hskjerping/streamlit-example/blob/2069dd1903af469de5ae92184d5758266011f9f8/camspecs.csv'
s = requests.get(url).content
df = pd.read_csv(io.StringIO(s.decode('utf-8')), parse_dates=True, index_col='date')

with user_input:
    st.sidebar.header('User Selection') 

    # Generating the list for states
    cams_list = []
    counties_list = []

    cams_list = df.cam.unique()
    cams_list.sort()


    cam = st.sidebar.selectbox('Selecct Your Camera:',cams_list) # We define the state variable

    # Generating the list of counties based on the state
    #state = input("Choose a state :")

    df_cams = df[(df.cam == cam)].copy()
   # counties_list = df_cam.county.unique()
    #conties_list = counties_list.sort()

    county = st.sidebar.selectbox('Select your cam:',cams_list) # We define the county variable

    table_days = st.sidebar.slider('Select the number of days you want to be display in the Summary Table. ', min_value = 3, max_value= 15, value= 5, step=1)

    moving_average_day = st.sidebar.slider('How many days to consider for the moving average? ', min_value = 5, max_value = 14, value = 7, step=1)

    # Creating the dataframe for the county
    df_county = df[(df.cam == cam)].copy()

    #Create a new column with new cases
    df_county['ifov'] = df_county.loc[:, 'ifov'].diff()

    #Create a new column for 7-day moving average
    df_county['framerate'] = df_county.loc[:,'framerate']

    #Create a 


