import streamlit as st
import requests
from datetime import datetime
import time
from geopy.geocoders import Nominatim

# Function to check internet connection
def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        return True
    except requests.RequestException:
        return False

# Function to get user's country and capital using ipinfo.io
def get_capital():
    try:
        my_ip = requests.get("https://ident.me/", timeout=10).content.decode("UTF-8")
        url = f"https://ipinfo.io/{my_ip}/json"
        response = requests.get(url, timeout=10)
        response.raise_for_status()
        result = response.json()
        
        country = result.get("country", "Unknown")
        city = result.get("city", "Unknown")
        lat, lon = map(float, result["loc"].split(","))

        return lat, lon, country

    except requests.exceptions.RequestException as e:
        st.error(f"⚠ Error fetching location: {e}")
        return None, None, "Unknown"

# Function to get ISS details
def get_details():
    try:
        request_details = requests.get("https://api.wheretheiss.at/v1/satellites/25544", timeout=10)
        request_details.raise_for_status()
        return request_details.json()
    except requests.exceptions.RequestException as e:
        st.error(f"⚠ Error fetching ISS details: {e}")
        return None

# Function to get ISS pass times
def get_passes(lat, lon):
    try:
        request_passes = requests.get(f'https://api.wheretheiss.at/v1/satellites/25544/positions?latitude={lat}&longitude={lon}&timestamps={int(time.time())}&units=kilometers', timeout=10)
        request_passes.raise_for_status()
        return request_passes.json()
    except requests.exceptions.RequestException as e:
        st.error(f"⚠ Error fetching ISS pass times: {e}")
        return None

# Function to get people currently in space
def get_people():
    try:
        people = requests.get("http://api.open-notify.org/astros.json", timeout=10)
        people.raise_for_status()
        return people.json()
    except requests.exceptions.RequestException as e:
        st.error(f"⚠ Error fetching people in space: {e}")
        return None

# Streamlit UI
st.title("🚀 ISS Tracker")

if connection():
    details = get_details()
    lat, lon, country = get_capital()
    passes = get_passes(lat, lon)
    people = get_people()

    if details:
        st.subheader("🌍 ISS Current Location")
        st.write(f"**Latitude:** {details['latitude']}")
        st.write(f"**Longitude:** {details['longitude']}")
        st.write(f"**Altitude:** {details['altitude']} km")
        st.write(f"**Velocity:** {details['velocity']} km/h")
    
    if people:
        st.subheader("🧑‍🚀 People Currently in Space")
        st.write(f"**Number of people in space:** {people['number']}")
        for p in people['people']:
            st.write(f"- {p['name']}")
    
    if details:
        st.subheader("🗺️ ISS Current Location on Map")
        google_maps_url = f"https://maps.google.com/?q={details['latitude']},{details['longitude']}&ll={details['latitude']},{details['longitude']}&z=3"
        st.write(f"[View ISS Location on Google Maps]({google_maps_url})")
else:
    st.error("⚠ No internet connection. Please check your connection and try again.")
