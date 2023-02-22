import csv
from collections import defaultdict

def divide_and_conquer(file_path):
    state_dict = defaultdict(list)
    in_state_packages = []
    out_state_packages = []
    international_packages = []

    with open(file_path, "r") as file:
        reader = csv.reader(file)
        for row in reader:
            package_num, _, state, country = [item.strip() for item in row]
            
            if state == "MA" and country == "US":
                in_state_packages.append(package_num)
            else:
                out_state_packages.append(package_num)
            
            if country != "US":
                international_packages.append(package_num)
                
            state_dict[state].append(package_num)
                
    for state, packages in state_dict.items():
        if len(packages) > 1:
            print(f"Package:{','.join(packages)} are allocated into same state:{state}.")
    
    for package in in_state_packages:
        print(f"Package:{package} is an in-state package.")
        
    for package in out_state_packages:
        print(f"Package:{package} is an out-of-state package.")
        
    for package in international_packages:
        print(f"Package:{package} is an international package.")
divide_and_conquer("/Users/12103/Desktop/CS566 HW/Assign 2/sample2.csv")