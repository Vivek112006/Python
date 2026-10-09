class Parent1():
    def show(self):
        print("Hello i am parent1")

class Parent2(Parent1):
    def show1(self):
        print("I am parent2")

class child(Parent2):
    def display(self):
        print("I am the child")

c = child()
c.show()
c.show1()
c.display()
