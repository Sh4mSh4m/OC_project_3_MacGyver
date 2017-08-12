OpenClassrooms project 3 for the Python developper course
Using Python 3.6.2, virtualenv and pylint

###########################
##  Project description  ##
###########################

Project aims to deliver a game coded in Python 3 using skills and tools learned with OpenClassrooms courses.
The theme is MacGyver lost in a maze from which he must exit collecting items to build a tranquilizer gun to pass the guard at the exit of the maze.

###########################
# Objectives and Features #
###########################

There is only one level. The structure of the maze (entrance, walls, exit) must be recorderd in a separate file to easily modify it if needed.

MacGyver is controlled with arrows keys.

Items required for exiting the maze are randomly distributed in the maze and must be reshuffled if the user leaves the game and launches the game again.

The game window will be a 15 sprites large square area.

MacGyver moves from case to case. moving onto an object makes him collect the item.

The program stops only when MacGyver has recovered all 3 items and found the exit. If he shows up to the exit without all three items : game over.

Program is standalone and can be executed on any computer.re exécuté sur n'importe quel ordinateur.


Steps

1 - Create initial frame

Start a Git rep and send it on Github.

Start building up the maze without the GUI. When the algorithm behind your maze is done, use the PyGame module to draw the GUI.

Then think about the 3 main game components : the guardian, MacGyver and the items. How can you represent them in the program. How are they distributed at the beginning of the game ?

2 - Animate main character

The only moving part is MacGyver. Create class methods to allow him moving and finding the exit.
For now, build a simplified version of the game where MacGyver wins when reaching the guard no matter what
 
3 - Collect items

Add items management. How does MacGyver collect them ? Add a counter that lists them
 
4 - Win !

Finally, change the end game : MacGyver only wins when he collected all the items and tranquilized the guard. Otherwise he looses

Deliverables

Code hosted on Github
Document explaining the way you coded and including the link to your source code (Github).
Explain the choices for the algorithm and focus on difficulties encountered and solutions found.
Document should be a pdf file and should not exceed 2 A4 pages.
 
Requirements

You will version your code using Git and publish on Github so your mentor can comment it.
You will respect PEP8 guidelines and code in a virtual environment using Python3.
Your code will be written in English (var, comments and functions).
