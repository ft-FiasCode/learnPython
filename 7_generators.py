# Generators: generators are functions that returns an object that can be ilterated and and a special
# thing is that they generate the items inside the object lazily which means they generates the items
# only at a time and only when you ask for it & because of this they are much more memory efficient
# than other objects when you have deal with large datesets 

def myGenarator():
    yield 1
    yield 2
    yield 3

g = myGenarator()

#for i in g:
#    print(i)

#value = next(g)
#print(value)

#print(sum(g)) 
# print(sorted(g))

#def countDown(num):
#    print('starting')
#    while num > 0:
#        yield num
#        num -=1

#cd = countDown(4)

#value = next(cd)
#print(value)

#print(next(cd))
#print(next(cd))
#print(next(cd))


# 0 1 1 2 3 5 8 13 ...
def fibonacci(limit):
    a , b = 0, 1
    while a < limit:
        yield a
        a , b = b, a+b

#fib = fibonacci(30)
#for i in fib:
    #print(i)


import sys
myGenarator1 = {i for i in range(10000)if i % 2 == 0}
print(sys.getsizeof(myGenarator1))


mylist = [i for i in range(10000)if i % 2 == 0]
print(sys.getsizeof(mylist))