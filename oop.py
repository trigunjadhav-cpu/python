# class Student:
#     def __init__(self,a,l):
#         self.age = a
#         self.location = l
#     def study(self):
#         print("Python OOP")
#     def playing(self):
#         print("UNO,chess")


# class student:
#     def info(self,s,m):
#         self.marks = m
#         self.subject = s

#     def loc(self,c,p):
#         self.city = c
#         self.pincode = p     

# s1 = student(78,"python","Pune",423113)
# s1.info()
# s1.loc()

# class students:
#     def __init__(self,n,a,s):
#         self.name = n
#         self.Age = a
#         self.Subject = s
# s = students("raj",23,["Python , c++"])
# print(s.name)
# print(s.Subject)
# print(s.Age)
class Student:
    def __init__(self, roll, name, marks, address):
        self.roll = roll
        self.name = name
        self.marks = marks
        self.address = address
s1 = Student(101, "Jay", 85, "Pune")
print(s1.roll)
print(s1.name)
print(s1.marks)
print(s1.address)


class Teacher:
    def __init__(self, name, salary, dep, address):
        self.name = name
        self.salary = salary
        self.dep = dep
        self.address = address

t1 = Teacher("Amit", 50000, "Computer", "Pune")
print(t1.name)
print(t1.salary)
print(t1.dep)
print(t1.address)