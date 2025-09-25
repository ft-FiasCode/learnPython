# Postion, name, age, level, salary
set1 = ["software engineer", "max", 30, "junior", 5000]
set2 = ["ai engineer", "bob", 40, "senior", 9000]


# class: is a blueprint(how something is define or the data sturture)
# instance (object)

class Engineer:

    # Class instance
    knownFor = "keyboard magician"  # Corrected typo

    def __init__(self, name, age, level, salary):
        # instance attributes
        self.name = name
        self.age = age
        self.level = level
        self.salary = salary

    # instance methods
    def code(self):
        print(f"{self.name} is writing code ...")

    def code_in_language(self, language):
        print(f"{self.name} is writing code in {language}...")

    def information(self):
        infor = f"name = {self.name}, age = {self.age}"
        return infor
    
    # D-under method or __ double method
#    def information1(self):
#        infor1 = f"name = {self.name}, age = {self.age}"
#        return infor1

    def __eq__(self, other):
        return self.name == other.name and self.age == self.age 
    
    # we donot use "self" as parameter in function. we can print with "self" as class instance but,
    # not as object instance. for object istance we use the @staticmethod
    @staticmethod
    def entrySalary(age):
        if age<20:
            return 5000
        if age<30:
            return 7000
        return 100
    
# Class instances
obj1 = Engineer("bob", 40, "senior", 9000)
obj2 = Engineer("max", 20, "junior", 3000)
obj3 = Engineer("max", 20, "junior", 3000)


#print(obj1.name, obj1.salary)
#print(Engineer.knownFor)

# Call instance methods
#obj1.code()
#obj2.code()
#obj1.code_in_language("python")
#obj2.code_in_language("C++")


#print(obj1.information())
##print(obj2)
#print(obj2 == obj3)


#print(obj1.entrySalary(18))
#print(obj1.entrySalary(38))
#print(Engineer.entrySalary(25))