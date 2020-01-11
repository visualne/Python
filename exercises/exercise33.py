import operator

def person_lister(f):
    def inner(people):

        #  This makes each element of the list..a list.
        #  turning the original people list into a list of
        #  lists.
        for i in range(len(people)):
            people[i] = people[i].split(' ')

        #  This sorts the list appropriately by age.
        people.sort(key = lambda x: x[2])

        #  Fixing elements in the list appropriately.
        for j in range(len(people)):
            people[j] = f(people[j])

        #  Returning final list of sorted people and changed people.
        return people

    return inner

@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[1]

if __name__ == '__main__':
    # people = [raw_input().split() for i in range(int(raw_input()))]
    people = ['Mike Thomson 20 M',
              'Robert Bustle 32 M',
              'Andria Bustle 30 F']
    print '\n'.join(name_format(people))
#


