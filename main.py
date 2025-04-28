import chars
import player
import help_win
import path
import battle
from colorama import init
init()

help_win.clear()

hero = player.Player(3, [chars.get_begin_char(), chars.get_begin_char(), chars.get_begin_char()])

def loop():
    block = False
    event = ''
    enemy = ''
    while (1):
        help_win.print_help()
        hero.print_battle_characters()
        print()

        if (event == 'char'):
            if (block == False):
                enemy = hero.generate_enemy()
                block = True
            print('\tyou meet: ')
            hero.print_char(enemy)
        elif (event == 'fruit'):
            print('\tfruit')
        elif (event == 'nothing'):
            print('\tnothing')

        print()
        print('\t -> ', end='')

        key = input()
        if (key == 's'):
            help_win.clear()
            hero.switch_char()
        elif (key == 'q'):
            break
        elif (key == 'g'):
            if (block == False):
                event = path.generate_event()
            help_win.clear()
        elif (key == 'b' and block):
            battle.battle(enemy, hero.get_battle_chars(), hero)
            block = False
        else:
            help_win.clear()

loop()