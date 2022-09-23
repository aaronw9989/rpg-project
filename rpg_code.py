#!/usr/bin/python3

""" Project II - RPG Game """


# main function of our program
def main():

    def showInstructions():
        # print a main menu and the commands
        print('''
    RPG Game
    ========
    Commands:
      go [direction]
      get [item]
    ''')


    def showStatus():
        # print the player's current status
        print('---------------------------')
        print('You are in the ' + currentRoom)
        # print the current inventory
        print('Inventory : ' + str(inventory))
        # print an item if there is one
        if "item" in rooms[currentRoom]:
            print('You see a ' + rooms[currentRoom]['item'])
        print("---------------------------")

        # print out available moves to player
        print('Moves available : ')
        if 'north' in rooms[currentRoom]:
            print('north')
        if 'south' in rooms[currentRoom]:
            print('south')
        if 'east' in rooms[currentRoom]:
            print('east')
        if 'west' in rooms[currentRoom]:
            print('west')
        print("---------------------------")


    """ Get the user move from the command line """
    def user_move():
        # get the player's next 'move'
        # .split() breaks it up into an list array
        # eg typing 'go east' would give the list:
        # ['go','east']
        move = ''
        while move == '':
            move = input('>')

        # split allows an items to have a space on them
        # get golden key is returned ["get", "golden key"]
        move = move.lower().split(" ", 1)

        return move


    """ This function print out a list of available rooms and returns
        the name of the desired location the user want to teleport to """
    def teleport():
        # print out all available rooms
        print("(a) Secret Room"
              "\n(b) Panic Room"
              "\n(c) Closet"
              "\n(d) Master Bedroom"
              "\n(e) Hall"
              "\n(f) Bathroom"
              "\n(g) Kitchen"
              "\n(h) Garage"
              "\n(i) Garden"
              "\n(j) Dining Room"
              "\n(k) Pantry"
              "")
        # map the user input to each room
        room_dict = {"a": "Secret Room",
                     "b": "Panic Room",
                     "c": "Closet",
                     "d": "Master Bedroom",
                     "e": "Hall",
                     "f": "Bathroom",
                     "g": "Kitchen",
                     "h": "Garage",
                     "i": "Garden",
                     "j": "Dining Room",
                     "k": "Pantry",
                     }
        teleport_location = ''
        while teleport_location == '':
            teleport_location = input('>')
            teleport_location = teleport_location.rstrip().lower()

            # If the user enters an invalid location, then they return to the panic room
            if teleport_location not in room_dict:
                teleport_location = "Panic Room"
            # return when the user will teleport to
            return room_dict[teleport_location]


    """ Banner when user wins the game """
    def game_won():
        # display if user wins the game
        print('  __        _____ _   _ _   _ _____ ____  _ _ _ ')
        print('  \ \      / /_ _| \ | | \ | | ____|  _ \| | | |')
        print('   \ \ /\ / / | ||  \| |  \| |  _| | |_) | | | |')
        print('    \ V  V /  | || |\  | |\  | |___|  _ <|_|_|_|')
        print('     \_/\_/  |___|_| \_|_| \_|_____|_| \_(_|_|_)')

    """ Game over banner """
    def game_over():
        # display game over
        print('   ____    _    __  __ _____    _____     _______ ____  ')
        print('   / ___|  / \  |  \/  | ____|  / _ \ \   / / ____|  _ \ ')
        print('  | |  _  / _ \ | |\/| |  _|   | | | \ \ / /|  _| | |_) | ')
        print('  | |_| |/ ___ \| |  | | |___  | |_| |\ V / | |___|  _ < ')
        print('   \____/_/   \_\_|  |_|_____|  \___/  \_/  |_____|_| \_\ ')


    # an inventory, which is initially empty
    inventory = []

    # a dictionary linking a room to other rooms
    # A dictionary linking a room to other rooms
    rooms = {

        'Master Bedroom': {
            'south': 'Hall',
            'west': 'Closet',
        },
        'Closet': {
            'east': 'Master Bedroom',
            'north': 'Panic Room',
        },
        'Panic Room': {
            'south': 'Closet',
        },
        'Hall': {
            'south': 'Kitchen',
            'east': 'Dining Room',
            'west': 'Bathroom',
            'north': 'Master Bedroom',
            'item': 'key'
        },
        'Kitchen': {
            'north': 'Hall',
            'item': 'monster',
            'south': 'Garage',
        },
        'Garage': {
            'north': 'kitchen',
        },
        'Dining Room': {
            'west': 'Hall',
            'south': 'Garden',
            'item': 'potion',
            'north': 'Pantry',
        },
        'Bathroom': {
            'east': 'Hall'
        },
        'Garden': {
            'north': 'Dining Room'
        },
        'Pantry': {
            'south': 'Dining Room',
            'north': 'Secret Room',
            'item': 'cookie',
        },
        'Secret Room': {
            'south': 'Pantry',
        },
        'Teleport Tunnel': {

        },
    }

    # start the player in the Hall
    currentRoom = 'Hall'

    showInstructions()

    # loop forever
    while True:

        showStatus()

        # grab the user move from the command line
        move = user_move()

        # if they type 'go' first
        if move[0] == 'go':
            # check that they are allowed wherever they want to go
            if move[1] in rooms[currentRoom]:
                # set the current room to the new room
                currentRoom = rooms[currentRoom][move[1]]
            # if the move west in the secret room it opens a teleport tunnel
            # this takes them to anywhere they want to be
            elif currentRoom == 'Panic Room' and move[1] == 'east':
                print("You have entered the teleportation tunnel. Select any room you would like to teleport to.")
                # returns the room the user want to teleport to
                currentRoom = teleport()
            # there is no door (link) to the new room
            else:
                print('You can\'t go that way!')

        # if they type 'get' first
        if move[0] == 'get':
            # if the room contains an item, and the item is the one they want to get
            if "item" in rooms[currentRoom] and move[1] in rooms[currentRoom]['item']:
                # add the item to their inventory
                inventory += [move[1]]
                # display a helpful message
                print(move[1] + ' got!')
                # delete the item from the room
                del rooms[currentRoom]['item']
            # otherwise, if the item isn't there to get
            else:
                # tell them they can't get it
                print('Can\'t get ' + move[1] + '!')


        # Define how a player can win
        if currentRoom == 'Garden' and 'key' in inventory and 'potion' in inventory:
            print('You escaped the house with the ultra rare key and magic potion... YOU WIN!')
            game_won()
            break


        # If a player enters a room with a monster
        elif 'item' in rooms[currentRoom] and 'monster' in rooms[currentRoom]['item']:
            # Alternate ending
            # Player can win by feeding a poison cookie to the monster
            if 'cookie' in inventory:
                print('A monster lunges at you, thinking quickly, you toss a cookie at the monster.')
                print('The monster accepts the cookie and explains he only wanted to eat you because he was hungry...')
                print('The monster eats the cookie in peace, smiling from ear to ear.')
                print('Monster: \"You are the first person to be kind to be, perhaps we could be frien..\"')
                print('The monster dies from eating a poison cookie. Mission Accomplished... YOU WIN!')
                game_won()
                break
            else:
                print('A monster has got you... GAME OVER!')
                game_over()
                break


# call our main function
if __name__ == "__main__":
    main()