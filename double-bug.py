# Exercise: Read the code below and write down what the bug is. How would you fix it?
 
# Buggy version:
def double(number):
    return number * 3  # Bug: the function is called "double" but multiplies by 3 instead of 2.
 
print(double(10))  # Returns 30 - wrong! Expected 20.
 
# Why type checking can't catch this:
# The function receives a number and returns a number - types are correct.
# The bug is in the logic, not the type. Type checking only checks types, not intent.
 
# Fix: change * 3 to * 2
def double_fixed(number):
    return number * 2
 
print(double_fixed(10))  