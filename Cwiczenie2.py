class Pet:
    pass


pet = Pet()

print(pet)
print(isinstance(pet, Pet))
print(isinstance(pet, object))


class Mammal(Pet):
    pass


class Reptile(Pet):
    pass


mammal = Mammal()
reptile = Reptile()

print(mammal)
print(isinstance(mammal, Mammal))
print(isinstance(mammal, Pet))
print(isinstance(mammal, object))

print(reptile)
print(isinstance(reptile, Reptile))
print(isinstance(reptile, Pet))
print(isinstance(reptile, object))

print(isinstance(reptile, Mammal))
print(isinstance(mammal, Reptile))


class Dog(Mammal):
    pass


class Cat(Mammal):
    pass


class Hamster(Mammal):
    pass


dog = Dog()
cat = Cat()
hamster = Hamster()

print(dog)
print(isinstance(dog, Dog))
print(isinstance(dog, Mammal))
print(isinstance(dog, Reptile))
print(isinstance(dog, Pet))
print(isinstance(dog, object))

print(cat)
print(isinstance(cat, Cat))
print(isinstance(cat, Mammal))
print(isinstance(cat, Reptile))
print(isinstance(cat, Pet))
print(isinstance(cat, object))

print(hamster)
print(isinstance(hamster, Hamster))
print(isinstance(hamster, Mammal))
print(isinstance(hamster, Reptile))
print(isinstance(hamster, Pet))
print(isinstance(hamster, object))


class Turtle(Reptile):
    pass


class Gecko(Reptile):
    pass


class Chameleon(Reptile):
    pass


turtle = Turtle()
gecko = Gecko()
chameleon = Chameleon()

print(turtle)
print(isinstance(turtle, Turtle))
print(isinstance(turtle, Reptile))
print(isinstance(turtle, Mammal))
print(isinstance(turtle, Pet))
print(isinstance(turtle, object))

print(gecko)
print(isinstance(gecko, Gecko))
print(isinstance(gecko, Reptile))
print(isinstance(gecko, Mammal))
print(isinstance(gecko, Pet))
print(isinstance(gecko, object))

print(chameleon)
print(isinstance(chameleon, Chameleon))
print(isinstance(chameleon, Reptile))
print(isinstance(chameleon, Mammal))
print(isinstance(chameleon, Pet))
print(isinstance(chameleon, object))
