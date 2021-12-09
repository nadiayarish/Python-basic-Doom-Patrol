#1
from typing import Any


class Laptop:
    def __init__(self):
        battery_state1 = Battery("Charging")
        battery_state2 = Battery("Not charging")
        self.battery_states = (battery_state1, battery_state2)

class Battery:
    def __init__(self, status):
        self.status = status
keyboard = Laptop()
print(keyboard.battery_states[0].status)
#Charging

#2
class Guitar:
    def __init__(self, number_of_string):
        self.number_of_string = number_of_string

class GuitarString:

    def __init__(self, number_of_string, name_of_string):
        self.number_of_string = number_of_string
        self.name_of_string = name_of_string
    def string_info(self):
        print(f"The name of string {number_of_string} is {name_of_string}" )

string1 = GuitarString(1, "E")
string1.string_info()
