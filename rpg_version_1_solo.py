"""
In this simple RPG game, the hero fights the goblin. He has the options to:

1. fight goblin
2. do nothing - in which case the goblin will attack him anyway
3. flee

"""

class Hero(object):

    # difference between class-level attributes/instance-level attributes?
    legs = 2
    def __init__(self):
        self.health = 10
        self.power = 5

    def attack(self, goblin):
        goblin.health -= self.power
        print "The hero does %d damage to the goblin." % self.power
        if goblin.health <= 0:
            print "The goblin is dead."


class Goblin(object):

    legs = 3
    def __init__(self):
        self.health = 6
        self.power = 2

    def attack(self, hero):
        hero.health -= self.power
        print "The goblin does %d damage to the hero." % self.power
        if hero.health <= 0:
            print "The hero is dead."




hero = Hero()
goblin = Goblin()


while goblin.health > 0 and hero.health > 0:
    print "You have %d health and %d power." % (hero.health, hero.power)
    print "The goblin has %d health and %d power." % (goblin.health, goblin.power)
    print
    print "What do you want to do?"
    print "1. fight goblin"
    print "2. do nothing"
    print "3. flee"
    print "> ",
    input = raw_input()
    if input == "1":
        # Hero attacks goblin
        hero.attack(goblin)
    elif input == "2":
        pass
    elif input == "3":
        print "Goodbye."
        break
    else:
        print "Invalid input %r" % input

    if goblin.health > 0:
        # Goblin attacks hero
        goblin.attack(hero)
