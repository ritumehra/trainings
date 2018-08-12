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
    """Function to find sum of two number"""
    print("Inside Sum Function:")
    return num+num1

print(sum.__doc__)

