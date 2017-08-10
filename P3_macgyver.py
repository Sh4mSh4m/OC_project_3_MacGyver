#! /usr/bin/env python3
# coding: utf-8


import pandas as pd
import random as rd

###################
###  Classes   ####
###################


class Case:
    """
    Main class that defines case objects for the maze.
    Each case is identified with its coordinates.
    Each case is either a corridor or a wall.
    """
    def __init__(self, coordinates_init, characteristic):
        self.coordinates = coordinates_init
        self.characteristic = characteristic

class Item:
    ITEM_INDEX = {
        str(1): "Seringue",
        str(2): "Anestésiant",
        str(3): "Pistolet"
    }        

class MacGyver:
    """
    Special class that defines the player on the maze
    MacGyver is an object with methods that will 
    allow it to :
        - play the game (i.e. move from case to case and assess
          whether he reached the exit or not)
        - scan the case he is about to go to
        - collect items
        - assess if the guard (and therefore the exit) 
    """
    
    def __init__(self, starting_position):
        # player coordinates are type list to modify position during the game
        self.loc = [starting_position[0], starting_position[1]]
        # initiating his list of items to collect
        self.item_list = []

    # Returns what the intended next case for the move (based on input) is
    # nx and ny correspond to the next move input for axis and ordinate
    def looks_up_next_case(self, nx, ny, map_df):
        return map_df[self.loc[0] + nx][self.loc[1] + ny ]

    # Updates the player's position
    def moves(self, nx, ny):
        self.loc[0] += nx
        self.loc[1] += ny
        print(self.loc)

    """
    Calls the moves method, updates the player's item list with item found
    Updates the map dataframe to remove the item location and turns it into
    a regular corridor case
    """
    def collects_item(self, nx, ny, map_df):
        self.moves(nx,ny)
        # After moving, player's position the item's are the same
        item_collected = map_df[self.loc[0]][self.loc[1]]
        # We update the player item_list
        self.item_list.append(item_collected)
        print("item {} has been collected !".format(item_collected))
        # WARNING : here, row index / ordinate is called before column / axis
        # the map_df is updated and we replace the case as a corridor case
        map_df.set_value(self.loc[1], self.loc[0], "o")
        print(map_df)

    """
    The function takes the dataframe as input to read map, which is the
    game board dataframe
        - if the next case from current position is "o" or "s",
          we move to the next case
        - if the next case is one of the 3 items "1", "2" or "3",
          we collect the item (and move to it with same method) 
        - if the next case is the exit, this is the end game and the 
          end of the method
        - otherwise, it's a wall, player gets a notification (or should
          be an exception raised) and we stay on same position 
          waiting for another input
    Simpler version with inputs as follow :
        - "j" to go up 
        - "k" to go left 
        - "l" to go down
        - "m" to go right
    """
    def plays(self, map_df):
        end_game = False
        while end_game == False:
            move = input()
            # the following specifies each move based on input
            if move.lower() == "j":
                nx = 0
                ny = -1
            elif move.lower() == "k":
                nx = -1
                ny = 0
            elif move.lower() == "l":
                nx = 0
                ny = +1
            elif move.lower() == "m":
                nx = +1
                ny = 0
            else:
                nx = 0 
                ny = 0
            # Identifies what the next intended case is
            ncase = self.looks_up_next_case(nx, ny, map_df)
            # Based on what the next case is, we call different actions
            if ncase in "os":
                self.moves(nx, ny)
            elif ncase in str(123):
                # collecting the item will also move player's position
                self.collects_item(nx, ny, map_df)
            elif ncase in "z":
                # Exit is found, we exit the plays method
                return end_game == True
            else:
                # It has to be a wall, so we do nothing
                print("This is a wall")


####################
## Game functions ##
####################

def game_board_building():
    """
    Creating a dataframe from the CSV file which contains the initial maze map
    On the map "x" is a wall, "o" a corridor, "s" the starting point and "z" 
    the exit
    The function returns a dataframe object we call map_df
    """
    print("Game board loading...")
    # Currently, the maze is modified with items already registered
    # going only up, enables to test items collection
    # other directions enables to test walls and regular moves
    map_df = pd.read_csv("data/maze1.csv", header=None, delim_whitespace=True)
    return map_df    

def generate_items_in(map_df):
    """
    Random distribution of items
    Function takes the map and returns map with items randomly 
    distributed on valid positions
    """
    for i in range(1, 4):
        x_item = rd.randint(1, 13)
        y_item = rd.randint(1, 13)
        # Reshuffle until we land on a corridor position
        while map_df[x_item][y_item] not in "o":
            x_item = rd.randint(1, 13)
            y_item = rd.randint(1, 13)
        else:
            # Warning, set_value first selects ordinate then axit
            # We update the map_df with item index
            map_df.set_value(y_item, x_item, str(i))
            print(x_item, y_item)
    return map_df


###################
###    Main    ####
###################


def main():
    
    # We initialize the dataframe map that contains the maze information
    map_df = game_board_building()
    map_df = generate_items_in(map_df)
    print(map_df)
    
    """
    List comprehension allowing to perform loops nested and run through all
    entries of the dataframe
    The following is most likely for display purposes. We create the objects.
    We initialize every case of the game board.
    And if the specification of the case is "s" or "z" (currently z is regular
    case
    """
    for x, y in [(x,y) for x in range(15) for y in range(15)]:
        if map_df[x][y] == "s":
            player = MacGyver((x, y))
            # We should store each object in a list to represent the boardgame
            game_board_case = Case((x,y), map_df[x][y])
        else:
            # We should store each object in a list to represent the boardgame
            game_board_case = Case((x,y), map_df[x][y])
    print("Ready to play !!!, press j to go up, k to go left, l to go down and m to go left")
    # Player moves until he finds the exit
    player.plays(map_df)
    # Assessing how many items were collected before exiting
    tranquilizer_gun = len(player.item_list)
    if tranquilizer_gun < 3:
        # Game over, player dies
        print("You didn't collect all the tranquilizer gun items, the guard killed you")
    else:
        # Game over, player wins
        print("You've finished the game ! Congratulations")


if __name__ == "__main__":
    main()