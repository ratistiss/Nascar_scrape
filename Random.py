from random import random
import math

rand_num = random()
comp_num = math.ceil(rand_num * 50)

while True:
    players_guess = int(input("Can you guess my random number: "))
    if players_guess == comp_num:
        print(f"{comp_num} it is winner winner chicken dinner")
        break
    elif players_guess >  comp_num:
        print("Too High try again")
    else:
        print("Too Low try again")