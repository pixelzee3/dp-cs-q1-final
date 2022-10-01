# Potential IOT device: Smart bike
# Device description: In terms of hardware, the smart bike is able to electronically adjust the seat and handlebar heights. The bike is also has a display to display information and reminders and an electronic gear shifter. Besides that, the smart bike is able to analyze the user's cycling performance using a collection of data.
# Device personality: Informative

from enum import Enum
import asyncio


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


class Utils:
    @staticmethod
    def insert_new_line(amount=1):
        for _ in range(amount):
            print()

    @staticmethod
    async def progress_dots(amount=3, interval=1):
        for _ in range(amount):
            await asyncio.sleep(interval)
            print('.')


class SmartBike:
    def __init__(self):
        # Base user information (with default values)
        self.user_name: str = ''
        self.user_weight: float = 0.0
        self.user_age: int = 0
        self.user_height: float = 0
        self.user_experience: Experience = Experience.BEGINNER
        self.user_cycle_frequency: CycleFrequency = CycleFrequency.EVERYDAY

        # Trip information (with default values)
        self.trip_starting_point: str = ''
        self.trip_destination: str = ''
        self.trip_average_speed: float = 0
        self.trip_end_energy: Energy = Energy.NORMAL

        # Personal note from me: Accumulating the data into a list is redundant. I'm just doing this for the sake of meeting the success criteria.
        self.accumulated_data = []

    def set_device_up(self):
        print("Congratulations on your new smart bike!\nPlease fill out the following information below to configure your bike: ")

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
                print("Please use integer formate.g., 4 or 69")
                continue
            if self.user_age <= 0:
                print("Please enter a valid age")
                continue
            break

        # This input variable collects the user's weight.
        # This information is relevant to the smart bike because it can be used to intelligently adjust the seating and handlebar heights in accordance to how far the user's legs and arms can reach.
        while True:
            try:
                self.user_height = float(input("Height (cm): "))
            except ValueError:
                print("Please use decimal formate.g., 69 or 42.0")
                continue
            break

        # This input variable collects the user's weight.
        # This information is relevant to the smart bike because it can be used to intelligently adjust the seating and handlebar heights to their optimal position (body fat can add additional cushioning around the butt which affects the body position).
        while True:
            try:
                self.user_weight = float(input("Weight (kg): "))
            except ValueError:
                print("Please use decimal formate.g., 69 or 42.0")
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
                    "Please input the number that corresponds to the choice you'd like to select")
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
                    "Please input the number that corresponds to the choice you'd like to select")
                continue
            break

        print(f"""
Great! Here's a review of your data:

    User name: {self.user_name}
    User weight: {self.user_weight} kg
    User height: {self.user_height} cm
    User age: {self.user_age} years
    User experience: {'Beginner' if self.user_experience == Experience.BEGINNER else 'Intermediate' if self.user_experience == Experience.INTERMEDIATE else 'Experienced'}
    User cycle frequency: {'Weekends' if self.user_cycle_frequency == CycleFrequency.WEEKEND else 'Weekdays' if self.user_cycle_frequency == CycleFrequency.WEEKDAY else 'Everyday'}
        """)

    async def trip(self):
        print("Let's begin a trip!")

        self.trip_starting_point = input(
            "Where are you starting from?: ").strip()
        self.trip_destination = input("Where would you like to go?: ").strip()

        print(
            f"Great! Let's begin a trip from {self.trip_starting_point} to {self.trip_destination}.")
        await Utils.progress_dots()

        print(f"You have arrived at {self.trip_destination}!")

        while True:
            print("""
        1 -> Exhausted
        2 -> Tired
        3 -> Normal
        4 -> Energetic
        """)
            try:
                self.trip_end_energy = Energy(
                    int(input("How are your energy levels?: ")))
            except ValueError:
                print(
                    "Please input the number that corresponds to the choice you'd like to select")
                continue
            break

        while True:
            try:
                self.trip_average_speed = float(
                    input("What was your average speed in km/h?: "))
            except ValueError:
                print("Please use decimal formate.g., 69 or 42.0")
                continue
            break

        print(f"""
Great! Here's a review of your data with your last trip information:

    User name: {self.user_name}
    User weight: {self.user_weight} kg
    User height: {self.user_height} cm
    User age: {self.user_age} years
    User experience: {'Beginner' if self.user_experience == Experience.BEGINNER else 'Intermediate' if self.user_experience == Experience.INTERMEDIATE else 'Experienced'}
    User cycle frequency: {'Weekends' if self.user_cycle_frequency == CycleFrequency.WEEKEND else 'Weekdays' if self.user_cycle_frequency == CycleFrequency.WEEKDAY else 'Everyday'}
    Last trip information:    
        Starting point: {self.trip_starting_point}
        Ending point: {self.trip_destination}
        Average speed: {self.trip_average_speed} km/h
        User energy level after trip: {'Exhausted' if self.trip_end_energy == Energy.EXHAUSTED else 'Tired' if self.trip_end_energy == Energy.TIRED else 'Normal' if self.trip_end_energy == Energy.NORMAL else 'Energetic'}
        """)

        self.accumulated_data = [
            self.user_name,
            self.user_weight,
            self.user_age,
            self.user_height,
            self.user_experience,
            self.user_cycle_frequency,
            self.trip_starting_point,
            self.trip_destination,
            self.trip_average_speed,
            self.trip_end_energy
        ]

        while True:
            try:
                self.accumulated_data.append(float(
                    input("How far was your trip in km? This will be added to your odometer: ")))
            except ValueError:
                print("Please use decimal formate.g., 69 or 42.0")
                continue
            break

        while True:

            print("""
        1 -> Yes
        2 -> No
        """)

            answer = 1
            try:
                answer = int(
                    input("Would you like to delete your last trip information?: "))
                if answer < 1 or answer > 2:
                    raise ValueError
            except ValueError:
                print(
                    "Please input the number that corresponds to the choice you'd like to select")
                continue
            if answer == 1:
                self.accumulated_data.remove(self.trip_average_speed)
                self.accumulated_data.remove(self.trip_destination)
                self.accumulated_data.remove(self.trip_starting_point)
                self.accumulated_data.remove(self.trip_end_energy)
            break


# Run the program (only when explicitly called)
if __name__ == "__main__":
    Utils.insert_new_line(2)
    bike = SmartBike()
    bike.set_device_up()
    asyncio.run(bike.trip())
    print(bike.accumulated_data)
