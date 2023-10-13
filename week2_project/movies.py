#!/usr/bin/python3
"""Find movies on streaming services."""

import os
import urllib.request
import requests
import json

def main():
    
    # Loop to accept input for search parameters
    while True:
        watch_typ_in = input("Do you want to watch a Moive (M) or TV Show (T)?\n")
        if watch_typ_in == "M":
            watch_type = "movie"
            print(f"You chose {watch_type}")
            watch_title = input("What movie do you want to watch?\n")
            break
        elif watch_typ_in == "T":
            watch_type = "show"
            print(f"You chose {watch_type}")
            watch_title = input("What TV show do you want to watch?\n")
            break
        else:
            print("Invalid input: Please use 'M' for movie or 'T' for TV show.")

#    watch_title = input("What movie do you want to watch?\n")
    search_param = [watch_type, watch_title]

    print(search_param)

    url = "https://streaming-availability.p.rapidapi.com/search/title"
    querystring = {"title":"{search_param[1]}","country":"us","{search_param[0]}":"movie","output_language":"en"}
    headers = {
	    "X-RapidAPI-Key": "863afdf1c3msh0418c841b7cb716p1ea8d6jsn31bc3d652f18",
	    "X-RapidAPI-Host": "streaming-availability.p.rapidapi.com"
    }
    response = requests.get(url, headers=headers, params=querystring)

    movie_data.write(response)

    # Opening JSON file
    f = open('movie_data')
 
    # returns JSON object as a dictionary
    movie_data = json.load(f)
 
    # Iterating through the json list
    for i in movie_data['service']:
        print(i)
 
    # Closing files
    f.close()
    movie_data.close()

if __name__ == "__main__":
    main()
