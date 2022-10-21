# Author: Calvin Atkeson
# Date: 11/8/21
# Purpose: Lab 3 city class

class City:
    # initial function
    # takes in the parameters given in the lab
    def __init__(self, country_code, name, region, population, latitude, longitude):
        self.country_code = str(country_code)
        self.name = str(name)
        self.region = str(region)
        self.population = int(population)
        self.latitude = float(latitude)
        self.longitude = float(longitude)

    # string function
    # no parameters
    def __str__(self):
        return self.name + "," + str(self.population) + "," + str(self.latitude) + "," +str(self.longitude)
