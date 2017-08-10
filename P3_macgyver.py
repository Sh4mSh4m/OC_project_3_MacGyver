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
    def generate(self, map_df):
        is_ok = False
        while is_ok == False:
            x_item = rd.randint(1, 13)
            y_item = rd.randint(1, 13)
            if map_df[x_item][y_item] in "o":
                print(map_df[x_item][y_item])
                self.position = [x_item, y_item]
                return is_ok == True


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
        self.position = [starting_position[0], starting_position[1]]
        self.item_list = []

    def move(self, map_df):
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
        As long as the player doesn't hit the exit, we keep moving
        """
        end_game = False
        while end_game == False:
            move = input()
            if move.lower() == "j":
                if map_df[self.position[0]][self.position[1] - 1] in "os":
                    self.position[1] -= 1
                    print(self.position) # print for test puposes
                elif map_df[self.position[0]][self.position[1] - 1] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")
            elif move.lower() == "k":
                if map_df[self.position[0] - 1][self.position[1]] in "os":
                    self.position[0] -= 1
                    print(self.position)
                elif map_df[self.position[0] - 1][self.position[1]] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")
            elif move.lower() == "l":
                if map_df[self.position[0]][self.position[1] + 1] in "os":
                    self.position[1] += 1
                    print(self.position)
                elif map_df[self.position[0]][self.position[1] + 1] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")
            elif move.lower() == "m":
                if map_df[self.position[0] + 1][self.position[1]] in "os":
                    self.position[0] += 1
                    print(self.position)
                elif map_df[self.position[0] + 1][self.position[1]] in "z":
                    return end_game == True
                else:
                    print("this is a wall, try again")


###################
###    Main    ####
###################


def main():

    """
    Creating a dataframe from the CSV file
    """
    print("Game board loading...")
    game_board_df = pd.read_csv("data/maze1.csv", header=None, delim_whitespace=True)
    print(game_board_df)
    """
    Random distribution of items
    We modify the map i don't really need objects item.
    """
    item_1 = Item("1")
    item_2 = Item("2")
    item_3 = Item("3")
    print(item_1.name)
    item_1.generate(game_board_df)
    item_2.generate(game_board_df)
    item_3.generate(game_board_df)
    print("item_1 est à la position {}".format(item_1.position))
    print("item_2 est à la position {}".format(item_2.position))
    print("item_3 est à la position {}".format(item_3.position))
        # must update the game_board_df so following items don't overlap
    # Warning : set_value takes row before col !
    game_board_df.set_value(item_1.position[1], item_1.position[0], item_1.name)
    game_board_df.set_value(item_2.position[1], item_2.position[0], item_2.name)
    game_board_df.set_value(item_3.position[1], item_3.position[0], item_3.name)
    print(game_board_df)

    """
    List comprehension allowing to perform loops nested and run through all
    entries of the dataframe
    The following is most likely for display purposes. We create the objects.
    We initialize every case of the game board.
    And if the specification of the case is "s" or "z" we initialize the 
    player and the exit
    """
    for x, y in [(x,y) for x in range(15) for y in range(15)]:
        if game_board_df[x][y] == "s":
            player = MacGyver((x, y))
            # We should store each object in a list to represent the boardgame
            game_board_case = Case((x,y), game_board_df[x][y])
        else:
            # We should store each object in a list to represent the boardgame
            game_board_case = Case((x,y), game_board_df[x][y])
        #print("La case {} a pour specification {}".format(game_board_case.coordinates, game_board_case.specification))
    print("Ready to play !!!")
    """
    Let's play, player moves until he finds the exit
    """
    # player.move(game_board_df)
    # print("You've finished the game ! Congratulations")

if __name__ == "__main__":
    main()