from MyLib import *
from Globals import *

def main():
    #kasus1
    kasusPertama()
    global dok
    print("Daftar semua elemen list : ",dok)

    #kasus2
    dok = list(map(float,input("Masukkan angka yang ada dalam list : ").split(" "))) #Contoh inputan dg spasi
    print("Jumlah seluruh elemen list : ",sumNana())
    print("rata ratanya : ", avgNana())
    print("Median dari list yang ada : ", medianNana())
    print("Nilai terkecil dari list : ",minNana())
    print("Nilai terbesar dari list : ", maxNana())

    #kasus3
    kasusketiga()

if __name__ == "__main__" :
    main()