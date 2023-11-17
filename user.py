"""User Input"""
def print_menu():
        print(f"Select from the following options\n[1] Register a vehicle\n[2] Verify vehicle registration\n[3] Display registered vehicles and save them to a file\
\n[4] Display daily charges a save them to file\n[5] Remove a vehicle\n[6] Clear vehicles\n[0] Exit")
        
def register_Vehicle(plates):
    """Lets user register a vehicle if there are spaces open"""
    
    if len(plates) >= 50:

        print("Sorry")

    else:

        plate_Num = input(f"The parking lot has space for your vehicle \nEnter you plate number: ")
        
        if plate_Num in plates:

            print("This plate is already registered")

        else:

            card_Num = input(f"Enter your card number (4.00 charge): ")

            return plate_Num, card_Num
            