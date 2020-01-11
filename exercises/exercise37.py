class EvenStream(object):
    def __init__(self):
        self.current = 0

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

class OddStream(object):
    def __init__(self):
        self.current = 1

    def get_next(self):
        to_return = self.current
        self.current += 2
        return to_return

def print_from_stream(n, stream=EvenStream()):

    #  Setting stream equal to None if
    #  no value was sent in.
    if stream == None:
        stream = EvenStream()

    for _ in range(n):
        print stream.get_next()


f = open('input','r')
for line in f.readlines()[1:]:
    stream_name = line.split(' ')[0]
    n =int(line.split(' ')[1])
    if stream_name == "even":
        print_from_stream(n)
    else:
        print_from_stream(n, OddStream())

#  Closing file appropriately.
f.close()
