i = 10
if i == 10:
    print('TRaining')

print("Training1")

# My Training Demo



print("=============== Indentation ===============")

print("For Started")
for i in range(1,11):
    print(i)
    if i == 5:
        break


print("For Started")

print("=============== Comments ===============")

# This is a comment
""" This is 
    a 
    multi line 
    comment"""

print("=============== Docstring ===============")


def sum(num, num1):
    """
        Desc: Function to find sum of two number
        :param : num : str
        :param : num1: first number ... int 
        :return : 
    """
    """ RITU """
    print("Inside Sum Function:")
    return num+num1

print(sum(2,3))
print(sum.__doc__)

