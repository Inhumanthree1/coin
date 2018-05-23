name = "coin"
import random
def flip():
    ans = random.randint(0,1)
    if ans == 0:
        return "Heads"
    if ans == 1:
        return "Tails"
def bet():
    ans = random.randint(0,1)
    choice = input("Pick between 0 and 1: ")
    if ans == choice:
        return("Win")
    else:
        return("Loss")

