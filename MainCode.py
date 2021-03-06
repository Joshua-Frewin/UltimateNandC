import pygame
import time
import random
import math

pygame.init()
clock = pygame.time.Clock()
#test comment

# load images of People
#InternetHistorianImg = pygame.image.load('InternetHistorian.png')
#AinsleyImg = pygame.image.load('Ainsley.png')
#PaigeImg = pygame.image.load('paige.png')
#AdamImg = pygame.image.load('adam.png')
#AnthonyImg = pygame.image.load('anthony.png')
#MaxImg = pygame.image.load('max.png')
#Harry1Img = pygame.image.load('harry1.png')
#HarryToungeImg = pygame.image.load('harrytounge.png')

# Load image of Crosses
OctocatImg = pygame.image.load('octocat.png')
# Load image of Crosses
CrossImg = pygame.image.load('Drawn_Cross.png')
# Load image of Naughts
NaughtImg = pygame.image.load('Drawn_Naught.png')
# Load image of Logo
Logo = pygame.image.load('Logo.png')

es = 6  # es = "edge space"

size = 60

dW = 9 * size
dH = 9 * size
game_display = pygame.display.set_mode((dW + 4*es,dH + 4*es))
pygame.display.set_caption('Ultimate Naughts and Crosses')

# Create colours
black  = (0,0,0)
white  = (255,255,255)
grey   = (220,220,220)
red    = (255,0,0)
green  = (0,255,0)
blue   = (0,0,255)
blue1  = (182,255,255)
blue2  = (0,152,202)
cyan   = (0,255,255)
yellow = (255,255,0)
pink   = (242,0,133)
pink1  = (255,226,235)

ticker = 60

ms00 = [[True,True,True],[True,True,True],[True,True,True]]
ms01 = [[True,True,True],[True,True,True],[True,True,True]]
ms02 = [[True,True,True],[True,True,True],[True,True,True]]
ms10 = [[True,True,True],[True,True,True],[True,True,True]]
ms11 = [[True,True,True],[True,True,True],[True,True,True]]
ms12 = [[True,True,True],[True,True,True],[True,True,True]]
ms20 = [[True,True,True],[True,True,True],[True,True,True]]
ms21 = [[True,True,True],[True,True,True],[True,True,True]]
ms22 = [[True,True,True],[True,True,True],[True,True,True]]
squares = [[ms00,ms01,ms02],[ms10,ms11,ms12],[ms20,ms21,ms22]]

def message_display(text = '"insert text"',text_size = 20, position = (dW/2,dH/2), colour = white):
    largeText = pygame.font.Font('freesansbold.ttf',text_size)
    text_surface = largeText.render(text, True, colour)
    text_rect = text_surface.get_rect()
    text_rect.center = position
    game_display.blit(text_surface, text_rect)

def blit_alpha(target, source, location, opacity):
        x = location[0]
        y = location[1]
        temp = pygame.Surface((source.get_width(), source.get_height())).convert()
        temp.blit(target, (-x, -y))
        temp.blit(source, (0, 0))
        temp.set_alpha(opacity)
        target.blit(temp, location)

def normal_button(pos_x, pos_y, width, height, CrossPNG = None, NaughtsPNG = None, text = '"Text"', action = None, colour = cyan, hover_colour = blue2, text_colour = white):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:
        pygame.draw.rect(game_display, hover_colour, (pos_x,pos_y,width,height))
        message_display(text = text, text_size = 20, position = (pos_x+width/2,pos_y+height/2), colour = text_colour)
        if click[0] == 1:
            if CrossPNG == None and NaughtsPNG == None:
                print('Cross none naughts none')
                action()
            elif NaughtsPNG == None and CrossPNG != None:
                print('naughts none')
                action(CrossPNG)
            elif CrossPNG == None and NaughtsPNG != None:
                print('cross none')
                action(NaughtsPNG)
            elif CrossPNG != None and NaughtsPNG != None:
                print('Both have image')
                action(CrossPNG, NaughtsPNG)
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
        message_display(text = text, text_size = 20, position = (pos_x+width/2,pos_y+height/2), colour = text_colour)

def Crosses_button(pos_x, pos_y, X, Y, x, y, squares, Game_records, image, width = size, height = size, colour = grey):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:

        # Highlighted Black Plus on Cyan background
        pygame.draw.rect(game_display, cyan, (pos_x,pos_y,width,height))
        pygame.draw.line(game_display, black, (pos_x+es    ,pos_y+size/2), (pos_x+size-es,pos_y+size/2 ),es)
        pygame.draw.line(game_display, black, (pos_x+size/2,pos_y+es    ), (pos_x+size/2 ,pos_y+size-es),es)

        if click[0] == 1:
            time.sleep(0.1)
            squares[X][Y][x][y] = 'Crosses'
            Game_records.append([X,Y,x,y])
            print(Game_records[-1])
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares, Game_records

