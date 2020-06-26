import operator


def person_lister(f):
    def inner(people):

        #  This makes each element of the list..a list.
        #  turning the original people list into a list of
        #  lists.
        for i in range(len(people)):
            people[i] = people[i].split(' ')

        #  This sorts the list appropriately by age.
        people.sort(key=lambda x: int(x[2]))

        #  Fixing elements in the list appropriately.
        for j in range(len(people)):
            people[j] = f(people[j])

        # Returning final list
        return people

    return inner


@person_lister
def name_format(person):
    return ("Mr. " if person[3] == "M" else "Ms. ") + person[0] + " " + person[
        1]


if __name__ == '__main__':
    people = ['Jake Jake 42 M',

    'Jake Kevin 57 M',

    'Jake Michael 91 M',

    'Kevin Jake 2 M',

    'Kevin Kevin 44 M',

    'Kevin Michael 100 M',

    'Michael Jake 4 M',

    'Michael Kevin 36 M',

    'Michael Michael 15 M',

    'Micheal Micheal 6 M']


    # people = [raw_input().split() for i in range(int(raw_input()))]
    print '\n'.join(name_format(people))



