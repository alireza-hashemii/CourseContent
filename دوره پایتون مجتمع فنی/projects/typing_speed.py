import time
import random

def compute_error_rate(org_text, user_text):    
    difference_len = len(org_text) - len(user_input)
    if difference_len > 0:
        user_text += difference_len * ' '
        
    elif difference_len < 0:
        return 'more characters than requierd'

    error = 0
    for char_number in range(len(org_text)):
        if org_text[char_number] != user_text[char_number]:
            error += 1

    return error


def compute_speed(start_time, end_time, user_text):
    time_elapsed = end_time - start_time
    time_elapsed_revised = round(time_elapsed, 2)
    speed = len(user_text) / time_elapsed_revised
    return round(speed,2)



if __name__ == '__main__':
    with open('resources/typespeed.txt', 'r') as file:
        total_text_options = file.readlines()
        selected_option = random.choice(total_text_options).lower()
        selected_option_len = len(selected_option)

        start_permission = input("The moment you hit enter your time starts: <ENTER>")
        if len(start_permission) == 0:
            start_time = time.time()
            print(selected_option)
            user_input = input("->> ")
            end_time = time.time()

            print(f'speed was {compute_speed(start_time, end_time, user_input)} words/second')
            print(f'total errors = {compute_error_rate(selected_option, user_input)}')
        else:
            print("not a valid input try something else next time.")