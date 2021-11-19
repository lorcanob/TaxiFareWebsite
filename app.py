import streamlit as st
import pandas as pd
import numpy as np
import requests
'''
# TaxiFareModel front
'''

'''
## Here we would like to add some controllers in order to ask the user to select the parameters of the ride

1. Let's ask for:
- date and time
- pickup longitude
- pickup latitude
- dropoff longitude
- dropoff latitude
- passenger count
'''

pickup_datetime = st.text_input('', '2012-10-06 12:10:20', placeholder='Pickup Datetime')

pickup_lat = st.number_input('Pickup Latitude', value=40.71)
pickup_lon = st.number_input('Pickup Longitude', value=-74)
dropoff_lat = st.number_input('Dropoff Latitude', value=40.71)
dropoff_lon = st.number_input('Dropoff Longitude', value=-74)

pass_count = st.selectbox(
     'Number of Passengers',
     (1, 2, 3, 4, 5, 6, 7, 8))

'''
## Once we have these, let's call our API in order to retrieve a prediction
'''

url = 'https://taxifare.lewagon.ai/predict'

params = {
    'key': pickup_datetime,
    'pickup_datetime': pickup_datetime,
    'pickup_longitude': pickup_lon,
    'pickup_latitude': pickup_lat,
    'dropoff_longitude': dropoff_lon,
    'dropoff_latitude': dropoff_lat,
    'passenger_count': pass_count
}

response = requests.get(url, params).json()

pred = response['prediction']


@st.cache
def get_map_data():

    return pd.DataFrame([[pickup_lat, pickup_lon], [dropoff_lat, dropoff_lon]],
                        columns=['lat', 'lon'])


df = get_map_data()

st.map(df)

'''

2. Let's build a dictionary containing the parameters for our API...

3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
st.markdown(f'# Fare prediction: ${round(pred,2)}')
