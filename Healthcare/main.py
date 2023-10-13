import tkinter

from Class_HealthcareApp import *
from clients import add_client

current_user_info = {"Name": "", "Age": 0, "Weight": 0, "Height": 0, "Blood Pressure": []}
data_entered = 0


def get_user_vitals():
    user_vitals = HealthcareApp(current_user_info["Name"], current_user_info["Age"], current_user_info["Weight"],
                                current_user_info["Height"], tuple(current_user_info["Blood Pressure"]))
    user_text = f"{user_vitals.get_bmi()}\n{user_vitals.get_blood_pressure_status()}\n{user_vitals.get_max_heartrate()}" \
                f"{user_vitals.get_max_heartrate()}\n{user_vitals.get_goal_pulse()}"
    return user_text


def open_new_window():
    user_text = get_user_vitals()
    data_window = tkinter.Toplevel(root)
    data_window.title("Your health information")

    data_label = Label(data_window, text=user_text)
    data_label.pack()


def store_name_info():
    current_user_info["Name"] = username


def store_age_info():
    user_age = age_bar.get()
    current_user_info["Age"] += int(user_age)


def store_height_info():
    user_height = height_bar.get()
    current_user_info["Height"] += int(user_height)


def store_weight_info():
    user_weight = weight_bar.get()
    current_user_info["Weight"] += int(user_weight)


def store_blood_pressure():
    user_blood_pressure = bp_bar.get()
    current_user_info["Blood Pressure"].append([int(x) for x in user_blood_pressure.split(" ")])


def get_ready():
    for key, value in current_user_info.items():
        if not value or value == 0:
            raise ValueError("Fill all the information bars!")
    add_client(current_user_info)
    open_new_window()


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
root.geometry("650x650")
root.title("HealthcareApp")

# Creating
#
# Name Box:
name_label = Label(root, text="Enter your name")
name_bar = Entry(root, width=60, borderwidth=8)
username = name_bar.get()
name_label.grid(row=0, column=0)
name_bar.grid(row=1, column=0)

# Name Button:
button_name = Button(root, text="Store", command=store_name_info)
button_name.grid(row=1, column=9)

# Creating
#
# Age Box:
age_label = Label(root, text="Enter your age")
age_bar = Entry(root, width=60, borderwidth=8)
age_label.grid(row=2, column=0)
age_bar.grid(row=3, column=0)

# Age Button:
button_age = Button(root, text="Store", command=store_age_info)
button_age.grid(row=3, column=9)

# Creating
#
# Height Box:
height_label = Label(root, text="Enter your height")
height_bar = Entry(root, width=60, borderwidth=8)
height_label.grid(row=4, column=0)
height_bar.grid(row=5, column=0)

# Height Button:

button_height = Button(root, text="Store", command=store_age_info)
button_height.grid(row=5, column=9)

# Creating
#
# Weight Box:
weight_label = Label(root, text="Enter your weight")
weight_bar = Entry(root, width=60, borderwidth=8)
weight_label.grid(row=6, column=0)
weight_bar.grid(row=7, column=0)

# Weight Button:
button_height = Button(root, text="Store", command=store_age_info)
button_height.grid(row=7, column=9)

# Creating
# Blood Pressure Box
bp_label = Label(root, text="Enter your blood pressure separated by space")
bp_bar = Entry(root, width=60, borderwidth=8)
bp_label.grid(row=8, column=0)
bp_bar.grid(row=9, column=0)
# Blood Pressure Button:

button_height = Button(root, text="Store", command=store_age_info)
button_height.grid(row=9, column=9)

# Button Ready:
button_ready = Button(root, text="Ready", command=get_ready)
button_ready.grid(row=10, column=5)

root.mainloop()
