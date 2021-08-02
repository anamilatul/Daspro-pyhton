import Globals as g
import random
import math

def initScreen(minX, maxX, minY, maxY):
    g.minX = minX
    g.maxX = maxX
    g.minY = minY
    g.maxY = maxY

def setPlayerPosition(x, y):
    g.playerX = x
    g.playerY = y

def setGoal():
    isExist = True
    while isExist :
        randX = random.randint(g.minX, g.maxY)
        randY = random.randint(g.minY, g.maxY)
        if randX != g.playerX and randY != g.playerY :
            g.goalX = randX
            g.goalY = randY
            isExist = False

def spawnEnemies(level):
    if level == "M" :
        g.cEnemies = 10
    elif level == "H" :
        g.cEnemies = 100

    for i in range(g.cEnemies):
        isExist = True
        while isExist :
            randX = random.randint(g.minX, g.maxY)
            randY = random.randint(g.minY, g.maxY)
            if randX != g.playerX and randY != g.playerY and randX != g.goalX and randY != g.goalY :
                g.enemiesPosX.append(randX)
                g.enemiesPosY.append(randY)
                isExist = False

# def lenEnemies() :
#     return(g.cEnemies)

def displayInitialStats(level):
    print("Level : " + level)
    print("Posisi player sekarang : " + str(g.playerX) + " " + str(g.playerY))
    print("Banyaknya musuh : " + str(g.cEnemies))

def distanceEuclid(x1, y1, x2, y2):
    x = (x1, y1, 0)
    y = (x2, y2, 0)
    distance = math.sqrt(sum([(a-b) ** 2 for a, b in zip(x,y)]))
    return distance

def distancePlayerWithGoal():
    return distanceEuclid(g.playerX, g.playerY, g.goalX, g.goalY)

def displayInGameStats():
    print("Jarak player dengan bintang : " + str(distancePlayerWithGoal()))

def checkPlayerMove(move) :
    if move == "U" :
        g.playerY += 1
    elif move == "D" :
        g.playerY -= 1
    elif move == "L" :
        g.playerX -= 1
    elif move == "R" :
        g.playerX += 1

    if g.playerX < g.minX or g.playerX > g.maxX or g.playerY < g.minY or g.playerY > g.maxY :
        print("Game Over!! Kamu telah menabrak pembatasnya")
        return False

    isMenabrak = False
    for i in range(g.cEnemies):
        if g.playerX == g.enemiesPosX[i] and g.playerY == g.enemiesPosY[i] :
            isMenabrak = True
            break
    if isMenabrak :
        print("Game Over!! Kamu telah menabrak musuh")
        return False
    
    if g.playerX == g.goalX and g.playerY == g.goalY :
        print("You Win!! Kamu berhasil untuk mendapatkan bintangnya")
        return False

    displayInGameStats()
