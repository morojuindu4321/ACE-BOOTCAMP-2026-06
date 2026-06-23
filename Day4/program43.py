from abc import ABC , abstractmethod
class Animal(ABC):
    @abstractmethod
    def eat(self):
        pass
    @staticmethod
    def sleep():
        return "I am sleeping"
class Dog(Animal):
    def eat(self):
        return "dog is eating"
d1=Dog()
print(d1.sleep())
print(d1.eat())