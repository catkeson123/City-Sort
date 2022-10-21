# Author: Calvin Atkeson
# Date: 11/8/21
# Purpose: Lab 3 city driver

from city import City

# file names
in_file_name = "world_cities.txt"
out_file_name = "cities_out.txt"

# open both files
in_file = open(in_file_name, "r")
out_file = open(out_file_name, "w")

#list of cities
cities = []

# add cities from input file to list
for line in in_file:
    strip_city = line.strip()
    split_city = strip_city.split(",")
    cities.append(City(split_city[0], split_city[1], split_city[2], split_city[3], split_city[4], split_city[5]))

# write cities to output file
for city in cities:
    out_file.write(str(city) + "\n")

in_file.close()
out_file.close()









