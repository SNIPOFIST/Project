# A mini weather forecast project that tells the weather for the place which is given by user as input
# used  api.weatherstack for free 250 api calls for one month
# using get request passing the API key and city name and fetching the data
import requests
import datetime
import streamlit as st


st.title("Weather Forecast using python ☁️🌪")

col1 ,col2 = st.columns(2)

with col1:
    query_val = st.text_input('Enter the city name ', 'New Delhi')
    st.caption(r'Weather forecast at {} currently '.format(query_val)) 


weaather_dict = {'Sunny' : "",
                 'Partly cloudy' :""
                 }
icons = {
    'day' : '⛅️',
    'not_day' : '🌙'
}
def Weather(query_val):
    data = {"access_key": "3cd9b3b9e0b7ae125ce30f4c04397d75",
            "query": query_val}
    # keys of dict params- access_key and query are constant and cannot be changed
    req = requests.get('http://api.weatherstack.com/current', params=data)
    page_response = req.json()
    print(page_response)
    with st.container():
        if page_response['current']['is_day'] == 'yes':
            it_is_day= True
        else:
            it_is_day= False
        icon = icons['day'] if it_is_day else icons['not_day']
        st.subheader("📍{},{} {}".format(page_response['location']['name'], page_response['location']['country'],icon))
        col1, col2, col3 = st.columns(3)
        col1.metric("Temperature", "{}°F".format(page_response['current']['temperature']))
        col2.metric("Wind", "{}mph".format(page_response['current']['wind_speed']))
        col3.metric("Humidity", "{}%".format(page_response['current']['humidity']))
        st.info("Local Time & Date at  {} is {} / {}".format(query_val,page_response['location']['localtime'][11:16] ,page_response['location']['localtime'][0:10]))
        st.info("Currently at {} it is {} ".format(query_val,page_response['current']['weather_descriptions'][0]))
        st.info("Latitude ⇀ {}".format(page_response['location']['lat']))
        st.info("Longitude ⇀ {}".format(page_response['location']['lon']))

Weather(query_val)
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")
st.write("")


