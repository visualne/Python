a = [5,2,7,1]

arr = [[10, 2, 5], [7, 1, 0], [9, 9, 9], [1, 23, 12], [6, 5, 9]]


k = 1

for i in range(len(arr)-1,-1,-1):
    #  Inner for loop that checks index in back of current
    #  index.
    for j in range(0,i):
        if arr[j][k] > arr[j + 1][k]:
            temp = arr[j+1]
            arr[j+1] = arr[j]
            arr[j] = temp

    arr[i] = map(str,arr[i])

for val in arr:
    print val



