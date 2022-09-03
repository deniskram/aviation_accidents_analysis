import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import scipy.stats as stats

###
#
# Dashboard for aviation data
# List of accidents by year (using slider)
# Heatmap of accidents by year,month
# Map with accidents by location
# Accidents by aircraft model (pie chart)
# Accidents by phase of flight

###

def draw_accident_map(df):
    loc_df = df.copy()
    map_df = loc_df[['latitude','longitude']].astype(str)
    map_data = map_df[~map_df.latitude.str.contains("N",na=False)]
    map_data = map_data[~map_data.latitude.str.contains("S",na=False)]
    map_data = map_data[~map_data.longitude.str.contains("E",na=False)]

    st.map(map_data.astype(float)[map_data != 'NaN'].dropna()[0:10])

def draw_accid

def draw_dashboard(df):
    draw_map(df)

def clean_data(df):
    df['Location'].fillna("Madagaskar",inplace=True)
    df['Country'].fillna("Madagaskar",inplace=True)
    
    #remove Event.ID
    df.drop(columns=["Event.Id","Accident.Number","Registration.Number","Schedule","Injury.Severity"],inplace=True,errors='ignore');

    #combine aircraft make and model into one feature and encode

    df['FAR.Description'].fillna(value='unknown',inplace=True)

    # Fill NA Lat/Lon with corresponding locations 

    # Fill empty aircraft category with 'unknown'
    df['Aircraft.Category'].fillna(value="unknown",inplace=True)

    #group events by year
    df['year'] = pd.DatetimeIndex(df['Event.Date']).year
    df['month'] = pd.DatetimeIndex(df['Event.Date']).month

    df = df.rename(columns={'Latitude':'latitude','Longitude':'longitude'})
    
    return df

def main():
    st.write("Aircraft accident analysis dashboard")

    # Load data
    df = pd.read_csv('archive/AviationData.csv',encoding='latin-1')

    # clean data
    df_cleaned = clean_data(df)

    # draw dashboard
    draw_dashboard(df_cleaned)


if __name__ == "__main__":
    sns.set_theme()
    main()
