#Single Inheritance
class Minerva:
    def func1(self):
        print("This function is in parent class.")

class Miro(Minerva):
    def func2(self):
        print("This function is in child class.")

obj = Miro()
obj.func1()
obj.func2()



#Multilevel Inheritance
class Rolando1:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

class Rolando2(Rolando1):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Rolando1.__init__(self, grandfathername)

class Rolando3(Rolando2):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Rolando2.__init__(self, fathername, grandfathername)

    def print_name(self):
        print('Grandfather name :', self.grandfathername)
        print('Father name :', self.fathername)
        print('Son name :', self.sonname)

s1 = Rolando3('Prince', 'Rampal', 'Lal mani')
print(s1.grandfathername)
s1.print_name()



#Hierarchical Inheritance
class Patricia:
    def func1(self):
        print("This function is in parent class.")

class Vin(Patricia):
    def func2(self):
        print("This function is in child 1.")

class Vim(Patricia):
    def func3(self):
        print("This function is in child 2.")

object1 = Vin()
object2 = Vim()
object1.func1()
object1.func2()
object2.func1()
object2.func3()