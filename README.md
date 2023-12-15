# ISS-Tracker - Tracking the International Space Station

ISS Tracker is a python script to collect real-time information related to the International Space Station (ISS) just from your terminal. This script uses [WTIA](https://wheretheiss.at/w/developer) and [Open Notify](http://open-notify.org/Open-Notify-API/) APIs to get the information related to ISS.

![iaa1](https://user-images.githubusercontent.com/55880211/80864038-98d3e880-8c9d-11ea-9879-da6f73ca2163.gif)

## Information Provided

- Space station date & time.
- Visibility of the space station. 
- Google Map URL for ISS Current Location.
- Number of people in space and their names.
- Automatically refresh data after every 60 seconds.
- ISS pass times (upcoming ISS passes for your country).
- Space station  Latitude, Longitude, Altitude (Km), Velocity (Km\h), Footprint.

## Git Installation
```
# clone the repo
$ git clone https://github.com/sameera-madushan/ISS-Tracker.git

# change the working directory to ISS-Tracker
$ cd ISS-Tracker

# install the requirements
$ pip3 install -r requirements.txt
```
## Usage
```
python tracker.py
```

## Support & Contributions
- Please ⭐️ this repository if this project helped you!
- Contributions of any kind welcome!

## License
ISS Tracker is made with ♥ by [@_\_sa_miya__](https://twitter.com/__sa_miya__) and it is released under the MIT license.

## Special Thanks
Devolopers of [WTIA](https://wheretheiss.at/w/developer) API and [Open Notify](http://open-notify.org/Open-Notify-API/) API --> Used to get real-time information about the ISS.

Devolopers of [REST Countries](https://restcountries.eu/) API --> Used to get capital of countries.

Devolopers of [ident.me](https://ident.me/) website and [IP location finder API](https://tools.keycdn.com/geo) by keycdn  --> Used to identify the country of the users based on their ip address.

Devolopers of [Geocode.xyz](http://geocode.xyz/api) API --> Used to get the cordinates of capitals using Forward Geocoding.



