import random
from help_win import start_battle_help, clear, battle_help
from arrow import pointer

battle_log = ''

def battle(enemy, main_chars, hero):
    global battle_log
    clear()
    pointer.arrow_start_position()
    choose_char = True
    main_char = ''

    while (1):
        if (choose_char):
            start_battle_help()
            print('\tyou meet: ')
            hero.print_char(enemy)
            print()
            hero.print_battle_characters()
            print('\n\t-> ', end='')
            k = input()
            if (k == 's'):
                pointer.arrow_down(len(main_chars) - 1)
            elif (k == 'w'):
                pointer.arrow_up(len(main_chars) - 1)
            elif (k == 'e'):
                choose_char = False
                main_char = main_chars[pointer.get_position()]
        else:
            battle_help()
            print('\tenemy:')
            hero.print_char(enemy)
            print('\n\tyour char:')
            hero.print_char(main_char)
            print(f'\n\t log: {battle_log}')
            print('\n\t-> ', end='')
            k = input()
            if (k == 'b'):
                beat(enemy, main_char)
                clear()
            elif (k == 'e'):
                if (main_char.eat_fruit()):
                    battle_log = 'your char eat fruit and restore full hp'
                else:
                    battle_log = 'no fruit for eat'
                clear()
        clear()

    pointer.arrow_exit()
    clear()

def beat(enemy, char):
    global battle_log
    if (char.get_speed_char() >= enemy.get_speed_char()):
        damage = char.get_power_char() - random.randint(0, 3)
        enemy.damage_health(damage)
        battle_log = f'char beat enemy on {damage} damage; '
        damage = enemy.get_power_char() - random.randint(0, 3)
        char.damage_health(damage)
        battle_log += f'enemy beat char on {damage} damage'
    else:
        damage = enemy.get_power_char() - random.randint(0, 3)
        char.damage_health(damage)
        battle_log = f'enemy beat char on {damage} damage; '
        damage = char.get_power_char() - random.randint(0, 3)
        enemy.damage_health(damage)
        battle_log += f'char beat enemy on {damage} damage'

    if (enemy.get_health_char() == 0):
        battle_log += '; you win'
    elif (char.get_health_char() == 0):
        battle_log += '; hp your char is 0! switch char'