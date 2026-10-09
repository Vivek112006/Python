class Parent:
    def show(self):
        print("Hi i am the parent")

class Child(Parent):
    def display(self):
        print("I am the child")

c = Child()
c.show()
c.display()