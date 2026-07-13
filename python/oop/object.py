# - objects are essentially an empty container originated from a class and thus with its own (empty) __dict__
# - objects even though made from the same class are totally independent in memory.
# - objects have a "hidden" pointer (__class__) back to the class that spawned it.


class Human:
    pass


adam = Human()

print(Human.__dict__)
# output: {'__module__': '__main__', '__firstlineno__': 6, '__static_attributes__': (),
# '__dict__': <attribute '__dict__' of 'Human' objects>, '__weakref__': <attribute '__weakref__' of 'Human' objects>, '__doc__': None}
print(adam.__dict__)
# output: {}


class Human:
    pass


adam = Human()
eve = Human()

print(adam == eve)
# output: False
print(id(adam), id(eve))
# output: 127172067526368 127172067444048


class Human:
    pass


adam = Human()

print(adam.__class__)
# output: <class '__main__.Human'>
