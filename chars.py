import random

class Char():
    def __init__(self, name, health, power, speed, lvl, exp):
        self.name = name
        self.health = health
        self.power = power
        self.speed = speed
        self.lvl = lvl
        self.exp = exp
        # fruit
        if random.random() < 0.50:
            self.pocket = 0
        else:
            self.pocket = 1

    def lvl_up(self):
        self.health += 3
        self.power += 3
        self.speed += 3
        self.lvl += 1
        self.exp = 0

    def get_char_info(self):
        return [self.name, self.health, self.power, self.speed, self.lvl, self.exp, self.pocket]
    
    def get_health_char(self):
        return self.health

    def get_power_char(self):
        return self.power
    
    def get_speed_char(self):
        return self.speed

def generate_name():
    name = ''
    n2 = ['a', 'o', 'e', 'i', 'u']
    n1 = ['q','w','r','t','y','p','s','d','f','g','h','j','k','l','z','x','c','v','b','n','m']
    count = random.randint(2, 3)
    for i in range(count):
        name += n1[random.randint(0, len(n1) - 1)]
        name += n2[random.randint(0, len(n2) - 1)]
    if (count == 2):
        name += n1[random.randint(0, len(n1) - 1)]

    return name

def get_begin_char():
    health = random.randint(3, 9)
    power = random.randint(3, 9)
    speed = random.randint(3, 9)
    return Char(generate_name(), health, power, speed, 1, 0)

