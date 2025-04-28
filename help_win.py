
def print_help():
    print()
    print('\tcommands' + '*' * 30)
    print('\t| go: "g"; battle: "b"; try run: "r" |')
    print(('\t| switch char: "s";').ljust(38, ' ') + '|')
    print('\t' + '*' * 38)
    print()

def switch_help():
    print()
    print('\tcommands' + '*' * 36)
    print('\t| arrow down: "s"; arrow up: "w"; use: "e" |')
    print(('\t| close: "q"; choose char for switch ').ljust(44, ' ') + '|')
    print('\t' + '*' * 44)
    print()

def start_battle_help():
    print()
    print('\tcommands' + '*' * 36)
    print(('\t| choose main char for battle').ljust(44, ' ') + '|')
    print(('\t| arrow down: "s"; arrow up: "w"; use: "e" |').ljust(44, ' '))
    print(('\t| try run: "r"').ljust(44, ' ') + '|')
    print('\t' + '*' * 44)
    print()

def battle_help():
    print()
    print('\tcommands' + '*' * 36)
    print(('\t| beat: "b"; catch: "c"; try run: "r"').ljust(44, ' ') + '|')
    print(('\t| eat fruit: "e", switch char: "s"').ljust(44, ' ') + '|')
    print('\t' + '*' * 44)
    print()

def clear():
    print('\033[H\033[J', end='', flush=True)