import random

class Char():
    def __init__(self, name, health, power, speed, lvl, exp):
        self.full_health = health
        self.name = name
        self.health = self.full_health
        self.power = power
        self.speed = speed
        self.lvl = lvl
        self.exp = exp
        self.lvl_threshold = 20

        # fruit
        if random.random() < 0.50:
            self.pocket = 0
        else:
            self.pocket = 1

    def get_name(self):
        return self.name

    def lvl_up(self):
        self.full_health += 3
        self.health = self.full_health
        self.power += 2
        self.speed += 1
        self.lvl += 1
        self.exp = 0
        self.lvl_threshold += self.lvl_threshold

    def update_xp(self):
        self.exp += 10
        if (self.exp >= self.lvl_threshold):
            self.lvl_up()
            return True
        return False

    def give_fruit(self):
        self.pocket += 1

    def restore_hp(self):
        self.health = self.full_health

    def eat_fruit(self):
        if (self.pocket > 0):
            self.health = self.full_health
            self.pocket -= 1
            return True
        return False

    def get_char_info(self):
        return [self.name, self.health, self.power, self.speed, self.lvl, self.exp, self.pocket]
    
    def get_health_char(self):
        return self.health
    
    def get_full_health(self):
        return self.full_health
    
    def get_lvl_char(self):
        return self.lvl

    def get_power_char(self):
        return self.power
    
    def get_speed_char(self):
        return self.speed
    
    def damage_health(self, count):
        if (self.health - count > 0):
            self.health -= count
        else:
            self.health = 0

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
    power = random.randint(2, 5)
    speed = random.randint(1, 3)
    return Char(generate_name(), health, power, speed, 1, 0)