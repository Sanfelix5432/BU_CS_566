import pandas as pd
import numpy as np

# Define memoize decorator to cache function results
def memoize(func):
    cache = {}
    def wrapper(*args):
        if args not in cache:
            cache[args] = func(*args)
        return cache[args]
    return wrapper

# Define function to calculate distance between two cities
@memoize
def get_distance(city1, city2):
    return np.random.randint(1, 100)

# Read package data from CSV file
df = pd.read_csv("/Users/12103/Desktop/CS566 HW/Assign 5/package_data2.csv", header=None, names=['Package', 'State', 'City'])

# Calculate distances between package cities and default city (Boston)
distances = [get_distance('Boston', city) for city in df['City']]

# Add distances as a new column in the dataframe
df['Distance'] = distances

# Sort the packages by distance in ascending order
df = df.sort_values('Distance')

# Print the sorted package list with priorities
print('Priority:')
print(df['Package'].values)

# Ask user to input new package data
while True:
    package_num = input('Enter package number (0 to stop): ')
    if package_num == '0':
        break
    if int(package_num) in df['Package'].values:
        print('Package number already exists. Please enter a new number.')
        continue
    state = input('Enter state abbreviation: ')
    city = input('Enter destination city: ')
    if city in df['City'].values:
        print('City already exists. Please enter a new city.')
        continue
    distance = get_distance('Boston', city)
    df = df.append({'Package': int(package_num), 'State': state, 'City': city, 'Distance': distance}, ignore_index=True)
    df = df.sort_values('Distance')
    print('New Priority:')
    print(df['Package'].values)
