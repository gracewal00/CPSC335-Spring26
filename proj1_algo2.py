#Names: Grace Walsh, Mathieu Partain-Martinez, Darren Nguyen
#CPSC 335, MW 10:00-11:15am
#Algorithm 2: Greedy Approach to Hamiltonian Problem
"""Find optimal starting city and display city index"""

def findStartingCity(distances, fuel, mpg):
    """Find and return the index of the preferred starting city given the distances, fuel, and mpg"""
    #Initialize the starting city and the current mileage
    starting_city = 0
    current_miles = 0
    #Loop through the cities to check gas and distances
    for i in range(len(distances)):
        #Calculate the mileage available after leaving the current city
        current_miles += fuel[i] * mpg - distances[i]
        #If current mileage is below 0, the previous starting cities will not work
        if current_miles < 0:
            starting_city = i + 1
            current_miles = 0
    return starting_city

def main():
    """Main function used to print the message"""
    city_distances = [5, 25, 15, 10, 15]
    fuel = [1, 2, 1, 0, 3]
    mpg = 10
    #Print the sample inputs, calculate the preferred starting city, and print the result
    print(f"city_distances = {city_distances}\nfuel = {fuel}\nmpg = {mpg}")
    print(f"The preferred starting city for the sample above is city {findStartingCity(city_distances, fuel, mpg)}")

if __name__ == '__main__':
    main()
