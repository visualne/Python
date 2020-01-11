cube = lambda x: x**3# complete the lambda function

class Fibonacci():
    def __init__(self, howMany):
        self.counter = howMany
        self.curFib = 0
        self.nextFib = 1

    def __iter__(self):
     #
     #  Return an object that exposes an __next__ method.
     #  self (whose type is Fibonacci) is such an object:
     #
        return self

    def next(self):

        if self.counter == 0:
        #
        #  We have returned the count of fibonacci numbers
        #
           raise StopIteration

        self.counter -= 1

        curFib = self.curFib
        self.curFib = self.nextFib
        self.nextFib = curFib + self.nextFib

        return curFib



def fibonacci(n):
    #  Sample list
    sampleList = []

    if n == 0:
        return 0
    elif n == 1:
        return  0
    elif n == 2:
        return 1
    else:
        #  Returning calculated fib value.
        return fibonacci(n-1)+fibonacci(n-2)

#  Temp List
a = [5,10,15]

if __name__ == '__main__':
    # n = int(raw_input())

    #  Fib sequence list
    fib_list = []

    n = 3
    print map(cube,Fibonacci(5))


    # print map(cube,[5])