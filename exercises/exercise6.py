#  Number of entries in queue
n = 6

#  Initializing bribes to zero.
bribes = 0

#  Reflection: When I hit a wall. It's almost like my mind can't keep the pace.
#  It's like I am running at a certain pace and start breathing hard and my
#  pace slows down. The only way i remedied this situation was by running
#  everyday. Maybe you should start logging the moment when you start to feel
#  burned out doing these problems. Or dedicate a certain amount of minutes to
#   pushing the mind. (5-10 minutes)

arr = [2,1,5,3,4]

for index in range(0,len(arr)):

    #  This if statement just deals with numbers at positions in the array that
    #  are actually legit in other words this number never moved around in the
    #  array and is in its original position.
    if index == arr[index] - 1:
        pass

    #  This test case deals with a number that was found at an index less then
    #  where it should be.
    if index < arr[index] - 1:

        #  (A POSITION THREE POSITIONS LESS THEN CURRENT POSITION IS ILLEGAL)
        #  The below if statement will check for that.
        if index < arr[index] - 3:
            print 'Too chaotic'
            exit(1)

        #  Incrementing bribes variable below. At this point it is considered a
        #  Legal move if the position of the number is found at is two or less
        #  positions away from where it should be then this is a legal move.
        #  Determining how far forward it is should be and incrementing the
        #  bribes variable appropriately.

        #  Incrementing the number of bribes appropriately.
        bribes = bribes + (arr[index] - 1) - index

    #  This else path deals with a number at an index that is greater then
    #  where it should be. This means this number took at least one bribe
    #  and was counted already above
    else:
        pass

#  Returning total number of bribes
print bribes


