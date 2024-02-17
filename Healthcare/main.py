import tkinter

from Class_HealthcareApp import *
from clients import add_client

current_user_info = {"Name": "", "Age": 0, "Weight": 0, "Height": 0, "Blood Pressure": []}

activity_window = None


def get_personal_data():
    store_name_info()
    store_age_info()
    store_height_info()
    store_weight_info()
    store_blood_pressure()


def open_activity_window():
    global activity_window
    activity_window = tkinter.Toplevel(root)
    activity_window.title("Activity Selector")

    # Creating Activity box
    activity_label = Label(activity_window, text="Enter activity")
    activity_bar = Entry(activity_window, width=60, borderwidth=8)
    activity_label.grid(row=0, column=0)
    activity_bar.grid(row=1, column=0)

    #     Creating Time box

    time_label = Label(activity_window, text="Enter time spent doing activity")
    time_bar = Entry(activity_window, width=60, borderwidth=8)
    time_label.grid(row=2, column=0)
    time_bar.grid(row=3, column=0)

    button_ready_activity = Button(activity_window, text="Activity", command=get_activity_result)
    button_ready_activity.config(width=15, height=2)
    button_ready_activity.grid(row=12, column=0)

    return activity_bar, time_bar


def get_activity_result():
    result = get_activity_info()
    data_window = tkinter.Toplevel(root)
    data_window.title("Your calorie information")
    data_label = Label(root, text=result, font=("Helvetica", 24))
    data_label.grid()


def get_activity_data():
    activity, time = [x.get() for x in open_activity_window()]
    return activity, time


def get_activity_info():
    activity_info = HealthcareApp(current_user_info["Name"], current_user_info["Age"], current_user_info["Weight"],
                                  current_user_info["Height"], tuple(current_user_info["Blood Pressure"]))

    result = activity_info.get_burned_calories(get_activity_data()[0], get_activity_data()[1])
    return result


def get_user_vitals():
    user_vitals = HealthcareApp(current_user_info["Name"], current_user_info["Age"], current_user_info["Weight"],
                                current_user_info["Height"], tuple(current_user_info["Blood Pressure"]))
    user_text = f"{user_vitals.get_bmi()}\n{user_vitals.get_blood_pressure_status()}\n" \
                f"{user_vitals.get_max_heartrate()}\n{user_vitals.get_goal_pulse()}"
    return user_text


def open_info_window():
    user_text = get_user_vitals()
    data_window = tkinter.Toplevel(root)
    data_window.title("Your health information")

    data_label = Label(data_window, text=user_text, font=("Helvetica", 24))
    data_label.pack()


def store_name_info():
    username = name_bar.get()
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
    blood_pressure_split = [int(x) for x in user_blood_pressure.split(" ")]
    current_user_info["Blood Pressure"].append(blood_pressure_split[0])
    current_user_info["Blood Pressure"].append(blood_pressure_split[1])


def get_ready():
    get_personal_data()

    for key, value in current_user_info.items():
        if not value or value == 0:
            raise ValueError("Fill all the information bars!")
    add_client(current_user_info)
    open_info_window()


root = Tk()
root.geometry("565x450")
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
height_label.grid(row=4, column=0)
height_bar.grid(row=5, column=0)

# Creating Weight Box:
weight_label = Label(root, text="Enter your weight")
weight_bar = Entry(root, width=60, borderwidth=8)
weight_label.grid(row=6, column=0)
weight_bar.grid(row=7, column=0)

# Creating Blood Pressure Box
bp_label = Label(root, text="Enter your blood pressure separated by space")
bp_bar = Entry(root, width=60, borderwidth=8)
bp_label.grid(row=8, column=0)
bp_bar.grid(row=9, column=0)

# Button Ready:
button_ready = Button(root, text="Ready", command=get_ready)
button_ready.config(width=15, height=2)
button_ready.grid(row=10, column=0)

# Button Activities
button_activity = Button(root, text="Activities", command=open_activity_window)
button_activity.config(width=15, height=2)
button_activity.grid(row=12, column=0)

root.mainloop()
