#
# Name: Ahmed Kamran
# Collaborator(s): none
#


'''
Write a program that computes and prints the great circle distance on Earth 
between any two different latitude/longitude coordinates, known as the Haversine distance.
'''

lat1, lon1 = (float(input("Give me a lat: ")),
              float(input("Give me a lon: ")))

lat2, lon2 = (float(input("Give me another lat: ")),
              float(input("Give me another lon: ")))

print(F"Coordinates: {(lat1,lon1)} => {(lat2,lon2)}")
