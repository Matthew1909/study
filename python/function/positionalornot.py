# / -> all args to the left HAVE TO BE positional
# * -> all args to the right HAVE TO BE keyword

# / can never be at the start of function scope; * can never be at the end;
# in case of using both the / have to appear before the * following the rule of:
#   positional, keyword // *args, **kwargs // /, *

# e.g.:
def my_function(a, b, c, /):
    print(a, b, c)


# all args must be positional
my_function(1, 2, 3)


def my_function(*, a, b, c):
    print(a, b, c)


# all args must be keyword
my_function(a=1, b=2, c=3)


def my_function(a, /, *, b, c):
    print(a, b, c)


# a must be positional, b and c must be keyword
my_function(1, b=2, c=3)
