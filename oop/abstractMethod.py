from abc import ABC, abstractmethod

class Animal(ABC):
    @abstractmethod
    def speak(self):
        pass

    def eat(self):
        print("Eating...")

class Dog(Animal):
    def speak(self):
        print("Woof!")

# animal = Animal() # This would raise a TypeError
dog = Dog()
dog.speak()
dog.eat()