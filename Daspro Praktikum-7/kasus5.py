#Kamus
n = int(input("masukkan batas : "))

#Algoritma
for i in range(n):
    angka1,angka2 = map(float,input().split())
    hasil = angka1 + angka2
    print(hasil)