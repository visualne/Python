#
# #  n is equal to number of columns in the array
# #  inputs is equal to the the moves 2d array.
# n, inputs = [int(n) for n in input().split(" ")]
#
# #  Creating a row of zeros equal to number of columns.
# list = [0]*(n+1)
#
# # inputs is equal to the 2d array of moves
# for _ in range(inputs):
#     #  Elements in row of 2d array.
#     x, y, incr = [int(n) for n in input().split(" ")]
#
#     #  Adding incr value to the index in list (based on x coordinate)
#     list[x-1] += incr
#
#     #  ex) 2,5 list size 7 5 is less then 7
#     #  Not sure why they are subtracting the incremented value
#     #  from list[y]
#     if((y)<=len(list)): list[y] -= incr;
#
# #  All this is doing is determining the max value in the array.
# max = x = 0
# for i in list:
#    x=x+i;
#    if(max<x): max=x;
# print(max)



#  2d array holding each of the inserts
queries = [[1,5,3],\
           [4,8,7],\
           [6,9,1]]

#  What would be neat is if you could figure out
#  The common indexes in as many rows as possible
#  Create a dictionary from it and the values in the
#  dictionary is the sum of last row

#  Setting n equal to the size of the list
n=10

#  Setting array equal to an empty list.
array = []

#  Creating array based on number of elements sent in
for val in range(n):
    array.append(0)

#  Setting largest in array equal to zero.
largest = 0

#  Setting largest_in_row to zero
largest_in_row = 0

#  Loop going through moves in 2d inserts array
for row in queries:
    #  Setting variable names appropriately.
    start = row[0]-1
    end = row[1]
    number_to_insert = row[2]

    #  Instead of looping through the elements in the array one person
    #  just added the value the first value in the list.
    array[start] +=number_to_insert

    #  For the ending coordinate. I am unsure why the number is being
    #  subtracted. That makes nose no sense to me.
    if ((end)<=len(array)):
        array[end] -= number_to_insert

#  This is strange
max = x = 0
for i in array:
   x=x+i
   if max<x:
       max=x
print max

#  Printing final array
print 'Final Array: '
print array
