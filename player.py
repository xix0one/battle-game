import chars
import random
from arrow import pointer
from help_win import switch_help, clear

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
        self.battle_characters = [ch[0], ch[1], ch[2]]
        self.switch_error = False

    def print_battle_characters(self):
        print('\tyour battle characters:' + '*' * 41)
        print_header()
        for i in range(len(self.battle_characters)):
            print('\t', end='| ')
            for j in range(len(self.battle_characters[i].get_char_info())):
                print((f'{self.battle_characters[i].get_char_info()[j]}').ljust(6, ' ') , '|', end=' ')

            if (pointer.get_position() >= 0):
                if (pointer.get_position() == i):
                    print(' <-')
                else:
                    print()

            else:
                print()
        print('\t' + '*' * 64)

    def add_character(self, ch):
        self.characters.append(ch)

    def print_info(self):
        print('\tyour all characters:' + '*' * 44)
        print_header()
        for i in range(len(self.characters)):
            print('\t', end='| ')
            char = self.characters[i].get_char_info()
            for j in range(len(char)):
                print((f'{char[j]}').ljust(6, ' ') + ' |', end=' ')
            if (i == pointer.get_position()):
                print(' <-')
            else:
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

    def print_char(self, char):
        e = char.get_char_info()
        print('\t' + '-' * 64)
        print_header()
        print('\t| ', end='')
        for i in range(len(e)):
            print((f'{e[i]}').ljust(6, ' '), end=' | ')
        print()
        print('\t' + '-' * 64)

    def switch_error(self, bool=False):
        b = bool
        return b

    def choose_in_switch_char(self, count, function):
        clear()
        switch_help()

        if (self.switch_error):
            print('\tyou cant do it')
            print()
            self.switch_error = False

        pointer.arrow_start_position()
        function()
        k = ''
        while (k != 'e'):
            print('\t-> ', end='')
            k = input()
            if (k == 's'):
                pointer.arrow_down(count)
            elif (k == 'w'):
                pointer.arrow_up(count)
            elif (k == 'q'):
                return 'q'
            clear()
            switch_help()
            function()
        ch = [self.characters[pointer.get_position()], pointer.get_position()]
        pointer.arrow_start_position()
        return ch

    def switch_char(self):
        while (1):
            new_battle_char = self.choose_in_switch_char(len(self.characters) - 1, self.print_info)
            if (new_battle_char == 'q'): break

            old_battle_char = self.choose_in_switch_char(len(self.battle_characters) - 1, self.print_battle_characters)
            if (old_battle_char == 'q'): break

            if (new_battle_char[1] != old_battle_char[1]):
                self.battle_characters[old_battle_char[1]] = new_battle_char[0]
                break
            else:
                self.switch_error = True

        pointer.arrow_exit()
        clear()

    def get_battle_chars(self):
        return self.battle_characters