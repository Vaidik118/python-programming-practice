# 15_composition.py

class Engine:
    def start(self):
        print("Engine started.")

    def stop(self):
        print("Engine stopped.")


class Car:
    def __init__(self, brand):
        self.brand = brand
        self.engine = Engine()

    def start_car(self):
        print(self.brand, "is starting.")
        self.engine.start()

    def stop_car(self):
        self.engine.stop()
        print(self.brand, "is stopped.")


car = Car("Toyota")

car.start_car()
print()
car.stop_car()