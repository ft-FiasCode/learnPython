# Variable is like a labeled box which holds data or values.
# Variables allow us to store information and reuse it later in the program.
# Variables do not require data type declaration, Python figures out the type automatically.

# Creating variables and assigning values:
name = "ft-FiasCode"       # string variable
age = 20            # integer variable
height = 5.9        # float variable
is_student = True   # boolean variable

print(name)
print(age)
print(height)
print(is_student)

# Updating variable values:
age = 21
print(age)

# Variables can be used in expressions:
greeting = "Hello, " + name
print(greeting)

# Variables can hold any data type and can change types later:
x = 10
x = "Now I'm a string!"
print(x)

# Variable naming rules:
# Variable names can contain letters, numbers, and underscores (_)
# Variable names cannot start with a number
# Variable names are case-sensitive (age and Age are different variables)
# Avoid using Python keywords as variable names (like 'print', 'if', 'for')

# Global variable: defined outside any function, accessible anywhere in the file
city = "New York"

# Local variable: defined inside a function, accessible only within that function
def show_city():
    country = "USA"   # local variable
    print(city)       # accessing global variable inside function
    print(country)    # accessing local variable inside function

show_city()
#print(country)  # This would cause an error because 'country' is not visible outside the function

# Using 'global' keyword to modify global variable inside a function
count = 0

def increment():
    global count
    count = count + 1

increment()
print(count)
