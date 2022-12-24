import random
import os
import time

def juego():

    nums = []
    ans = []

    while True:

        simon = random.randint(1, 9)
        nums.append(simon)

        for num in nums:
            num_tmp = str(num)
            print("Sys: " + num_tmp)
            time.sleep(1)
            os.system('cls')

        for num in nums:
    
            inp = int(input("You: "))
            if inp != num:
                break
            ans.append(inp)
            os.system('cls')

        if nums != ans:
            break

        ans = []
        

juego()