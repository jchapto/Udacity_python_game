
import time
import random
items = []
monster = random.choice(["cracken", "gorgon", "dragon"])


def print_pause(message_to_print):
    print(message_to_print)
    time.sleep(2)


def valid_input(prompt, option1, option2):
    while True:
        response = raw_input(prompt)
        if response == option1:
            break
        elif response == option2:
            break
        else:
            print_pause("Sorry, I don't understand.")
    return response


def field():
    print_pause("Enter 1 to knock on the door of the house.")
    print_pause("Enter 2 to peer into the cave.")
    response = valid_input("Please enter 1 or 2\n", "1", "2")
    if response == "1":
        house()
    elif response == "2":
        cave()


def house():
    print_pause("You approach the door of the house.")
    print_pause("You are about to knock")
    print_pause("When the door opens and out steps a " + monster + "!")
    print_pause("Eep! This is the " + monster + "'s house!")
    print_pause("The " + monster + " attacks you!")
    if "sword" in items:
        print_pause("Would you like to (1) fight or (2) run away?")
    else:
        print_pause("You feel a bit under-prepared for this"
                    "only having a tiny dagger.")
        print_pause("Would you like to (1) fight or (2) run away?")
    response = valid_input("Please enter 1 o 2\n", "1", "2")
    if response == "1":
        fight()
    elif response == "2":
        print_pause("You run back into the field."
                    "Luckily, you don't seem to have been followed.")
        field()


def fight():
    if "sword" in items:
        print_pause("As the " + monster + "moves to attack, you unsheath "
                    "your new sword.")
        print_pause("The Sword of Ogoroth shines brightly in your hand"
                    "as you brace yourself for the attack.")
        print_pause("But the " + monster + "takes one look at your shiny new"
                    "toy and runs away!")
        print_pause("You have rid the town of the " + monster +
                    ". You are victorious!")
        restart()
    else:
        print_pause("You do your best...")
        print_pause("but your dagger is no match for the " + monster)
        print_pause("You have been defeated!")
        restart()


def cave():
    print_pause("You peer cautiously into the cave.")
    if "sword" in items:
        print_pause("You've been here before, and gotten all the good stuff."
                    " It's just an empty cave now.")
        print_pause("You walk back out to the field.")
        field()
    else:
        items.append("sword")
        print_pause("It turns out to be only a very small cave.")
        print_pause("Your eye catches a glint of metal behind a rock.")
        print_pause("You have found the magical Sword of Ogoroth!")
        print_pause("You discard your silly old dagger and take the sword"
                    "with you.")
        print_pause("You walk back out to the field.")
        field()


def restart():
    response = valid_input("Would you like to play again? (y/n)\n", "y", "n")
    if response == "y":
        intro()
    elif response == "n":
        print_pause("Ok goodbye!")


def intro():
    print_pause("You find yourself standing in an open field, "
                "filled with grass and yellow wildflowers.")
    print_pause("Rumor has it that a " + monster + " is somewhere around here,"
                "and has been terrifying the nearby village.")
    print_pause("In front of you is a house.")
    print_pause("To your right is a dark cave.")
    print_pause("In your hand you hold your trusty (but not very effective) "
                "dagger.")
    field()


intro()
