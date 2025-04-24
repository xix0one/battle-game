import chars
import player
import help_win
import path
from colorama import init
init()

def clear():
    print('\033[H\033[J', end='', flush=True)

clear()

help_win.print_help()

hero = player.Player(3, [chars.get_begin_char(), chars.get_begin_char(), chars.get_begin_char()])
hero.add_character(chars.get_begin_char())
hero.add_character(chars.get_begin_char())
# hero.print_info()

hero.print_battle_characters()
print()

event = path.generate_event()

if (event == 'char'):
    enemy = hero.generate_enemy()
    hero.print_enemy(enemy)
elif (event == 'fruit'):
    print('\tfruit')
elif (event == 'nothing'):
    print('\tnothing')

print()
print('\t -> ', end='')

# key = input()
key = 's'
if (key == 's'):
    clear()
    hero.switch_char()