#
# Name: Ahmed Kamran
# Collaborator(s): none
#


'''
Write a program that computes and prints the great circle distance on Earth 
between any two different latitude/longitude coordinates, known as the Haversine distance.

Get the coordinates from a geocoding API
'''

import math
import requests


def choose_addr(res):
    '''
        Function that takes a response.json() disctionary from the API and returns the address that fits best
    '''
    valid_res = [data for data in res if all (prop in data for prop in ["lat", "lon", "display_name"])] #Valid responses have a lat, lon and display_name property 
    if (len(valid_res)>1):
        print("Which of these most closely matches your selection? Provide the index [starting at 0] \n")
        for index,r in enumerate(valid_res):
            print(F"{index}) {r['display_name']}")
        return valid_res[int(input("Select address: "))]
    elif(len(valid_res) == 1):
        return valid_res[0]
    else:
        return None
    
def get_coords(addr1, addr2):
    res = choose_addr(requests.get(F'https://nominatim.openstreetmap.org/search?q={addr1}&format=json').json())
    if(res):
        lat1, lon1 = res["lat"], res["lon"]
        res = choose_addr(requests.get(F'https://nominatim.openstreetmap.org/search?q={addr2}&format=json').json())
        if(res):
            lat2, lon2 = res["lat"], res["lon"]
            return (float(lat1), float(lon1), float(lat2), float(lon2))
        else:
            print("Could not find address 2 coordinates")
            return None
    else:
        print("Could not find address 1 coordinates")
        return None

print("I will compute the distance between two coordinates.")
addr1 = input("Give me the first address? ")
addr2 = input("Give me the second address? ")
coords = get_coords(addr1,addr2)

if(coords):
    lat1, lon1, lat2, lon2 = coords
    lat1, lon1, lat2, lon2 = math.radians(lat1), math.radians(lon1), math.radians(lat2), math.radians(lon2)
    unit = input("Do you want the answer in kilometers or miles? Put k for kilometers and m for miles: ").lower()

    # Haversine distance calculation
    dlon = lon2 - lon1
    dlat = lat2 - lat1
    a = math.pow(math.sin(dlat / 2), 2) + math.cos(lat1) * math.cos(lat1) * math.pow(math.sin(dlon / 2), 2)
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))
    R_km = 6367
    R_mi = 3956
    d = (R_km * c) if (unit == "k") else (R_mi * c)

    print(F"The Haversine distance from {addr1} to {addr2} is {round(d,3)} {'km' if (unit=='k') else 'mi'}")
