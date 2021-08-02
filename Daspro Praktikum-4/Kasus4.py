#Program Input panjang dan lebar
#Kamus
luas = 0

#Algoritma
panjang = float(input("panjang :"))
lebar = float(input("lebar :"))
luas = panjang*lebar
print("luas :", int(luas))
if (panjang == lebar) :
    print("ini persegi")