class parent1:
    def show(self):
        print("i am parent1")

class son(parent1):
    pass

class daughter(parent1):
    pass

class grandson(son, daughter):
    def display(self):
        print("I am the grandson")

obj = grandson()
obj.show()
obj.display()