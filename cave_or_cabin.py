"""
File name: cave_or_cabin.py
Author: Brandon Smith
Date: 11/13/23
Description: A text based game in which a character decides if they
want to go to a cabin or cave and their choices have some unexpected
outcomes.
"""
import time
import random

# global variables

# points cannot go lower than 0, no max
points = 0

# gold starts at 1000, can go to 0 based on choice
gold = 1000

# default name
name = ""


def point_updater(amount):
    global points
    return points + amount


def status(name, points):
    return f"{name}, you currently have {points} points."


def clear_screen():
    for i in range(10):
        time.sleep(0.5)
        print("")


def intro_text():
    global name
    print("Welcome brave adventurer. What is your name?")
    name = input("> ")
    if name == "":
        name = "Taeves"
    time.sleep(1)
    for i in range(4):
        time.sleep(0.5)
        print()
    print(f"""
    {name}, you are walking through a forest on a foggy morning.
    You have a pocket full of gold and are whistling a merry tune.
    In the distance, you see a cottage.""")
    print("""
    Do you
    1) Knock on the door
    2) Keep walking?""")
    choice = int(input("> "))
    if choice == 1:
        cottage_intro()
    elif choice == 2:
        cave_intro()
    return None


def cottage_art():
    print(r"""
                               (   )
                          (    )
                           (    )
                          (    )
                            )  )
                           (  (                  /\
                            (_)                 /  \  /\
                    ________[_]________      /\/    \/  \
           /\      /\        ______    \    /   /\/\  /\/\
          /  \    //_\       \    /\    \  /\/\/    \/    \
   /\    / /\/\  //___\       \__/  \    \/
  /  \  /\/    \//_____\       \ |[]|     \
 /\/\/\/       //_______\       \|__|      \
/      \      /XXXXXXXXXX\                  \
        \    /_I_II  I__I_\__________________\
               I_I|  I__I_____[]_|_[]_____I
               I_II  I__I_____[]_|_[]_____I
               I II__I  I     XXXXXXX     I
            ~~~~~"   "~~~~~~~~~~~~~~~~~~~~~~~~
    """)


def cottage_intro():
    cottage_art()
    time.sleep(1)
    clear_screen()
    global points
    global name
    points = point_updater(10)
    print("You gain 10 points.", end=" ")
    print(status(name, points))
    time.sleep(0.5)
    print("""
    When you knock on the door, it creaks open 
    to reveal a smoky, dark interior with a fire burning 
    in the fireplace and the delicious smell of stew cooking. 
    A gruff voice says, "Come in. What did you bring me today?" """)
    print("""
    You say: 
    1) "I brought you a bottle of juice."
    2) "I'm hungry. Give me some of your stew."
    3) "I'm sorry, I didn't bring anything today." """)
    choice = int(input("> "))
    if choice == 1:
        juice_scene()
    elif choice == 2:
        feed_me_scene()
    elif choice == 3:
        nothing_scene()


def juice_scene():
    global points
    global name
    clear_screen()
    clear_screen()
    print(f"""
    A man's face appears from the darkness. His stern face
    softens when he sees the bottle.
    "Wow, what an unexpected surprise. I haven't seen this
    juice since my childhood." """)
    print(f"You gain 3 points", end=" ")
    points += 3
    print(status(name, points))
    time.sleep(1)
    clear_screen()
    clear_screen()
    print(f"""
    "As a token of my gratitude, take this bowl of stew.
    I hope you find that it gives you strength and warmth
    on this foggy day.""")
    time.sleep(1)
    points += 6
    print(f"You gain 6 points", end=" ")
    print(status(name, points))
    time.sleep(1)
    clear_screen()
    time.sleep(1)
    good_cottage_ending()


def feed_me_scene():
    global points
    points -= 6
    print(f"You lose 6 points for a total of {points} points.")
    print(f"""
        A growl fills the cabin, and the strong man in 
        well-used work clothes stands up from his bowl of stew.
        His stern face appears from the darkness and hardens. 
        "No food for you! Now get out!" """)
    steal_apologize()


def steal_apologize():
    global points
    global name
    print(f"""
        What do you do?
        1) Steal the bowl of stew and run back outside.
        2) Apologize deeply and explain you have no money and you are starving.
        """)
    choice = int(input("> "))
    if choice == 1:
        points = 0
        time.sleep(1)
        print(f"{name}, you have lost all of your points.")
        time.sleep(1)
        clear_screen()
        time.sleep(1)
        print(f"""
        You are too slow and the mysterious man catches you. He also
        takes all of your gold that you had hidden in your boot before he takes
        you to jail.""")
        time.sleep(1)
        bad_ending()
    elif choice == 2:
        points += 1
        print("You have gained only one point for your dishonesty")
        print(status(name, points))
        time.sleep(1)
        clear_screen()
        print(f"""
        The man eyes your coin pouch, scowls, then ladles you a small bowl of
        soup. 
        "Eat your stew quickly and leave my cabin. I don't like liars."
        """)
        time.sleep(2)
        clear_screen()
        time.sleep(1)
        good_cottage_ending()


