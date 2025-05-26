room_prices = {
    "standard": 50,
    "premium": 100,
    "executive": 150,
}

while True:

    user_input = input("Do you want to make a booking [Y/N]: ").upper()

    if user_input == "Y":

        print("Standard: £50")
        print("Premium: £100")
        print("Executive: £150")
        user_room = input("What type of room do you want?: ").lower()

        if user_room not in room_prices:
            print("Error! Please select a valid room type!")
            continue

        try:
            user_nights = int(input("How many nights are you staying?: "))

            if user_nights <= 0:
                print("Error! Number of nights must be positive and above 0!")
                continue

        except ValueError:
            print("Error! Please select a valid number of nights!")
            continue

        total_price = user_nights * room_prices[user_room]
        print(f"The total price will be £{total_price}.")
        break

    elif user_input == "N":

        print("Booking not made! ... Exiting program")
        break

    else:
        print("Error! Please enter 'Y' or 'N'!")