def flip():
    coin = randint(0,1)
    if coin == 0:
        return "Heads"
    else:
        return "Tails"
def bet():
    coin = randint(0,1)
    choice = input("Pick between 0 and 1: ")
    if coin == choice:
        return "Win"
    else:
        return "Loss"
