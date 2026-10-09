class Parent1():
    def show(self):
        print("Hello i am parent1")

class child1(Parent1):
    def show1(self):
        print("I am parent2")

class child2(Parent1):
    def display(self):
        print("I am the child")

c1 = child1()
c2 = child2()
c1.show()
c1.show1()
c2.show()
c2.display()
