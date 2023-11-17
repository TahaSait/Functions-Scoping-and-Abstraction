import user
import admin

plate_reader = open("Plates.txt")
card_reader = open("Cards.txt")

plates = plate_reader.read().split()
cards = card_reader.read().split()

plate_reader.close()
card_reader.close()

print(f"****************************************************************************\n*** Welcome to Park and Go Parking Application!\
***\nPark from 6PM to Midnight for a flat fee of 4.00\n****************************************************************************")
while True:

    user.print_menu()
    
    choice = input(">>> ")

    if choice not in ["0","1","2","3","4","5","6"]:
        print("Invalid Input")

    elif choice == "0":
         break
    
    elif choice == "1":
        plate_num, card_num = user.register_Vehicle(plates)

        plates.append(plate_num)
        cards.append(card_num)

    elif choice in ["2","3","4","5","6"]:
        password_check = admin.check_password()
        if password_check == True:
            if choice == "2":
                plate = input("Enter your plate number: ")
                admin.verify_vehicle(plate)

            elif choice == "3":
                admin.display_vehicles(plates, cards)

            elif choice == "4":
                admin.display_charges(plates, cards)

            elif choice == "5":
                vehicle = input("Enter Vehicle: ")
                admin.remove_vehicle(vehicle)

            elif choice == "6":
                admin.clear_vehicles()

    input("Press Enter to continue....")