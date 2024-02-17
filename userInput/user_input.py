def get_pit():
    while True:
        try:
            pit = input("Enter Pit:")
            if not pit.isdigit():
                raise ValueError
            else:
                pit = int(pit)
        except ValueError:
            print("Enter an Integer!!")
            continue
        else:
            return pit


def get_turn_num():
    while True:
        try:
            turn = input("Would you like to play as player one? [y/n] \n").lower()
            if turn != 'y' and turn != 'n':
                raise ValueError
        except ValueError:
            print("Please enter y or n")
            continue
        else:
            return turn.lower()

