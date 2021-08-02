import MyLib as h
import math

def main() :
    level = input("Masukkan level yang kamu pilih (Easy(E)/Medium(M)/Hard(H)) : ")
    optLevel = ["H", "E", "M"]
    if level.upper() not in optLevel :
        print("Pilihan level yang kamu masukkan salah")
        return

    h.initScreen(0, 10, 0, 10)
    h.setPlayerPosition(0, 0)
    h.setGoal()
    h.spawnEnemies(level)
    h.displayInitialStats(level)

    while True :
        move = input("Gerak (atas(U)/bawah(D)/kiri(L)/kanan(R)) : ")
        optMove = ["U", "D", "L", "R"]
        if move.upper() not in optMove :
            print("Pilihan yang kamu masukan salah")
            break
        if h.checkPlayerMove(move) == False :
            break

if __name__ == "__main__" :
    main()