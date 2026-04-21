# a = [1, [2, 3]]
# b = a   # no copy

# b[1][0] = 99

# print(a)  # [1, [9, 3]]
# print(b)  # [1, [99, 3]]
# print(id(a))
# print(id(b))


# import copy
# import copy


# import copy

# a = [1, [2, 3]]
# b = copy.copy(a)     # shallow copy

# print(id(a))
# print(id(b))         # DIFFERENT

# print(id(a[1]))
# print(id(b[1]))      # SAME inner list


# class A:
#     def add(self, x, y):
#         return x + y

# class B(A):
#     def add(self, x, y):
#         return x + y + 10

# print(B().add(5, 5))

# class Test:
#     def add(self, *nums):   # simulated overloading
#         print(sum(nums))

# t = Test()
# t.add(10)
# t.add(10, 20)
# t.add(10, 20, 30)
# t.add(10)

# class Test:
#     def add(self, a):
#         print(a)

#     def add(self, a, b):
#         print(a + b)

# t = Test()
# t.add(10, 20)  # works
# t.add(10,3,7)      # ERROR: missing argument


# # ------------------------------
# # POLYMORPHISM EXAMPLE IN PYTHON
# # ------------------------------

# # BASE CLASS / PARENT CLASS
# class Animal:
#     def sound(self):                # INSTANCE METHOD
#         print("Some generic animal sound")  # default behavior

# # CHILD CLASS 1
# class Dog(Animal):
#     def sound(self):                # OVERRIDING (runtime polymorphism)
#         print("Woof Woof")          # Dog-specific behavior

# # CHILD CLASS 2
# class Cat(Animal):
#     def sound(self):                # OVERRIDING
#         print("Meow Meow")         # Cat-specific behavior

# # DUCK TYPING CLASS (No inheritance)
# class Airplane:
#     def sound(self):                # same method name
#         print("Airplane sound")    # completely different class

# # FUNCTION demonstrating polymorphism
# def make_sound(obj):                # obj can be any object with sound() method
#     obj.sound()                     # works for all objects → duck typing

# # ------------------------------
# # OBJECTS / INSTANCES
# # ------------------------------
# a1 = Animal()                       # object of parent
# d1 = Dog()                           # object of child 1
# c1 = Cat()                           # object of child 2
# p1 = Airplane()                      # object of unrelated class

# # ------------------------------
# # POLYMORPHIC BEHAVIOR
# # ------------------------------
# animals = [a1, d1, c1, p1]

# for obj in animals:
#     make_sound(obj)                  # same function call, different behavior

# # ------------------------------
# # OUTPUT EXPLAINED WITH #
# # ------------------------------
# # Animal.sound() → "Some generic animal sound"
# # Dog.sound()    → "Woof Woof"
# # Cat.sound()    → "Meow Meow"
# # Airplane.sound() → "Airplane sound"

from abc import ABC, abstractmethod

# ABSTRACT CLASS
class Vehicle(ABC):
    @abstractmethod
    def start(self):
        pass      # NO implementation here

    @abstractmethod
    def stop(self):
        pass      # NO implementation here

# CONCRETE CLASS - IMPLEMENTATION HAPPENS HERE
class Car(Vehicle):
    def start(self):
        print("Car started")   # IMPLEMENTATION

    def stop(self):
        print("Car stopped")   # IMPLEMENTATION

class Bike(Vehicle):
    def start(self):
        print("Bike started")  # IMPLEMENTATION

    def stop(self):
        print("Bike stopped")  # IMPLEMENTATION

# OBJECTS
c = Car()
b = Bike()

# CALL METHODS
c.start()   # Car started
c.stop()    # Car stopped
b.start()   # Bike started
b.stop()    # Bike stopped
