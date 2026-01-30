name = 'John Doe'
age = 25
my_variable_name = 'freeCodeCamp'
user_age = 28

 # This is my first day of writing python
 # wish me well

first_module = 'started'
print('Hello world of Python!')
print('I have not eaten today and I have arabic class now which')

my_integer_var = 10
print('Integer:', my_integer_var)
Integer: 10

my_float_var = 4.50
print('Float:', my_float_var)
Float: 4.5

my_string_var = 'hello'
print('String:', my_string_var)

my_boolean_var = True
print('Boolean:', my_boolean_var)
Boolean: True

# set is an unordered collection of unique elements
my_set_var = {4,7,2}
print('Set:', my_set_var)

#Dictionary: A collection of key-value pairs enclosed in curly b\races
my_dictionary_var = {'name': 'Aish', 'age': 25}
print('Dictionary:', my_dictionary_var)   
      
# Tuple: An immutable ordered collection, enclosed in brackets
my_tuple_var = (7,6,4)
print('Tuple:', my_tuple_var)

#Range: A sequence of numbers, often used in loops
my_range_var = range(10)
print('Range:', my_range_var)

# List: An ordered collection of elements that supports different data types.
my_list_var = [3, 'hello', 5.6, True]
print('List:', my_list_var)

# None: A special value that represents the absence of a value.
my_none_var = None
print('None:', my_none_var)

# To get the data type of a variable, you can use the type() function:
my_var_1 = 'Aish prcticing python'
my_var_2 = 42
print(type(my_var_1))  # Output: <class 'str'>
print(type(my_var_2))  # Output: <class 'int'>

# The built-in isinstance() function lets you check if a variable matches a specific data type. It takes in an object and the type you want to check it against, then returns a boolean.

my_var_3 = None
print(isinstance(my_var_3, type(None)))  # Output: True
#isinstance(None, type(None)) 

# Strings and string immutability
my_str_1 = '''Multiline
string'''
msg = 'It\'s a beautiful day!'

# in operator
print('a long' in msg)

# indexing, you use the len() function to get the length of the string
print(len(msg))  # Output: 21
print(msg[0])   # Output: I
print(msg[-4])  # Output: d
print(msg[-1])  # Output: !

# Strings are immutable data types in Python. This means that you can reassign a different string to a variable:
greeting = 'Hi'
greeting = 'Hello'  # Reassigned to a new string
print(greeting)  # Output: Hello
# greeting[0] = 'd'  # This will raise a TypeError

#string concatenation, using the + operator
my_str_1 = 'Hello '
my_str_2 = 'world!'
str_plus_str = my_str_1 + my_str_2
print(str_plus_str)
# youcan't concatenate a string with a non-string data type directly, like a string and integer
# convert the integer to a string using the str() function
name = 'Aish'
age = 25
greeting = 'My name is ' + name + ' and it\'s written that I am ' + str(age) + ' years old.'
print(greeting)
#f-strings (formatted string literals) helps with interrpolation
name = 'Aish'
age = 25
name_and_age = f'My name is {name} and I am {age} years old.'
print(name_and_age)
num1 = 10
num2 = 28
print(f'The sum of {num1} and {num2} is {num1 + num2}.')
#slicing string[start:stop]
my_str = 'Waiver to differ'
print(my_str[7:]) 
print(my_str)
# [start:stop:step]
visa_app = 'Applicationfee'
print(visa_app[0:10:2])

#working with integers and floats
# addition using +
# subtraction using -
# multiplication using *
# division using /
# pwerforming basic operations bwteen integers and floats returns a flaot 
int_1 = 10
int_2 = 3
floor_division = int_1 // int_2
print(floor_division)  # Output: 3

# augumented assignment operators
# syntax: variable operator= value 
# which means variable = variable <operator> value
my_var = 15
my_var += 5  # Equivalent to my_var = my_var + 5
print(my_var)  # Output: 20

total_pages = 42
total_pages //= 4
print(total_pages)  # Output: 10

greet = 'Hello'
greet += ' my dear'
print(greet)  # Output: Hello my dear

# you can only use + and * operators with strings
repeat_str = 'ha' * 3
print(repeat_str)  # Output: hahaha

# booleans and conditionals
# if condition:
#  pass   # code to execute if condition is True
# pass serves as a placeholder for code that will be added later
# In python, code blocks are determined by indentation

age = 16
if age >= 18:
    print('O ti ripe lati dibo')  # Output: O ti ripe lati dibo
else:
    print('gba ile yin lor')

# elif statement for multiple conditions
age = 20

if age >= 65:
    print('O le gba ifowopamosi agbalagba')
elif age >= 18:
    print('you never old reach')
else:
    print('du sind kind')

# truthy and falsy values
# Falsy values in Python include: False, None, 0, 0.0, '', [], {}, set(), range(0)
# Everything else is considered truthy
# boolean operators: and, or, not
is_raining = True
has_umbrella = False
if is_raining and has_umbrella:
    print('You can go outside.')
else:
    print('Better stay indoors.')

# use or to check if at least one condition is true
is_weekend = True
has_homework = False
if is_weekend or has_homework:
    print('You can relax or do your homework.')
else:
    print('Time to study!') 

# use not to invert a boolean value, it returns True if the value is False and vice versa
is_sunny = False
if not is_sunny:
    print('It\'s not sunny outside.')
else:
    print('Enjoy the sunshine!')

# functions and scopes
# input() function to get user input as a string
name = input('Enter your damn name')
print('hello', name)

# custom functions using def keyword
def first_function():
    print('now, we write functions and fight crimes')
first_function()
def calculate_sum(a,b):
    print(a + b)
calculate_sum(3, 7)

# return keyword to send back a value from a function
my_sum = calculate_sum(10, 15)
print(my_sum)  # python returns None if return is not expliitly used
def calculate_sum(a, b):
    return a + b

my_sum = calculate_sum(9, 76)
print(my_sum)

# scope: local, enclosing, global and built-in scopes (LEGB)
# use global keyword to modify a global variable inside a function
# use nonlocal keyword to modify a variable in the enclosing scope
counter = 0  # global scope
def increment_counter():
    global counter
    counter += 1
increment_counter()
print(counter)  # Output: 1
#a rough patch to explain commit messages
counter = 0
def outer_function():
    counter = 10  # enclosing scope
    def inner_function():
        nonlocal counter
        counter += 5
    inner_function()
    print(counter)  # Output: 15