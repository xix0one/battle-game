import random
from help_win import start_battle_help, clear, battle_help, end_battle
from arrow import pointer

battle_log = ''
choose_char = True

def start_battle(enemy, main_chars, hero):
    global choose_char
    clear()
    while (1):
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
            return main_char
        clear()

def win(update_xp_char, hero):
    global battle_log
    pointer.arrow_exit()
    battle_log = 'you win, all hp chars will be restore'

    for i in range(len(update_xp_char)):
        update_xp_char[i].restore_hp()

    while (1):
        clear()
        end_battle()
        hero.print_battle_characters()
        print(f'\n\t log: {battle_log}')
        print('\n\t-> ', end='')
        k = input()
        if (k == 'q'): break


def battle(enemy, main_chars, hero):
    global battle_log
    global choose_char
    clear()
    pointer.arrow_start_position()
    main_char = ''
    update_xp_char = []

    while (1):
        if (choose_char):
            main_char = start_battle(enemy, main_chars, hero)
            update_xp_char.append(main_char)
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
                if (main_char.get_health_char() > 0):
                    if (beat(enemy, main_char)):
                        win(update_xp_char, hero)
                        choose_char = True
                        battle_log = ''
                        break
                else:
                    battle_log = 'switch char'
                    clear()
            elif (k == 'e'):
                if (main_char.eat_fruit()):
                    battle_log = 'your char eat fruit and restore full hp'
                else:
                    battle_log = 'no fruit for eat'
                clear()
            elif (k == 's'):
                main_char = start_battle(enemy, main_chars, hero)
                if main_char not in update_xp_char:
                    update_xp_char.append(main_char)
        clear()

    pointer.arrow_exit()
    clear()

def miss():
    return random.random() < 0.25 

def beat(enemy, char):
    global battle_log

    if (char.get_speed_char() >= enemy.get_speed_char()):

        if (miss()):
            battle_log = 'char miss; '
        else:
            damage = char.get_power_char() - random.randint(0, 2)
            enemy.damage_health(damage)
            battle_log = f'char beat enemy on {damage} damage; '

        if (enemy.get_health_char() > 0):
            if (miss()):
                battle_log += 'enemy miss; '
            else:
                damage = enemy.get_power_char() - random.randint(0, 2)
                char.damage_health(damage)
                battle_log += f'enemy beat char on {damage} damage; '
    else:
        if (miss()):
                battle_log = 'enemy miss; '
        else:
            damage = enemy.get_power_char() - random.randint(0, 2)
            char.damage_health(damage)
            battle_log = f'enemy beat char on {damage} damage; '
        if (char.get_health_char() > 0):
            if (miss()):
                battle_log += 'char miss; '
            else:
                damage = char.get_power_char() - random.randint(0, 2)
                enemy.damage_health(damage)
                battle_log += f'char beat enemy on {damage} damage; '

    if (enemy.get_health_char() == 0):
        battle_log += 'you win'
        return True
    elif (char.get_health_char() == 0):
        battle_log += 'hp your char is 0! switch char'