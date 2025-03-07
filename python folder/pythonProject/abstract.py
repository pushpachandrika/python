from abc import ABC, abstractmethod
class Animal(ABC):

    @abstractmethod
    def make_sound(self):
        """Abstract method that must be implemented in a subclass."""
        pass

    def sleep(self):
        """Non-abstract method that can be used directly by subclasses."""
        print("This animal is sleeping.")
# A subclass that implements the abstract method
class Dog(Animal):

    def make_sound(self):
        print("Woof!")
# Another subclass that implements the abstract method
class Cat(Animal):
    def make_sound(self):
        print("Meow!")
# Create instances of Dog and Cat
dog = Dog()
dog.make_sound()
dog.sleep()
cat = Cat()
cat.make_sound()
cat.sleep()







from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def dog_info(self):
        self.move()
dog = Dog()
dog.make_sound()
dog.dog_info()







from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def create_and_call(self):
        dog_instance = Dog()
        dog_instance.make_sound()
        dog_instance.move()
dog = Dog()
dog.create_and_call()






from abc import ABC, abstractmethod
class Animal(ABC):
    @abstractmethod
    def make_sound(self):
        pass
    def move(self):
        print("The animal moves.")
class Dog(Animal):
    def make_sound(self):
        print("Woof! Woof!")
    def create_and_call(self):
        dog_instance = Dog()
        dog_instance.move()
dog = Dog()
dog.create_and_call()


