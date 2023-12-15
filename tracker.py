from geopy.geocoders import Nominatim
from prettytable import PrettyTable
from datetime import datetime
import requests
import time
import os





def connection(url='http://www.google.com/', timeout=5):
    try:
        req = requests.get(url, timeout=timeout)
        req.raise_for_status()
        return True
    except requests.HTTPError as e:
        print("Checking internet connection failed, status code {0}.".format(
        e.response.status_code))
    except requests.ConnectionError:
        print("No internet connection available.")
    return False

def get_details():

    request_deatils = requests.get("https://api.wheretheiss.at/v1/satellites/25544").json()
    value_list = []
    for i, v in request_deatils.items():
        if i in ['name', 'id', 'units', 'units']:
            pass
        else:
            value_list.append(str(v)) 

    return value_list
            
def get_capital():

    my_ip = requests.get("https://ident.me/").content.decode("UTF-8")
    url = ("https://tools.keycdn.com/geo.json?host={}").format(my_ip)
    result = requests.get(url).json()
    country = result["data"]["geo"]["country_name"]
    
    url2 = 'https://restcountries.eu/rest/v2/name/{}?fields=capital'.format(country)

    capital = requests.get(url2).json()[0]
    for _k, v in capital.items():

        return [v , country]
    
   
def get_coordinates():

    global capital
    capital = get_capital()[0]
    country = get_capital()[1]

    coordinates = requests.get('https://geocode.xyz/{0},{1}?json=1'.format(capital, country)).json()

    coordinates_list = []
    for k, v in coordinates.items():
        if k == 'latt':
            coordinates_list.append(v)
        if k == 'longt':
            coordinates_list.append(v)
    
    return coordinates_list

def get_passes():

    try:
        lat = get_coordinates()[1]
        lon = get_coordinates()[0]
        request_passes = requests.get('http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(lat, lon)).json()

        return request_passes

    except IndexError:
        geolocator = Nominatim(user_agent="ISS-Tracker")
        location = geolocator.geocode(capital)
        lat = location.latitude
        lon = location.longitude
        request_passes = requests.get('http://api.open-notify.org/iss-pass.json?lat={}&lon={}'.format(lat, lon)).json()

        return request_passes

def get_people():

    people = requests.get("http://api.open-notify.org/astros.json").json()

    return people

def main():

    details = get_details()

    t = datetime.now()
    current_time = t.strftime("%Y-%m-%d %H:%M:%S")
    print("Your local date & time: " + current_time)
    
    station_time = datetime.utcfromtimestamp(int(details[6]))
    print("Space station date & time: " + str(station_time) + " " + "(UTC)" + "\n")

    if details[4] == 'eclipsed':
        print("The ISS is in Earth's shadow.\n")
    else:
        print("The ISS is in daylight.\n")

    x = PrettyTable()

    x.field_names = ["Latitude", "Longitude", "Altitude (Km)", "Velocity (Km\h)", "Footprint"]
    x.add_row([details[0], details[1], details[2], details[3], details[5]])
    print(x)

    capital, country = get_capital()[0], get_capital()[1]
    passes = get_passes()

    print('\n'"Upcoming ISS passes for " + capital + "," + country + ":")
    print("Number of passes: " + str(passes["request"]["passes"]) + '\n')
    for x in passes["response"]:
        p = time.ctime(x["risetime"])
        print(p + " " "|" + " " + "Duration - " + str(x["duration"]) + "s")

    people = get_people()

    print('\n'"Amount of People In Space Right Now: " + str(people["number"]))
    for x in people['people']:
        print(x["name"])

    url = ("https://maps.google.com/?q={0},{1}&ll={0},{1}&z=3").format(details[0], details[1])
    print('\n'"Google Map URL for ISS Current Location: " + url)
    time.sleep(60)

if connection() == True:
    try:
        while True:
            main()
    except(KeyboardInterrupt):
        print("Programme Interrupted")
else:
    quit()
