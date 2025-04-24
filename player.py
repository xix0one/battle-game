import chars
import random

def print_header():
    stats = [
            'name ',
            'health ',
            'power ',
            'speed',
            'lvl ',
            'exp ',
            'fruit'
        ]

    print('\t| ', end='')
    for i in range(len(stats)):
        print((stats[i]).ljust(7, ' '), end='| ')
    print()
    print('\t' + '-' * 64)

class Player():
    def __init__(self, fr, ch):
        self.fruit = fr
        self.characters = ch
        self.battle_characters = [0, 1, 2]

    def print_battle_characters(self):
        print('\tyour battle characters:' + '*' * 41)
        print_header()
        for i in range(len(self.battle_characters)):
            print('\t', end='| ')
            for j in range(len(self.characters[self.battle_characters[i]].get_char_info())):
                print((f'{self.characters[self.battle_characters[i]].get_char_info()[j]}').ljust(6, ' ') , '|', end=' ')
            print()
        print('\t' + '*' * 64)

    def add_character(self, ch):
        self.characters.append(ch)

    def print_info(self):
        print()
        print('\tyour all characters:' + '*' * 43)
        print_header()
        for i in range(len(self.characters)):
            print('\t', end='| ')
            char = self.characters[i].get_char_info()
            for j in range(len(char)):
                print((f'{char[j]}').ljust(6, ' ') + ' |', end=' ')
            print()
        print('\t' + '-' * 64)
        print()
    
    def generate_enemy(self):
        max_health = 0
        max_power = 0
        max_speed = 0
        for i in range(len(self.characters)):
            if (max_health < self.characters[i].get_health_char()):
                max_health = self.characters[i].get_health_char()
            if (max_power < self.characters[i].get_power_char()):
                max_power = self.characters[i].get_power_char()
            if (max_speed < self.characters[i].get_speed_char()):
                max_speed = self.characters[i].get_speed_char()

        return chars.Char(chars.generate_name(), 
                          random.randint((max_health - 2), (max_health + 3)),
                          random.randint((max_power - 2), (max_power + 3)),
                          random.randint((max_speed - 2), (max_speed + 3)),
                          1,
                          0
                          )

    def print_enemy(self, enemy):
        e = enemy.get_char_info()
        print('\tyou meet: ')
        print('\t' + '-' * 64)
        print_header()
        print('\t| ', end='')
        for i in range(len(e)):
            print((f'{e[i]}').ljust(6, ' '), end=' | ')
        print()
        print('\t' + '-' * 64)

    def switch_char(self):
        self.print_info()
        self.print_battle_characters()

