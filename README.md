# ISS-Tracker - Tracking the International Space Station

ISS Tracker is a Python script that collects real-time information about the International Space Station (ISS) using a **Streamlit Web Interface**. This project utilizes [WTIA](https://wheretheiss.at/w/developer) for ISS details and [Open Notify](http://open-notify.org/Open-Notify-API/) for astronaut data.


## Information Provided

- Real-time ISS location (Latitude, Longitude, Altitude, Velocity).
- Google Map URL for ISS Current Location.
- Number of people currently in space and their names.
- ISS pass times (upcoming ISS passes for your country).
- Automatic updates every **60 seconds**.

## Git Installation
```
# Clone the repo
git clone https://github.com/yourusername/ISS-Tracker.git

# Change to the working directory
cd ISS-Tracker

# Install the requirements
pip install -r requirements.txt
```

## Running the Streamlit App
```
streamlit run iss_tracker.py
```

This will start the Streamlit web app, and you can access it via the local URL displayed in the terminal.

## Support & Contributions
- Please ⭐️ this repository if you find it useful!
- Contributions are welcome! Feel free to open a pull request. 🚀
