def merge(left, right):
    result = []
    i = j = 0
    while i < len(left) and j < len(right):
        if left[i][3] <= right[j][3]:
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    result += left[i:]
    result += right[j:]
    return result

def merge_sort(data):
    if len(data) <= 1:
        return data
    mid = len(data) // 2
    left = merge_sort(data[:mid])
    right = merge_sort(data[mid:])
    return merge(left, right)

def read_csv(filename):
    data = []
    with open(filename, 'r') as f:
        for line in f:
            line = line.strip().split(',')
            data.append([int(line[0]), line[1], line[2], int(line[3])])
    return data

def main():
    data = read_csv("/Users/12103/Desktop/CS566 HW/Assign 3/sample2.csv")
    data = merge_sort(data)
    state_city = {}
    for package in data:
        state = package[1]
        city = package[2]
        if state not in state_city:
            state_city[state] = {}
        if city not in state_city[state]:
            state_city[state][city] = []
        state_city[state][city].append(package[0])
    print("Delivery Order:", end=" ")
    for package in data:
        print("#" + str(package[0]), end=", ")
    print()
    for state in state_city:
        print(state + ":")
        for city in state_city[state]:
            print("\t" + city + ": Package #" + ", Package #".join([str(x) for x in state_city[state][city]]))

if __name__ == "__main__":
    main()


