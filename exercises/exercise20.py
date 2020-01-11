#  First argument n - number of elements
#  Second argument arr - array to print in reverse.

def printArrayInReverse(n,arr):

    #  Creating empty array that will hold values in reverse
    reverseArray = []

    #  Printing the array elements in reverse.
    for index in range(len(arr)-1,-1,-1):
        reverseArray.append(arr[index])

    #  Return the reverse array.
    return reverseArray


arr = [2,4,5,6]

#  Calling function to print the elements in reverse order
printArrayInReverse(4,arr)

