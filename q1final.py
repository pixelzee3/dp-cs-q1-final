# Potential IOT device: Smart bike
# Device description: In terms of hardware, the smart bike is able to electronically adjust the seat and handlebar heights. The bike is also has a display to display the user's name and reminders for checking the tire pressures. Besides that, the smart bike is able to analyze the user's cycling performance using a collection of data.
# Device personality: Informative

from enum import Enum


class Experience(Enum):
    BEGINNER = 1
    INTERMEDIATE = 2
    EXPERIENCED = 3


class CycleFrequency(Enum):
    WEEKEND = 1
    WEEKDAY = 2
    EVERYDAY = 3


class Energy(Enum):
    EXHAUSTED = 1
    TIRED = 2
    NORMAL = 3
    ENERGETIC = 4


class SmartBike:
    def __init__(self):
        # Base information
        self.user_name: str = None
        self.user_weight: float = None
        self.user_height: float = None
        self.user_experience: Experience = None
        self.user_cycle_frequency: CycleFrequency = None

        # Trip information
        self.trip_starting_point: str = None
        self.trip_destination: str = None
        self.trip_half_energy: Energy = None
        self.trip_average_speed: float = None
        self.trip_end_energy: Energy = None

        # Idea for the two additional user datas: odometer & something else

    def set_device_up(self):
        # TODO: do type checking here
        print("\nCongratulations on your new smart bike!\nPlease fill out the following information below to configure your bike: \n")

        self.user_name = input("Name: ")

        self.user_weight = input("Weight (kg): ")

        self.user_height = input("Height (cm): ")

        print("""
        1 -> Beginner (< 10 km trips, < 10 km/h avg. speed)
        2 -> Intermediate (< 30 km trips, < 20 km/h avg. speed)
        3 - > Experienced (30+ km/h trips, 30+ km/h avg. speed)
        """)
        self.user_experience = int(input("Experience: "))

        print("""
        1 -> Weekends
        2 -> Weekdays
        3 - > Everyday
        """)
        self.user_cycle_frequency = input("Cycling days: ")


# Run the program (only when explicitly called)
if __name__ == "__main__":
    bike = SmartBike()
    bike.set_device_up()
