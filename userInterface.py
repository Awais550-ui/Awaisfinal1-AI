#Final AI Project
import pygame
from pieces import *
from ratings import Ratings
import time

class UserInterface:



    def __init__(self, surface, Board):
        self.surface = surface
        self.inPlay = True
        self.squareSize = 80
        self.pieces = 64
        self.mouseInitialX = 0
        self.mouseInitialY = 0

        self.mouseFinalX = 0
        self.mouseFinalY = 0

        self.chessboard = Board
        self.playerMove = ""
        self.computerMove = ""
        self.playerColor = ""
        self.computerColor = ""




    def drawComponent(self):
        for i in range(0, self.pieces, 2):
            pygame.draw.rect(self.surface, (120, 60, 30), [(i % 8+(i//8) % 2)*self.squareSize, (i//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws brown squares
            pygame.draw.rect(self.surface, (245, 245, 220), [((i+1) % 8-((i+1)//8) % 2)*self.squareSize, ((i+1)//8)*self.squareSize, self.squareSize, self.squareSize])  # Draws beige squares

        for index in range(self.pieces):
            currentPosition = self.chessboard.boardArray[index//8][index % 8]
            if currentPosition == "P":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_pl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_pd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "p":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_pd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_pl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "K":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_nl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_nd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))

            elif currentPosition == "k":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_nd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_nl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "B":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_bl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_bd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "b":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_bd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_bl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "R":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_rl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_rd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "r":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_rd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_rl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "Q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_ql.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_qd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "q":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_qd.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_ql.png")  # Load peice image
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))


            elif currentPosition == "A":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_kl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_kd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))

            elif currentPosition == "a":
                if self.playerColor == "W":
                    chessPieces = pygame.image.load("assets/Chess_tile_kd.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))
                else:
                    chessPieces = pygame.image.load("assets/Chess_tile_kl.png")
                    chessPieces = pygame.transform.scale(chessPieces, (self.squareSize, self.squareSize))
                    self.surface.blit(chessPieces, ((index % 8)*self.squareSize, (index//8)*self.squareSize))

        pygame.display.update()


    def eventHandler(self):
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                self.inPlay = False
                break


            if event.type == pygame.MOUSEBUTTONDOWN:

                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseInitialX = pygame.mouse.get_pos()[0]
                    self.mouseInitialY = pygame.mouse.get_pos()[1]


            if event.type == pygame.MOUSEBUTTONUP:
                if pygame.mouse.get_pos()[0] < 8*self.squareSize and pygame.mouse.get_pos()[1] < 8*self.squareSize:
                    self.mouseFinalX = pygame.mouse.get_pos()[0]
                    self.mouseFinalY = pygame.mouse.get_pos()[1]
                    self.computeMove()

    def computeMove(self):

        rowInitial = self.mouseInitialY//self.squareSize
        columnInitial = self.mouseInitialX//self.squareSize
        rowFinal = self.mouseFinalY//self.squareSize
        columnFinal = self.mouseFinalX//self.squareSize


        if rowFinal == 0 and rowInitial == 1 and self.chessboard.boardArray[rowInitial][columnInitial] == "P":

            promotionPeice = input("Choose a piece to promote [K,Q,R,B]: ")

            self.playerMove += str(columnInitial) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][columnFinal])+ promotionPeice + "P"

        elif rowFinal == 7 and (columnInitial == 0 or columnInitial == 7) and self.chessboard.boardArray[rowInitial][columnInitial] == "R" and self.chessboard.boardArray[rowFinal][columnFinal] == "A":

            if columnInitial == 0:
                self.playerMove += str(columnInitial) + str(columnFinal-1) + str(columnFinal) + "R" + "C"
            elif columnInitial == 7:
                self.playerMove += str(columnInitial) + str(columnFinal+1) + str(columnFinal) + "R" + "C"


        else:
            self.playerMove += str(rowInitial) + str(columnInitial) + str(rowFinal) + str(columnFinal) + str(self.chessboard.boardArray[rowFinal][(columnFinal)])

        print(f"Player Move: {self.playerMove}")
        print(f"Generated Move List: {self.chessboard.generateMoveList()}")


        if self.playerMove in self.chessboard.generateMoveList():
            self.chessboard.computeMove(self.playerMove)
            self.drawComponent()
            self.computerMoves()
        else:
            print("Move is Invalid or Unsafe")
        self.playerMove = ""
        self.computerMove = ""

    def computerMoves(self):

        if self.computerColor == "W":
            print("It's White's Turn!!")

        else:
            print("It's Black's Turn!!")
        start_time = time.time()
        self.chessboard.changePerspective()
        self.computerMove = self.chessboard.alphaBeta(self.chessboard.MAXDEPTH, float("inf"), -float("inf"), "", 0)
        if self.computerMove is None:
            print("CHECKMATE!! You're finished!!")
            time.sleep(15)
            self.inPlay = False

        else:
            self.chessboard.computeMove(self.computerMove)

        self.chessboard.changePerspective()
        self.drawComponent()

        if len(self.chessboard.generateMoveList()) == 0:
            if self.chessboard.kingissafe() is False:
                print("CHECKMATE!! You're finished!!")
                time.sleep(15)
                self.inPlay = False

            else:
                print("STALEMATE!")
                time.sleep(15)
                self.inPlay = False


        if self.chessboard.kingissafe() is False:
            print("It's a Check, Move your king!!!")


        print("AI has taken time: ", time.time() - start_time, "Sec")
        if self.playerColor == "W":
            print("It's White's Turn!!")
        else:
            print("It's Black's Turn!!")


    def playGame(self):
        self.surface.fill((0, 0, 0))
        while(self.playerColor != "W" and self.playerColor != "B"):
            self.playerColor = input("Select one color White(W) or Black(B): ")

        self.drawComponent()


        if self.playerColor == "W":
            self.computerColor = "B"
        else:
            self.computerColor = "W"


        if self.playerColor == "W":
            print("It's White's Turn!!")

        else:
            print("It's White's Turn!!")
            self.computerMoves()
            print("It's Black's Turn!!")

        while self.inPlay:
            self.eventHandler()
