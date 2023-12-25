from .text import *

def menu() -> int:
    print(main_menu)
    while True:
        choice = input(menu_choice)
        if choice.isdigit() and 0 < int(choice) < 7:
            return int(choice)
        print(input_error)

def print_message(message: str):
    print('\n')
    print(message)
    print('\n')


def select_class_input() -> int:
    print(print_message(select_class))
    choice = input(menu_choice)
    if choice.isdigit() and 0 < int(choice) < 8:
        return int(choice)
    print(input_error)

def input_name_animals():
    name = input(input_new_animals[0])
    return name

def input_age_animals():
    age = input(input_new_animals[1])
    return age

def input_commands_animals():
    commands = input(input_new_animals[2])
    return commands

def input_new_command() -> str:
    new_command_animal = input(text_input_new_command)
    return new_command_animal


