## player dictionary

player_status = {
    'money': 0,
    'tool': 0
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
        cut_grass()
        print( f"you have ${player_status['money']} and cutting with a {player_status['tool']}")
    elif(player_input == "upgrade"):
        upgrade_tool()
        print( f"you upgraded to {player_status['tool']}")
    elif(player_input == "quit"):
        quit()
    else:
        print("player needs to type cut, upgrade or quit to proceed!")



## a player can cut the grass and make money dependent on the tool they have. the player_status should update their money only in this case

def cut_grass():
    current_tool_ind = player_status['tool']
    #print(current_tool_ind)
    tool_now = tool_list[current_tool_ind]
    #print(tool_now)
    service_charge = tool_now['chargeable']
    #print(service_charge)
    player_status['money'] += service_charge
    return player_status


## a player can upgrade their cutting method. the player_status should update their tool only in this case

def upgrade_tool():
    player_status['tool'] += 1
    return player_status



## a player should be able to quit the game. print "the game ended"

def quit():
    print("better luck next time, mate")

## a player can win the game if money is over 1000 and tool is at index 4 (student_team)

def win():
    print("you won becasue you have more than 1000 dollars and cutting with a student team")
        

## start the game. run the input function, then runt the win function to double check if it should keep going
def start_game():
    while(player_status['tool'] <= 4 and player_status['money'] <= 1000):
        get_input()
    win()

start_game()









    
