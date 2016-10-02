# Hero vs. monster turn-based RPG

### A text-based game to practice classes and objects in Python

**Background**

This was an exercise our cohort was assigned with the intention of furthering understanding and implementation of classes and objects in Python. With a fellow classmate, the idea was to pair-program changes and enhancements to a game created by our instructor. There are two files included here: version 1 was his initial version of the game, which was quite simple; and version 2 was his final version of the game, which was considerably more complex and what I ended up investing a lot more time into.

**Explanation**

The gameplay is fairly straightforward. You play as the Hero and your goal is to defeat the enemies that the game throws at you one by one. It features turn-based combat, so instructions are constantly being printed to the screen to tell you what's happening and what you can do next. Outside of battle, there's also a store from which the Hero can purchase and use items.

**Challenges**

There were a were a wide variety of assigned challenges to take on, including: assigning characters unique special moves (both offensive and defensive), adding new attributes to the characters, creating new enemies and items, giving the enemies a bounty, and fixing a bug intentionally included by our instructor that let the Hero buy items at the shop even with negative money.

**Difficulties**

Although I was familiar with the concept and utility of classes from online courses I'd taken learning about the object prototype in JavaScript, this was the first time I'd ever tried to implement them in a real program. It took me a while to get the hang of the program flow, but once I did I still ran into a lot of problems both when I was working with a partner and later when adding things on my own:

_the 'asleep' attribute_
One of the new enemies my partner and I came up with to include was Jigglypuff, a classic character from the Pokémon series who can serenade its opponents with a siren song. We wanted to include this ability to put our Hero to sleep and cause them to miss their next chance to attack. Our original solution was to give the Hero include an attribute called 'asleep' set to 'False' and then customize Jigglypuff's attack to modify it to 'True' when it sang sweetly. Later on, I ended up moving that attribute to the Character class so that other enemies could be put to sleep with use of an item or other to-be-determined effects.

Two problems that arose once we had that implemented were that 1) Jigglypuff would sing even after being killed by the Hero and 2) once put to sleep, the Hero would never wake up again. To resolve the first, we just needed to check if Jigglypuff still had health points before getting on the mic. As for the second, since eternal slumber wasn't the goal, we needed to make sure that the Hero woke up after missing his chance to attack, but before the next round had started. Later on, I went back and made it so the wake-up was random and not guaranteed in order to add more tension.

_the 'speed' attribute'


****
