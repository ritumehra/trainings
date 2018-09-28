# Operators

print("=========== Arithmetic Operators =============")

x = 5
y = 2

# Output: x + y = 7
print('x + y =', x + y)

# Output: x - y = 3
print('x - y =', x - y)

# Output: x * y = 10
print('x * y =', x * y)

# Division Returns Exact Quotient
# Output: x / y = 2.5
print('x / y =', x / y)

# Floor Division : Returns Quotient
# Output: x // y = 2
print('x // y =', x // y)

# Exponent :
# Output: x ** y = 16
print('x ** y =', x ** y)

# Modulas : Returns remainder
print('x % y =', x % y)


print("=========== Comparision Operators =============")

x = 10
y = 12

# Output: x > y is False
print('x > y  is', x > y)

if x>y:
    print("X is greater")
else:
    print("y is greater")

# Output: x < y is True
print('x < y  is', x < y)

# Output: x == y is False
print('x == y is', x == y)

# Output: x != y is True
print('x != y is', x != y)

# Output: x >= y is False
print('x >= y is', x >= y)

# Output: x <= y is True
print('x <= y is', x <= y)

print("=========== Logical Operators =============")

x = True
y = False

# Output: x and y is False
print('x and y is', x and y)

# Output: x or y is True
print('x or y is', x or y)

# Output: not x is False
print('not x is', not x)

print("=========== Identity Operators =============")

x1 = 5
y1 = 5
x2 = 'Hello'
y2 = 'Hello'
x3 = [1,2,3]
y3 = [1,2,3]

# Output: False
print(x1 is not y1)

# Output: True
print(x2 is y2)

# Output: False
print(x3 is y3)

print("print(type(x1) is int):::")
print(type(x1) is int)

print("=========== Membership Operators =============")

x = 'Hello world'
y = {1:'a','xoriant':'b'}

# Output: True
print('H' in x)

# Output: True
print('hello' not in x)

# Output: True
print(1 in y)

if('xoriant' in y):
    print(y['xoriant'])

# Output: False
print('a' in y)