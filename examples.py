def sayHello(name):
  print(f'Hello {name}')

sayHello2 = sayHello

IS_DEV = False

def fetch_data_real():
  # fetch data from server/database/etc.
  print('Fetching data from server...')

def fetch_data_fake():
  print('Returning fake data...')
  return { 'name': 'Shaun' }

fetch_data = fetch_data_fake if IS_DEV else fetch_data_real

# Lists o functions ##########################################################

# f(x) = 2x
def double(x):
  return x * 2

# f(x) = x - 1
def subtract_one(x):
  return x - 1

# f(x) = x^2
def square(x):
  return x * x

# f(x) = (2x - 1)^2

function_list = [
  double,
  subtract_one,
  square,
]

my_number = 10

for func in function_list:
  my_number = func(my_number) # Don't actually do this

# Passing Functions as Arguments ###########################

def add(x, y):
  return x + y

def subtract(x, y):
  return x - y

def combine(x, y, op):
  return op(x, y)

  # Returning Functions ##################################

def create_printer():
  def printer():
    print('Hello functional')
  
  return printer

def create_multiplier(y):
  def multiplier(x):
    return x * y

  return multiplier

# Closure ##########################

def create_number_printer():
  my_favorite_number = 42

  def printer():
    print(f'My favorite number is {my_favorite_number}')

  return printer

# Higher-Order Functions ######################

def divide(x, y):
  return x / y

def create_safe_version(func, arg_checks):
  def safe_version(*args, **kwargs):
    check_results = [check(*args, **kwargs) for check in arg_checks]
    if (not all(check_results)):
      print('Argument check failed!')
      return
    return func(*args, **kwargs)

  return safe_version

def first_arg_isnt_100(*args):
  return args[0] != 100

person = {
  'name': ''
}

# zip_safe = create_safe_version(zip, [args_are_same_length])
# my_function_safe = create_safe_version(my_function, [first_arg_isnt_100, second_arg_isnt_zero, args_are_same_length])


def args_are_same_length(*args):
  return len(args[0]) == len(args[1])

def second_arg_isnt_zero(*args):
  return args[1] != 0

divide_safe = create_safe_version(divide, [second_arg_isnt_zero])

# Map ##############

numbers = [1, 2, 3, 4, 5, 6, 7, 8]
strings = ['a', 'b', 'c']
people = [{
  'name': 'John',
  'age': 100,
}, {
  'name': 'Jane',
  'age': 54,
}, {
  'name': 'Bill',
  'age': 25,
}]

def double(x):
  return x * 2

def uppercase(x):
  return x.upper()

def some_function(x, y, z):
  return x + y + z

def create_property_getter(property):
  def get_property(dictionary):
    return dictionary[property]

  return get_property

doubled_numbers = list(map(double, numbers))
uppercased_strings = list(map(uppercase, strings))
ages = list(map(create_property_getter('age'), people))

# Filter ###########

def is_even(x):
  return x % 2 == 0

def create_age_test(min_age):
  def age_test(person):
    return person['age'] > min_age

  return age_test

even_numbers = list(filter(is_even, numbers))
old_people = list(filter(create_age_test(60), people))

# Reduce ###########

# List Comprehensions ###################

doubled_numbers_lc = [x * 2 for x in numbers]
uppercased_strings_lc = [str.upper() for str in strings]
people_names = [person['name'] for person in people]

even_numbers_lc = [x for x in numbers if x % 2 == 0]
old_people_lc = [person['name'] for person in people if person['age'] > 25]