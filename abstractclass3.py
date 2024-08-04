from abc import ABC, abstractmethod

class Parent(ABC):
    @abstractmethod
    def abstract_method(self):
        pass

class Child(Parent):
    def abstract_method(self):
        print("Implementation in Child")

    def create_and_call(self):
        child_instance = Child()
        child_instance.abstract_method()

child = Child()
child.create_and_call()