def nothing_scene():
    global name
    global points
    steal_apologize()
    return None


def cave_art():
    print(r"""
            ___..-.
     ._/  __ \_`-.__        
     / .'/##\_ `-.  \--.     
     .-_/#@@##\  /-' `\_    
    - /########\_  \._   `-
    " "'"''"'"'''" ''"'"''"
    """)


def witch_art():
    print(r"""
                                     
               (       "     )   
                ( _  *           
                   * (     /      \    ___
                      "     "        _/ /
                     (   *  )    ___/   |
                       )   "     _ o)'-./__
                      *  _ )    (_, . $$$
                      (  )   __ __ 7_ $$$$
                       ( :  { _)  '---  $\
                  ______'___//__\   ____, \
                   )           ( \_/ _____\_
                 .'             \   \------''.
                 |='           '=|  |         )
                 |               |  |  .    _/
                  \    (. ) ,   /  /__I_____\
                   '._/_)_(\__.'   (__,(__,_]
                  @---()_.'---@
    """)


def boot_art():
    print(r"""
           ________
    __(_____  <|
   (____ / <| <|
   (___ /  <| L`-------.
   (__ /   L`--------.  \
   /  `.    ^^^^^ |   \  |
  |     \---------'    |/
  |______|____________/]
  [_____|`-.__________]

    """)


def cave_intro():
    global name
    global points

    points += 5
    print(f"You have gained {points} points.")
    print(status(name,points))
    print(f"""
    As you walk down the forest path, you see a cave to your right.""")
    time.sleep(1.5)
    cave_art()
    time.sleep(1)
    clear_screen()
    print(f"""What do you do?
    1) Enter the cave
    2) Keep walking """)
    choice = int(input("> "))
    if choice == 1:
        points += 15
        print(f"You have gained 15 points for your bravery")
        print(status(name, points))
        time.sleep(1)
        clear_screen()
        witch_encounter()
    elif choice == 2:
        if points <= 4:
            print(f"You are a coward and now have 0 points.")
            points = 0
        else:
            points -= 5
            print(f"{name}, you have lost 5 points due to your cowardice.")
            print(status(name, points))
        cave_intro()


def witch_encounter():
    global name
    global points
    print(f"""
    You enter the cave and notice a strange smell in the air. You continue
    forward and after a while see a faint glow in the distance. Eventually,
    you come into a large opening and see a witch at a cauldron""")
    time.sleep(2)
    clear_screen()
    witch_art()
    time.sleep(1)
    clear_screen()
    clear_screen()
    print(f"""She turns to you and says "Hello, brave traveller. You have
    trespassed into my cave, but I see that you are carrying a pouch with
    1000 gold in it. I will give you 2 options so you can escape with your
    life...""")
    time.sleep(2)
    clear_screen()
    print(f"""
    1) Give me all of your gold and your shoes
    2) Give me half of your gold and fetch me a branch."
    As you ponder this strange request, you notice she is blind. Then,
    you see a bottle of potion within your reach. What do you do? 
    
    1) Give her all of your gold and your shoes
    2) Give her half of your gold and then go outside the cave to get a branch
    3) Steal the mysterious potion """)
    choice = int(input("> "))

    if choice == 1:
        time.sleep(1)
        clear_screen()
        treasure_shoes_scene()
    elif choice == 2:
        time.sleep(1)
        clear_screen()
        staff_scene()
    elif choice == 3:
        time.sleep(1)
        clear_screen()
        potion_scene()


def treasure_shoes_scene():
    global name
    global points
    item = "treasure shoes"
    boot_art()
    time.sleep(1)
    clear_screen()
    print(f"You now have 0 gold.")
    print(f"You gain 10 points.", end=" ")
    print(status(name, points))
    time.sleep(1)
    clear_screen()
    print("""
    The witch takes your gold and your shoes.
    She puts some mysterious ingredients into the cauldron
    and dips your shoes in the cauldron...""")
    time.sleep(1)
    clear_screen()
    clear_screen()
    print("""
    She takes your shoes out of the cauldron, hands them to
    you and says, "You now have shoes that will lead you to
    treasure." """)
    time.sleep(1)
    clear_screen()
    good_cave_ending(item)


def staff_scene():
    global name
    global points
    item = "staff"
    print(f"You now have 500 gold.")
    print(f"You gain 4 points.", end=" ")
    print(status(name, points))
    time.sleep(1)
    clear_screen()
    print("""
        The witch takes your half of your gold and you leave
        the cave in search of the perfect walking stick. When
        you return, she puts some mysterious ingredients into 
        the cauldron and dips the walking stick in the cauldron...""")
    time.sleep(1)
    clear_screen()
    clear_screen()
    print("""
        She takes the walking stick out of the cauldron, hands it to
        you and says, "You now have a staff that will generate food
        and water any time you need it. May this keep you well fed 
        on your journeys" """)
    time.sleep(1)
    clear_screen()
    good_cave_ending(item)


