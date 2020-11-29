import unittest
import CreateReport
from dataclasses import dataclass


@dataclass()
class City:
    name: str
    total_cases: int
    new_cases: int
    active_cases: int
    total_deaths: int
    new_deaths: int
    total_recovered: int
    new_recovered: int
    total_tests: int
    cases_to_mil: int
    deaths_to_mil: int
    test_to_mil: int
    population: int


def init_city(city):
    city.total_cases = int(input("enter amount of total cases of COVID19 in this city"))
    city.new_cases = int(input("enter amount of new cases of COVID19 in this city"))
    city.active_cases = city.total_cases + city.new_cases
    city.total_deaths = int(input("enter amount of total patient's deaths from COVID19 in this city"))
    city.new_deaths = int(input("enter amount of new patient's deaths from COVID19 in this city"))
    city.total_recovered = int(input("enter amount of total recovered patients from COVID19 in this city"))
    city.total_tests = int(input("enter amount of total tests of COVID19 in this city"))
    city.population = int(input("enter city's population"))
    city.cases_to_mil = (city.total_cases / city.population) * 1000000
    city.deaths_to_mil = (city.total_deaths / city.population) * 1000000
    city.tests_to_mil = (city.total_tests / city.population) * 1000000


class TestCreateReport(unittest.TestCase):
    def test_create_report_function(self):
        self.name = input("enter city's name to enter values to it")
        init_city(self)
        self.assertIsNone(CreateReport.create_report(self), "should be none")
