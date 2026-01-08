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