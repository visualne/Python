#  Create a selection sort
#  Find the smallest element in the unsorted sublist - move it up the list
#  appropriately
def selectionSortUnoptimized(arr):
    # arr = [2,5,4,1,3,6]

    #  Sample on feature

    #  Initialzing count to zero
    count = 0

    #  Find the smallest element in the unsorted list.
        #  Create for loop to look through each element in the list
        #  and compare it to the smallest element that you defined
        #  in the outter loop.
    for i in range(len(arr)):
        #  Setting smallestValue to arr[i]
        smallestValue = arr[i]

        # Setting switch bool to False.
        switchBool = False

        #  This for loop is used to compare all values in the array
        #  to the smallestValue set above.
        for j in range(i,len(arr)):
            if arr[j] < smallestValue:
                #  Setting smallestValue to arr[j]
                smallestValue = arr[j]

                #  Setting smallest index
                smallestIndex = j

                #  Setting switch bool to True. this means a switch is going
                #  to happen.
                switchBool = True

        #  Checking to see if switchBool is set to True.
        #  if switch is set to true then values in the array
        #  will be moved around.
        if switchBool:
            #  Moving smallest value to a index farther up the array
            tempValue = arr[i]
            #  Replacing arr[i] with the smallest value.
            arr[i] = arr[smallestIndex]
            arr[smallestIndex] = tempValue

            #  Incrementing the moves count to zero.
            count = count + 1

    #  Move it up the list
    # print arr

    #  Total number of moves.
    print 'Total Moves: ' + str(count)

def bubbleSortUnoptimized(arr):
    #  Two elements at a time in the list.
    #  if one element is bigger then the other switch them.
    #  Do this until the entire list is sorted.

    #  Loop through each value in the list.
    #  compare the current index value with an index one ahead of it.
    for i in range(len(arr),0,-1):
        #  For loop to compare each value to the value together
        #  When this loop is finished the largest value will have
        #  made its way down the list.
        for index in range(0,i):
        # exit(1)
            #  Making sure we aren't at the end of the list
            if index != len(arr) - 1:
                #  This is the comparison
                if arr[index] > arr[index+1]:
                    #  Switch will happen here
                    tempValue = arr[index]
                    arr[index] = arr[index+1]
                    arr[index+1] = tempValue
                    print arr
            else:
                pass

    print arr


# arr = [2,5,4,1,3,6]

#  Reading inputs into arr variable
f = open('input2','r')

#  Reading values into arr
arr = map(int,f.readline().split())

selectionSortUnoptimized(arr)
