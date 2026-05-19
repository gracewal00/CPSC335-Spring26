#Algo 2: Boats to Save People

"""
Input: array people[] filled with weights (len = # people)
       int boat capacity
Output: int num required boats

Boats carry max 2 people
"""

def numBoats(people, capacity):
    required_boats = 0
    print(f"Original List: {people}\nCapacity: {capacity}")
    while True:
        # PRINT current list
        print(f"Current List: {people}")
        # stop loop when all elements have been removed (put into boats)
        if not people:
            break
        # if weight is capacity, person is alone in boat
        if people[0] == capacity:
            required_boats += 1
            print(f"Boat {required_boats}: ({people.pop(0)})")
            continue
        closest_sum = 0
        partner_index = 0
        for index, weight in enumerate(people[1:]):
            current_sum = people[0] + weight
            # capacity found, return pair together
            if current_sum == capacity:
                closest_sum = current_sum
                partner_index = index
                required_boats += 1
                print(f"Boat {required_boats}: ({people.pop(0)}, {people.pop(partner_index)})")
                break
            # update closest_sum if current_sum is closer to capacity
            if current_sum <= capacity and current_sum > closest_sum:
                closest_sum = current_sum
                partner_index = index
        # no sum fit in a boat, person is alone in boat
        if partner_index == 0:
            required_boats += 1
            print(f"Boat {required_boats}: ({people.pop(0)})")
            continue
        # return closest sum partners in boat together
        elif closest_sum != capacity:
            required_boats += 1
            print(f"Boat {required_boats}: ({people.pop(0)}, {people.pop(partner_index)})")
            continue

    return required_boats


def main():
    print(f"EXAMPLE 1:")
    print(f"Expected Output: 3\nActual Output: {numBoats([3, 2, 2, 1], 3)}\n")
    print(f"EXAMPLE 2:")
    print(f"Expected Output: 5\nActual Output: {numBoats([3, 5, 3, 4, 2, 2, 1, 4, 1], 5)}\n")
    print(f"EXAMPLE 3:")
    print(f"Expected Output: 3\nActual Output: {numBoats([1, 3, 3], 3)}\n")

if __name__ == '__main__':
    main()
