class Animal:
    def __init__(self, name):
        self.__name = name

    def get_name(self):
        return self.__name

    def eat(self):
        print(f"{self.get_name()} eats food.")

    def make_sound(self):
        print(f"{self.get_name()} makes a sound.")

class Lion(Animal):
    def make_sound(self):
        print(f"{self.get_name()} roars loudly!")

    def eat(self):
        print(f"{self.get_name()} eats fresh meat.")

class Elephant(Animal):
    def make_sound(self):
        print(f"{self.get_name()} trumpets!")

    def eat(self):
        print(f"{self.get_name()} eats grass and fruits.")

class Monkey(Animal):
    def make_sound(self):
        print(f"{self.get_name()} chatters!")

    def eat(self):
        print(f"{self.get_name()} eats bananas.")

animals = [Lion("Simba"), Elephant("Dumbo"), Monkey("George")]

for animal in animals:
    animal.make_sound()
    animal.eat()
    print("-----")
