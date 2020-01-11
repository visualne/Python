#  Print the minimum number of swaps for the array listed below.
arr = [2,1,3,5,4]

#  Creating totalMoves variable this will be used to keep track
#  if the total number of moves that were made.
moves = 0

#  Print the index next to each of the values in the current arr
arr = enumerate(arr)

#  Sort the values in arr by where they should be
arr = sorted(arr,key=lambda x:x[1])

#  Visited indexes dictionary
visitedIndexes = {}

#  Creating dictionary and setting each visited index to false
for index in range(len(arr)):
    visitedIndexes[index] = False


#  Loop to loop through each value in the array
for i in range(len(arr)):

    #  Declaring counter variable. This will keep track of the
    #  number of moves.
    counter = 0

    #  Setting j (this is the index in arr list that is sorted
    #  by where the elements should go.
    j = i

    if visitedIndexes[j] or arr[j][0] == j:
        continue

    #  For loop to go through list of visited indexes
    while not visitedIndexes[j]:

        #  Setting the index to visited
        visitedIndexes[j] = True

        #  Moving the index appropriately in the arrpos list
        j = arr[j][0]

        #  Incrementing the counter.
        counter = counter + 1

    #  Checking counter and subtracting 1. (Two moves is equivalent
    #  to one move.
    if counter >= 2:
        counter = counter - 1

        #  Adding total number of moves to counter.
        moves = moves + counter


print moves
