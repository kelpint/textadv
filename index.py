#!/usr/bin/env python3

Inventory = []

name = input('what is your name? ')

print(f'greetings, {name}')

print('You are trapped inside of a cold building in the middle of a snowstorm. You are trapped with your three friends ari, brooke, and kellan. their are two sets of stairs and one elevator. You can either ask brooke, kellan or ari what to do, or you can go downstairs, upstairs, or in the elevator.')

room_beginning_tookkey = False
def room_beginning() :
    global room_beginning_tookkey
    command1 = input('what would you like to do(1 for ask your friends, 2 to go up the stairs, 3 to go down the stairs, and 4 to go into the elevator.)')

    if command1 == '0':
        print('you took the key.')
        Inventory.append(key)
        room_beginning_tookkey = True
        room_beginning()

    elif command1 == '1':
        print('What should we do? you asked your friends.')

    elif command1 == '2':
        print('You told your friends to come up the stairs with you. They obliged and walked with you. ')

    elif command1 == '3':
        print('You decided to go downstairs."Come on, lets go downstairs."')
        room_downstairs()
    elif command1 == '4':
        print("Let's go to the elevator, you said to your friends")

    else:
        print('invalid command!')

def room_downstairs():
    command2 = input('You are now downstairs. It is very dark down here and you cant see very well. the only source of light is a faint glowing furnace. You can either feel around for something useful(1) or go back upstairs(2)')

    if command2 == '1':
        print('"lets feel around for anything useful, you said." You and your friends started looking around. You found a dusty old key, some furniture, and a locked box.')

room_beginning()
