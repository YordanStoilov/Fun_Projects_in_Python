from Class_HealthcareApp import *
from tkinter import filedialog


def open_bmi_window():
    bmi_window = Toplevel()
    bmi_window.title("BMI Calculator")

    messagebox_height = Label(bmi_window, text="Enter your height")
    messagebox_weight = Label(bmi_window, text="Enter your weight")
    height_bar = Entry(bmi_window, width=35, borderwidth=5)
    weight_bar = Entry(bmi_window, width=35, borderwidth=5)

    messagebox_height.grid()
    messagebox_weight.grid()
    height_bar.grid()
    weight_bar.grid()



root = Tk()

# Creating Buttons on First Menu:

button_get_bmi = Button(root, text="Get BMI", padx=81, pady=20, command=open_bmi_window)
button_blood_pressure_status = Button(root, text="Get Blood Pressure Status", padx=60, pady=20)
button_max_heartrate = Button(root, text="Get Max Heart Rate", padx=45, pady=20)
button_goal_pulse = Button(root, text="Get Goal Pulse", padx=60, pady=20)
button_burned_calories = Button(root, text="Get Burned Calories", padx=79, pady=20)

# Drawing Buttons:

button_get_bmi.grid(row=0, column=0)
button_blood_pressure_status.grid(row=0, column=1)

button_goal_pulse.grid(row=1, column=0)
button_burned_calories.grid(row=1, column=1)

button_max_heartrate.grid(row=2, column=0)

root.mainloop()
