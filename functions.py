# Create a function
def greet(msg):
    """This function greets to
    the person passed in as
    parameter"""
    print("Hello, " + msg + ". Good morning!")

#Function Call
greet("Everyone")

# Return from a function
def absolute_value(num):
    """This function returns the absolute
    value of the entered number"""

    if num >= 0:
        return num
    else:
        return -num

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))