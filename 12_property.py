
class SoftwareEngineer:

    def __init__(self):
        self._salary = None       

    
    # getter
    @salary.setter
    def salary(self):
        return  self._salary
   
    # setter
    @property
    def salary(self, value):
        self._salary = value


# object
se = SoftwareEngineer()

se.salary = 6000
print(se.salary)

