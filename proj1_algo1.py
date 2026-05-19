#Names: Grace Walsh, Mathieu Partain-Martinez, Darren Nguyen
#CPSC 335, MW 10:00-11:15am
#Algorithm 1: Connecting Pairs of Persons
"""Pair together couples in a list, beginning with 0&1, 2&3, ..."""

from random import shuffle

#function that returns the number of swaps needed to get the correct pairs together
def connectingPairs(row):
    swapCount = 0
    #go through the seating in pairs
    for i in range(0, len(row), 2):
        firstSeatInPair = row[i]
        #find expected partner next to the first seat in the pair
        if firstSeatInPair % 2 == 0:
            expectedPartner = firstSeatInPair + 1
        else:
            expectedPartner = firstSeatInPair - 1
        #if the person next to the first person in pair is not next to them find index of expected partner and swap
        if row[i+1] != expectedPartner:
            #find the real index of the expected partner
            realPartnerIndex = row.index(expectedPartner)
            row[i+1], row[realPartnerIndex] = row[realPartnerIndex], row[i+1]
            swapCount += 1
            print("Swapped the seats", i+1, "and", realPartnerIndex, "row now:", row)
    print("Amount of swaps:", swapCount)
    return row

def main():
    # get number of people in the row
    num_people = int(input("Enter an even number of people in the row: "))
    row = []
    for i in range(num_people):
        row.append(i)
    # make sure there are an even number of people
    if len(row) % 2 != 0:
        print(f"Uneven number of people")
        exit()
    # randomize the order
    shuffle(row)
    print("Initial seating: ", row)
    # pair up couples
    finalSeating = connectingPairs(row)
    print("Final seating: ", finalSeating)

if __name__ == "__main__":
    main()
