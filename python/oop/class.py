# - class in py creates a new type.
# - class is an object.
# - class define a block of code that will execute even though I have not created an instance of it.
# - class is a big dict for its attribute.
# - class can have attributes that will be shared among the objects (all pointing to the same place in memory)
# - class is a bag of data in its purest mode.
# - class attributes can be modified for an instance only.
# - class __dict__ is created brand new for an instance.

class Animal:
    pass


dog = Animal()
print(type(dog))
# output: <class '__main__.Animal'>
# this says: this is an object of class type, in __main__ "current file" and Animal is the class name.

print(type(Animal))
# output: <class 'type'>
# this says: that the class Animal is nothing more than an instance of class type


class Animal:
    print("This is an animal.")

# output: This is an animal.
# it works, in other languages class only tells the compiler instructions on how to build the object
# in python the code is executed even without an instance.


class Animal:
    name = "Lion"
    habitat = "Savanna"


print(Animal.__dict__['name'])
# output: Lion
print(Animal.__dict__['habitat'])
# output: Savanna


class Cart:
    products = []


client1 = Cart()
client2 = Cart()

client1.products.append("Laptop")

print(client1.products)
# output: ['Laptop']
print(client2.products)
# output: ['Laptop']


class Animal:
    pass


Animal.name = "Whale"
Animal.habitat = "Sea"

print(Animal.name)
# output: Whale
print(Animal.habitat)
# output: Sea


class Animal:
    habitat = "Savanna"


whale = Animal()
whale.habitat = "Sea"

print(whale.habitat)
# output: Sea
print(Animal.habitat)
# output: Savanna
# when I use the = operator to assign a new value to habitat in an object, the .habitat is written in
# that instance __dict__ brand new. If instead of writting I tryed to read the value it would follow
# the logic: search in instance __dict__ if not found then searched in class __dict__ if also not
# found AttributeError.


class Animal:
    name = "Lion"


dog = Animal()

print(Animal.__dict__['name'])
# output: Lion
print(dog.__dict__)
# output: {}
# that helps understand why if I try dog.name = "dog" the class attribute name in Animal won't be changed.
