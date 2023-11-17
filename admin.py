"""Admin Inputs"""
def check_password():
    """Checks if password entered is correct"""
    admin_password = "password"
    pass_word = input(f"Enter password: ")

    if pass_word == admin_password:
        return True
    else:
        print("Incorrect Password!")

def file_writer(plates, cards):

    plate_writer = open("Plates.txt", "w")
    plates_joined = " ".join(plates)
    plate_writer.write(plates_joined)
    plate_writer.close()

    card_writer = open("Cards.txt", "w")
    cards_joined = " ".join(cards)
    card_writer.write(cards_joined)
    card_writer.close()
    
def verify_vehicle(plate):
    """Verfies wether a vehicles plate is in our system or not"""
    file_reader = open("Plates.txt")
    plates = file_reader.read().split()
    file_reader.close()
    if plate in plates:

        print(plate)

    else:

        print("None")

def display_vehicles(plates, cards):
    
    print(f"="*20)
    print(" "*7,"Plate",sep="")
    print("="*20)
    for Plate in plates:
        print(" "*(10-int(len(Plate)/2)),Plate,sep="")
    print("="*20)
    file_writer(plates,cards)


def display_charges(plates, cards):
    """ Displays and saves a list of registered plates"""
    charges_writer = open("Charges.txt", "w")

    print("="*60 + "\n" + " "*7 + "Plate" + " "*13 + "Credit Card" + " "*8 + "Charge in $" + "\n"*2 + "="*60 + "\n")

    charges_writer.write("="*60 + "\n" + " "*7 + "Plate" + " "*13 + "Credit Card" 
                         + " "*8 + "Charge in $" + "\n"*2 + "="*60 + "\n")

    for index in range(len(plates)):
        print(f"{plates[index]:^20}{cards[index]:^20}{4:^20}\n")
        charges_writer.write(f"{plates[index]:^20}{cards[index]:^20}{4:^20}\n")

    total_price = 4*len(plates)

    print("="*60 + "\n" + " "*7 + "Total" + f"{total_price:^75}")

    charges_writer.write("="*60 + "\n" + " "*7 + "Total" + f"{total_price:^75}")
    charges_writer.close()


def remove_vehicle(plate_number, plates_list, cards_list):
    """Removing a chosen vehicle"""
        
    "Searches for requested plate number"
    for index in range(len(plates_list)):
        if plates_list[index] == plate_number:
            captured = index
            exists = True
            break

        else:
            exists = False
    "If vehicle exists it will removed, if the vehicle does not exist program will return 'is not registered'"
    if exists == False:

        print(f"{plate_number} is not registered")

    else:
        
        print(f"{plate_number} is removed")

        plates_list.remove(plate_number)
        cards_list.remove(cards_list[captured])

    return(plates_list, cards_list)


def clear_vehicles():
    """Clears Vehicles from the lot in preparation for next set"""

    clear = open("Plates.txt","W")
    clear.close

