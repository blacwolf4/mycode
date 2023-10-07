#!/usr/bin/env python3
"""Returning the location of the ISS in latitude/longitude"""
import requests
import datetime
import reverse_geocoder as rg

URL= "http://api.open-notify.org/iss-now.json"
def main():
    resp= requests.get(URL).json()

    #json data import
    lon = resp["iss_position"]["longitude"]
    lat = resp["iss_position"]["latitude"]
    epoch = resp["timestamp"]
    
    #convert epoch to readable date and time
    iss_time=datetime.datetime.fromtimestamp(epoch)
    
    #convert location data via reverse_geocoder
    coords_tuple= (lat, lon)
    result = rg.search(coords_tuple, verbose=False)

    print(f"""As of:
    {iss_time}
    The ISS is currently at:
    {result}
    """)
    #Lat: {lat}
    #Lon: {lon}
    #""")

#epoch=123456789
#print("The epoch is:")
#print(epoch)
#datetime_obj=datetime.fromtimestamp(epoch)
#print("The datetime object is:")
#print(datetime_obj)


if __name__ == "__main__":
    main()

