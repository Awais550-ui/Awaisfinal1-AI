

## TO Run the Game
Download the Files and folders as it is and run chess.py to play the game.


## References:
* Program Uses pygame: http://www.pygame.org/

  * Chess tile graphics were used from Wikimedia Commons: http://commons.wikimedia.org/wiki/File:Chess_tile_pd.png

  * alphaBeta Function was created based on the pseudocode Provided by wikipedia: https://en.wikipedia.org/wiki/Alpha%E2%80%93beta_pruning


  * Used 'Fruit' values for rating material and similar values for other ratings from chessprogramming wikispace : https://chessprogramming.wikispaces.com/Point%20Value

  * Generating Move lists for each piece class was inspired by chessprogramming wikispace on move lists: https://chessprogramming.wikispaces.com/Move%20List

  * Board representation 'boardArray' is based off the 8x8 board array method: https://chessprogramming.wikispaces.com/8x8%20Board

  * Chess.com for descriptions of basic and special moves pieces can make:
  https://www.chess.com/learn-how-to-play-chess

## Description: 
Pychess is a pygame-based Player-Vs-AI chess engine that allows a player to play chess versus a computer that makes its own moves.
The chess board and pieces in the game were created utilizing polymorphism and several class-based structures.

The Alphabeta Pruning Search Algorithm is used by the Computer Ai to evaluate potential moves.



### The following important milestones were reached throughout the development of this project:



* The creation of a board class that contains all of the pieces and functions needed to move across the board, determine if the player or the computer is in check, and so on.



* The creation of unique piece classes with their own set of moves based on the piece. Each piece class derives from an abstract 'piece' class, which has its own set of variables and functions.
  #### The following move sets are included in the game
 * Promotions: When a pawn moves to the opposite side of the board, it may exchange its current piece for a rook, a queen, a bishop, or a knight. 

* Castling: On a player's turn, he may move his king two squares to one side and then move the rook from that side's corner right next to the king on the opposite side.

* Creation of computer Ai that evaluates each individual move and decides which move to make based on the alpha beta pruning search algorithm

 #### Alpha Beta Pruning Summary: 
TThe method maintains two numbers, alpha and beta, which reflect the minimum and maximum scores that the maximizing and minimizing players are guaranteed of, respectively. The initial values of alpha and beta are negative infinity and positive infinity, respectively, indicating that both players begin with their lowest possible score. When the minimizing player's (beta) maximum score falls below the maximizing player's (alpha) minimum score (i.e. beta = alpha), the maximizing player does not need to consider the descendants of this node because they will never be reached in actual play. (according to Wikipedia)

IMPORTANT NOTE: At this time, the maximum depth is 3 plys. The algorithm is in favor of. The algorithm supports
  running up to for plys however for the sake of running time and time it takes computers
  to make move it is 1 lower. You can set self.MAXDEPTH = 4 in the board initalizer method,
  if you want to see computer compute 'deeper' moves at the cost of how long method
  takes to return move

  Refer to link for more information on algorithm: https://www.geeksforgeeks.org/minimax-algorithm-in-game-theory-set-4-alpha-beta-pruning/

* Creation of rating class that the computer uses to evaluate how ‘good’ a move is based on different factors.

* Creating  a graphical user interface using pygame that draws the board and chess pieces and allows user to play the game and make moves with the mouse and prompts or certain tasks are displayed on the terminal while game is running.

#### The contents in the file include:
* assets folder: Contains all the chess piece sprites used for game’s graphics.
* chess.py : Main program used to run interface and game. Run this program when starting the game
* board.py: Contains board class and it’s methods. Also contains the alphabeta method that the computer uses to make moves
* pieces.py: Contains the master class ‘Peices’ as well as all individual piece classes that inheret the main class.
* ratings.py : Contains the ratings class with methods that evaluate the rating of a move.
* userInterface.py: Contains the userInterface class that is used to play the game and display the game using pygame.

## Evaluation Metrics

* The main aim of the project is AI agent should generate optimal moves within less times. This has been shown during the code execution.
  After every turn of AI a time has been displayed in seconds which indicates how much time AI has taken to make its moves.

  It's mostly less than 1sec.

* ##### Validating Moves

    Another most important aspect of chess is each piece has it's own rule for moving along the board.
    These rules are described in project presentation and evaluation can be made by manually trying to move each piece in the board

* Default depth is set to 3, project can be evaluated by changing the deptth to different values and measure its performance.
  Depth can be changed in board.py --> init constructor --> self.MAXDEPTH
  
  




 
 
