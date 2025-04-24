import random

def generate_event():
    path = random.random()
    if path < 0.25:
        return 'fruit'
    elif path < 0.75:
        return 'char'
    else: 
        return 'nothing'