

# Single Inheritance
class Minerva:
    def __init__(self):
        self.name = "Minerva"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

    def func1(self):
        print("This function is in parent class.")


class Miro(Minerva):
    def func2(self):
        print("This function is in child class.")


obj = Miro()
obj.func1()
obj.func2()
print(obj.get_name())
obj.set_name("Miro")
print(obj.get_name())


# Multilevel Inheritance
class Rolando1:
    def __init__(self, grandfathername):
        self.grandfathername = grandfathername

    def get_grandfathername(self):
        return self.grandfathername

    def set_grandfathername(self, grandfathername):
        self.grandfathername = grandfathername


class Rolando2(Rolando1):
    def __init__(self, fathername, grandfathername):
        self.fathername = fathername
        Rolando1.__init__(self, grandfathername)

    def get_fathername(self):
        return self.fathername

    def set_fathername(self, fathername):
        self.fathername = fathername


class Rolando3(Rolando2):
    def __init__(self, sonname, fathername, grandfathername):
        self.sonname = sonname
        Rolando2.__init__(self, fathername, grandfathername)

    def get_sonname(self):
        return self.sonname

    def set_sonname(self, sonname):
        self.sonname = sonname

    def print_name(self):
        print("Grandfather name :", self.get_grandfathername())
        print("Father name :", self.get_fathername())
        print("Son name :", self.get_sonname())


s1 = Rolando3("Prince", "Rampal", "Lal mani")
print(s1.get_grandfathername())
s1.print_name()

s1.set_grandfathername("New Grandfather")
s1.set_fathername("New Father")
s1.set_sonname("New Son")
s1.print_name()


# Hierarchical Inheritance
class Patricia:
    def __init__(self):
        self.name = "Patricia"

    def get_name(self):
        return self.name

    def set_name(self, name):
        self.name = name

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

print(object1.get_name())
object1.set_name("Vin")
print(object1.get_name())

print(object2.get_name())
object2.set_name("Vim")
print(object2.get_name())
