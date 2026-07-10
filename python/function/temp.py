# THIS TEMP IS JUST A FILE TO IMPORT STUFF FROM OTHER FILES.PY TO TEST CONCEPTS

# By testing stuff this way I found out that python has a "weird" way to treat modules and imports
# it basically run all the original file first and then run the file where you imported the function
# so to avoid any weirdness you should use __name__ == '__main__' to test in your original file.

from closure import list_num, outer_function

# TEST: power of exporting/importing closures:
# NOT GOOD; by importing the variable you import "an object" and so, you have one context only
list_num(8)
list_num(7)
list_num(6)

# list_num2 = list_num() # can't do that
list_num2 = list_num
# can do but will be the same as just renaming list_num the context is still the same.
list_num2(5)
list_num2(4)
list_num2(3)

# by importing the function itself everytime you create an instance you get a new fresh context
list = outer_function()
list(10)
list(9)
list(8)

# creates a fresh new context.
list1 = outer_function()
list1(10)
list1(9)
list1(8)

# RESUME: CLOSURE IS BASICALLY A CLASS GENERATING OBJECTS; (now it makes more sense to say that everything
# in python is an object)

print("==========================================================================")
print("==========================================================================")
print("==========================================================================")
