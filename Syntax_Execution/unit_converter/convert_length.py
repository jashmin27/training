"""
Program 5: Length Converter (KM <-> Miles, Meters <-> Feet)
Concepts used: variables, constants, arithmetic operators
"""

KM_TO_MILES = 0.621371
METER_TO_FEET = 3.28084

km = float(input("Enter distance in kilometers: "))
miles = km * KM_TO_MILES
print(f"{km} km = {miles:.2f} miles")

meters = float(input("Enter distance in meters: "))
feet = meters * METER_TO_FEET
print(f"{meters} m = {feet:.2f} feet")
