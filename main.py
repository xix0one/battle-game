from colorama import init
init()

import chars

def clear():
    print('\033[H\033[J', end='', flush=True)

clear()
char = chars.get_begin_char()
char.test_print_char()
