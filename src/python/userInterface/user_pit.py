
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