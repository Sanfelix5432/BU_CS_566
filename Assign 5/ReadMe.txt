Should not input package number already exist(system will show error) and city name should spelling right(
system will ask you retype). 
The time efficiency of the whole code is dependent on several factors, including the size of the input data (i.e., the number of packages), the complexity of the distance calculation, and the efficiency of the sorting algorithm used to prioritize the packages.

In the current implementation, the get_distance() function uses dynamic programming to cache previously calculated distances between pairs of cities, which can improve performance by avoiding redundant calculations. However, the implementation of the get_distance() function can impact the overall time complexity of the system, as discussed earlier.

The time complexity of the sorting algorithm used in the get_priority() method is O(n log n), where n is the number of packages in the system. This is because the sorting algorithm used in Python's built-in sorted() function is a variation of the quicksort algorithm, which has an average time complexity of O(n log n) for a list of n elements.

The overall time efficiency of the system can be impacted by the size of the input data and the number of times the get_distance() function is called. If the number of packages in the system is very large, or if the distance calculation algorithm is very complex, the overall time efficiency of the system could be slow.