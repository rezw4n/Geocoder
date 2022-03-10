# Geocoder
A geocoder with UI made with Openstreetmap's Nominatim API, Python and Streamlit.
The app is deployed [here](https://share.streamlit.io/rezw4n/geocoder/Geocoder.py)  
![Geocoder](https://raw.githubusercontent.com/rezw4n/Geocoder/master/Animation.gif "Geocoder")

To use it, upload a csv file(size < 200mb) and select the address column of your csv file and start geocoding!

## Setup Locally  
Due to heavy user load, the server may through a timeout error. So it is suggested to use the app locally on your own desktop. You need to have [python](https://www.python.org/) installed and make sure you add it to your path when you install. Then just follow these steps to get up and running.   
- Clone this repository or just download as zip.  
```git clone https://github.com/rezw4n/Geocoder.git```  
- Open the cloned directory.  
```cd Geocoder```  
- Install all the required python packages via pip.  
```pip install -r requirements.txt```  
- Fire up the app.  
```streamlit run Geocoder.py```
