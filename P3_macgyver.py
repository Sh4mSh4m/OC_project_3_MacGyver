#! /usr/bin/env python3
# coding: utf-8


import pandas as pd
import random as rd
import pygame as pyg
from pygame.locals import *
import pdb

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

    def displays_gb(self, window, g_border_x, g_border_y):
        if self.characteristic in "so123":
            game_board_img = pyg.image.load("img/floor.png").convert()
        elif self.characteristic == "z":
            game_board_img = pyg.image.load("img/guard.png").convert()
        else:
            game_board_img = pyg.image.load("img/wall.png").convert()
        window.blit(game_board_img, (self.coordinates[0] * 40 + g_border_x, \
                                  self.coordinates[1] * 40 + g_border_y))
        pyg.display.flip()


class Item(Case):

    def __init__(self, coordinates_init, characteristic):
        super().__init__(coordinates_init, characteristic)

    def displays_gb(self, window, g_border_x, g_border_y):
        if self.characteristic in "1":
            game_board_img = pyg.image.load("img/seringue.png").convert_alpha()            
        elif self.characteristic in "2":
            game_board_img = pyg.image.load("img/anesthesiant.png").convert_alpha()            
        elif self.characteristic in "3":
            game_board_img = pyg.image.load("img/tranq_gun.png").convert_alpha()            
        window.blit(game_board_img, (self.coordinates[0] * 40 + g_border_x, \
                                  self.coordinates[1] * 40 + g_border_y))
        pyg.display.flip()

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
    
    # Manages player sprite on graphic interface
    def appears(self, window, g_border_x, g_border_y):
        player_img = pyg.image.load("img/player.png").convert_alpha()
        player_mov = player_img.get_rect()
        # player sprite moved to initial position
        player_mov = player_mov.move(self.loc[0] * 40 + g_border_x, self.loc[1] * 40 + g_border_y)
        # window.blit(player_img, player_mov)
        pyg.display.flip()
        return player_img, player_mov

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
    def plays(self, map_df,  g_border_x, g_border_y, window, player_img, player_mov):
        end_game = False
        while end_game == False:
            for event in pyg.event.get():
                # the following specifies each move based on input
                if event.type == KEYDOWN and event.key == K_UP:
                    nx = 0
                    ny = -1
                elif event.type == KEYDOWN and event.key == K_LEFT:
                    nx = -1
                    ny = 0
                elif event.type == KEYDOWN and event.key == K_DOWN:
                    nx = 0
                    ny = +1
                elif event.type == KEYDOWN and event.key == K_RIGHT:
                    nx = +1
                    ny = 0
                elif event.type == QUIT or \
                    event.type == KEYDOWN and event.key == K_ESCAPE:
                    end_game = True
                    return main_switch == True
                else:
                    nx = 0 
                    ny = 0
                # Identifies what the next intended case is
                ncase = self.looks_up_next_case(nx, ny, map_df)
                # Based on what the next case is, we call different actions
                if ncase in "os":
                    player_img, player_mov = self.moves(nx, ny, g_border_x, g_border_y, window, player_img, player_mov)
                elif ncase in str(123):
                    # collecting the item will also move player's position
                    player_img, player_mov = self.collects_item(nx, ny, g_border_x, g_border_y, map_df, window, player_img, player_mov)
                elif ncase in "z":
                    # Exit is found, we exit the plays method
                    end_game = True
                else:
                    # It has to be a wall, so we do nothing
                    print("This is a wall")

    # Returns what the intended next case for the move (based on input) is
    # nx and ny correspond to the next move input for axis and ordinate
    def looks_up_next_case(self, nx, ny, map_df):
        return map_df[self.loc[0] + nx][self.loc[1] + ny ]

    # Updates the player's position, updates the sprite position
    def moves(self, nx, ny, g_border_x, g_border_y, window, player_img, player_mov):
        game_board_img = pyg.image.load("img/floor.png").convert()
        window.blit(game_board_img, (self.loc[0] * 40 + g_border_x, \
                                  self.loc[1] * 40 + g_border_y))
        self.loc[0] += nx
        self.loc[1] += ny
        print(self.loc)
        player_mov = player_mov.move(nx * 40, ny * 40)
        window.blit(player_img, player_mov)
        pyg.display.flip()
        return player_img, player_mov

    """
    Calls the moves method, updates the player's item list with item found
    Updates the map dataframe to remove the item location and turns it into
    a regular corridor case
    """
    def collects_item(self, nx, ny, g_border_x, g_border_y, map_df, window, player_img, player_mov):
        player_img, player_mov = self.moves(nx, ny, g_border_x, g_border_y, window, player_img, player_mov)
        # After moving, player's position the item's are the same
        item_collected = map_df[self.loc[0]][self.loc[1]]
        # We update the player item_list
        self.item_list.append(item_collected)
        print("item {} has been collected !".format(item_collected))
        # WARNING : here, row index / ordinate is called before column / axis
        # the map_df is updated and we replace the case as a corridor case
        map_df.set_value(self.loc[1], self.loc[0], "o")
        print(map_df)
        return player_img, player_mov

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
    
    # Initializing pygame module
    pyg.init()
    window = pyg.display.set_mode((800,700))
    
    # Starting loop for Display which is on, as long as game is on going
    main_switch = False

    while main_switch == False:
        # loads and convert the picture
        background_img = pyg.image.load("img/background.jpg").convert()
        # sticks "background" on the window
        window.blit(background_img,(0,0))
        # window refreshes with the following to actually display the image
        pyg.display.flip()
        # each sprite is 40 pixels wide and we start away from border
        g_border_x = 150
        g_border_y = 90
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
                # We should store each object in a list to represent the boardgame
                game_board_case = Case((x,y), map_df[x][y])
                game_board_case.displays_gb(window, g_border_x, g_border_y)
                # Player is displayed on top of corridor, so created after
                player = MacGyver((x, y))
                # MacGyver's displays method must return both objects to be used later
                player_img, player_mov = player.appears(window, g_border_x, g_border_y)
            elif map_df[x][y] in str(123):
                game_board_case = Case((x,y), map_df[x][y])
                game_board_case.displays_gb(window, g_border_x, g_border_y)
                item = Item((x,y), map_df[x][y])
                item.displays_gb(window, g_border_x, g_border_y)
            else:
                # We should store each object in a list to represent the boardgame
                game_board_case = Case((x,y), map_df[x][y])
                game_board_case.displays_gb(window, g_border_x, g_border_y)
        print("Ready to play !!!")
        # Player moves until he finds the exit (second loop in the game)
        player.plays(map_df, g_border_x, g_border_y, window, player_img, player_mov)
        # Assessing how many items were collected before exiting
        tranquilizer_gun = len(player.item_list)
        if tranquilizer_gun < 3:
            # Game over, player dies
            print("You didn't collect all the tranquilizer gun items, the guard killed you")
        else:
            # Game over, player wins
            print("You've finished the game ! Congratulations, press Q to quit")
            main_switch = True

if __name__ == "__main__":
    main()