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

class Energy(Enum):
    EXHAUSTED = 1
    TIRED = 2
    NORMAL = 3
    ENERGETIC = 4


class Bike:
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

    def setup_device(self):
        pass
