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
    A case can also be an item.
    A case can also contain the exit.
    A case can also contain the starting point for 
    MacGyver.
    """

    """ Object initialization with info extracted from the
    dataframe """
    def __init__(self, coordinates_init, specification):
        self.coordinates = coordinates_init
        self.specification = specification

        
class Item:
    """
    Class of object that creates itself depending on the map
    """
    def __init__(self, name):
        self.name = name
        self.position = []

    # Function that returns tuple of valid coordinates for item



class MacGyver:
    """
    Special class that defines the player on the maze
    MacGyver is an object with methods that will 
    allow it to :
      - scan the position where he is at, looking for
        items to collect
      - assess if the guard (and therefore the exit) is
      - move to another case in the maze 
    """
    
    def __init__(self, starting_position):
        # player coordinates are type list to modify position in the game
        self.loc = [starting_position[0], starting_position[1]]
        self.item_list = []

    def plays(self, map_df):
        """
        The function takes the dataframe as input to read map, which is the
        game board dataframe
            - if the next case on map is "o" or "s", we move
            - else prints that this is a wall and we don't move
        Simpler version with inputs as follow :
            - "j" to go up 
            - "k" to go left 
            - "l" to go down
            - "m" to go right
        We compare player's position to the map intended move
        As long as the player doesn't hit the exit, we keep playing
        """
        end_game = False
        while end_game == False:
            move = input()
            # we set those variable for readibility 
            col = self.loc[0]
            row = self.loc[1]
            if move.lower() == "j":
                """
                If the next case is a corridor or starting point:
                  - we update the position
                """
                if map_df[col][row - 1] in "os":
                    self.loc[1] -= 1
                    print(self.loc)
                elif map_df[col][row - 1] in str(123):
                    self.loc[1] -= 1
                    print(self.loc)
                    self.item_list.append(map_df[col][row - 1])
                    print(self.item_list)
                    map_df.set_value(row - 1, col, "o")
                    print(map_df)
                elif map_df[col][row - 1] in "z":
                    return end_game == True
                else:
                    print("This is a wall, try agin")
            elif move.lower() == "k":
                if map_df[col - 1][row] in "os":
                    self.loc[0] -= 1
                    print(self.loc)
                elif map_df[col - 1][row] in str(123):
                    self.loc[0] -= 1
                    print(self.loc)
                    self.item_list.append(map_df[col - 1][row])
                    print(self.item_list)
                    map_df.set_value(row, col - 1, "o")
                    print(map_df)
                elif map_df[col - 1][row] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")
            elif move.lower() == "l":
                if map_df[col][row + 1] in "os":
                    self.loc[1] += 1
                    print(self.loc)
                elif map_df[col][row + 1] in str(123):
                    self.loc[1] += 1
                    print(self.loc)
                    self.item_list.append(map_df[col][row + 1])
                    print(self.item_list)
                    map_df.set_value(row + 1, col, "o")
                    print(map_df)
                elif map_df[col][row + 1] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")
            elif move.lower() == "m":
                if map_df[col + 1][row] in "os":
                    self.loc[0] += 1
                    print(self.loc)
                elif map_df[col + 1][row] in str(123):
                    self.loc[1] += 1
                    print(self.loc)
                    self.item_list.append(map_df[col + 1][row])
                    print(self.item_list)
                    map_df.set_value(row, col + 1, "o")
                    print(map_df)
                elif map_df[col + 1][row] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")


####################
## Game functions ##
####################

def game_board_building():
    """
    Creating a dataframe from the CSV file
    CSV file contains the map :
    On the map "x" is a wall, "o" a corridor
    "s" the starting point and "z" the exit
    The function returns a dataframe object
    """
    print("Game board loading...")
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
            # Warning, set_value first selects row then col
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
    And if the specification of the case is "s" or "z" we initialize the 
    player and the exit
    """
    for x, y in [(x,y) for x in range(15) for y in range(15)]:
        if map_df[x][y] == "s":
            player = MacGyver((x, y))
            # We should store each object in a list to represent the boardgame
            game_board_case = Case((x,y), map_df[x][y])
        else:
            # We should store each object in a list to represent the boardgame
            game_board_case = Case((x,y), map_df[x][y])
        #print("La case {} a pour specification {}".format(game_board_case.coordinates, game_board_case.specification))
    print("Ready to play !!!, press j to go up, k to go left, l to go down and m to go left")
    """
    Let's play, player moves until he finds the exit
    """
    player.plays(map_df)
    tranquilizer_gun = len(player.item_list)
    if tranquilizer_gun < 3:
        print("You didn't collect all the tranquilizer gun items, the guard killed you")
    else:
        print("You've finished the game ! Congratulations")


if __name__ == "__main__":
    main()