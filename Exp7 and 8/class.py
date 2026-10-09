# class Student:
#     def display(self):
#         print("Hello World")

# s1 = Student()
# s1.display()

# class Student:
#     def show(self):
#         name = input("Enter your name: ")
#         roll = int(input("Enter Roll No: "))
#         div = input("Enter Div: ")
#         print(name, roll, div)

# s = Student()
# s.show()


# class Student:
#     def __init__(self, name, roll, div):
#         self.name = name
#         self.roll = roll
#         self.div = div
#     def display(self):
#         print("Name:", self.name)
#         print("Roll No:", self.roll)
#         print("Division:", self.div)
# name = input("Enter name: ")
# roll = int(input("Enter roll number: "))
# div = input("Enter division: ")
# s1 = Student(name, roll, div)
# s1.display()

# class Student:
#     def __init__(self, name, age):
#         self.name = name
#         self.age = age

#     def show(self):
#         print(self.name, self.age)

# s1 = Student("Rahul", 20)
# s2 = Student("Priya", 21)
# s3 = Student("Amit", 19)

# s1.show()
# s2.show()
# s3.show()


class Student:
    def __init__(self, name, roll, div):
        self.name = name
        self.roll = roll
        self.div = div

    def display(self):
        print("Name:", self.name)
        print("Roll No:", self.roll)
        print("Division:", self.div)

    def __del__(self):
        print("Destructor")
name = input("Enter name: ")
roll = int(input("Enter roll number: "))
div = input("Enter division: ")

s1 = Student(name, roll, div)
s1.display()
del s1