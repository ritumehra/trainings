print("=========== Number Data Types =============")

a = 5
b = 3.4
# Output: <class 'int'>
print("Type of variable a = 5: {}".format(type(a)))

# Output: <class 'float'>
print("Type of variable b = 3.4: {}".format(type(b)))

# Output: (8+3j)
c = 5 + 3j
print(c + 3)

# Output: True
print(isinstance(c, complex))

print("=========== String Data Types =============")

# all of the following are equivalent
my_string = 'Hello'
print(my_string)

my_string = "Hello"
print(my_string)

my_string = '''Hello'''
print(my_string)

# triple quotes string can extend multiple lines
my_string = """Hello, welcome to
           the world of Python"""
print(my_string)

# access characters in a string

str = 'programiz'
print('str = ', str)

#first character
print('str[0] = ', str[0])

#last character
print('str[-1] = ', str[-1])

#slicing 2nd to 5th character
print('str[1:5] = ', str[1:5])

#slicing 6th to 2nd last character
print('str[5:-2] = ', str[5:-2])

# Iterating through a string

count = 0
for letter in 'Hello World':
    if(letter == 'l'):
        count += 1
print(count,'letters found')

var_bool = True
print("Value: {} and Type: {}".format(var_bool,type(var_bool)))