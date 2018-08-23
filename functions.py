def sum(num1,num2):
    total_sum = num1+num2
    print("def sum(num1,num2):::",total_sum)
    # return total_sum

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
    val = sum(1, 2)

    if num >= 0:
        return num
    else:
        return -num

ret_val = absolute_value(2)
# Output: 2
print(ret_val)

# Output: 2
print(absolute_value(2))

# Output: 4
print(absolute_value(-4))



# val = sum(1,2)
# print(val)

