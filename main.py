print("Выберете лучшую игру в roblox")

game = ""

while game != "завершить":
    print("1 - grow a garden")
    print("2 - steal a brainrot")
    print("3 - 99 nights in the forest")
    print("4 - Blox Fruits")
    print("Для выхода введите 'завершить'")
    
    game = input("Выберете лучшую игру: ")
    
    if game == "1":
        print("Это очень известная игра в roblox")
        input("Нажмите Enter чтобы продолжить...")
    elif game == "2":
        print("Это смешная игра и популярная в roblox")
        input("Нажмите Enter чтобы продолжить...")
    elif game == "3":
        print("Это затягивающая игра")
        input("Нажмите Enter чтобы продолжить...")
    elif game == "4":
        print("Потрясающая игра про one piece!")
        input("Нажмите Enter чтобы продолжить...")
    elif game == "завершить":
        print("Завершение программы...")
    else:
        print("Такой игры нету в списке попробуйте еще раз!")
        input("Нажмите Enter чтобы продолжить...")
    print()