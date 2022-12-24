import random
import argparse

user_input = int(input("Ingrese la cantidad de dados: "))

def calculate(times):

    for elem in range(times):
        print(random.randint(1, 6))
     

calculate(user_input)

###################################################################################################################################################
# def validation(answer):

#     parser = argparse.ArgumentParser()

#     if answer.strip() in {'1', '2', '3', '4', '5', '6'}:
#         return int(answer)
    
#     else:
#         parser.error("ERROR")


def calculate2(times2):

    list = []

    for number in range(times2):
        rolls = random.randint(1, 6)
        list.append(rolls)

    return list

user_input2 = int(input("Seleccione otro num: "))

# parsed_answer = validation(user_input2)
result  = calculate2(user_input2)
print(result)