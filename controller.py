from view import text
from view import menu, print_message
from view.console import select_class_input
from view.animals import cat, dog, hamster, horse, donkey, camel


def start():
    while True:
        choice = menu()
        match choice:
            case 1:
                menu_select_class()
            case 2:
                menu_select_command()
            case 3:
                menu_new_command()
            case 4:
                print(cat.information())
                print(dog.information())
                print(hamster.information())
                print(horse.information())
                print(donkey.information())
                print(camel.information())
            case 5:
                menu_lisen_animal()
            case 6:
                print_message(text.exit_program)
                break

def menu_select_class():
    while True:
        choice = select_class_input()
        match choice:
            case 1:
                cat.new_animal()
                print(cat.information())

            case 2:
                dog.new_animal()
                print(dog.information())
            case 3:
                hamster.new_animal()
                print(hamster.information())
            case 4:
                horse.new_animal()
                print(horse.information())
            case 5:
                donkey.new_animal()
                print(donkey.information())
            case 6:
                camel.new_animal()
                print(camel.information())
            case 7:
                break

def menu_select_command():
    while True:
        choice = select_class_input()
        match choice:
            case 1:
                print(cat.information())
                print(cat.information_on_commands())
            case 2:
                print(dog.information())
                print(dog.information_on_commands())
            case 3:
                print(hamster.information())
                print(hamster.information_on_commands())
            case 4:
                print(horse.information())
                print(horse.information_on_commands())
            case 5:
                print(donkey.information())
                print(donkey.information_on_commands())
            case 6:
                print(camel.information())
                print(camel.information_on_commands())
            case 7:
                break

def menu_new_command():
    while True:
        choice = select_class_input()
        match choice:
            case 1:
                cat.new_command()
                print(cat.information())
                print(cat.information_on_commands())
            case 2:
                dog.new_command()
                print(dog.information())
                print(dog.information_on_commands())
            case 3:
                hamster.new_command()
                print(hamster.information())
                print(hamster.information_on_commands())
            case 4:
                horse.new_command()
                print(horse.information())
                print(horse.information_on_commands())
            case 5:
                donkey.new_command()
                print(donkey.information())
                print(donkey.information_on_commands())
            case 6:
                camel.new_command()
                print(camel.information())
                print(camel.information_on_commands())
            case 7:
                break

def menu_lisen_animal():
    while True:
        choice = select_class_input()
        match choice:
            case 1:
                print(cat.cat_voice())
            case 2:
                print(dog.dog_voice())
            case 3:
                print(hamster.hamster_voice())
            case 4:
                print(horse.horse_voice())
            case 5:
                print(donkey.donkey_voice())
            case 6:
                print(camel.camel_voice())
            case 7:
                break