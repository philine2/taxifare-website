import streamlit as st

import datetime

import requests
import pandas as pd

st.set_page_config(
            page_title="Taxifare",
            layout="wide", # wide
            initial_sidebar_state="auto")

'''
#TaxiFareModel front
'''

st.markdown('''
Remember that there are several ways to output content into your web page...

Either as with the title by just creating a string (or an f-string). Or as with this paragraph using the `st.` functions
''')

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




columns = st.columns(6)

date = columns[0].date_input("pickup date")

time =columns[1].time_input('time')

pickup_lat = columns[2].number_input('Insert a pickup latitude', value = -73.83)
pickup_lon = columns[3].number_input('Insert a pickup longitude',value = 42.8)

dropoff_lat = columns[4].number_input('Insert a dropoff latitude',value = -73.4)
dropoff_lon = columns[5].number_input('Insert a dropoff longitude', value = 42.2)

passengers = st.slider('passenger number', 1, 4, 1)




'''
## Once we have these, let's call our API in order to retrieve a prediction

See ? No need to load a `model.joblib` file in this app, we do not even need to know anything about Data Science in order to retrieve a prediction...

🤔 How could we call our API ? Off course... The `requests` package 💡
'''

url = 'https://taxifare.lewagon.ai/predict'

if url == 'https://taxifare.lewagon.ai/predict':

    st.markdown('Maybe you want to use your own API for the prediction, not the one provided by Le Wagon...')

'''

2. Let's build a dictionary containing the parameters for our API...


3. Let's call our API using the `requests` package...

4. Let's retrieve the prediction from the **JSON** returned by the API...

## Finally, we can display the prediction to the user
'''
var = datetime.datetime.combine(date, time)

params = {
    'dpickup_datetime' : var,
    'pickup_latitude' : pickup_lat,
    'pickup_longitude' : pickup_lon,
    'dropoff_latitude' : dropoff_lat,
    'dropoff_longitude' : dropoff_lon,
    'passenger_count' : passengers

}
st.write(params)

response = requests.get(url, params=params)

response
