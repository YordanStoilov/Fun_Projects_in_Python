clients = []


def add_client(name: str, age: int, weight: float, height: int, blood_pressure: tuple):
    error_message = "Please enter valid "
    if not name or not name.isalpha():
        return f"{error_message}{name}"
    if not isinstance(age, int):
        return f"{error_message}{age}"
    if not isinstance(weight, (float, int)):
        return f"{error_message}{weight}"
    if not isinstance(height, int):
        return f"{error_message}{height}"
    for item in blood_pressure:
        if not isinstance(item, int):
            return f"{error_message}{blood_pressure}"

    current_profile = {name: {"Age": age, "Weight": weight}, "Height": height, "Blood Pressure": blood_pressure}
    clients.append(current_profile)
