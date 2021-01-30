###########################
# 6.0002 Problem Set 1a: Space Cows 
# Name:
# Collaborators:
# Time:

from ps1_partition import get_partitions
import time

#================================
# Part A: Transporting Space Cows
#================================

# Problem 1
def load_cows(filename):
    """
    Read the contents of the given file.  Assumes the file contents contain
    data in the form of comma-separated cow name, weight pairs, and return a
    dictionary containing cow names as keys and corresponding weights as values.

    Parameters:
    filename - the name of the data file as a string

    Returns:
    a dictionary of cow name (string), weight (int) pairs
    """
    # TODO: Your code here
    file = open(filename, 'r')
    cows_dict = {}
    for line in file:
        name, weight = line.split(',')
        cows_dict[name] = int(weight)
    file.close()
    return cows_dict

# Problem 2
def greedy_cow_transport(cows,limit=10):
    """
    Uses a greedy heuristic to determine an allocation of cows that attempts to
    minimize the number of spaceship trips needed to transport all the cows. The
    returned allocation of cows may or may not be optimal.
    The greedy heuristic should follow the following method:

    1. As long as the current trip can fit another cow, add the largest cow that will fit
        to the trip
    2. Once the trip is full, begin a new trip to transport the remaining cows

    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    sorted_cows = sorted(cows, key=cows.get, reverse=True)
    result = []
    while len(sorted_cows) > 0:
        totalWeight = 0
        trip = []
        for name in sorted_cows[:]:
            if cows[name] + totalWeight <= limit:
                trip.append(name)
                totalWeight = totalWeight + cows[name]
                sorted_cows.remove(name)
        result.append(trip)
    return result

# Problem 3
def brute_force_cow_transport(cows,limit=10):
    """
    Finds the allocation of cows that minimizes the number of spaceship trips
    via brute force.  The brute force algorithm should follow the following method:

    1. Enumerate all possible ways that the cows can be divided into separate trips 
        Use the given get_partitions function in ps1_partition.py to help you!
    2. Select the allocation that minimizes the number of trips without making any trip
        that does not obey the weight limitation
            
    Does not mutate the given dictionary of cows.

    Parameters:
    cows - a dictionary of name (string), weight (int) pairs
    limit - weight limit of the spaceship (an int)
    
    Returns:
    A list of lists, with each inner list containing the names of cows
    transported on a particular trip and the overall list containing all the
    trips
    """
    # TODO: Your code here
    result = []
    for partition in get_partitions(cows.keys()):
        score = []
        for trip in partition:
            totalWeight = 0
            for name in trip:
                totalWeight += cows[name]
            if totalWeight <= 10:
                score.append(1)
            else:
                score.append(0)
        if len(partition) == sum(score):
            result.append(partition)
    return result
        
# Problem 4
def compare_cow_transport_algorithms():
    """
    Using the data from ps1_cow_data.txt and the specified weight limit, run your
    greedy_cow_transport and brute_force_cow_transport functions here. Use the
    default weight limits of 10 for both greedy_cow_transport and
    brute_force_cow_transport.
    
    Print out the number of trips returned by each method, and how long each
    method takes to run in seconds.

    Returns:
    Does not return anything.
    """
    # TODO: Your code here
    cows = load_cows('ps1_cow_data.txt')
    cows2 = load_cows('ps1_cow_data_2.txt')
    # greedy
    print("Running Greedy_cow_transport()")
    start = time.time()
    result = greedy_cow_transport(cows)
    end = time.time()
    print(f' Execution time for ps1_cow_data.txt was {end - start}.')
    print(f' Problem was solved within {len(result)} trips.')
    start = time.time()
    result = greedy_cow_transport(cows2)
    end = time.time()
    print(f' Execution time for ps1_cow_data_2.txt was {end - start}.')
    print(f' Problem was solved within {len(result)} trips.')
    # brute force
    print("Running Brute_force_cow_transport()")
    start = time.time()
    result = brute_force_cow_transport(cows)
    end = time.time()
    print(f' Execution time for ps1_cow_data.txt was {end - start}.')
    print(f' Problem was solved within {len(result)} trips.')
    start = time.time()
    result = brute_force_cow_transport(cows2)
    end = time.time()
    print(f' Execution time for ps1_cow_data_2.txt was {end - start}.')
    print(f' Problem was solved within {len(result)} trips.')


# TESTING CODE for all the functions above.
if __name__ == '__main__':
    # problem 1
    print("begin testing ps1a.py")
    print("p1-------------------")
    load_dict = load_cows('ps1_cow_data.txt')
    print("data loaded via ps1_cow_data.txt")
    print(load_dict)
    print("---------------------")
    cows = load_cows('ps1_cow_data.txt')
    cows2 = load_cows('ps1_cow_data_2.txt')
    # problem 2
    print("p2-------------------")
    print("result of Greedy_cow_transport()")
    print(greedy_cow_transport(cows))
    print("---------------------")
    # problem 3
    print("p3-------------------")
    print("result of Brute_force_cow_transport()")
    print(brute_force_cow_transport(cows))
    print("---------------------")
    # problem 4
    print("p4-------------------")
    compare_cow_transport_algorithms()

