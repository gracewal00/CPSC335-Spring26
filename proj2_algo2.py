#Names: Grace Walsh, Mathieu Partain-Martinez, Darren Nguyen
#CPSC 335, MW 10:00-11:15am
#Algorithm 2: Boats to Save People
"""Find the minimum number of boats needed for a given group of people"""

def numBoats(people, capacity):
    """Find and return the minimum number of boats needed given a list of weights and the boat capacity"""
    required_boats = 0
    print(f"Original List: {people}\nCapacity: {capacity}")
    # Loop through all given people
    for index, weight in enumerate(people):
        # Find the perfect compatable weight for current person
        other_weight = capacity - weight
        # If current person is already at capacity, they are in a boat by themselves
        if other_weight <= 0:
            required_boats += 1
            continue
        # Check for compatable weight in remaining people, place in boat together if found
        if other_weight in people[index+1:]:
            people.remove(other_weight)
            required_boats += 1
        else:
            # If no perfect compatable weight is found, check for smaller weights that are closest to capacity
            small_list = [item for item in people if item < other_weight]
            # If there are no smaller weights remaining, they are in a boat by themselves
            if not small_list:
                required_boats += 1
                continue
            # Find the closest weight to capacity with the current weight, place in boat together if found
            small_weight = max(small_list)
            people.remove(small_weight)
            required_boats += 1
    return required_boats

def main():
    """Main function used to print the examples"""
    print(f"EXAMPLE 1:")
    print(f"Expected Output: 3\nActual Output: {numBoats([3, 2, 2, 1], 3)}\n")
    print(f"EXAMPLE 2:")
    print(f"Expected Output: 5\nActual Output: {numBoats([3, 5, 3, 4, 2, 2, 1, 4, 1], 5)}\n")
    print(f"EXAMPLE 3:")
    print(f"Expected Output: 3\nActual Output: {numBoats([1, 3, 3], 3)}\n")

if __name__ == '__main__':
    main()
