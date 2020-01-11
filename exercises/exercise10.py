#  Check to see if string is palindrome. The string is the same
#  forwards as it is backwards.

sample_string = 'w3oooooooo3w'

#  Loop to check the letters starting against
#  the letters in the front against the letters in the back.

#  Initalizing counter variable to keep track of indexes starting at back.
n = len(sample_string) - 1

for i in range(len(sample_string)):
    #  Check i against characters starting from the back
    if i > n:
        print 'This string is a palindrome'
        break
    elif sample_string[i] == sample_string[n]:
        #  Decrementing n variable.
        n = n - 1
    else:
        print 'This string is not a palindrome'
        exit(1)