def unoptimized(arr):

    #  Outter for loop looking at every value in the list.
    for loopNumber in range(len(arr)-1,0,-1):
        #  Inner for loop that will be decrementing by 1 every time.
        #  This is because on pass 1 the last element in the list
        #  will be the highest element
        for index in range(loopNumber):
            #  Comparing elements in the array against each other.
            if arr[index] > arr[index+1]:

                #  Moving the larger value up one element in the array.
                placeHolder = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = placeHolder

    return arr


def optimizedBubbleSort(arr):

    # Initializing count variable to zero
    count = 0
    switch=True
    n=len(arr)

    #  One update needs to happen as well as pass count needs to be at least
    #  greater then 1 in order for the loop to run. The optimization
    #  I believe is this outter for loop. If you were to do something like
    #  this for val in range(len(arr)-1,0,-1) and then have the same
    #  inner for loop it would take forever. I need to look more into this.
    while(switch==True and n>1):
        switch = False
        for index in range(len(arr)-1):
            #  If this doesn't happen atleast once that means the entire
            #  array is sorted.
            if arr[index]>arr[index+1]:
                tempValue = arr[index]
                arr[index] = arr[index+1]
                arr[index+1] = tempValue
                switch = True

        n = n - 1

    return arr


