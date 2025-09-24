# fUNCTION: 

def fun(a, b, c, d=4):
    print(a, b,c,d)

#fun(c=3,b=2,a=1) # knows as key word argument 

#defult function
#fun(1,2,5) #known as positional arguments

#print("using args, kwargs")
def fun1 (a , b, *args, **kwargs):
    print(a, b)
    for arg in args:
        print(arg)
    for key in kwargs:
        print(key, kwargs[key])

#fun1(1, 2, 3, 4, 5, six=6, seven=7)
#fun1(6, 7, 8, 9)

def fun2 (a , b, *, c, d): #before asterisk * use position arguments & after use key word argument 
    print(a, b, c, d)

#fun2(1, 2, c=3, d=4)

# unpacking arguments : in unpacking arguments number of position argument must be same or
    # the length of container must match the numbers parameter in function  
def fun3(a, b, c):
    print(a, b, c)

myList = [1, 2, 3]
#fun3(*myList)

myTuple = (8,7,6)
#fun3(*myTuple)

myDict = {'a':7, 'b':9, 'c':0}
#fun3(**myDict)


