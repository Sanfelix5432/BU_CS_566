import csv
from heapq import heappush, heappop

# Define the default city and state
DEFAULT_CITY = "Boston"
DEFAULT_STATE = "MA"

# Define the distances between cities
distances = {
    ("Boston", "MA"): 0,
    ("Worcester", "MA"): 45,
    ("Phoenix", "AZ"): 2300,
    ("Tucson", "AZ"): 2700,
    ("San Francisco", "CA"): 3100,
    ("San Diego", "CA"): 2600,
    ("Las Vegas", "NV"): 2500
}

# Define a function to get the distance between two cities
def get_distance(city1, state1, city2, state2):
    if city1 == city2 and state1 == state2:
        return 0
    return distances.get((city1, state1), float('inf')) + distances.get((city2, state2), float('inf'))

# Read the CSV file
packages = []
with open('/Users/12103/Desktop/CS566 HW/Assign 4/packages.csv', 'r') as file:
    reader = csv.reader(file)
    for row in reader:
        package_num, dest_state, dest_city = row
        packages.append((int(package_num), dest_state, dest_city.strip()))

# Use Dijkstra's algorithm to prioritize the packages
priority_queue = []
visited = set()
for package in packages:
    package_num, dest_state, dest_city = package
    if dest_city == DEFAULT_CITY:
        priority = float('-inf')
    else:
        priority = get_distance(DEFAULT_CITY, DEFAULT_STATE, dest_city, dest_state)
    heappush(priority_queue, (priority, package_num))
    visited.add(package)

prioritized_packages = []
while priority_queue:
    priority, package_num = heappop(priority_queue)
    prioritized_packages.append(f"Package: {package_num}")
    
print("Prioritization:")
print(', '.join(prioritized_packages))