def Naughts_button(pos_x, pos_y, X, Y, x, y, squares, Game_records, image, width = size, height = size, colour = grey):
    mouse = pygame.mouse.get_pos()
    click = pygame.mouse.get_pressed()
    if pos_x + width > mouse[0] > pos_x and pos_y + height > mouse[1] > pos_y:

        # Highlighted Black Plus on Cyan background
        pygame.draw.rect(game_display, cyan, (pos_x,pos_y,width,height))
        pygame.draw.line(game_display, black, (pos_x+es    ,pos_y+size/2), (pos_x+size-es,pos_y+size/2 ),es)
        pygame.draw.line(game_display, black, (pos_x+size/2,pos_y+es    ), (pos_x+size/2 ,pos_y+size-es),es)

        if click[0] == 1:
            time.sleep(0.1)
            squares[X][Y][x][y] = 'Naughts'
            Game_records.append([X,Y,x,y])
            print(Game_records[-1])
    else:
        pygame.draw.rect(game_display, colour, (pos_x,pos_y,width,height))
    return squares, Game_records

def Undo(squares, Game_records):
    if (pygame.key.get_pressed()[pygame.K_BACKSPACE]):
        try:
            X, Y, x, y = Game_records[-1]
            squares[X][Y][x][y] = True
            Game_records.pop(-1)
            time.sleep(0.5)
        except:
            # Do nothing
            mainmenu_loop()
    return squares, Game_records

def check_if_gameover(NandC):
    winner = None
    for Type in ['Naughts', 'Crosses']:
        if NandC[1][1] == Type: # if middle square is equal to the tpye
            if NandC[1][0] == Type and NandC[1][2] == Type: # if left middle and right middle
                winner = Type
            if NandC[0][0] == Type and NandC[2][2] == Type: # if top right and bottom left
                winner = Type
            if NandC[0][1] == Type and NandC[2][1] == Type: # if top middle and bottom middle
                winner = Type
            if NandC[0][2] == Type and NandC[2][0] == Type: # if bottom left and top right
                winner = Type
        if NandC[0][0] == Type: # if top left has won
            if NandC[0][1] == Type and NandC[0][2] == Type: # if top middle and top right
                winner = Type
            if NandC[1][0] == Type and NandC[2][0] == Type: # if right middle and bottom right
                winner = Type
        if NandC[2][2] == Type: # if bottom left has won
            if NandC[0][2] == Type and NandC[1][2] == Type: # top right and middle right
                winner = Type
            if NandC[2][0] == Type and NandC[2][1] == Type: # bottom left and bottom middle
                winner = Type
    return winner

def HasMiniGameWon(squares,X,Y,NandC):
    current = NandC[X][Y]
    NandC[X][Y] = '-'
    listof = ['Naughts', 'Crosses']
    if current == 'Naughts':
        listof.remove('Crosses')
    elif current == 'Crosses':
        listof.remove('Naughts')

    for Type in listof:
        if squares[X][Y][1][1] == Type: # if middle square is equal to the tpye
            if squares[X][Y][1][0] == Type and squares[X][Y][1][2] == Type: # if left middle and right middle
                NandC[X][Y] = Type
            if squares[X][Y][0][0] == Type and squares[X][Y][2][2] == Type: # if top right and bottom left
                NandC[X][Y] = Type
            if squares[X][Y][0][1] == Type and squares[X][Y][2][1] == Type: # if top middle and bottom middle
                NandC[X][Y] = Type
            if squares[X][Y][0][2] == Type and squares[X][Y][2][0] == Type: # if bottom left and top right
                NandC[X][Y] = Type
        if squares[X][Y][0][0] == Type: # if top left has won
            if squares[X][Y][0][1] == Type and squares[X][Y][0][2] == Type: # if top middle and top right
                NandC[X][Y] = Type
            if squares[X][Y][1][0] == Type and squares[X][Y][2][0] == Type: # if right middle and bottom right
                NandC[X][Y] = Type
        if squares[X][Y][2][2] == Type: # if bottom left has won
            if squares[X][Y][0][2] == Type and squares[X][Y][1][2] == Type: # top right and middle right
                NandC[X][Y] = Type
            if squares[X][Y][2][0] == Type and squares[X][Y][2][1] == Type: # bottom left and bottom middle
                NandC[X][Y] = Type
    return NandC

