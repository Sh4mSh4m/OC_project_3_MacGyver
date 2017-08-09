#! /usr/bin/env python3
# coding: utf-8


import pandas as pd

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
        self.coordinates = [starting_position[0], starting_position[1]]
        self.item_list = []

    # Method that looks up the case attributes and returns
    
    def scans_the_room():
        pass

    def move(self, df):
        """
        The function takes the dataframe as input to read map:
            - if the next case on map is "o" or "s", we move
            - else prints that this is a wall and we don't move
        Simpler version with inputs as follow :
            - "j" to go up 
            - "k" to go left 
            - "l" to go down
            - "m" to go right
            - "q" to end game
        """
        move = input()
        if move.lower() == "j":
            if df[self.coordinates[0]][self.coordinates[1] - 1] in "os":
                self.coordinates[1] -= 1
                print(self.coordinates)
            else:
                print("this is a wall")
                print(self.coordinates)
        elif move.lower() == "k":
            if df[self.coordinates[0] - 1][self.coordinates[1]] in "os":
                self.coordinates[0] -= 1
                print(self.coordinates)
            else:
                print("this is a wall")
                print(self.coordinates)
        elif move.lower() == "l":
            if df[self.coordinates[0]][self.coordinates[1] + 1] in "os":
                self.coordinates[1] += 1
                print(self.coordinates)
            else:
                print("this is a wall")
                print(self.coordinates)
        elif move.lower() == "m":
            if df[self.coordinates[0] + 1][self.coordinates[1]] in "os":
                self.coordinates[0] += 1
                print(self.coordinates)
            else:
                print("this is a wall")
                print(self.coordinates)

###################
###  Functions ####
###################


def game_board_init():
    """
    Creating a dataframe from the CSV file
    """
    print("Game board loading...")
    game_board_df = pd.read_csv("data/maze1.csv", header=None, delim_whitespace=True)
    # Here I can also place the items and randomly place them and modify the df

    """
    List comprehension allowing to perform loops nested and run through all
    entries of the dataframe
    We initialize every case of the game board.
    And if the specification of the case is "s" or "z" we initialize the 
    player and the exit
    """
    for x, y in [(x,y) for x in range(15) for y in range(15)]:
        if game_board_df[x][y] == "s":
            player = MacGyver((x, y))
            game_board_case = Case((x,y), game_board_df[x][y])
        else:
            game_board_case = Case((x,y), game_board_df[x][y])
        #print("La case {} a pour specification {}".format(game_board_case.coordinates, game_board_case.specification))
    print("Ready to play !!!")
    again = False
    while again == False:
        player.move(game_board_df)


###################
###    Main    ####
###################


def main():
    game_board_init()



if __name__ == "__main__":
    main()