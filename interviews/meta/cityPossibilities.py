"""
Given a list of city names and their corresponding populations, write a 
program to output a city name subject to the following constraint: 
the probability of the program to output a city's name is 
based on its population divided by the sum of all cities' population. 
Assume the program will be repeatedly called many times.

Example input
    NY: 7M
    SF: 5M
    LA: 8M

Example output
    NY
"""

from random import randint
from typing import List


class City:
    def __init__(self, name: str, population: int):
        self.name = name
        self.population = population
        self.start = None
        self.end = None


def __getTotalPopulation(cities):
    totalPopulation = 0

    for city in cities:
        totalPopulation += city.population

    return totalPopulation


def __getCity(cities: List[City], totalPopulation: int):
    randInt = randint(1, totalPopulation)
    accum = 1

    for city in cities:
        limit = accum + city.population

        if accum <= randInt <= limit:
            return city.name

        accum = limit


def getCities(cities, numOfCities):
    totalPopulation = __getTotalPopulation(cities)

    for _ in range(numOfCities):
        print(__getCity(cities, totalPopulation))


""" NOTES

//The probability to generate NY is 7/20, SF is 1/4.

{
    city: String
    population: int
}

{
    city: NY
    population: 7000000
}

{
    city: SF
    population: 5000000
}

{
    city: LA
    population: 8000000
}

totalPopulation = 20000000


5 // 20


1 / 4

f"

num = 15
accum = 12
limit = accum + population = 20

{
    city: NY
    population: 7
}

{
    city: SF
    population: 5
}

{
    city: LA
    population: 8
}
"""
