#Kostki
import random
p1_win = 0
p2_win = 0
p1_lose = 0
p2_lose = 0
def rzut_kostka():
    rzut = random.randrange(1, 7)
    return rzut

def gracz():
    gracz = random.randrange(1, 7)
    return gracz

def half_tura():
    gracz1 = gracz()
    gracz2 = gracz()
    return gracz1, gracz2

def tura():
    g1, g2 = half_tura()
    g3, g4 = half_tura()
    print("Gracz1 wyrzucił",g1 + g3,"oczek.")
    print("Gracz2 wyrzucił",g2 + g4,"oczek.")
    return g1+g3, g2+g4

def punkty():
    points1, points2 = tura()
    global p1_win, p1_lose, p2_win, p2_lose
    if points1 > points2:
        p1_win += 1
        p2_lose += 1
    else:
        p2_win  += 1
        p1_lose += 1
    print("Gracz1 wygrał",p1_win,"razy i przegrał",p1_lose,"razy.")
    print("Gracz2 wygrał",p2_win,"razy i przegrał",p2_lose,"razy.")
    return p1_win, p1_lose, p2_win, p2_lose
        
def gra(n):
    
    while n:
        p1_win, p1_lose, p2_win, p2_lose = punkty()
        n -= 1

    while p1_win == p2_win:
        tura()
        punkty()
    if p1_win > p2_win:
        print("Gracz1 wygrał!")
    else:
        print("Gracz2 wygrał!")
        

gra(4)

    
    
