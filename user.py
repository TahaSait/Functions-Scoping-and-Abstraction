    
def register_Vehicle():
    plate_reader = open("Plates.txt")
    card_reader = open("Cards.txt")

    plates = plate_reader.read().split()
    cards = card_reader.read().split()

    plate_reader.close()
    card_reader.close()

    if len(plates) >= 50:

        print("Sorry")

    else:

        plate_Num = input(f"The parking lot has space for your vehicle \nEnter you plate number: ")
        
        if plate_Num in plates:

            print("This plate is already registered")

        else:

            plates.append(plate_Num)
            plate_writer = open("Plates.txt", "w")
            plates_joined = " ".join(plates)
            plate_writer.write(plates_joined)
            plate_writer.close()

            card_Num = input(f"Enter your card number (4.00 charge): ")
            cards.append(card_Num)
            card_writer = open("Cards.txt", "w")
            cards_joined = " ".join(cards)
            card_writer.write(cards_joined)
            card_writer.close()