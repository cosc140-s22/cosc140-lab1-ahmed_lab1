#
# Name: Ahmed Kamran
# Collaborator(s): none
#


'''
Write a program that computes and prints the great circle distance on Earth 
between any two different latitude/longitude coordinates, known as the Haversine distance.
'''

import math


lat1, lon1, lat2, lon2 = float(input("Give me a lat: ")), float(input("Give me a lon: ")), float(input("Give me another lat: ")), float(input("Give me another lon: "))
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

print(F"The Haversine distance from {(round(lat1,2),round(lon1,2))} to {(round(lat2,2),round(lon2,2))} is {d} {'km' if (unit=='k') else 'mi'}")
