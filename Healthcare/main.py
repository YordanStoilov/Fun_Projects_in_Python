from Class_HealthcareApp import *
from tkinter import messagebox


def open_window():
    window = Toplevel()
    # Creating Buttons on Second Menu:
    button_get_bmi = Button(window, text="Get BMI", padx=81, pady=20)
    button_blood_pressure_status = Button(window, text="Get Blood Pressure Status", padx=60, pady=20)
    button_max_heartrate = Button(window, text="Get Max Heart Rate", padx=45, pady=20)
    button_goal_pulse = Button(window, text="Get Goal Pulse", padx=60, pady=20)
    button_burned_calories = Button(window, text="Get Burned Calories", padx=79, pady=20)

    # Drawing Buttons on Second Menu:
    button_get_bmi.grid(row=0, column=0)
    button_blood_pressure_status.grid(row=0, column=1)
    button_goal_pulse.grid(row=1, column=0)
    button_burned_calories.grid(row=1, column=1)
    button_max_heartrate.grid(row=2, column=0)


root = Tk()
root.geometry("1280x720")
root.title("HealthcareApp")

# Creating Name Box:
name_label = Label(root, text="Enter your name")
name_bar = Entry(root, width=60, borderwidth=8)
name_label.grid(row=0, column=0)
name_bar.grid(row=1, column=0)

# Creating Age Box:
age_label = Label(root, text="Enter your age")
age_bar = Entry(root, width=60, borderwidth=8)
age_label.grid(row=2, column=0)
age_bar.grid(row=3, column=0)

# Creating Height Box:
height_label = Label(root, text="Enter your height")
height_bar = Entry(root, width=60, borderwidth=8)
height_label.grid(row=0, column=1)
height_bar.grid(row=1, column=1)

# Creating Weight Box:
weight_label = Label(root, text="Enter your weight")
weight_bar = Entry(root, width=60, borderwidth=8)
weight_label.grid(row=2, column=1)
weight_bar.grid(row=3, column=1)

root.mainloop()
