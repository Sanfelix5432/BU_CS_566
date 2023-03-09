import csv
import urllib.request

# define a function to calculate the distance between two cities using their coordinates
def distance(city1, city2):
    return ((city1[0]-city2[0])**2 + (city1[1]-city2[1])**2) ** 0.5

# read the cities from the online CSV file
url = 'https://raw.githubusercontent.com/wagebrite/US-Cities-Database-SQL-CSV/main/us_cities.csv'
response = urllib.request.urlopen(url)
reader = csv.reader(response.read().decode('utf-8').splitlines())
next(reader)  # skip the header row
cities = [(row[1], row[3], float(row[5]), float(row[6])) for row in reader]

# read the packages from the local CSV file
packages = []
with open('/Users/12103/Desktop/CS566 HW/Assign6/package2.csv', newline='') as csvfile:
    reader = csv.reader(csvfile)
    for row in reader:
        packages.append((int(row[0]), row[1], row[2]))

# calculate the shortest delivery path for each package
for package in packages:
    state, city = package[1], package[2]
    start = (42.3601, -71.0589)  # Boston, MA
    end = None
    min_distance = float('inf')
    for i, c in enumerate(cities):
        if state == 'MA' and city == c[1]:  # if the city is in MA, we can deliver directly
            end = c
            break
        elif state != 'MA' and state == c[0]:  # if the city is in the same state, we can deliver directly
            if distance(start, c[2:]) < min_distance:
                min_distance = distance(start, c[2:])
                end = c
    if end is None:  # if there is no city in the same state, we choose the closest city
        for c in cities:
            if distance(start, c[2:]) < min_distance:
                min_distance = distance(start, c[2:])
                end = c
    # print the shortest delivery path for the package
    path = [start, end]
    total_distance = distance(start, end[2:])
    for c in cities:
        if c[1:] == end[1:]:
            break
        elif state == 'MA' and city == c[1]:  # if the city is in MA, we can deliver directly
            path.append(c[2:])
            total_distance += distance(end[2:], c[2:])
            break
        elif state != 'MA' and state == c[0]:  # if the city is in the same state, we can deliver directly
            path.append(c[2:])
            total_distance += distance(end[2:], c[2:])
    # calculate priority based on distance
    priority = 1 / total_distance
    print(f"Shortest path for package {package[0]}:")
    print(f"Start: Boston, MA")
    print(f"End: {end[1]}, {end[0]}")
    print(f"Path: {' -> '.join(str(x) for x in path)}")
    print(f"Total Distance: {total_distance}")
    print(f"Priority: {priority}")
    print()

package_priorities = []  # create an empty list to store package priorities
for package in packages:
    state, city = package[1], package[2]
    start = (42.3601, -71.0589)  # Boston, MA
    end = None
    min_distance = float('inf')
    for i, c in enumerate(cities):
        if state == 'MA' and city == c[1]:
            end = c
            break
        elif state != 'MA' and state == c[0]:
            if distance(start, c[2:]) < min_distance:
                min_distance = distance(start, c[2:])
                end = c
    if end is None:
        for c in cities:
            if distance(start, c[2:]) < min_distance:
                min_distance = distance(start, c[2:])
                end = c
    path = [start, end]
    total_distance = distance(start, end[2:])
    for c in cities:
        if c[1:] == end[1:]:
            break
        elif state == 'MA' and city == c[1]:
            path.append(c[2:])
            total_distance += distance(end[2:], c[2:])
            break
        elif state != 'MA' and state == c[0]:
            path.append(c[2:])
            total_distance += distance(end[2:], c[2:])
    priority = total_distance
    package_priorities.append((package[0], priority))  # add the package priority to the list

# sort the list based on priority
package_priorities = sorted(package_priorities, key=lambda x: x[1])

# print the ordered list of packages with their priorities
print("Ordered list of packages with their priorities:")
for package_priority in package_priorities:
    print(f"Package {package_priority[0]}: {package_priority[1]}")