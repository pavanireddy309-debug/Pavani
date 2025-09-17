a=int(input("enter a number between 1 and 10:"))

match a:
    case 1:
        print("you won a charger")
    case 4:
        print("you won a laptop")
    case 7:
        print("you won a mobile phone")
    case _:
        print("Better luck next time")
