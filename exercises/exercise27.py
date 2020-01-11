some_list = [2,9,1,3,5]

for i in range(len(some_list)-1,-1,-1):
    for j in range(0,i):
       if some_list[j] > some_list[j+1]:
            temp = some_list[j]
            some_list[j] = some_list[j+1]
            some_list[j+1] = temp

print some_list