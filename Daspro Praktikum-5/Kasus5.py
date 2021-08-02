#Program uang bulanan anak kos
#Kamus
uang = 0

#Algoritma
uang = int(input("Masukkan jumalah uang :"))
if uang >= 1200000 :
    if uang < 1700000 :
        print("Soni tidak bisa menonton konser karena uang kurang")
    elif uang >= 1700000 and uang < 2200000 :
        print("Soni jadi menonton konser dengan tempat duduk biasa")
    elif uang >= 2200000 :
        print("Soni jadi menonton konser dengan tempat duduk VIP")
else :
    print("Input tidak valid")