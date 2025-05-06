import random
from help_win import start_battle_help, clear, battle_help, end_battle
from arrow import pointer

battle_log = ''
choose_char = True

def lose(hero):
    global battle_log
    global choose_char

    pointer.arrow_exit()
    battle_log = 'all your battle chars is knocked, you lost 1 life, all hp chars will be restore'

    for i in range(len(hero.get_battle_chars())):
        hero.get_battle_chars()[i].restore_hp()

    while (1):
        clear()
        end_battle()
        print(f'\t log: {battle_log}')
        print('\n\t-> ', end='')
        k = input()
        if (k == 'q'): break

    battle_log = ''
    choose_char = True
    

def check_lose(hero, main_chars):
    if (main_chars[0].get_health_char() == 0 
        and main_chars[1].get_health_char() == 0
        and main_chars[2].get_health_char() == 0):
        hero.lost_life()
        return True
    return False

def start_battle(enemy, main_chars, hero):
    global choose_char
    clear()
    while (1):
        start_battle_help()
        print('\tyou meet: ')
        hero.print_char(enemy)
        print()
        hero.print_battle_characters(True)
        print('\n\t-> ', end='')
        k = input()
        if (k == 's'):
            pointer.arrow_down(len(main_chars) - 1)
        elif (k == 'w'):
            pointer.arrow_up(len(main_chars) - 1)
        elif (k == 'e'):
            if (main_chars[pointer.get_position()].get_health_char() > 0):
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
        if (update_xp_char[i].update_xp()):
            battle_log += f'\n\t {update_xp_char[i].get_name()} lvl up! health + 3, power + 2, speed + 1'

    while (1):
        clear()
        end_battle()
        hero.print_battle_characters(False)
        print(f'\n\t log: {battle_log}')
        print('\n\t-> ', end='')
        k = input()
        if (k == 'q'): break

def catch(enemy, hero, char):
    global battle_log

    if (char.get_health_char() <= 0):
        return False
    
    health_percent = (enemy.get_health_char() * 100) / enemy.get_full_health()
    catch_chance = 100 - health_percent

    if ((random.random() * 100) <= catch_chance):
        enemy.restore_hp()
        hero.add_character(enemy)
        hero.restore_all_hp()
        while (1):
            clear()
            end_battle()
            hero.print_battle_characters(False)
            print(f'\n\t log: you catch {enemy.get_name()}!')
            print('\n\t-> ', end='')
            k = input()
            if (k == 'q'): break
        return True
    
    return False

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
                if (check_lose(hero, main_chars)):
                    lose(hero)
                    break
                else:
                    if (main_char.get_health_char() > 0):
                        if (beat(enemy, main_char)):
                            win(update_xp_char, hero)
                            choose_char = True
                            battle_log = ''
                            break
                    else:
                        battle_log = 'switch char or eat fruit'
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
                if (main_char.get_health_char() > 0):
                    beat_after_switch(enemy, main_char)
                if (check_lose(hero, main_chars)):
                    lose(hero)
                    break
            elif (k == 'c'):
                if (catch(enemy, hero, main_char)):
                    choose_char = True
                    battle_log = ''
                    break
                else:
                    beat_after_switch(enemy, main_char)
            elif (k == 'r'):
                if (hero.try_run()):
                    hero.restore_all_hp()
                    choose_char = True
                    battle_log = ''
                    break
                else:
                    beat_after_switch(enemy, main_char)
                    battle_log += ' cant run'
                
        clear()

    pointer.arrow_exit()
    clear()

def miss():
    return random.random() < 0.25

def beat_after_switch(enemy, char):
    global battle_log

    if (char.get_health_char() <= 0):
        battle_log = 'hp your char is 0! switch char or eat fruit'
    else:
        if (miss()):
            battle_log = 'enemy miss; '
        else:
            damage = enemy.get_power_char() - random.randint(0, 2)
            char.damage_health(damage)
            battle_log = f'enemy beat char on {damage} damage; '
        if (char.get_health_char() <= 0):
            battle_log += 'hp your char is 0! switch char or eat fruit'

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
        battle_log += 'hp your char is 0! switch char or eat fruit'