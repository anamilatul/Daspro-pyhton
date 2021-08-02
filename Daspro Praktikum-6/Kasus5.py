#Program Cek bilangan prima
#Kamus
bil = 0
i = 0

#Algoritma
bil = int(input("Masukkan bilangan :"))
if bil > 1 :
    for i in range (2,bil) :
        if (bil % i) == 0 :
            print(bil, "Bukan bilangan prima")
            break
    else:
        print(bil, "Bilangan prima")
else:
    print(bil, "Bukan bilangan prima")