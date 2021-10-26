import pygame
pygame.init()

#Colors
PEACH_COLOR = (230, 230, 208)
GREEN_COLOR = (126, 142, 96)

#Checker pieces
RED_PIECE = pygame.image.load("red_piece.png")
BLACK_PIECE = pygame.image.load("black_piece.png")

#Display Settings
win = pygame.display.set_mode((400, 400))
pygame.display.set_caption("Checkers_AI")
win.fill((GREEN_COLOR))
x = 0
y = 0
switchRow = True

pieceLocationList = "1p1p1p1p/p1p1p1p1/1p1p1p1p/8/8/P1P1P1P1/1P1P1P1P/P1P1P1P1"

locationX = 2
locationY = 2

def squareLocation (corX, corY):
    return 0

#add a loop for squareLocation, X and Y to find the coordinated of the square

while True:
    pygame.time.delay(50)
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()

    #Draws the board
    for i in range(8):
        for i in range (8):
            pygame.draw.rect(win, PEACH_COLOR, (x, y, 50, 50))
            x += 100
        y += 50
        if switchRow == True:
            x = 50
            switchRow = False
        elif switchRow == False:
            x = 0
            switchRow = True

    #Places the pieces on the board, refering to fen
    for i in range(len(pieceLocationList)):

        if pieceLocationList[i] != "P" and pieceLocationList[i] != "p" and pieceLocationList[i] != "/":
            for i in range(int(pieceLocationList[i])):
                locationX += 50

        elif pieceLocationList[i] == "p":
            win.blit(BLACK_PIECE, (locationX, locationY))
            locationX += 50

        elif pieceLocationList[i] == "P":
            win.blit(RED_PIECE, (locationX, locationY))
            locationX += 50

        elif pieceLocationList[i] == "/":
            locationX = 2
            locationY += 50



    pygame.display.update()