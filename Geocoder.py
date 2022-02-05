import requests
import pandas as pd
import streamlit as st
from stqdm import stqdm


st.set_page_config(page_title="Geocoder", page_icon="🌍",)

css_style = """
            <style>
            #MainMenu {visibility: hidden;}
            footer {visibility: hidden;}
            </style>
            """

st.markdown(css_style, unsafe_allow_html=True)


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
    address = st.selectbox("Select address column of your file:",
                           options=["<select>", *df.columns])
    start = st.button('Start Geocoding')

    if address != "<select>" and start:
        stqdm.pandas()
        df['Latitude and Longitude'] = df[address].progress_apply(lambda x: geocode(x))
        df['latitude'] = df['Latitude and Longitude'].apply(lambda x: x[0])
        df['longitude'] = df['Latitude and Longitude'].apply(lambda x: x[1])
        df.drop('Latitude and Longitude', axis=1, inplace=True)
        st.write(df)


        @st.cache
        def convert_df(data_frame):
            return data_frame.to_csv().encode('utf-8')


        csv = convert_df(df)
        st.download_button(
            "Download Geocoded CSV",
            csv,
            "Geocoded.csv",
            "text/csv",
            key='download-csv'
        )
