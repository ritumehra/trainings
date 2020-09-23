# Example keywords

import keyword
print(keyword.kwlist)

# Identifiers

# Cannot use keywords as (identifiers) variable/function  names
# if = 1

# Case Sensitive
train_var = " Training";
train_Var = "Training Var";
train_var = " Training Var";
print(train_var, "\n", train_Var)

# Cannot start with a digit.
# Cannot use special symbols like !, @, #, $, % etc.
# below statements gives error
# 1var = 1
# var@123 = 123