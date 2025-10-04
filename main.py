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
    "coin": 0
}

# List of random events
events = ["find a coin", "meet a monster", "do nothing"]

# Randomly choose one event
event = random.choice(events)
print(f"While exploring, you {event}!")

# Update player stats based on the event
if event == "find a coin":
    player["coin"] += 1
    print(f"{player['name']} found a coin, {player['name']} now has {player['coin']} coins.")
elif event == "meet a monster":
    player["health"] -= 10
    print(f"{player['name']} got hurt during the combat with monster, health is now {player['health']}.")
else:
    print("Nothing happened this time.")
