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

def display_vehicles():
    plate_obj = open("Plates.txt","r")
    plate_list = plate_obj.read().split()
    plate_obj.close()
    print("="*20)
    print(" "*7,"Plate",sep="")
    print("="*20)
    for Plate in plate_list:
        print(" "*(10-int(len(Plate)/2)),Plate,sep="")
    print("="*20)

def display_charges():
    """ Displays and saves a list of registered plates"""
    plate_obj = open("Plates.txt","r")
    plate_list = plate_obj.read().split()
    plate_obj.close()
    cards_obj = open("Cards.txt","r")
    cards_list = cards_obj.read().split()
    cards_obj.close()
    print("="*60)
    print(" "*7,"Plate"," "*12,"Credit Card", " "*9,"Charge in $",sep="")
    print("\n","="*60)
    for n in range(len(plate_list)):
        plate_len = int(10-(len(plate_list[n])/2))
        card_len = int(10-(len(cards_list[n])/2))
        print(
            " "*plate_len,plate_list[n]," "*(20-plate_len-len(plate_list[n])),
            " "*card_len,cards_list[n]," "*(20-card_len-len(cards_list[n])),
            " "*9,"4",
            sep=""
        )
    print("="*60)
    total_price = str(4*len(plate_list))
    print(" "*7,"Total"," "*28," "*(10-int(len(total_price)/2)),total_price, sep="")

def remove_vehicle(plate_number):
    """Removing a chosen vehicle"""
    plates_file = open("Plates.txt", "r")
    cards_file = open("Cards.txt", "r")

    plates_list = plates_file.read().split()
    cards_list = cards_file.read().split()

    plates_file.close()
    cards_file.close() 

    plates_write = open("Plates.txt", "w")
    cards_write = open("Cards.txt", "w")

    for index in range(len(plates_list)):
        if plates_list[index] == plate_number:
            captures = index
            exists = True
            break

        else:
            exists = False
    if exists == False:

        print(f"{plate_number} is not registered")

    else:
        
        print(f"{plate_number} is removed")

        plates_list.remove(plate_number)
        cards_list.remove(cards_list[captures])

        plates_joined = " ".join(plates_list)
        cards_joined = " ".join(cards_list)

        plates_write.write(plates_joined)
        cards_write.write(cards_joined)

        plates_write.close()
        cards_write.close()


def clear_vehicles():
    """Clears Vehicles from the lot in preparation for next set"""
    clear = open("Plates.txt","W")
    clear.close

