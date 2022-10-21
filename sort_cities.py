# Author: Calvin Atkeson
# Date: 11/8/21
# Purpose: Lab 3 sorting cities driver

from city import City
from quicksort import *

# open all files
in_file = open("world_cities.txt", "r")
alpha = open("cities_alpha.txt", "w")
populations = open("cities_population.txt", "w")
latitudes = open("cities_latitude.txt", "w")

# add cities from input file to list
cities = []
for line in in_file:
    strip_city = line.strip()
    split_city = strip_city.split(",")
    cities.append(City(split_city[0], split_city[1], split_city[2], split_city[3], split_city[4], split_city[5]))

# compare population function
# takes in two cities
def compare_population(city1, city2):
    return city1.population > city2.population

# compare name function
# takes in two cities
def compare_alpha(city1, city2):
    return city1.name.lower() <= city2.name.lower()

# compare latitude function
# takes in two cities
def compare_latitude(city1, city2):
    return city1.latitude <= city2.latitude

# sort by name
sort(cities, compare_alpha)
for city in cities:
    alpha.write(str(city) + "\n")

# sort by latitude
sort(cities, compare_latitude)
for city in cities:
    latitudes.write(str(city) + "\n")

# sort by population
sort(cities, compare_population)
for city in cities:
    populations.write(str(city) + "\n")

alpha.close()
populations.close()
latitudes.close()