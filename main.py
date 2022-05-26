dest_array = ["destination one", "destination two", "destination three", "destination four"]
rest_array = ["restaurant one", "restaurant two", "restaurant three", "restaurant four"]
tran_array = ["transportation one", "transportation two", "transportation three", "transportation four"]
ent_array = ["entertainment one", "entertainment two", "entertainment three", "entertainment four"]

import random

def choose_random(arr):
    happy = False
    while happy==False:
        # print(len(arr))
        rand_num = random.randint(0, len(arr)-1)
        print(rand_num)
        rand_choice = arr[rand_num]
        user_input = input(f'{rand_choice} has been chosen. Are you happy with this choice? Y/N ')
        if user_input.lower() == "y":
            happy = True
    return rand_choice

def app():
    dest_choice = choose_random(dest_array)
    rest_choice = choose_random(rest_array)
    tran_choice = choose_random(tran_array)
    ent_choice = choose_random(ent_array)
    print(f'You have chosen destination {dest_choice}, restaurant {rest_choice}, transportation {tran_choice}, and entertainment {ent_choice}')
    confirm = input('Are you happy with your trip? Y/N')
    if confirm == 'n':
        app()
    else:
        print(f'You have chosen destination {dest_choice}, restaurant {rest_choice}, transportation {tran_choice}, and entertainment {ent_choice}')


app()
