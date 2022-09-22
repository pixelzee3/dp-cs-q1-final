# Potential IOT device: Smart bike
# Device description: In terms of hardware, the smart bike is able to electronically adjust the seat and handlebar heights. The bike is also has a display to display information and reminders and an electronic gear shifter. Besides that, the smart bike is able to analyze the user's cycling performance using a collection of data.
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
        self.user_age: int = None
        self.user_height: float = None
        self.user_experience: Experience = None
        self.user_cycle_frequency: CycleFrequency = None

        # Trip information
        self.trip_starting_point: str = None
        self.trip_destination: str = None
        self.trip_average_speed: float = None
        self.trip_end_energy: Energy = None

        # ? Ideas for the two additional user data: odometer & something else

    def set_device_up(self):
        print("\nCongratulations on your new smart bike!\nPlease fill out the following information below to configure your bike: \n")

        # This input variable collects the user's name.
        # This information is relevant to the smart bike because it can use the name to create an online profile for the user. This profile may contain relevant information such as the user's experience or past cycles and can be used to connect with other users.
        # Aside from that, the name can also be displayed on the screen in case the bike is lost.
        self.user_name = input("Name: ")

        # This input variable collects the user's age.
        # This information is relevant to the company creating the smart bikes because they can figure out the product's audience and potentially support them better (e.g., if the mean age of the users were older, the company could push a software update that improves the experience for older people)
        while True:
            try:
                self.user_age = int(input("Age (years): "))
            except ValueError:
                print("\nPlease use integer format\ne.g., 4 or 69\n")
                continue
            if self.user_age <= 0:
                print("\nPlease enter a valid age\n")
                continue
            break

        # This input variable collects the user's weight.
        # This information is relevant to the smart bike because it can be used to intelligently adjust the seating and handlebar heights in accordance to how far the user's legs and arms can reach.
        while True:
            try:
                self.user_height = float(input("Height (cm): "))
            except ValueError:
                print("\nPlease use decimal format\ne.g., 69 or 42.0\n")
                continue
            break

        # This input variable collects the user's weight.
        # This information is relevant to the smart bike because it can be used to intelligently adjust the seating and handlebar heights to their optimal position (body fat can add additional cushioning around the butt which affects the body position).
        while True:
            try:
                self.user_weight = float(input("Weight (kg): "))
            except ValueError:
                print("\nPlease use decimal format\ne.g., 69 or 42.0\n")
                continue
            break

        # This input variable collects the user's experience in cycling.
        # This information is relevant to the smart bike because it can be used to adjust the complicatedness of the gear shifter to avoid confusion for less experienced users.
        # For example, the gear shifter can be set to automatically change if the user is still a beginner.
        # Then, if the user is an intermediate, the rear gears (cassette) can be manually adjusted.
        # Subsequently, if the user is experienced, both the rear and front gears (cassette and chainrings) can be manually adjusted.
        while True:
            print("""
        1 -> Beginner
        2 -> Intermediate
        3 -> Experienced
        """)
            try:
                self.user_experience = Experience(int(input("Experience: ")))
            except ValueError:
                print(
                    "\nPlease input the number that corresponds to the choice you'd like to select")
                continue
            break

        # This input variable collects the days where the user likes to cycle.
        # This information is relevant to the smart bike because it can be used to remind the user to check their tire pressures the day before they cycle
        while True:
            print("""
        1 -> Weekends
        2 -> Weekdays
        3 -> Everyday
        """)
            try:
                self.user_cycle_frequency = CycleFrequency(
                    int(input("Cycling days: ")))
            except ValueError:
                print(
                    "\nPlease input the number that corresponds to the choice you'd like to select")
                continue
            break


# Run the program (only when explicitly called)
if __name__ == "__main__":
    bike = SmartBike()
    bike.set_device_up()
