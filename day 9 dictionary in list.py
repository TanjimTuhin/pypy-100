country = input("Enter country name: ")  # Add country name
visits = int(input("Enter number of visits: "))  # Number of visits
list_of_cities = input("Enter cities, separated by commas: ").split(", ")  # Create a list from formatted string

travel_log = [
  {
    "country": "France",
    "visits": 12,
    "cities": ["Paris", "Lille", "Dijon"]
  },
  {
    "country": "Germany",
    "visits": 5,
    "cities": ["Berlin", "Hamburg", "Stuttgart"]
  },
]

# Function to add new countries to the travel_log
def add_new_country(country, visits, cities):
    new_country = {
        "country": country,
        "visits": visits,
        "cities": cities
    }
    travel_log.append(new_country)

# Do not change the code below
add_new_country(country, visits, list_of_cities)
print(f"I've been to {travel_log[2]['country']} {travel_log[2]['visits']} times.")
print(f"My favourite city was {travel_log[2]['cities'][0]}.")
