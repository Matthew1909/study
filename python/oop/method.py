# method in a class is a pure function stored in class.__dict__ but when called from instance.func() then it's a method
# method has a self (instance) being injected by the . operator into the self argument
# method object is a real object in memory that unites: real function + object address (self)
# method (self) injection by . operator "can be broken" by using @classmethod and @staticmethod


class Dog:
    def __init__(self):
        pass

    def bark(self):
        return "Bark! Bark!"


rex = Dog()

print(type(Dog.bark))
# output: <class 'function'>
print(type(rex.bark))
# output: <class 'method'>


class Dog:
    def __init__(self):
        pass

    def bark(self):
        return "Bark! Bark!"


rex = Dog()

print(rex.bark() == Dog.bark(rex))
# output: True


class Dog:
    def __init__(self):
        pass

    def bark(self):
        return "Bark! Bark!"


rex = Dog()

bound_method = rex.bark

print(bound_method.__func__)
# output: <function Dog.bark at 0x7187b929f480>
print(bound_method.__self__)
# output: <__main__.Dog object at 0x7187b9290590>


class Dog:
    def __init__(self):
        pass

    def bark(self):
        return "Bark! Bark!"


rex = Dog()


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    @staticmethod
    def a_person():
        return "You are a person!"

    @classmethod
    def birth_year(cls, name, year):
        age = 2026 - year
        return cls(name, age)

    @classmethod
    def test(cls):
        return cls


print(Person.a_person())
# output: You are a person!

me = Person.birth_year("Matthew", 2002)
print(type(me))
# output: <class '__main__.Person'>
print(me.age)
# output: 24
print(me.test() == Person)
# output: True
# while self == object // cls == class
