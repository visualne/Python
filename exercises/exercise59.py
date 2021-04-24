from itertools import permutations

sample = 'ifailuhkqq'

valuesDictionary = {}

for index in range(len(sample)):
    for val in range(index,len(sample)+1):
        if val == index:
            continue
        else:
            # print(str(index) + ',' + str(val))
            # print(sample[index:val])

            #  Looking forward ex) abc
            forward_value = sample[index:val]

            #  Looking backward
            reverse_value = forward_value[::-1]

        #  If value already in dictionary, increase count.
        #  a count value > 1 means an anagram was found.
        if forward_value in valuesDictionary:
            valuesDictionary[forward_value] = valuesDictionary[forward_value] + 1
        else:
            #  Filling valuesDictionary
            valuesDictionary[forward_value] = 0

        #  Getting all permutations of reversed string
        permutation = [''.join(p) for p in permutations(reverse_value)]

        if reverse_value == forward_value and len(reverse_value) > 1:
            valuesDictionary[forward_value] = valuesDictionary[forward_value] + 1


for k,v in valuesDictionary.items():
    if valuesDictionary[k] == 1:
        print(k,v)
