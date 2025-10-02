import random
import time

CHANCE_NUMBER = 3
system_number = random.randint(1,10)

for guess in range(3):
    user_guess = int(input("Provide a number between 1 and 10: "))
    if user_guess == system_number:
        print("we have a winner here.")
        break
    else:
        print("not that one.")
        time.sleep(2)
