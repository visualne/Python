#  Maybe sort the space stations list first
#  [1,5,9]
#  [0,1,2,3,4,5,6,7,8,9,10]

#  The maximum can only exist in one of three places
    # In front of space station (cities with lower values)
        # This is for cases where the cities fall before the first space stat
    #  In between space stations
    #  After a space station
        #  This is for cases where the cities exist after the largest
        # space station

# So with the above being the case the logic will be as follows to potentially
# get the greatest distance

# Sort the space stations list first.

# for loop to run through the sorted space station list

# add the city values before the lowest space station index (Get a total count)
# add the city values in between space stations (Get a total count)
# add the city values after the largest space station value (Get a total count)

# Once the longest count is found you need logic to determine what city
# is the farthest away


# Complete the flatlandSpaceStations function below.
def flatlandSpaceStations(n, c):
    #  Making normal looking variables
    cities = n
    spaceStations = c

    #  Running through the sorted spaceStations list.
    for city in sortedSpaceStationsList:

        #  Logic here to determine how many elements exist before first
        #  first city in array