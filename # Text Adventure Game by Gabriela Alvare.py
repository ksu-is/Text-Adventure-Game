# Text Adventure Game by Gabriela Alvarez

def show_instructions():
    print("""
Adventure Game
==============
Commands: go [north/south/east/west], get [item], use [item], exit
""")

def show_status():
    print("---------------------------")
    print("You are in the", current_room)
    print("Inventory:", inventory)
    if "item" in rooms[current_room]:
        print("You see a", rooms[current_room]["item"])
    print("---------------------------")

# Define rooms and connections
rooms = {
    "Forest": {
        "north": "River",
        "east": "Cave",
        "text": "You are in a dark forest. Paths lead north and east."
    },
    "River": {
        "south": "Forest",
        "text": "You stand beside a rushing river. There is a small boat here.",
        "item": "boat"
    },
    "Cave": {
        "west": "Forest",
        "text": "You are in a damp cave. You see glittering gold on the ground.",
        "item": "gold"
    }
}

# start player in the Forest
current_room = "Forest"
inventory = []

show_instructions()

while True:
    show_status()
    print(rooms[current_room]["text"])
    move = input("> ").lower().split()

    if len(move) == 0:
        print("Empty input not allowed.")
        continue

    if move[0] == "go":
        direction = move[1] if len(move) > 1 else ""
        if direction in rooms[current_room]:
            current_room = rooms[current_room][direction]
        else:
            print("You can't go that way.")

    elif move[0] == "get":
        item = move[1] if len(move) > 1 else ""
        if "item" in rooms[current_room] and item == rooms[current_room]["item"]:
            inventory.append(item)
            print(f"You picked up the {item}!")
            del rooms[current_room]["item"]
        else:
            print("You can't get that.")

    # 🆕 NEW: add command for using the boat
    elif move[0] == "use":
        item = move[1] if len(move) > 1 else ""
        if item == "boat" and "boat" in inventory and current_room == "River":
            print("You get into the boat and sail across the river... You win! 🏆")
            break
        else:
            print("You can't use that here.")

    elif move[0] == "exit":
        print("Thanks for playing!")
        break

    else:
        print("Invalid command.")

    # Winning condition if you have both items
    if "gold" in inventory and "boat" in inventory:
        print("\nYou sail away with your gold — you win! 🏆")
        break