def mainmenu_loop(CrossPNG = None, NaughtsPNG = None):
    mainmenu = True
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)

        message_display(text = 'ULTIMATE', position = (dW*(10/20),dH*(4/20)), text_size = 50, colour = black)
        message_display(text = 'Naughts', position = (dW*(10/20),dH*(8/20)), text_size = 50, colour = blue)
        message_display(text = 'and', position = (dW*(10/20),dH*(10/20)), text_size = 50, colour = black)
        message_display(text = 'Crosses', position = (dW*(10/20),dH*(12/20)), text_size = 50, colour = red)

        normal_button(dW*(3/20), dH*(14/20), dW*(6/20), dH*(2/20), text = 'Play', action = game_loop, CrossPNG = CrossPNG, NaughtsPNG = NaughtsPNG, text_colour = black)
        normal_button(dW*(11/20), dH*(14/20), dW*(6/20), dH*(2/20), text = 'Options?', action = options_loop, text_colour = black)
        normal_button(dW*(3/20), dH*(17/20), dW*(6/20), dH*(2/20), text = 'Instructions', action = instructions_loop, text_colour = black)
        normal_button(dW*(11/20), dH*(17/20), dW*(6/20), dH*(2/20), text = 'Credits', action = credits_loop, text_colour = black)

        pygame.display.update()
        clock.tick(60)
    intro = False

def options_loop(mainmenu = True):
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)

        message_display(text = 'OPTIONS', position = (dW*(10/20),dH*(4/20)), text_size = 50, colour = black)

        normal_button(dW*(3/20), dH*(14/20), dW*(6/20), dH*(2/20), text = 'Play', action = game_loop, text_colour = black)
        normal_button(dW*(1/20), dH*(1/20), dW*(6/20), dH*(2/20), text = 'Main Menu', action = mainmenu_loop, text_colour = black)

        pygame.display.update()
        clock.tick(60)
    intro = False

def instructions_loop(mainmenu = True):
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)

        message_display(text = 'INSTRUCTIONS', position = (dW*(10/20),dH*(4/20)), text_size = 50, colour = black)

        normal_button(dW*(3/20), dH*(14/20), dW*(6/20), dH*(2/20), text = 'Play', action = game_loop, text_colour = black)
        normal_button(dW*(1/20), dH*(1/20), dW*(6/20), dH*(2/20), text = 'Main Menu', action = mainmenu_loop, text_colour = black)

        pygame.display.update()
        clock.tick(60)
    intro = False

def credits_loop(mainmenu = True):
    while mainmenu:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        game_display.fill(white)

        message_display(text = 'CREDITS', position = (dW*(10/20),dH*(4/20)), text_size = 50, colour = black)
        message_display(text = 'Paige Windmill', position = (dW*(10/20),dH*(8/20)), text_size = 50, colour = black)
        message_display(text = 'and', position = (dW*(10/20),dH*(10/20)), text_size = 50, colour = black)
        message_display(text = 'Anthony Dunford', position = (dW*(10/20),dH*(12/20)), text_size = 50, colour = black)

        normal_button(dW*(3/20), dH*(14/20), dW*(6/20), dH*(2/20), text = 'Play', action = game_loop, text_colour = black)
        normal_button(dW*(1/20), dH*(1/20), dW*(6/20), dH*(2/20), text = 'Main Menu', action = mainmenu_loop, text_colour = black)

        pygame.display.update()
        clock.tick(60)
    intro = False

