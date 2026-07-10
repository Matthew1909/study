# LEGB -> Local, enclosing, global, built-in
# global flag mark a variable that you wanna change in global scope
# nonlocal flag mark a variable that you wanna change in nonlocal and not global scope
# e.g:
# Base test
var_global = 10


def my_function():
    var_enclosing = 9

    def inner_function():
        var_local = 8
        return var_local

    return inner_function


# built-in
# print("Hello World!")

# ==============================================================================

# Change the global
var = 10


def my_function():
    var = 9
    print("nonlocal/enclosing:", var)

    def inner_function():
        global var
        var = 8
        return True

    x = inner_function()
    if x:
        print("nonlocal/enclosing:", var)

    return inner_function


print("====================================")
print("Global:", var)
my_function()
print("Global changed:", var)

# ==============================================================================

# Change the nonlocal
var = 10


def my_function():
    var = 9
    print("nonlocal/enclosing:", var)

    def inner_function():
        nonlocal var
        var = 8
        return True

    x = inner_function()
    if x:
        print("nonlocal/enclosing after change:", var)

    return inner_function


print("====================================")
print("Global:", var)
my_function()
print("Global:", var)
