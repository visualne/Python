#  Setting n equal to the size of the list
n=10

#  Setting array equal to an empty list.
array = []

#  2d array holding each of the inserts
queries = [[1,5,3],\
           [4,8,7],\
           [6,9,1]]

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

    print array


print 'What the array looks like before'
print array

#  This is interesting. He is adding value of the index
#  to each element in the array and then determining which
#  one of those values is the biggest.
max = x = 0
for i in array:
   x=x+i;
   if(max<x): max=x;
print(max)


# #  Printing final array
# print 'Final Array: '
# print array
#
# #  Printing largest value
# print 'Largest value in array is: ' + str(largest)