from typing import List

# Abstraction
class Vehicle:
    def __init__(self, name: str = "", brand: str = "", year: int = 0) -> None:
        self.name = name
        self.brand = brand
        self.year = year

    def drive(self) -> None:
        print(
            f"Vehicle {self.name} from the brand {self.brand} is driving since {self.year}"
        )


# Inheritance
class Car(Vehicle):
    def __init__(self, name: str = "", brand: str = "", year: int = 0):
        super().__init__(name, brand, year)


# Polymorphism
class Plane(Vehicle):
    def __init__(
        self, name: str = "", brand: str = "", year: int = 0, price: float = 0
    ):
        super().__init__(name, brand, year)
        self.price = price

    def drive(self) -> None:
        print(
            f"Plane {self.name} from the brand {self.brand} is flying since {self.year} and costed {self.price}"
        )


# Encapsulation
class Person:
    def __init__(self, name: str = "", vehicles: List[Vehicle] = []) -> None:
        self.name = name
        self.vehicles = vehicles

    def print_vehicles(self) -> None:
        print(f"{self.name} has the following vehicles:")

        for vehicle in self.vehicles:
            print(f"- {vehicle.name}")


vehicle = Vehicle()
vehicle.drive()

car = Car("Camaro", "Chevrolet", 2010)
car.drive()

plane = Plane("Boeing", "Jet 2 Holliday", 2020, 1000000)
plane.drive()

person = Person("Jeff", [car, plane])
person.print_vehicles()
