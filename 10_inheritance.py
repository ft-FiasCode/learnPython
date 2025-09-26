# inheritance is a process by which one class takes on the attributes and methods of onther class, so this newly form
# class is then called child class and the onther one is called parent class 

# inherits, extend, override
class Employee:
    
    def __init__(self, name, age,salary):
        self.name = name
        self.age = age
        self.salary = salary

    def work(self):
        print(f"{self.name} is working ...")

class SoftwareEngineer(Employee):
    
    def __init__(self, name, age, salary, level):
        super().__init__(name, age, salary)
        self.level = level

    def debug(self):
        print(f"{self.name} is dubuging ...")

#    def work(self):
#        print(f"{self.name} is coding ...")



class Designer(Employee):
    def draw(self):
        print(f"{self.name} is drawing ...")

    def work(self):
        print(f"{self.name} is desiging ...")



# istances
emp1 = SoftwareEngineer("max", 33, 3000,"junior")
##print(emp1.name,emp1.age,emp1.salary,emp1.level)
#print(emp1.level)
#emp1.debug()
#emp1.work()

emp2 = Designer("bob",22, 4000)
##print(emp2.name, emp2.age)
#emp2.draw()
#emp2.work()

# Polymorphism : many forms, which works in super class and sub class

employees = [SoftwareEngineer("lisa", 33, 8000,"senior"),
             SoftwareEngineer("max", 19, 6000,"junior"),
             SoftwareEngineer("maa", 20, 3000,"junior"),
             Designer("bob",22, 4000)]





def motivate_employees(employees):
    for employee in employees:
        employee.work()



motivate_employees(employees)