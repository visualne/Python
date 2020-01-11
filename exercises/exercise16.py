import timeit
# http://docs.python.org/3.3/library/timeit.html

# Intersection
print("List intersections")

version1="""
l1 = set(range(2000))
l2 = set(range(1000,3000))
l3 = l1 & l2
"""
print("Version 1 - Set approach")
print(timeit.repeat(version1, number=10, repeat=4))
print('END Version 1')

version2="""
l1 = range(2000)
l2 = range(1000,3000)
l3 = []
for elem1 in l1:
    for elem2 in l2:
        if elem1 == elem2:
            l3.append(elem1)
"""
print("Version 2 - Frontal approach")
print(timeit.repeat(version2, number=10, repeat=4))
print('END Version 2')


version3="""
l1 = range(2000)
l2 = range(1000,3000)
d1 = {}
l3 = []
for key in l1:
    d1[key] = True

for key2 in l2:
    if key2 in d1:
        l3.append(key2)
"""
print("Version 3 - Hash table approach")
print(timeit.repeat(version3, number=10, repeat=4))
print('END Version 3')