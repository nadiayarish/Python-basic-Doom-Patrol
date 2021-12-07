# 1. Create a Vehicle class with max_speed and mileage instance attributes
class Vehicle:

    def __init__(self, max_speed, mileage):
        self.max_speed = max_speed
        self.mileage = mileage

    def print_info(self):
        print(f"Max speed of my vehicle is {self.max_speed}, mileage of my vehicle is {self.mileage}")


my_vehicle = Vehicle(100, 1500)
my_vehicle.print_info()


# Max speed of my vehicle is 100, mileage of my vehicle is 1500

# 2. Create a child class Bus that will inherit all the variables and methods of the Vehicle class and will have seating_capacity own method
class Bus(Vehicle):
    def __init__(self, max_speed, mileage, seating_capacity):
        super().__init__(max_speed, mileage)
        self.seating_capacity = seating_capacity

    def seating_info(self):
        print(f"Seating capacity of my bus is {self.seating_capacity}")

# 3. Determine which class a given Bus object belongs to (Check type of an object)
my_bus = Bus(100, 1200, 30)
print(type(my_bus))
# <class '__main__.Bus'>

# 4. Create an instance of Bus named school_bus and determine if school_bus is also an instance of the Vehicle class
school_bus = Bus(60, 1002, 35)
school_bus.print_info()
# Max speed of my vehicle is 60, mileage of my vehicle is 1002
school_bus.seating_info()
# Seating capacity of my bus is 35
print(isinstance(school_bus, Vehicle))
#True

# 5. Create a new class School with get_school_id and number_of_students instance attributes

class School:


    def __init__(self, get_school_id, number_of_students):
        self.get_school_id = get_school_id
        self.number_of_students = number_of_students

# 6*. Create a new class SchoolBus that will inherit all the methods from School and Bus and will have its own - bus_school_color

class SchoolBus(School, Bus):
    def __init__(self, get_school_id, number_of_students, max_speed, mileage, seating_capacity, bus_school_color):
        School.__init__(self, get_school_id, number_of_students)
        Bus.__init__(self, max_speed, mileage, seating_capacity)
        self.bus_school_color = bus_school_color

# 7. Polymorphism: Create two classes: Bear, Wolf. Both of them should have make_sound method. Create two instances, one of Bear and one of Wolf,
# make a tuple of it and by using for call their action using the same method.

class Bear:

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

class Wolf:

    def __init__(self, sound):
        self.sound = sound

    def make_sound(self):
        print(self.sound)

Bear_ex = Bear ("Grrr")
Wolf_ex = Wolf ("Wooo")
tuple = (Bear_ex, Wolf_ex)
for sound in tuple:
    print(make_sound())
