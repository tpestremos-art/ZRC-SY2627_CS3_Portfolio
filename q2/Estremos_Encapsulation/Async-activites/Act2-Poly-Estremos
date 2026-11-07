#1. Answer the following questions:
#a. What is duck typing, as explained in the video?

#Answer: According to the video, duck typing is another way to achieve polymorphism besides using Inheritance.
#The object must have the minimum necessary attributes or methods for it to be used.
#The name duck typing comes from the phrase "If it looks like a duck and quacks like a duck, it must be a duck." 
#This means that if an object behaves like the other classes (has the necessary methods and properties), it can be treated the same, even if it doesn't really inherit from it.

#b. What did the Car class need to have so it could work inside the same loop as Dog and Cat, even if it does not inherit from the Animal class?

#Answer: The Car class needed to have the same method (in this case, the 'speak' method) that the Dog and Cat classes have. 
#This way, when the loop calls the 'speak' method on each object, it can call it on Car as well, even though Car does not inherit from Animal. 
#As long as Car has a 'speak' method, it can be treated like an Animal in that context.


#2. Create the Python code:
class Car:
    def move(self):
        print("The car drives on the road.")

class Boat:
    def move(self):
        print("The boat sails on water.")

class Drone:
    def move(self):
        print("The drone flies in the sky.")

def start_trip(vehicle):
    vehicle.move()

car = Car()
boat = Boat()
drone = Drone()


vehicles = [car, boat, drone]

for vehicle in vehicles:
    start_trip(vehicle)    


#3. How does the code in 2.2 demonstrate polymorphism?

#Answer: The code in 2.2 demonstrates polymorphism through the use of duck typing.
#The 'start_trip' function takes the 'vehicle' parameter, which can be any object that has the method 'move'.
#In the loop, I created a list of different vehicle objects (car, boat, and drone) and called the 'start_trip' function on each of them.
#Even though these objects are of different classes, they all have the 'move' method, so they can be all treated the same way.
