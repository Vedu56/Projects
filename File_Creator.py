while True:

    userInput = input("Create File? [Y/N]: ").upper()

    if userInput == "Y":
        fileName = input("Enter File Name: ").strip().upper()
        
        try:
            with open(f"{fileName}.txt", "x") as file:
                print(f"File {fileName}.txt created successfully!")
                break

        except FileExistsError:
            print(f"The file {fileName}.txt already exists!")
    
    elif userInput == "N":
        print("File not created! ... Exiting program")
        break
    
    else:
        print("Enter Y or N please!")






   



