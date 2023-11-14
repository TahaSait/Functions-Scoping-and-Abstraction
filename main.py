import user
import admin

admin_password = "password"

print(f"****************************************************************************\n*** Welcome to Park and Go Parking Application!\
***\nPark from 6PM to Midnight for a flat fee of 4.00\n****************************************************************************")
while True:

    print(f"Select from the following options\n[1] Register a vehicle\n[2] Verify vehicle registration\n[3] Display registered vehicles and save them to a file\
\n[4] Display daily charges a save them to file\n[5] Remove a vehicle\n[6] Clear vehicles\n[0] Exit")
    
    choice = input(">>> ")

    if choice not in ["0","1","2","3","4","5","6"]:
        print("Invalid Input")

    elif choice == "0":
         break
    
    elif choice == "1":
        user.register_Vehicle()

    elif choice in ["2","3","4","5","6"]:
        pass_word = input(f"Enter password: ")
        if pass_word == admin_password:
            if choice == "2":
                plate = input("Enter your plate number: ")
                admin.verify_vehicle(plate)

            elif choice == "3":
                admin.display_vehicle()

            elif choice == "4":
                admin.display_charges()

            elif choice == "5":
                admin.remove_vehicle()

            elif choice == "6":
                admin.clear_vehicle()
        else:
            print("Incorrect Password!")

    input("Press Enter to continue")