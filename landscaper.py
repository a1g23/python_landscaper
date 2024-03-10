## player dictionary

player_status = {
    'money': 0,
    'tool': 0,
    'chargeable': 0
}

## tool List

tool_list = [
    {'name': 'teeth', 'chargeable': 1, 'price': 0},
    {'name': 'rusty scissors', 'chargeable': 5, 'price': 5},
    {'name': 'old-time push lawnmower', 'chargeable': 50, 'price': 25},
    {'name': 'fancy lawnmower', 'chargeable': 100, 'price': 250},
    {'name': 'student team', 'chargeable': 250, 'price': 500}
]

## a player can give input to cut grass, upgrade a tool, or quit the game

def get_input():
    player_input = input("do you want to cut grass, upgrade a tool, or quit the game?")
    if(player_input == "cut"):
        print("player wants to cut")
    elif(player_input == "upgrade"):
        print("player wants to upgrade")
    elif(player_input == "quit"):
        print("player wants to quit")
    else:
        print("player needs to type cut, upgrade or quit to proceed!")

get_input()

## a player can cut the grass and make


    
