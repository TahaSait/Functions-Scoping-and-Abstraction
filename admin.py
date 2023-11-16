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

def remove_vehicle():
    pass

def clear_vehicles():
    pass
