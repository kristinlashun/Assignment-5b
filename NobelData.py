# Author: Kristin Towns
# GitHub username: kristinlashun
# Date: 2/7/2024
'''
This Python class, NobelData, is designed to interact with a 
JSON file containing Nobel Prize data, allowing users to search for Nobel laureates based on the year and category of the prize. 
Upon initialization, the class reads and stores the data from a local file named 'nobels.json', making this data accessible for queries.
'''
import json

class NobelData: 
    def __init__(self):
        self.__data = self.__read_data()

    def __read_data(self):
        try:
            with open('nobels.json', 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            print("The file nobels.json was not found.")
            return[]

    def search_nobel(self, year, category): 
        surnames = []
        for prize in self.__data.get('prizes', []):
            if prize.get('year') == year and prize.get('category') == category:
                for laureate in prize.get('laureates', []):
                    surnames.append(laureate.get('surname'))
        return sorted(surnames)
