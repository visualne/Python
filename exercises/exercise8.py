# arr = [1,7,3,2,4,5,6]
# arr = [1,2,4,3,5]
# First Pass
# [1,3,4,2,5]
# [1,2,4,3,5]
# [1,2,3,4,5]]

#  something random on master branch

#  Create a selection sort
#  Find the smallest element in the unsorted sublist - move it up the list
#  appropriately

# arr = [1,3,5,2,4,6,7]

#  Create outer for loop to compare the current element against every
#  other element in the list
#  Create inner for loop that loops through every element in the list
#  and compares it the smallestElement value. If a value is found that
#  is smaller then smallestElement, that value will become the smallest.

#  Opening up input file for reading
f = open('input2','r')
# #
arr = map(int,f.readline().split(' '))

#  Initializing moves count to 0.
movesCount = 0

#  Initializing i variable to zero. This will be used to keep
#  of the starting position in the array. Because putting sorted
#  items at the front of the list it will increment by 1 every time.
i = 0

#  Getting the length of array and setting it to n. This
#  value will be checked by the outter for loop to make sure you
#  aren't at the front of the list
n = len(arr)

#  Setting switch bool to True. This is assuming that this list
#  is unsorted on the first first pass.
switch = True

while(n>1):
# for i in range(len(arr)):
    smallestElement = arr[i]

    #  Setting switch bool. Assuming no switch is going to happen.
    switch = False

    for j in range(i, len(arr)):

        if arr[j] < smallestElement:
            #  Smaller element is found so it is set to arr[j]
            smallestElement = arr[j]

            #  Setting smallestIndex appropriately.
            smallestIndex = j

            #  Setting switch to True
            switch = True

    #  If a smaller value was found the switch bool was set to true.
    if switch:
        #  Here I am doing the switch. Moving the smallest element found
        #  to wherever the original smallestElement lived.
        tempValue = arr[i]
        arr[i] = arr[smallestIndex]
        arr[smallestIndex] = tempValue

        #  Incrementing moves count
        movesCount = movesCount + 1

    #  Incrementing i value. This value is being incremented
    #  because at this point the smallest value on the run through
    #  the array is at position i in the array.
    i = i + 1

    #  Decrementing n value
    n = n - 1

print arr
#  Printing total amount of moves
print 'Total moves: ' + str(movesCount)


