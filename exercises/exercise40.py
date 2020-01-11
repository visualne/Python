from __future__ import print_function
from fractions import Fraction
from fractions import gcd


# The reduce() function applies a function of two arguments cumulatively on a list of objects in succession
# from left to right to reduce it to one value. Say you have a list, say [1,2,3] and you have to find its sum.
reduce(lambda x, y : x + y, [1,2,3], -3)

# You can also define an initial value. If it is specified, the function will assume initial value as the value
# given, and then reduce. It is equivalent to adding the initial value at the beginning of the list. For example:
reduce(gcd, [2,4,8], 3)


def product(fracs):
    #  Find greatest common denominator of the two arguments
    #  associated with fracs.
    #  fracs is a list of fraction arguments in the form
    #  [fracs(1,2), fracs(2,5), fracs(5,9)]
    # complete this line with a reduce statement

    t = reduce(lambda x, y : x * y, fracs)
    return t.numerator, t.denominator

if __name__ == '__main__':
    fracs = []
    sample = [[10,20],[3,10],[3,6]]
    for x in range(len(sample)):
        fracs.append(Fraction(*map(int, sample[x])))
        # fracs.append(Fraction(*map(int, raw_input().split())))

    # print(fracs)
    result = product(fracs)
    print(*result)

