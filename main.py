import chars
import player
import help_win
import path
import battle
import pick_fruit
from colorama import init
init()

help_win.clear()

hero = player.Player([chars.get_begin_char(), chars.get_begin_char(), chars.get_begin_char(), chars.get_begin_char()])

def loop():
    block = False
    fruit = False
    event = ''
    enemy = ''
    while (1):
        help_win.print_help()
        hero.print_battle_characters(False)
        print()

        if (event == 'char'):
            if (block == False):
                enemy = hero.generate_enemy()
                block = True
            print('\tyou meet: ')
            hero.print_char(enemy)
        elif (event == 'fruit'):
            print('\tfruit')
            fruit = True
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
            event = ''
            enemy = ''
            block = False
        elif (key == 'e'):
            if (fruit):
                fruit = False
                event = ''
                pick_fruit.choose_char_fruit(hero)
            help_win.clear()
        else:
            help_win.clear()

loop()