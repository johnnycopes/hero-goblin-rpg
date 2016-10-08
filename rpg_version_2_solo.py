"""
Added a store. The hero can now buy a tonic or a sword. A tonic will add 2 to the hero's health wherease a sword will add 2 power.
"""
import random
import time


# Character template

class Character(object):
    def __init__(self):
        self.armor = 0
        self.asleep = False
        self.sleep_counter = 0

    def alive(self):
        return self.health > 0

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
        if self.asleep:
            print "%s is asleep and can't attack this round" % self.name
            self.sleep_counter += 1
        else:
            print "%s attacks %s" % (self.name, enemy.name)
            enemy.receive_damage(self.power)
            if self.much_faster(enemy):
                print "The %s is much quicker than the %s and strikes again!" % (self.name, enemy.name)
                enemy.receive_damage(self.power)
        time.sleep(2)

    def evade(self):
        if self.agility > random.randint(1, 10):
            return True
        else:
            return False

    def calculate_damage(self, points):
        if self.armor > points:
            return 0
        else:
            return points - self.armor

    def receive_damage(self, points):
        if self.evade():
            print "The %s dodged the attack!" % self.name
        else:
            damage = self.calculate_damage(points)
            self.health -= damage
            print "%s receives %d damage." % (self.name, damage)
            if not self.alive():
                print "%s is dead." % self.name
            if self.asleep == True and self.sleep_counter > 1:
                self.asleep = False
                print "%s wakes up!" % self.name

    def print_status(self):
        print "%s has %d health and %d power." % (self.name, self.health, self.power)


# Our Hero!

class Hero(Character):
    def __init__(self):
        self.name = 'Hero'
        self.health = 10
        self.power = 5
        self.speed = 5
        self.agility = 1
        self.coins = 20
        super(Hero, self).__init__()

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

    def loot(self, enemy):
        self.coins += enemy.coins


# The baddies

class Goblin(Character):
    def __init__(self):
        self.name = 'Goblin'
        self.health = 6
        self.speed = 4
        self.power = 2
        self.agility = 1
        self.coins = 5
        super(Goblin, self).__init__()

class Harambe(Character):
    def __init__(self):
        self.name = 'Harambe'
        self.health = 15
        self.speed = 6
        self.agility = 2
        self.power = 3
        self.coins = 12
        super(Harambe, self).__init__()

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
        self.health = 11
        self.speed = 3
        self.agility = 1
        self.power = 2
        self.coins = 6
        super(Jigglypuff, self).__init__()

    def attack(self, enemy):
        if not self.alive():
            return
        if enemy.asleep == False:
            self.sing(enemy)
        super(Jigglypuff, self).attack(enemy)

    def sing(self, enemy):
        print "Jigglypuff is singing!"
        print "JIIIIIIGUHLYY PUUUF LA LA LAAA"
        sedate = random.random() < 0.8
        if sedate:
            print "The %s is serenaded to sleep!" % enemy.name
            enemy.asleep = True
        else:
            print "The sweet tune has no effect"

class Medic(Character):
    def __init__(self):
        self.name = 'Medic'
        self.health = 11
        self.speed = 4
        self.agility = 1
        self.power = 2
        self.coins = 7
        super(Medic, self).__init__()

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
        self.health = 8
        self.speed = 9
        self.agility = 6
        self.power = 2
        self.coins = 5
        super(Shadow, self).__init__()

class Zombie(Character):
    def __init__(self):
        self.name = 'Zombie'
        self.health = 4
        self.agility = 0
        self.speed = 1
        self.power = 1
        super(Zombie, self).__init__()

    def alive(self):
        return True

class Wizard(Character):
    def __init__(self):
        self.name = 'Wizard'
        self.health = 13
        self.speed = 3
        self.agility = 0
        self.power = 2
        self.coins = 7
        super(Wizard, self).__init__()

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
            time.sleep(1.5)

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
            hero.loot(enemy)
            "Hero collects %d coins from the spoils" % enemy.coins
            return True
        else:
            print "YOU LOSE!"
            return False


# Items for sale
# ----------------------------- how to make the cost go up for sale each time item is purchased?

class OrangeJuice(object):
    cost = 15
    name = 'orange juice'
    def apply(self, hero):
        hero.armor += 1
        print "%s's armor increased to %d." % (hero.name, hero.armor)

class BlueberrySmoothie(object):
    cost = 10
    name = 'blueberry smoothie'
    def apply(self, hero):
        hero.agility += 1
        print "%s's agility increased to %d." % (hero.name, hero.agility)

class Tonic(object):
    cost = 5
    name = 'tonic'
    def apply(self, hero):
        hero.health += 2
        print "%s's health increased to %d." % (hero.name, hero.health)

class SuperTonic(object):
    cost = 10
    name = 'supertonic'
    def apply(self, hero):
        hero.health += 5
        print "%s's health increased to %d." % (hero.name, hero.health)

class ProteinShake(object):
    cost = 10
    name = 'protein shake'
    def apply(self, hero):
        hero.power += 1
        print "%s's power increased to %d." % (hero.name, hero.power)


# The store

class Store(object):
    # If you define a variable in the scope of a class:
    # This is a class variable and you can access it like
    # Store.items => [Tonic, Sword]
    items = [Tonic, SuperTonic, ProteinShake, BlueberrySmoothie, OrangeJuice]
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
                else:
                    print "Not enough coins to purchase this"
                time.sleep(2)



# Declarations and bird's eye view of game

hero = Hero()
enemies = [Goblin(), Shadow(), Medic(), Jigglypuff(), Wizard(), Harambe()]
battle_engine = Battle()
shopping_engine = Store()

for enemy in enemies:
    hero_won = battle_engine.do_battle(hero, enemy)
    if not hero_won:
        print "YOU LOSE!"
        exit(0)
    shopping_engine.do_shopping(hero)

print "YOU WIN!"
