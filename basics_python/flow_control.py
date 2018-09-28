#
# print("=========== if.. elif..else =============")
#
# # If the number is positive, we print an appropriate message
#
# # num = 3
# # if num > 0:
# #     print(num, "is a positive number.")
# # print("This is always printed.")
#
# # num = -1
# # if num > 0:
# #     print(num, "is a positive number.")
# # print("This is also always printed.")
#
# num = 4
# if num > 0:
#     print(num, "is a positive number.")
# else:
#     print(num, "is a nehative number.")
#
# num = -9
# if num > 0:
#     print(num, "is a positive number.")
# elif num == 0:
#     print(num, "is ZERO.")
# elif num < 0:
#     print(num, "is a negative number.")
# else:
#     print("INVALID NUMBER")
#
# num = 3
#
# # Try these two variations as well.
# # num = -5
# # num = 0
#
# if num >= 0:
#     print("Positive or Zero")
# else:
#     print("Negative number")
#
# num = 3.4
#
# # Try these two variations as well:
# # num = 0
# # num = -4.5
#
# if num > 0:
#     print("Positive number")
# elif num == 0:
#     print("Zero")
# else:
#     print("Negative number")

print("=========== for loop =============")

# Program to find the sum of all numbers stored in a list
#
# # List of numbers
# numbers = [1, 1, 1, 1, 1]
#
# # variable to store the sum
# sum=0
#
# # iterate over the list
# for val in numbers:
#     sum = sum+val
#
# # Output: The sum is 48
# print("The sum is", sum)
#
# # A for loop can have an optional else block as well. The else part is executed if the items in the sequence used in for loop exhausts.
#
# digits = [0, 1, 5]
#
# for i in digits:
#     print(i)
# else:
#     print("No items left.")

# print("=========== while loop =============")

# n = 10
#
# # initialize sum and counter
# sum = 0
# i = 1
#
# while i <= n:
#     sum = sum + i
#     i = i+1    # update counter
#
# print("i::",i)
# # print the sum
# print("The sum is", sum)
#
# counter = 0
#
# # The else part is executed if the condition in the while loop evaluates to False.
#
# while counter < 3:
#     print("Inside loop")
#     counter = counter + 1
# else:
#     print("Inside else")

# print("=========== break statement =============")
#
# # Use of break statement inside loop
#
# for val in "string":
#     if val == "i":
#         break
#     print(val)
#
# print("The end")
#
# print("=========== continue statement =============")
#
# # Program to show the use of continue statement inside loops
#
# for val in "string":
#     if val == "i":
#         continue
#     print(val)
#
# print("The end")

for val in "string":
    pass