def game_loop(Cross_Image = None, Naughts_Image = None, squares = squares):

    # Alternate grey variables needed
    AG = 255
    AG_change = -1
    alternate_grey = (AG,AG,AG)

    # Image Handling
    if Cross_Image != None:
        Mcross = pygame.transform.scale(Cross_Image, (size, size))
        Lcross = pygame.transform.scale(Cross_Image, (3*size, 3*size))
    if Naughts_Image != None:
        Mnaught = pygame.transform.scale(Naughts_Image, (size, size))
        Lnaught = pygame.transform.scale(Naughts_Image, (3*size, 3*size))

    winner = None

    NandC = [['-','-','-'],['-','-','-'],['-','-','-']]

    Game_records = []

    while winner == None:
        # If Quit
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                print(Game_records)
                pygame.quit()
                quit()

        #Crosses has turn
        game_display.fill(white)
        pygame.draw.rect(game_display, black, (es,es,dW+2*es,dH+2*es))
        for LX in range(0,3):
            for LY in range(0,3):
                for MX in range(0,3):
                    for MY in range(0,3):

                        pos_x = (3*size+es)*LX+size*MX+es
                        pos_y = (3*size+es)*LY+size*MY+es

                        if squares[LX][LY][MX][MY] == True:
                            try:
                                # If Game records exist and we can access the last one in the list
                                BigX, BigY = Game_records[-1][2:]
                                if LX == BigX and LY == BigY:
                                    if len(Game_records) % 2 == 0:
                                        # Makes Crosses button
                                        squares, Game_records = Crosses_button(pos_x, pos_y, LX, LY, MX, MY, squares, Game_records, image = Cross_Image, colour = alternate_grey)
                                    else:
                                        # Makes Naughts button
                                        squares, Game_records = Naughts_button(pos_x, pos_y, LX, LY, MX, MY, squares, Game_records, image = Naughts_Image, colour = alternate_grey)
                                else:
                                    # Fill in white square if no button
                                    pygame.draw.rect(game_display, white, (pos_x,pos_y,size,size))
                            except:
                                # If no game records exist then only allow the starting positions to be buttons
                                if LX == 1 and LY == 1 and (MY, MX) != (1, 1):
                                    # Only center squares but not the middle middle square
                                    squares, Game_records = Crosses_button(pos_x, pos_y, LX, LY, MX, MY, squares, Game_records, image = Cross_Image, colour = alternate_grey)
                                else:
                                    # Fill in white square if no button
                                    pygame.draw.rect(game_display, white, (pos_x,pos_y,size,size))

                        elif squares[LX][LY][MX][MY] == 'Naughts':

                            # Draws Cicle

                            if [LX,LY,MX,MY] == Game_records[-1]: # Highlight the latest circle
                                pygame.draw.rect(game_display, blue1, (pos_x,pos_y,size,size))
                            else:
                                pygame.draw.rect(game_display, white, (pos_x,pos_y,size,size))
                            # put on mini naught image
                            if Naughts_Image == None:
                                pygame.draw.circle(game_display, blue, (int(pos_x+size/2),int(pos_y+size/2)), int(size/2-es), es)
                                pygame.draw.circle(game_display, blue, (int(pos_x+size/2),int(pos_y+size/2)), int(size/2-es), es)
                            else:
                                game_display.blit(Mnaught, (pos_x, pos_y))

                        elif squares[LX][LY][MX][MY] == 'Crosses':

                            # Draws Cross
                            if [LX,LY,MX,MY] == Game_records[-1]: # Highlight the latest cross
                                pygame.draw.rect(game_display, pink1, (pos_x,pos_y,size,size))
                            else:
                                pygame.draw.rect(game_display, white, (pos_x,pos_y,size,size))
                            # put on mini cross image
                            if Cross_Image == None:
                                pygame.draw.line(game_display, red, (pos_x+es,pos_y+es     ), (pos_x+size-es,pos_y-es+size),es)
                                pygame.draw.line(game_display, red, (pos_x+es,pos_y-es+size), (pos_x+size-es,pos_y+es     ),es)
                            else:
                                game_display.blit(Mcross, (pos_x, pos_y))

                # Check if any big squares have been won
                NandC = HasMiniGameWon(squares,LX,LY,NandC)

                pos_X = LX*(3*size+es)
                pos_Y = LY*(3*size+es)
                if NandC[LX][LY] == 'Crosses': # if large box has been won by crosses
                    if Cross_Image == None:
                        # left-top to right-bottom
                        pygame.draw.line(game_display, red, (pos_X+2*es,pos_Y+4*es), ((LX+1)*(size*3+es)-3*es,(LY+1)*(size*3+es)-es),es)
                        pygame.draw.line(game_display, red, (pos_X+4*es,pos_Y+2*es), ((LX+1)*(size*3+es)-es,(LY+1)*(size*3+es)-3*es),es)
                        # right-bottom to left-top
                        pygame.draw.line(game_display, red, (pos_X+4*es,(LY+1)*(size*3+es)-es), ((LX+1)*(size*3+es)-es,pos_Y+4*es),es)
                        pygame.draw.line(game_display, red, (pos_X+2*es,(LY+1)*(size*3+es)-3*es), ((LX+1)*(size*3+es)-3*es,pos_Y+2*es),es)
                    else:
                        blit_alpha(game_display, Lcross, (pos_X+es, pos_Y+es), opacity = 150)

                elif NandC[LX][LY] == 'Naughts': # if large box has been won by naughts
                    if Naughts_Image == None:
                        pygame.draw.circle(game_display, blue, (int(pos_X+es+size*3/2),int(pos_Y+es+size*3/2)), 3*int(size/2)-4*es, es)
                        pygame.draw.circle(game_display, blue, (int(pos_X+es+size*3/2),int(pos_Y+es+size*3/2)), 3*int(size/2)-es, es)
                    else:
                        blit_alpha(game_display, Lnaught, (pos_X+es, pos_Y+es), opacity = 150)

        AG += AG_change
        if AG == 255:
            AG_change = -1
        elif AG == 200:
            AG_change = 1

        alternate_grey = (AG,AG,AG)
        pygame.display.update()
        clock.tick(ticker)

        squares, Game_records = Undo(squares, Game_records)

        winner = check_if_gameover(NandC)

mainmenu_loop(CrossPNG = OctocatImg, NaughtsPNG = AinsleyImg)
#mainmenu_loop()
