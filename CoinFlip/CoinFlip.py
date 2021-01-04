import random
import time



def FlipCount():
    flip_counter = 0
    num_flips = int(input("How many times do you want to flip the coin?"))
    heads = 0
    tails = 0
    begin_time = time.time()

    while flip_counter < num_flips:
        coin = random.choice(["Heads", "Tails"])
        if coin == "Heads":
            heads += 1
        elif coin == "Tails":
            tails += 1
        flip_counter += 1
    heads_cent = round((heads / num_flips) * 100, 2)
    tails_cent = round((tails/num_flips) * 100, 2)
    print(f"Total Heads: {heads} - {heads_cent}%")
    print(f"Total Tails: {tails} - {tails_cent}%")
    print(f"Total time: {time.time() - begin_time} seconds")

FlipCount()