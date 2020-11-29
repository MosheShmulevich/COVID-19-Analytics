def total_to_mil(city):
    cases_to_mil = (city.total_cases / city.population)*1000000
    deaths_to_mil = (city.total_deaths / city.population)*1000000
    tests_to_mil = (city.total_tests / city.population) * 1000000

def create_report(city):
    print("City name: ", end=city.name)
    print("Total cases: ", end=city.total_cases)
    print("New Cases ", end=city.new_cases)
    print("Active Cases: ", end=city.active)
    print("Total Deaths: ", end=city.total_deaths)
    print("New Deaths: ", end=city.new_deaths)
    print("Total Recovered ", end=city.total_recovered)
    print("New Recovered:", end=city.new_recovered)
    print("Total Tests:", end=city.total_tests)
    print("Total Cases to 1M population: ", end=city.cases_to_mil)
    print("Total Deaths to 1M population: ", end=city.deaths_to_mil)
    print("Total Tests to 1M population: ", end=city.tests_to_mil)
    print("Total Population: ", end=city.population)