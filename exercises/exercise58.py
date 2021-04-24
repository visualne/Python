import itertools

word = 'BANANA'

for val in itertools.islice(word, 2,None):
    print(val)

# for val in set(list(itertools.permutations(word, 2))):
#     print(val)