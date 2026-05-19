#Names: Grace Walsh, Mathieu Partain-Martinez, Darren Nguyen
#CPSC 335, MW 10:00-11:15am
#Algorithm 1: The Spread of Fire in a Forest
"""Determine the minimum number of days for all healthy trees in a forest to burn down"""

# 0. Empty (no tree)
# 1. Healthy Tree
# 2. Burned Tree

# Every day, any healthy tree that is adjacent (up, down, left, or right) to a burned tree will also burn down

import copy

def minBurnDays(forest):
    """Find the min number of days it will take for all healthy trees to burn down"""
    if not any(2 in row for row in forest):
        return -1       # no burned trees initially - impossible
    
    day_counter = 0
    change = True

    print(f"Initial grid: {forest}")

    while change:
        change = False
        temp_forest = copy.deepcopy(forest)

        # for every 2 (burned tree), if touching a 1 (healthy), change 1 to 2
        for vindex, row in enumerate(temp_forest):
            for hindex, tree in enumerate(row):
                # current = [vindex][hindex]
                if tree == 2:
                    if vindex != 0:
                        ## up = [vindex - 1][hindex]
                        if temp_forest[vindex - 1][hindex] == 1:
                            forest[vindex - 1][hindex] = 2
                            change = True
                    if vindex != len(forest)-1:
                        ## down = [vindex + 1][hindex]
                        if temp_forest[vindex + 1][hindex] == 1:
                            forest[vindex + 1][hindex] = 2
                            change = True
                    if hindex != 0:
                        ## left = [vindex][hindex - 1]
                        if temp_forest[vindex][hindex - 1] == 1:
                            forest[vindex][hindex - 1] = 2
                            change = True
                    if hindex != len(row)-1:
                        ## right = [vindex][hindex + 1]
                        if temp_forest[vindex][hindex + 1] == 1:
                            forest[vindex][hindex + 1] = 2
                            change = True
        if change:
            day_counter += 1
            print(f"After day {day_counter} : {forest}")

    if any(1 in row for row in forest):
        return -1       # remaining healthy trees - impossible
    
    return day_counter      # all trees burned


def main():
    """Main function used to print the examples"""
    print(f"EXAMPLE 1:")
    forest = [
        [2,1,1], 
        [1,1,0], 
        [0,1,1]
    ]
    print(f"Expected Output: 4\nActual Output: {minBurnDays(forest)}\n")
        # At day 1: the healthy trees at (1,2) and (2,1) burn.
        # At day 2: the healthy trees at (2,2) and (3,1) burn.
        # At day 3: the healthy tree at (2,3) burns.
        # At day 4: the healthy tree at (3,3) burns.

    print(f"EXAMPLE 2:")
    forest = [
        [2,1,1], 
        [0,1,1], 
        [1,0,0]
    ]
    print(f"Expected Output: -1\nActual Output: {minBurnDays(forest)}\n")
        # The healthy tree at (2,0) cannot burn because there are no adjacent burned trees.

    print(f"EXAMPLE 3:")
    forest = [
        [0,2]
    ]
    print(f"Expected Output: 0\nActual Output: {minBurnDays(forest)}\n")
        # No healthy trees to burn

if __name__ == '__main__':
    main()
