import requests
import json

class GetPrograms:

    def get_programs(self):
        URL = "https://data.cityofnewyork.us/resource/uvks-tn5n.json"

        response = requests.get(URL)
        return response.content

# Create an instance of GetPrograms and call the get_programs() method
programs = GetPrograms().get_programs()

# Print the JSON response
print(programs)
