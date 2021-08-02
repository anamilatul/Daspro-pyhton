#Program Korek Api
#Kamus
n = 0

#Algoritma
n = int(input("Masukkan batas :"))
for i in range (n) :
    angka = int(input())
    jumlah = 0
    if angka == 0 :
        jumlah = 6
    elif angka == 1 :
        jumlah = 2
    elif angka == 2 :
        jumlah = 5
    elif angka == 3 :
        jumlah = 5
    elif angka == 4 :
        jumlah = 4
    elif angka == 5 :
        jumlah = 5
    elif angka == 6 :
        jumlah = 6
    elif angka == 7 :
        jumlah = 3
    elif angka == 8 :
        jumlah = 7
    elif angka == 9 :
        jumlah = 6
    print("Banyaknya batang korek api :", jumlah)
    