import random

game_name = "Escaping"  

# Greeting with aligned equal signs using f-string
print(f"Welcome to {game_name}!")
print("=" * (len(game_name) + 15))

# Ask for the character's name
print("Before we begin, what is your character's name?")
name = input("> ")

# Print the personalized greeting using f-string
print(f"Great, {name}! Let's begin the adventure!")

# Dictionary for player stats
player = {
    "name": name,
    "health": 100,
    "coin": 0,
    "x": 0,
    "y": 0
}



# List of random events
events = ["find a coin", "meet a monster", "do nothing"]
map_size = 9

def check_event():
    """Randomly choose and handle an event."""
    global player
    event = random.choice(events)
    print(f"While exploring, you {event}!")

    if event == "find a coin":
        player["coin"] += 1
        print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
    elif event == "meet a monster":
        player["health"] -= 10
        print(f"{player['name']} got hurt during the combat with a monster, health is now {player['health']}.")
    else:
        print("Nothing happened this time.")
def draw_ui(x, y):
    print("=========================")
    for i in range(map_size):
        for j in range(map_size):
            if i == y and j == x:
                print("C", end="  ")
            elif i == map_size - 1 and j == map_size - 1:
                print("M", end="  ")
            else:
                print(".", end="  ")
        print()
    print("=========================")
    print(f"Health: {player['health']}")
    print("-------------------------")
    print(f"Coin: {player['coin']}")
    print("=========================")
def move(direction):
    """Move the character in the specified direction."""
    global player
    if direction == "w" and player["y"] > 0:
        player["y"] -= 1
    elif direction == "s" and player["y"] < map_size - 1:
        player["y"] += 1
    elif direction == "a" and player["x"] > 0:
        player["x"] -= 1
    elif direction == "d" and player["x"] < map_size - 1:
        player["x"] += 1
    else:
        print("You can't move in that direction!")
def main():
    draw_ui(player["x"], player["y"])
    direction = input("Your next move (w/a/s/d/q): ")

    while direction != "q":
        move(direction)

        # Reached the gate
        if player["x"] == map_size - 1 and player["y"] == map_size - 1:
            print("Congratulations! You reached the gate for the next level.")
            break

        check_event()
        draw_ui(player["x"], player["y"])
        direction = input("Your next move (w/a/s/d/q): ")

# --- Start the game ---
if __name__ == "__main__":
    main()