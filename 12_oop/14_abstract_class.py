# 14_abstract_class.py

from abc import ABC, abstractmethod


class Vehicle(ABC):

    @abstractmethod
    def start(self):
        pass

    @abstractmethod
    def stop(self):
        pass


class Car(Vehicle):

    def start(self):
        print("Car started.")

    def stop(self):
        print("Car stopped.")


class Bike(Vehicle):

    def start(self):
        print("Bike started.")

    def stop(self):
        print("Bike stopped.")


car = Car()
car.start()
car.stop()

print()

bike = Bike()
bike.start()
bike.stop()