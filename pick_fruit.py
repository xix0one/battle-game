from arrow import pointer
from help_win import clear, pick_fruit

def choose_char_fruit(hero):
    pointer.arrow_start_position()
    count_chars = len(hero.get_chars()) - 1

    while (1):
        clear()
        pick_fruit()
        hero.print_info(True)
        hero.print_battle_characters(False)
        
        print()
        print('\t -> ', end='')
        key = input()
        
        if (key == 's'):
            pointer.arrow_down(count_chars)
        elif (key == 'w'):
            pointer.arrow_up(count_chars)
        elif (key == 'e'):
            hero.get_chars()[pointer.get_position()].give_fruit()
            break
        elif (key == 'q'):
            break

    pointer.arrow_exit()