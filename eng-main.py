#English version
print("Select the best Roblox game:")

game = ""

while game != "exit":
    print("1 - Grow a Garden")
    print("2 - Steal a Brainrot") 
    print("3 - 99 Nights in the Forest")
    print("4 - Blox Fruits")
    print("Type 'exit' to quit")
    
    game = input("Choose your favorite game: ")
    
    if game == "1":
        print("This is a very popular Roblox game!")
        input("Press Enter to continue...")
    elif game == "2":
        print("This is a funny and popular Roblox game!")
        input("Press Enter to continue...")
    elif game == "3":
        print("This is an addictive game!")
        input("Press Enter to continue...")
    elif game == "4":
        print("Amazing One Piece game!")
        input("Press Enter to continue...")
    elif game == "exit":
        print("Program terminated...")
    else:
        print("This game is not in the list! Try again!")
        input("Press Enter to continue...")
    
    print()
