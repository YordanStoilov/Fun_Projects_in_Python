from tkinter import *


class HealthcareApp:
    activities_mets = {
        "walking": 4.5,
        "swimming": 7,
        "jogging": 7,
        "stretching": 4,
        "running": 9,
        "yoga": 3,
        "weightlifting": 8
    }

    def __init__(self, name: str, age: int, weight: float, height: int, blood_pressure: tuple):
        self.name = name
        self.age = age
        self.weight = weight
        self.height = height
        self.blood_pressure = blood_pressure
        self.max_heartrate = 0

    def get_bmi(self):
        height_in_m = self.height / 100
        bmi_value = self.weight / (height_in_m ** 2)
        return f"Patient BMI: {round(bmi_value, 2)}"

    def get_blood_pressure_status(self):
        status = ""
        if self.blood_pressure[0] < 110 and self.blood_pressure[1] < 70:
            status = "Low Blood Pressure"
        elif self.blood_pressure[0] < 120 and self.blood_pressure[1] <= 80:
            status = "Normal Blood Pressure"
        elif 120 <= self.blood_pressure[0] < 130 and self.blood_pressure[1] <= 90:
            status = "Elevated Blood Pressure"
        elif 130 <= self.blood_pressure[0] < 140 and self.blood_pressure[1] <= 90:
            status = "Pre-Hypertension"
        elif 140 <= self.blood_pressure[0] < 160 and self.blood_pressure[1] >= 90:
            status = "Stage 1 Hypertension"
        elif self.blood_pressure[0] >= 160 and self.blood_pressure[1] > 100:
            status = "Stage 2 Hypertension"

        return f"Patient Blood Pressure Status: {status}"

    def get_max_heartrate(self):
        self.max_heartrate = 220 - self.age
        return f"Patient Max Heat Rate: {self.max_heartrate}"

    def get_goal_pulse(self):
        low_threshold = 0.5 * self.max_heartrate
        high_threshold = 0.85 * self.max_heartrate
        return f"Patient Target Heat Rate: {round(low_threshold)} to {round(high_threshold)} BPM"

    def get_burned_calories(self, activity: str, minutes: int):
        try:
            calories_per_minute = self.activities_mets[activity] * (self.weight / 2.2) / 200
            total_calories = round(calories_per_minute * minutes, 2)
            return f"Patient Burned Calories while {activity} for {minutes} minutes: {total_calories}"
            # return total_calories
        except KeyError:
            return "Invalid activity!"


# patient_1 = HealthcareApp("Yordan", 27, 78, 186, (120, 85))
#
# print(patient_1.get_bmi())
# print(patient_1.get_blood_pressure_status())
# print(patient_1.get_max_heartrate())
# print(patient_1.get_goal_pulse())
# print(patient_1.get_burned_calories("weightlifting", 50))
