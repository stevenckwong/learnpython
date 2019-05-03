# Branches and Functions
from sys import exit

def gold_room():
    print("This room is full of gold. How much do you take?")
    choice = input("> ")
    # if "0" in choice or "1" in choice:
    if choice.isdigit():
        how_much = int(choice)
    else:
        dead("Man, learn to type a number.")

    if how_much < 50:
        print("Nice. You're not greedy. You win!")
        exit(0)
    else:
        dead("You greedy bastard!")


def bear_room():
    print("There is a bear here")
    print("The bear has a bunch of honey.")
    print("The far bear is in front of another door.")
    print("How are you going to move the bear?")
    print("- 'take honey' or 'taunt bear' or 'leave'")

    bear_moved = False
    while True:
        choice = input("> ")
        if choice == "take honey":
            dead("The bear looks at you and then slaps your face off")
        elif choice == "taunt bear" and not bear_moved:
            print("The bear has moved from the door.")
            print("You can go through it now.")
            print("What do you want to do next? ")
            print("- 'open door' or 'leave'")
            bear_moved = True
        elif choice == "taunt bear" and bear_moved:
            dead("The bear gets pissed off and chews your leg off")
        elif choice == "open door" and bear_moved:
            gold_room()
        elif choice == "leave":
            start()
        else:
            print("I got no idea what that means.")


def cthulhu_room():
    print("""
        Here, you see the great evil Cthulhu.
        He, it whatever stares at you and you go insane
        Do you flee for your life or eat your head?
        (- 'flee' or 'head')
        """)
    choice = input("> ")

    if "flee" in choice:
        start()
    elif "head" in choice:
        dead("Well that was tasty!")
    else:
        cthulhu_room()

def dead(why):
    print(why, "\nYou're dead. Good job.")
    exit(0)

def start():
    print("""
        You are in a dark room.
        There is a door to your right and left
        Which one do you take?
    """)
    choice = input("> ")

    if choice == "left":
        bear_room()
    elif choice == "right":
        cthulhu_room()
    else:
        dead("You stumble around the room until you starve.")

start()