def potion_scene():
    global points
    global name
    rand_num = random.randint(1, 10)
    print(f"""
    Even though the witch is blind, she senses your deception and theft.
    She casts a spell that freeze you in place.
    "How dare you steal from me!", she cries."
    "Now you will drink the potion and see what happens." """)
    time.sleep(1)
    clear_screen()
    potion_bottle_art()
    time.sleep(1)
    clear_screen()
    print(f"""
    You feel a strange sensation throughout your body and...""")
    time.sleep(1)
    clear_screen()
    if 1 <= rand_num <= 7:
        points = 0
        print(f"""
    everything goes black, you crash to the floor, and you see that
    you now have paws. You have been turned into a weasel and you
    have lost everything.""")
        print(status(name, points))
        time.sleep(1)
        bad_ending()
    else:
        item = "new powers"
        points += 1000

        print(f"""
    everything goes black, you crash to the floor, then wake
    up a few minutes later. When you wake up you feel different;
    more energized, more powerful - like you have a connection
    with everything around you. You realize you now have the same
    powers as the witch. You cast a spell to freeze her in place
    temporarily and quickly run from the cave.""")
        time.sleep(3)
        print(status(name, points))
        time.sleep(1)
        clear_screen()
        good_cave_ending(item)


def good_cave_ending(item):
    global name
    global points
    good_ending_art()
    time.sleep(1)
    clear_screen()
    print(f"""
        With {points} points, you, {name} the adventurous traveler,
        exit the cave with your {item} and continue down the road
        in search of more adventures""")
    time.sleep(2)


def good_ending_art():
    print(r"""
                                               _
                 ___                          (_)
               _/XXX\
_             /XXXXXX\_                                    __
X\__    __   /X XXXX XX\                          _       /XX\__      ___
    \__/  \_/__       \ \                       _/X\__   /XX XXX\____/XXX\
  \  ___   \/  \_      \ \               __   _/      \_/  _/  -   __  -  \__/
 ___/   \__/   \ \__     \\__           /  \_//  _ _ \  \     __  /  \____//
/  __    \  /     \ \_   _//_\___     _/    //           \___/  \/     __/
__/_______\________\__\_/________\_ _/_____/_____________/_______\____/_______
                                  /|\
                                 / | \
                                /  |  \
                               /   |   \
                              /    |    \
                             /     |     \
                            /      |      \
                           /       |       \
                          /        |        \
                         /         |         \

    """)


def good_cottage_ending():
    global name
    global points
    good_ending_art()
    time.sleep(1)
    print(f"""
    With {points} points, you, {name} the adventurous traveler, 
    continue down the road in search of more adventures""")


def bad_ending():
    print(f"""
    It looks like you made some bad choices.
    """)
    print(r"""
     _______  _______  _______  _______    _______           _______  _______ 
(  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
| (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
| |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
| | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
| | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
| (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
(_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/
                                                                          
                                                                          """)
    time.sleep(1)

def thanks_for_playing():
    print(f"""
    Thanks for playing!
    """)
    print(r"""
         _______  _______  _______  _______    _______           _______  _______ 
    (  ____ \(  ___  )(       )(  ____ \  (  ___  )|\     /|(  ____ \(  ____ )
    | (    \/| (   ) || () () || (    \/  | (   ) || )   ( || (    \/| (    )|
    | |      | (___) || || || || (__      | |   | || |   | || (__    | (____)|
    | | ____ |  ___  || |(_)| ||  __)     | |   | |( (   ) )|  __)   |     __)
    | | \_  )| (   ) || |   | || (        | |   | | \ \_/ / | (      | (\ (   
    | (___) || )   ( || )   ( || (____/\  | (___) |  \   /  | (____/\| ) \ \__
    (_______)|/     \||/     \|(_______/  (_______)   \_/   (_______/|/   \__/

                                                                              """)
    time.sleep(1)
def potion_bottle_art():
    print(r"""
      _____
     `.___,'
      (___)
      <   >
       ) (
      /`-.\
     /     \
    / _    _\
   :,' `-.' `:
   |         |
   :         ;
    \       /
     `.___.' 
    
    """)


def main():
    global points
    while True:
        intro_text()
        play_again = input("Would you like to play again? (yes or no)")
        if play_again.lower() == "yes":
            points = 0
            continue
        elif play_again.lower() == "no":
            print(status(name,points))
            thanks_for_playing()
            return
        else:
            print("I'll assume you mean yes and you get to play again.")
            points = 0
            continue


if __name__ == '__main__':
    main()
