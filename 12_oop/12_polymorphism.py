# 12_polymorphism.py

class Dog:
    def sound(self):
        print("Dog barks.")


class Cat:
    def sound(self):
        print("Cat meows.")


class Cow:
    def sound(self):
        print("Cow moos.")


def make_sound(animal):
    animal.sound()


dog = Dog()
cat = Cat()
cow = Cow()

make_sound(dog)
make_sound(cat)
make_sound(cow)