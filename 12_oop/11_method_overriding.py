# 11_method_overriding.py

class Animal:
    def speak(self):
        print("Animal makes a sound.")


class Dog(Animal):
    def speak(self):
        print("Dog barks.")


class Cat(Animal):
    def speak(self):
        print("Cat meows.")


animal = Animal()
dog = Dog()
cat = Cat()

animal.speak()
dog.speak()
cat.speak()