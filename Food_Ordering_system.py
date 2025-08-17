menu = {
    1: ("Veg Burger", 3.50),
    2: ("Chicken Burger", 4.00),
    3: ("Beef Burger", 3.00),
    4: ("Vegan Burger", 5.00),
    5: ("Fries L", 3.50),
}

while True:

    user_dining = int(input("Eat in (1) or Take away? (2)?: "))

    if user_dining == 1 or user_dining == 2:

        for key,(name, price) in menu.items():
            print(f"{key}: {name} - £{price:.2f}")

        user_choice = int(input(f"Please enter your options from the menu (1-{len(menu)}): "))

        if user_choice not in menu:
            print("Error! Please select a valid option from the menu!")
            continue

        try:
            
            user_quantity = int(input("Please enter the quantity: "))

            if user_quantity <= 0:
                print(f"Error! Please enter a valid option from 1 to {len(menu)} inclusive!")
                continue

        except ValueError:
            print("Error! Please enter a number!")
            continue

        item_name, item_price = menu[user_choice]
        total_price = item_price * user_quantity

        print(f"{item_name} x {user_quantity}")
        print(f"Order total is £{total_price:.2f}")

        break
    
    else:
        print("Error! Please enter either 1 or 2!")
        continue

    