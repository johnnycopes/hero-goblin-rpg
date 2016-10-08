# Hero vs. monster turn-based RPG

### A text-based game to practice classes and objects in Python

**Background**

This was an exercise our cohort was assigned in our third week. Its intention was to further understanding and implementation of classes and objects in Python. The idea was to pair-program changes and enhancements to a game created by our instructor. There are two files included here: version 1 was his initial, simple version of the game; version 2 was his final version of the game, which was considerably more complex and what I ended up investing a lot more time into on my own.

**Explanation**

The gameplay is fairly straightforward. You play as the Hero character and your goal is to defeat the enemies that the game introduces to you one by one. It features turn-based combat, so instructions are constantly being printed to the screen to tell you what's happening and what you can do next. Outside of battle, there's also a store from which the Hero can purchase and use items.

**Challenges**

There were a were a wide variety of assigned challenges to take on, including: assigning characters unique special moves (both offensive and defensive), adding new attributes to the characters, creating new enemies and items, giving the enemies a bounty, and fixing a bug intentionally included by our instructor that let the Hero buy items at the shop with a negative amount of money.

**Difficulties**

Although I was familiar with the utility of object-oriented programming from online courses I'd taken (in JavaScript, specifically), this was the first time I'd ever tried to implement it in a real program. It took me a while to get the hang of it, but I gained a pretty good grip on the concept both working with my partner and later on my own. Of course, there were plenty of problems I ran into along the way:

**** Object attributes ****

I ended up adding several new attributes on the characters, including 'asleep', 'agility', 'speed', 'armor', and 'coins'. Right away, I ran into trouble correctly including and referencing them on all of the different characters. After some trial and error, I came to the conclusion that the ones that varied between characters ('speed', 'agility', and 'coins') should be set individually under the __init__ method of each individual character whereas the attributes with a consistent starting point ('asleep' and 'armor') should be set on the parent object's __init__ method and accessed via the 'super' method.

**** Program flow ****

Once the attributes were stable, I began thinking about creative ways to implement their impact. My initial attempts had to do with modifying the main program flow, the 'battle engine' section of the program but I quickly realized how messy that could become; the different characteristics had the possibility of overriding each other's effects or putting them in an illogical order. My solution was to increase the privacy of the objects, only modifying their attributes in their own methods and having them return lots of boolean values to determine what the next course of action in the program flow should be.

**** Sophisticated items ****
