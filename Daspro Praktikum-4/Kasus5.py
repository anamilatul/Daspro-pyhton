#Program Luas tanah - Sengketa Lahan
#Kamus
luas = 0

#Algoritma
panjang = int(input("masukkan panjang :"))
lebar = int(input("masukkan lebar :"))
pilihan = input("Apakah kamu setuju? [setuju/tidak setuju] :")
luas = panjang*lebar
print("Luas tanah awal", float(luas))
if (pilihan == "Setuju" or pilihan == "setuju") :
    print("Luas tanah akhir :", float(luas/2))
else :
    print("Luas tanah akhir :", float(luas))
