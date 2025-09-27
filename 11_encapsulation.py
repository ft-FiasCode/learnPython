# Encapsulation: is the mechanism of hiding of data implemation and restrication the access;
# so this means that instance variable are kept private and
# there is only one access method form the outside form which we can acess or change these instance variables.
# so this erstrict the public methods so called get & set methods and instance methods can be kept private,
# so they can be use internaly, not from the outside.

class SoftwareEngineer:

    def __init__(self, name, age):
        self.name = name
        self.age = age
        # _x is called a "protected" attribute(one underscore)
        # __x is called a "private" attribute(double underscore)
        self._salary = None # if we use '_' then it can be access form the ojbect
        #self.__salary1 = None
        self.numBugSolved = 0


    def code(self):
        self.numBugSolved += 1

    # setter
    def setSalary(self, base_value):
        self._salary = self._calculateSalary(base_value)


    def _calculateSalary(self, base_value):
        if self.numBugSolved < 10:
            return base_value
        if self.numBugSolved < 100:
            return base_value * 2
        return base_value * 3

    # getter
    def getSalary(self):
        return  self._salary


# object
se = SoftwareEngineer("Max",34)
print(se.age, se.name)

# we should not access the salary for outside
#print(se._salary)
#print(se.__salary1)


for i in range(20):
    se.code()

se.setSalary(5000)
print(se.getSalary())

