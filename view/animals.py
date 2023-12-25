from view import input_new_command
from view.console import input_name_animals, input_age_animals, input_commands_animals, select_class_input


class Animals:
    def __init__(self, name: str, age: int, commands: str):
        self.name = name
        self.age = age
        self.commands = commands

    def new_animal(self):
        self.name = input_name_animals()
        self.age = input_age_animals()
        self.commands = self.commands + (input_commands_animals())

    def new_command(self):
        if self.name == None:
            return f''
        else:
            self.commands = self.commands + ', ' + (input_new_command())


class HomeAnimals(Animals):
    def __init__(self, clases: str, name: str, age: int, commands: str):
        super().__init__(name, age, commands)
        self.clases = clases

    def information(self) -> str:
        return f'{self.clases} | {self.name} | {self.age}'

    def information_on_commands(self):
        if self.name == None:
            return f'Такого животного пока нет'
        return f' команды : {self.commands}'

class Cats(HomeAnimals):

    def cat_voice(self) -> str:
        if self.name == None:
            return f'Такого животного пока нет'
        return f'Мяу'

class Dogs(HomeAnimals):
    def dog_voice(self) -> str:
        if self.name == None:
            return f'Такого животного пока нет'
        return f'Гав'

class Hamsters(HomeAnimals):
    def hamster_voice(self) -> str:
        if self.name == None:
            return f'Такого животного пока нет'
        return f'Писк'


class PackAnimals(Animals):
    def __init__(self, clases: str, name: str, age: int, commands: str):
        super().__init__(name, age, commands)
        self.clases = clases

    def information(self) -> str:
        return f'{self.clases} | {self.name} | {self.age}'

    def information_on_commands(self):
        if self.name == None:
            return f'Такого животного пока нет'
        return f'{self.commands}'

class Horses(PackAnimals):
    def horse_voice(self) -> str:
        if self.name == None:
            return f'Такого животного пока нет'
        return f'Иго-го'

class Donkeys(PackAnimals):
    def donkey_voice(self) -> str:
        if self.name == None:
            return f'Такого животного пока нет'
        return f'Иа'


class Camels(PackAnimals):
    def camels_voice(self) -> str:
        if self.name == None:
            return f'Такого животного пока нет'
        return f'ыыыыыы'



cat = Cats('кошка', None, None, ' ')
dog = Dogs('собака', None, None, ' ')
hamster = Hamsters('хомяк', None, None, ' ')
horse = Horses('лошадь', None, None, ' ')
donkey = Donkeys('осел', None, None, ' ')
camel = Camels('верблюд', None, None, ' ')