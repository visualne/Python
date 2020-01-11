# def outer():
#     x = 1
#     b = 2
#     def inner():
#         return x + b # 1
#     return inner
#
#
# foo = outer()
# print foo()

# def test(x,y,*args):
#     print x,y,args
#
# test(1,2,3,4,5,6)

#  Arguments can be passed into functions as follows.
#  if they are passed in as *lst they will be unpacket appropirtely.
# def add(x,y,*args):
#     print x + y
#
# lst = [1,2,3]
# #  Call function as follows
# add(*lst)
#
# #  kwargs will be a dictionary that will be of random length.
# def test(**kwargs):
#     print kwargs
#
#
# #  Call function as follows
# test(a=1,b=2,c=3)
#
# #  Call also fill in variables as follows with a dictionary
# dct = {'x': 1, 'y': 2}
# def bar(x, y):
#     return x + y
#
# bar(**dct)

#
#  Decorator example using *args and **kwargs
# def logger(func):
#     def inner(*args, **kwargs): #1
#         print "Arguments were: %s, %s" % (args, kwargs)
#         return func(*args, **kwargs) #2
#     return inner
#
#
# @logger
# def foo1(x, y=1):
#     return x * y
#
# a = {'x':5,'y':4}
# foo1(**a)

# class myDecorator(object):
#
#     def __init__(self, f):
#         print "inside myDecorator.__init__()"
#         f() # Prove that function definition has completed
#
# @myDecorator
# def aFunction():
#     print "inside aFunction()"

def entryExit(f):
    def new_f():
        print "Entering", f.__name__
        f()
        print "Exited", f.__name__
    return new_f

a = 1
b = 2
@entryExit
def func1():
    print "inside func1()"

func1(a,b)

