import pygame as pg 
import sys 
import os
import random

WINDOW_SIZE = 600

cross = pg.image.load(os.path.join("assets/cross.png"))
circle = pg.image.load(os.path.join("assets/circle.png"))
human = pg.image.load(os.path.join("assets/human.png"))
computer = pg.image.load(os.path.join("assets/computer.png"))

def drawCross(surface, g1, g2):
    surface.blit(cross, (WINDOW_SIZE//3*g1, WINDOW_SIZE//3*g2))

def drawCircle(surface, g1, g2):
    surface.blit(circle, (WINDOW_SIZE//3*g1, WINDOW_SIZE//3*g2))

def drawHuman(surface, x1, x2):
    surface.blit(human, (x1, x2))
def drawComp(surface, x1, x2):
    surface.blit(computer, (x1, x2))

def winlos(board, turn):
    if turn%2 == 0:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == 'X':
                return 'X'
            if board[0][i] == board[1][i] == board[2][i] == 'X':
                return 'X'
        if board[0][0] == board[1][1] == board[2][2] == 'X':
            return 'X'
        elif board[0][2] == board[1][1] == board[2][0] == 'X':
            return 'X'
    if turn%2 != 0:
        for i in range(3):
            if board[i][0] == board[i][1] == board[i][2] == 'O':
                return 'O'
            if board[0][i] == board[1][i] == board[2][i] == 'O':
                return 'O'
        if board[0][0] == board[1][1] == board[2][2] == 'O':
            return 'O'
        elif board[0][2] == board[1][1] == board[2][0] == 'O':
            return 'O'
    return 0

def isDraw(board):
    for i in board:
        if 0 in i: return False
    return True

def grid(surface, rows, w):
    sizbet = w // rows
    x = y = 0
    
    for i in range(rows-1):
        x += sizbet
        y += sizbet
        pg.draw.line(surface, (255, 255, 255), (x, 0), (x, w))
        pg.draw.line(surface, (255, 255, 255), (0, y), (w, y))

def menu():
    pg.init()
    font = pg.font.Font('freesansbold.ttf', 64)
    text = font.render("Tic Tac Toe", True, (248,212,138))
    textRect = text.get_rect()
    textRect.center = (300, 200)
    clock = pg.time.Clock()
    pg.display.set_caption("ttt")
    win = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) 
    win.fill((60, 60, 60))
    selec = 0
    men = True
    humanpos = human.get_rect()
    comppos = computer.get_rect()
    humanpos.center = (290, 370)
    comppos.center = (300, 450)
    while men:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.display.quit()
                pg.quit()
                sys.exit()
            if i.type == pg.MOUSEBUTTONDOWN:
                pos = pg.mouse.get_pos()
                if humanpos.collidepoint(pos):
                    return 1
                elif comppos.collidepoint(pos):
                    return 2
                
        clock.tick(60)
        win.blit(text, textRect)
        drawHuman(win, 200, 300)
        drawComp(win, 200, 400)

        pg.display.update() 
        
def winscreen(c):
    pg.init()
    font = pg.font.Font('freesansbold.ttf', 32)
    text = font.render("Won The Game", True, (248,212,138))
    text3 = font.render("It Is A Draw!", True, (248,212,138))
    text2 = font.render("Play Again? (Y/N)", True, (248,212,138))

    textRect = text.get_rect()
    textRect.center = (300, 250)
    textRect2 = text.get_rect()
    textRect2.center = (300, 300)
    textRect3 = text3.get_rect()
    textRect3.center = (290, 200)

    clock = pg.time.Clock()
    pg.display.set_caption("ttt")
    win = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) 
    win.fill((60, 60, 60))
    win.blit(text2, textRect2)
    
    if c == 'X':
        drawCross(win, 1, 0)
        win.blit(text, textRect)
        

    elif c == 'O':
        drawCircle(win, 1, 0)
        win.blit(text, textRect)
        
    else:
        win.blit(text3, textRect3)

    

    while True:
        for i in pg.event.get():
            if i.type == pg.QUIT:
                pg.display.quit()
                pg.quit()
                sys.exit()
            if i.type == pg.KEYDOWN:
                if i.key == pg.K_y:
                    return True
                elif i.key == pg.K_n:
                    return False

        clock.tick(60)
        pg.display.update()



def main(selec):
    pg.init()
    clock = pg.time.Clock()
    pg.display.set_caption("ttt")
    win = pg.display.set_mode((WINDOW_SIZE, WINDOW_SIZE)) 
    win.fill((60, 60, 60))
    turn = random.randint(0, 1)
    board = [[0, 0, 0], [0, 0, 0], [0, 0, 0]]
    if selec == 1:
        while True:
            for i in pg.event.get():
                if i.type == pg.QUIT:
                    pg.display.quit()
                    pg.quit()
                    sys.exit()
                if winlos(board, turn) != 0:
                    if winlos(board, turn) == 'X':
                        pg.quit()
                        return 'X'
                    else:
                        pg.quit()
                        return 'O'
                elif isDraw(board) == True:
                    pg.quit()
                    return("D")
                elif i.type == pg.MOUSEBUTTONDOWN:
                    if winlos(board, turn) != 0:
                        if winlos(board, turn) == 'X':
                            pg.quit()
                            return 'X'
                        else:
                            pg.quit()
                            return 'O'
                    elif isDraw(board) == True:
                        pg.quit()
                        return("D")
                    
                    pos = pg.mouse.get_pos()
                    x = pos[0] // (WINDOW_SIZE // 3)
                    y = pos[1] // (WINDOW_SIZE // 3)
                    if board[y][x] != 0: continue
                    if turn%2 == 0:
                        drawCross(win, x, y)
                        board[y][x] = 'X'
                        if winlos(board, turn) != 0:
                            if winlos(board, turn) == 'X':
                                pg.quit()
                                return 'X'
                        elif isDraw(board) == True:
                            pg.quit()
                            return("D")
                    if turn%2 != 0:
                        drawCircle(win, x, y)
                        board[y][x] = 'O'
                        if winlos(board, turn) != 0:
                            if winlos(board, turn) == 'O':
                                pg.quit()
                                return 'O'
                        elif isDraw(board) == True:
                            pg.quit()
                            return("D")
                    turn += 1
                    
                        

            clock.tick(60)
            grid(win, 3, WINDOW_SIZE)
            pg.display.update()    
    elif selec == 2:
        while True:
            if winlos(board, turn) != 0:
                if winlos(board, turn) == 'X':
                    pg.quit()
                    return 'X'
                else:
                    pg.quit()
                    return 'O'
            
                    
            elif isDraw(board) == True: 
                pg.quit()
                return 'D'
            
            else:
                for i in pg.event.get():
                    if i.type == pg.QUIT:
                        pg.display.quit()
                        pg.quit()
                        sys.exit()
                    if turn%2 != 0:
                        x1 = random.randint(0, 2)
                        y1 = random.randint(0, 2)
                        while board[y1][x1] != 0:
                            x1 = random.randint(0, 2)
                            y1 = random.randint(0, 2)
                        drawCircle(win, x1, y1)
                        board[y1][x1] = 'O'
                        turn += 1
                    elif i.type == pg.MOUSEBUTTONDOWN:
                        pos = pg.mouse.get_pos()
                        x = pos[0] // (WINDOW_SIZE // 3)
                        y = pos[1] // (WINDOW_SIZE // 3)
                        
                        if board[y][x] != 0: continue
                        drawCross(win, x, y)
                        board[y][x] = 'X'
                        turn += 1
                

            clock.tick(60)
            grid(win, 3, WINDOW_SIZE)
            pg.display.update()    


num = menu()
char = main(num)
again = winscreen(char)
while again:
    num = menu()
    char = main(num)
    again = winscreen(char)