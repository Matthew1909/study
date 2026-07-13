# - attribute don't store values, it stores pointers.
# - attribute in a class x instance: class -> static/shared instance -> dinamic/unique; related to __dict__
# - attribute resolution don't operate in LEGB; it looks first in instance __dict__ then class __dict__
# - attribute can be methods hidden underneath using @property


class Car:
    model = "Ferrari"


a = Car()
b = Car()

print(a.model == b.model == Car.model)
# output: True
print(id(a.model) == id(b.model) == id(Car.model))
# output: True


class Car:
    model = "Ferrari"


car1 = Car()
car2 = Car()
car1.name = "Spider 488"

print(car1.name)
# output: Spider 488
print(car1.model)
# output: Ferrari
print(car2.model)
# output: Ferrari
# print(car2.name) ->
# output: AttributeError
print(car1.__dict__)
# output: {'name': 'Spider 488'}
print(car2.__dict__)
# output: {}
print(Car.__dict__)
# output: {'__module__': '__main__', '__firstlineno__': 20, 'model': 'Ferrari', '__static_attributes__': (),
# '__dict__': <attribute '__dict__' of 'Car' objects>, '__weakref__': <attribute '__weakref__' of 'Car' objects>, '__doc__': None}


class Car:
    name = "Spider 488"
    model = "Ferrari"


price = 4_000_000

car1 = Car()
car1.name = "SF90 Spider"

print(car1.name)
# output: SF90 Spider
print(car1.model)
# output: Ferrari
# print(car1.price) ->
# output: AttributeError


class Circle:
    def __init__(self, radius):
        self.radius = radius

    @property
    def diameter(self):
        return self.radius * 2


c = Circle(5)
print(c.diameter)
# output: 10
