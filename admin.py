"""Admin Inputs"""

def verify_vehicle(plate):
    """Verfies wether a vehicles plate is in our system or not"""
    file_reader = open("Plates.txt")
    plates = file_reader.read().split()
    file_reader.close()
    if plate in plates:

        print(plate)

    else:

        print("None")

def display_vehicle():
    pass

def display_charges():
    pass

def remove_vehicle():
    pass

def clear_vehicle():
    pass
