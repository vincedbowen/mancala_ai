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


def get_option():
    while True:
        print("Please select an option:")
        print("1. Simulate game(s) (random vs. AI)")
        print("2. Play against an AI")
        try:
            selection = input("[1/2] \n")
            if selection != '1' and selection != '2':
                raise ValueError
        except ValueError:
            print("Please enter a 1 or 2")
            continue
        else:
            if selection == '1':
                return "random_simulate.py"
            else:
                return "play.py"


def get_num_sims():
    while True:
        try:
            sims = input("Enter Number of simulations [1, 100]:")
            if not sims.isdigit():
                raise ValueError
            else:
                sims = int(sims)
            if sims < 1 or sims > 100:
                raise ValueError
        except ValueError:
            print("Enter an Integer between 1 and 100!!")
            continue
        else:
            return sims
