
def get_pit():
    while True:
        try:
            pit = int(input("Enter Pit:"))
        except ValueError:
            print("Enter an Integer!!")
            continue
        else:
            return pit
            break

get_pit()