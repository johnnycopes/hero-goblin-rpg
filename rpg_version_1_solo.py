"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Character(object):

    # I don't understand slide 29 from Friday -- "calls internally"
    # is there any point in initailizing attributes on the main character class since they get defined later?
    def attack(self, enemy):
        enemy.health -= self.power
        print "The %s does %d damage to the %s." % (self.name, self.power, enemy.name)
        if not enemy.alive():
            print "The %s is dead." % enemy.name

    def alive(self):
        return self.health > 0

    def print_status(self):
        print "The %s has %d health and %d power." % (self.name, self.health, self.power)


class Hero(Character):

    # difference between class-level attributes/instance-level attributes?
    legs = 2
    def __init__(self):
        self.name = "hero"
        self.health = 10
        self.power = 5


class Goblin(Character):

    legs = 3
    def __init__(self):
        self.name = "goblin"
        self.health = 6
        self.power = 2


class Zombie(Character):

    def __init__(self):
        self.name = "zombie"
        self.health = 4
        self.power = 1

    def alive(self):
        return True
        print alive()


hero = Hero()
monster = Goblin()


while monster.alive() and hero.alive():
    hero.print_status()
    monster.print_status()
    print "What do you want to do?"
    print "1. fight %s" % monster.name
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks monster
        hero.attack(monster)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if monster.alive():
        # Monster attacks hero
        monster.attack(hero)
