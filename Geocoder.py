import requests
import pandas as pd
import streamlit as st
from stqdm import stqdm


def geocode(address, country='', city=''):
    api = f"https://nominatim.openstreetmap.org/search.php?q={address}&country={country}&city={city}&format=jsonv2"
    try:
        response = requests.get(api).json()[0]
        return [float(response['lat']), float(response['lon'])]
    except IndexError:
        return [0, 0]


st.title('Geocoder')
file = st.file_uploader('Upload a csv file:', type='csv')

if file:
    df = pd.read_csv(file)
    st.write(df)
    address = st.selectbox("Select a column you'd like to geocode",
                           options=["<select>", *df.columns])

    if address != "<select>":
        stqdm.pandas()
        df['Latitude and Longitude'] = df[address].progress_apply(lambda x: geocode(x))
        df['latitude'] = df['Latitude and Longitude'].apply(lambda x: x[0])
        df['longitude'] = df['Latitude and Longitude'].apply(lambda x: x[1])
        df.drop('Latitude and Longitude', axis=1, inplace=True)
        st.write(df)
