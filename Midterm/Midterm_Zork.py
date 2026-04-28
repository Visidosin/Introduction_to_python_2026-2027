import random

# This is where I assign doors and rooms to specific colours and where exit is

rooms = {
    "Yellow": {"north": "Blue", "south": "Red"},
    "Red": {"north": "Yellow", "west": "Green"},
    "Green": {"east": "Red", "south": "Exit"},
    "Blue": {"south": "Yellow", "west": "White"},
    "White": {"east": "Blue"},
}

# This is where implemented random plays the big role with connecting rooms with keys like exit, talk with dragon if you get the riddle and boxes to open

room_names = list(rooms.keys())

player_room = random.choice(room_names)
has_key = False
exit_unlocked = False

box_rooms = random.sample(room_names, 2)
gold_box_room = box_rooms[0]
silver_box_room = box_rooms[1]

key_in_gold = random.choice([True, False])

dragon_room = random.choice(room_names)
dragon_answered = False
dragon_helped = False

# Now series of if-statements according to the place and actionsA

def describe_room():
    print(f"\nYou are in the {player_room} room.")

# I wrote commands here that are supposed to be written in order for you to move and do specific actions in the rooms for clarity

    print("Type commands like: 'go north', 'go south', 'open gold', 'talk', 'unlock', 'exit'")

# If-statement for exit room and how to get out

    exits = rooms.get(player_room, {})
    for direction in exits:
        if exits[direction] == "Exit":
            print(f"There is an EXIT to the {direction.upper()} (locked).")
        else:
            print(f"There is a door {direction}.")

# Boxes with possibly a key and a dragon 

    if player_room == gold_box_room:
        print("There is a Gold box here")
    if player_room == silver_box_room:
        print("There is a Silver box here")

    if player_room == dragon_room:
        print("There is a dragon here")

# Defined functions for each statement

def move(direction):
    global player_room
    if direction in rooms[player_room]:
        player_room = rooms[player_room][direction]
        if player_room == "Exit":
            attempt_exit()
        else:
            describe_room()
    else:
        print("You can't go that way.")

def attempt_exit():
    global exit_unlocked
    if exit_unlocked:
        print("You escaped!")
        exit()
    else:
        print("The EXIT is locked")

def open_box(box):
    global has_key

    if box == "gold" and player_room == gold_box_room:
        print("You opened the Gold box")
        if key_in_gold:
            print("You found the key!")
            has_key = True
        else:
            print("Nothing inside")
    elif box == "silver" and player_room == silver_box_room:
        print("You opened the Silver box.")
        if not key_in_gold:
            print("You found the key!")
            has_key = True
        else:
            print("Nothing inside")
    else:
        print("No such box here")

def talk_dragon():
    global dragon_answered, dragon_helped

    if player_room != dragon_room:
        print("No dragon here")
        return

    if dragon_helped:
        print("Dragon already told you the answer.")
        return

    if not dragon_answered:
        print("Dragon asks: What has to be broken before you can use it?")
        answer = input("Your answer: ").lower()

        if "egg" in answer:
            print("Correct!")
            dragon_helped = True
            if key_in_gold:
                print("The key is in the GOLD box.")
            else:
                print("The key is in the SILVER box.")
        else:
            print("Wrong! Dragon will not help anymore.")
            dragon_answered = True

def unlock_exit():
    global exit_unlocked
    if player_room == "Green" and has_key:
        exit_unlocked = True
        print("The EXIT is now unlocked!")
    else:
        print("You can't unlock it.")

# Game loop for actions and movement

print("Welcome to ZORK (simplified)!")
describe_room()

while True:
    command = input("\n> ").lower().split()

    if len(command) == 0:
        continue

    if command[0] == "go" and len(command) > 1:
        move(command[1])

    elif command[0] == "open" and len(command) > 1:
        open_box(command[1])

    elif command[0] == "talk":
        talk_dragon()

    elif command[0] == "unlock":
        unlock_exit()

    elif command[0] == "exit":
        attempt_exit()

    else:
        print("Unknown command.")