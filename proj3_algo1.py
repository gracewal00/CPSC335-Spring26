#Names: Grace Walsh, Mathieu Partain-Martinez, Darren Nguyen
#CPSC 335, MW 10:00-11:15am
#Algorithm 1: The Spread of Fire in a Forest
"""Determine the minimum number of days for all healthy trees in a forest to burn down"""

# Every day, any healthy tree that is adjacent (up, down, left, or right) to a burned tree will also burn down
# 0. Empty (no tree)
# 1. Healthy Tree
# 2. Burned Tree

from collections import deque

def minBurnDays(forest):
    """Find the min number of days it will take for all healthy trees to burn down"""
    
    print(f"Initial grid: {forest}")

    # create variables for forest data
    rows = len(forest)
    cols = len(forest[0])
    healthy_trees = 0
    burn_trees = 0
    burn_positions = deque()

    # Loop through the whole forest to find positions of burned trees and number of burned and healthy trees
    for row in range(rows):
        for col in range(cols):
            if forest[row][col] == 2:
                burn_positions.append((row, col))
                burn_trees += 1
            elif forest[row][col] == 1:
                healthy_trees += 1

    # If no burned trees, impossible to burn healthy trees
    if burn_trees == 0:
        return -1
    # If no healthy trees, nothing to burn, no days needed
    if healthy_trees == 0:
        return 0

    # Positions for down, up, right, left from current tree
    directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
    day_counter = 0

    # Loop through burned trees until all have expanded
    while burn_positions:
        change = False
        # Number of trees to loop through in the current day
        current_burn = len(burn_positions)
        # Loop through burned trees to be expanded in the current day
        for _ in range(current_burn):
            # Take oldest element (new burns from previous day) and store row, col of one burning tree
            row, col = burn_positions.popleft()
            # Get positiions of neighboring trees down, up, right, left from current tree
            for row_change, col_change in directions:
                new_row = row + row_change
                new_col = col + col_change
                # Check for healthy tree next to burn (within edges of forest)
                if 0 <= new_row < rows and 0 <= new_col < cols and forest[new_row][new_col] == 1:
                    # Burn healthy tree and add to queue to expand/burn tomorrow
                    forest[new_row][new_col] = 2
                    burn_positions.append((new_row, new_col))
                    healthy_trees -= 1
                    change = True
        if change:
            day_counter += 1

    print(f"Final grid: {forest}")

    # Return min number of days it took to burn all healthy trees
    if healthy_trees == 0:
        return day_counter
    # If healthy trees remain, it is impossible to burn all healthy trees
    else:
        return -1


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
