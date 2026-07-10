# Closure: is a function inside another function
my_list = []


def my_function(x):
    my_list.append(x)
    print(my_list)


# my_function(8)
# my_function(7)
# my_function(6)
# after these the output will be:
# [8]
# [8, 7]
# [8, 7, 6]
# if this is what I want to, then I can use closure so the "outer" list can be imported with the function
# it belongs to.
# e.g.:


def outer_function():
    my_list = []

    def inner_function(x):
        my_list.append(x)
        print(my_list)

    # in order to run this inner_function the outer_function must return the inner
    return inner_function


list_num = outer_function()


if __name__ == '__main__':
    # by doing so list_num now is basically inner_function + my_list, so:
    list_num(8)
    list_num(7)
    list_num(6)
