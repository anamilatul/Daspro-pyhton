from MyLib import *
from Globals import *

def main() :
    NIM = str(input("Masukkan NIM : "))
    nama = str(input("Masukkan Nama : "))
    matkul = [str]*10
    nilai = [int]*10
    inputMatkul(matkul)
    inputNilai(nillai)
    DisplayTranskrip(NIM, nama, matkul, nilai)

if __name__ == "__main__" :
    main()