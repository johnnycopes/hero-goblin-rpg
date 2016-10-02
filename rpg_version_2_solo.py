"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time


# Character template
# is it at all necessary to include the def __init__ attributes? ########################## <----------------

class Character(object):
    def __init__(self):
        self.name = '<undefined>'
        self.health = 10
        self.power = 5
        self.speed = 4
        self.asleep = False
        self.coins = 20

    def alive(self):
        return self.health > 0

    def asleep(self):
        return self.asleep

    def faster(self, enemy):
        return self.speed > enemy.speed

    def much_faster(self, enemy):
        return self.speed >= enemy.speed * 2

    def wake_up(self):
        if self.asleep == True:
            if random.random() < 0.5:
                print "%s wakes up" % self.name
                self.asleep = False
            else:
                print "%s is still sleeping" % self.name

    def attack(self, enemy):
        if not self.alive():
            return
        # changing this to 'if self.asleep:' makes both characters sleep no matter what. why? ########################## <----------------
        if self.asleep == True:
            print "%s is asleep and can't attack this round" % self.name
        else:
            print "%s attacks %s" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
            if self.much_faster(enemy):
                print "The %s is much quicker than the %s and strikes again!" % (self.name, enemy.name)
                enemy.receive_damage(self.power)
        time.sleep(2)

    def receive_damage(self, points):
        self.health -= points
        print "%s receives %d damage." % (self.name, points)
        if not self.alive():
            print "%s is dead." % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


# Our Hero!

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.speed = 5
        self.coins = 20

    def attack(self, enemy):
        double_damage = random.random() < 0.2
        if double_damage:
            self.power *= 2
            print "The %s's weapon glows bright!" % self.name
        super(Hero, self).attack(enemy)
        if double_damage:
            self.power /= 2

    # Hero wins speed ties
    def faster(self, enemy):
        return self.speed >= enemy.speed

    def restore(self):
        self.health = 10
        print "%s's heath is restored to %d!" % (self.name, self.health)
        time.sleep(2)

    def buy(self, item):
        self.coins -= item.cost
        item.apply(hero)


# The baddies

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.speed = 4
        self.power = 2


class Harambe(Character):
    def __init__(self):
        self.name = 'Harambe'
        self.health = 15
        self.speed = 6
        self.power = 3

    def attack(self, enemy):
        hyped_up = random.random() < 0.3
        if hyped_up:
            print "Harambe is getting hyped up!"
            self.power *= 2
            self.speed *= 1.5
        super(Harambe, self).attack(enemy)
        if hyped_up:
            self.power /= 2
            self.speed /= 1.5


class Jigglypuff(Character):
    def __init__(self):
        self.name = 'Jigglypuff'
        self.health = 7
        self.speed = 3
        self.power = 1

    def attack(self, enemy):
        if not self.alive():
            return
        # I want to add a condition where Jigglypuff won't sing if the enemy is asleep, but it ignores enemy.asleep here ########################## <----------------
        print "Jigglypuff is singing!"
        print "JIIIIIIGUHLYY PUUUF LA LA LAAA"
        sedate = random.random() < 0.8
        if sedate:
            print "The %s is serenaded to sleep!" % enemy.name
            enemy.asleep = True
        else:
            print "The sweet tune has no effect"
        super(Jigglypuff, self).attack(enemy)


class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 11
        self.speed = 4
        self.power = 2

    def receive_damage(self, points):
        super(Medic, self).receive_damage(points)
        if self.alive():
            recuperate = random.random() < 0.4
            if recuperate:
                print "Medic recuperated 4 health points"
                self.health += 2


class Shadow(Character):
    def __init__(self):
        self.name = 'Shadow'
        self.health = 1
        self.speed = 9
        self.power = 1

    def receive_damage(self, points):
        evade = random.random() < 0.9
        if evade:
            print "%s evades the attack!" % self.name
        else:
            super(Shadow, self).receive_damage(points)


class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 4
        self.speed = 1
        self.power = 1

    def alive(self):
        return True


class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 8
        self.speed = 3
        self.power = 1

    def attack(self, enemy):
        swap_power = random.random() < 0.5
        if swap_power:
            print "%s swaps power with %s during attack" % (self.name, enemy.name)
            self.power, enemy.power = enemy.power, self.power
        super(Wizard, self).attack(enemy)
        if swap_power:
            self.power, enemy.power = enemy.power, self.power


# The battle

class Battle(object):
    def do_battle(self, hero, enemy):
        print "====================="
        print "Hero faces the %s" % enemy.name
        print "====================="
        while hero.alive() and enemy.alive():

            hero.wake_up()
            enemy.wake_up()
            time.sleep(2)

            print "-----------------------"
            print "What do you want to do?"
            print "1. fight %s" % enemy.name
            print "2. do nothing"
            print "3. flee"
            print "> ",
            input = int(raw_input())

            if input == 1:
                if hero.faster(enemy):
                    hero.attack(enemy)
                else:
                    enemy.attack(hero)
            elif input == 2:
                pass
            elif input == 3:
                print "Goodbye."
                exit(0)
            else:
                print "Invalid input %r" % input
                continue
            if not enemy.faster(hero):
                enemy.attack(hero)
            else:
                hero.attack(enemy)

        if hero.alive():
            print "You defeated the %s" % enemy.name
            return True
        else:
            print "YOU LOSE!"
            return False


# Items for sale

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, character):
        character.health += 2
        print "%s's health increased to %d." % (character.name, character.health)

class Sword(object):
    cost = 10
    name = 'sword'
    def apply(self, hero):
        hero.power += 2
        print "%s's power increased to %d." % (hero.name, hero.power)


# The store

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, Sword]
    def do_shopping(self, hero):
        while True:
            print "====================="
            print "Welcome to the store!"
            print "====================="
            print "You have %d coins." % hero.coins
            print "What do you want to do?"
            for i in xrange(len(Store.items)):
                item = Store.items[i]
                print "%d. buy %s (%d)" % (i + 1, item.name, item.cost)
            print "10. leave"
            input = int(raw_input("> "))
            if input == 10:
                break
            else:
                ItemToBuy = Store.items[input - 1]
                item = ItemToBuy()
                if hero.coins >= item.cost:
                    hero.buy(item)
                    time.sleep(2)
                else:
                    print "Not enough coins to purchase this"
                    time.sleep(2)



# Declarations and bird's eye view of game

hero = Hero()
enemies = [Harambe(), Jigglypuff(), Shadow(), Medic(), Goblin(), Wizard()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
