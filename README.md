OpenClassrooms project 3 for the Python developper course

Python 3.6.2

Features

There is only one level. The structure of the maze (entrance, walls, exit) must be recorderd in a separate file to easily modify it if needed.

MacGyver is controlled with arrows keys.

Items required for exiting the maze are randomly distributed in the maze and must be reshuffled if the user leaves the game and launches the game again.

The game window will be a 15 sprites large square area.

MacGyver moves from case to case. moving onto an object makes him collect the item.

The program stops only when MacGyver has recovered all 3 items and found the exit. If he shows up to the exit without all three items : game over.

Program is standalone and can be executed on any computer.re exécuté sur n'importe quel ordinateur.


Steps

1 - Create initial frame

Start a Git rep and send it on Github DONE.

Start building up the maze without the GUI. When the algorithm behind your maze is done, use the PyGame module to draw the GUI.

Then think about the 3 main game components : the guardian, MacGyver and the items. How can you represent them in the program. How are they distributed at the beginning of the game ?

########### To be translated ############
2 - Animer le personnage

Le seul élément mouvant est MacGyver. Créez les méthodes de classe qui permettent de l'animer et de trouver la sortie. Pour l'instant, faites une version simplifiée du jeu dans laquelle MacGyver gagne en arrivant face au gardien.

 
3 - Récupérer les objets

Ajoutez la gestion des objets. Comment MacGyver les ramasse-t-il ?  Ajoutez également un compteur qui les listera.

 
4 - Gagner !

Enfin, changez la fin du jeu : MacGyver gagne s'il a bien ramassé tous les objets et endormi le garde. Sinon, il perd.

Livrables

Programme hébergé par Github,
Document texte expliquant votre démarche et comprenant le lien vers votre code source (sur Github). Développez notamment le choix de l'algorithme. Expliquez également les difficultés rencontrées et les solutions trouvées. Le document doit être en format pdf et ne pas excéder 2 pages A4.
 
Contraintes

Vous versionnerez votre code en utilisant Git et le publierez sur Github pour que votre mentor puisse le commenter,
Vous respecterez les bonnes pratiques de la PEP 8 et développerez dans un environnement virtuel utilisant Python 3,
Votre code devra être écrit en anglais : nom des variables, commentaires, fonctions...
Pensez à mettre à jour votre page de profil quand votre mentor aura validé votre projet !
 

Compétences à valider

Coder efficacement en utilisant les outils adéquats
Conceptualiser l'ensemble de son application en décrivant sa structure (Entités / Domain Objects)
Créer des scripts pour le web en utilisant Python
Gérer les différentes versions de Python et ses modules en fonction des projets
Lire et comprendre une documentation de module
Utiliser un algorithme pour résoudre un besoin technique
Créé par

 logo OpenClassrooms
OpenClassrooms, 1ère plateforme e-Education en Europe
