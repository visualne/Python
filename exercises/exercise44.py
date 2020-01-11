# A valid postal code
#
# have to fullfill both below requirements:
#
# must be a number in the range from 100000 to 999999 inclusive
# must not contain more than one alternating repetitive digit pair.
#
#
# Alternating repetitive digits are digits which repeat immediately after the
# next digit. In other words, an alternating repetitive digit pair is formed
# by two equal digits that have just a single digit between them.
#
#
# Your task is to provide two regular expressions regex_integer_in_range and
# regex_alternating_repetitive_digit_pair. Where:
#
# regex_integer_in_range should match only integers range from
# to 100000 to 999999 inclusive
#
# inclusive regex_alternating_repetitive_digit_pair should find alternating
# repetitive digits pairs in a given string.
import re

# For example:
#
# 121426 # Here, 1 is an alternating repetitive digit.

sample = '121426'

for i in range(len(sample)):
    if i + 3 <= len(sample)- 1:
        match = re.match('(\d)(\d)(\d)',sample[i:i+3])

        #  Checking for repeating digit match.
        if match:
            if match.group(1) == match.group(3):
                print 'repeating digit found'
    else:
        break


#  For loop to check three digits a time. Moving outter index up by one
#  each time.
# for i in range(len(sample)):
    #  Inner for loop that is checking an index two ahead of the
    #  current index

    #  Regex here to set start and end position




# 523563 # Here, NO digit is an alternating repetitive digit.
# 552523 # Here, both 2 and 5 are alternating repetitive digits.
