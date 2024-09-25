import requests
from bs4 import BeautifulSoup
import json


def SaveIfChanged(filePath, data):
    try:
        with open(filePath, 'r') as jsonFile:
            existingData = json.load(jsonFile)

        if existingData == data:
            print("No changes detected. Data not saved.")
            return

    except FileNotFoundError:
        print(f"{filePath} not found. Creating a new file.")

    with open(filePath, 'w') as jsonFile:
        json.dump(data, jsonFile, indent=4)

    print(f"Data saved to {filePath}")


def GetCountryDataFromWikipediaTable():
    countriesData = {}

    url = "https://en.wikipedia.org/wiki/List_of_European_Union_member_states_by_population"
    response = requests.get(url)
    soup = BeautifulSoup(response.content, 'html.parser')

    tbody = soup.find('tbody')
    rows = tbody.find_all('tr')

    for row in rows:
        country = row.findNext('a').get_text()
        if country == "European Union":
            continue

        if country not in countriesData:
            countriesData[country] = {}

        cols = row.find_all('td')
        rowData = [col.get_text() for col in cols]

        if not rowData:
            continue

        population = rowData[1]
        percentage = rowData[2]

        populationAsInt = int(population.replace(',', ''))
        percentageAsFloat = float(percentage.split("%")[0])

        countriesData[country]['country_population'] = populationAsInt
        countriesData[country]['country_population_percentage'] = percentageAsFloat

    return countriesData


data = GetCountryDataFromWikipediaTable()
filePath = 'data.json'

SaveIfChanged(filePath, data)
