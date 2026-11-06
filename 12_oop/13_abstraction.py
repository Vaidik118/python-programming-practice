# 13_abstraction.py

from abc import ABC, abstractmethod


class Animal(ABC):

    @abstractmethod
    def sound(self):
        pass

    def sleep(self):
        print("Animal is sleeping.")


class Dog(Animal):

    def sound(self):
        print("Dog barks.")


class Cat(Animal):

    def sound(self):
        print("Cat meows.")


dog = Dog()
cat = Cat()

dog.sound()
dog.sleep()

cat.sound()
cat.sleep()