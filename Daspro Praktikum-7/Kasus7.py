#Program pulsa
#Kamus
import random
saldoAwal = int(input("Masukkan saldo awal :"))
tanggalLahir = int(input("Masukkan tanggal lahir mama :"))
tanggalLahirMama = 12
counter = 0.0
randcounter = random.randint(0,9)

#Algoritma
if tanggalLahir != tanggalLahirMama :
    print("Ini penipu!")
else:
    jumlahPulsa = int(input("Masukkan jumlah pulsa yang diinginkan mama :"))
    for i in range (randcounter) :
        while counter <= 0.5 :
            counter = random.random()
            print("Mohon tunggu. . . .")
            break
        if i == 2 :
            print("Transaksi gagal")
            break
        if jumlahPulsa > saldoAwal :
            print("Saldo tidak cukup")
            break
        if saldoAwal == jumlahPulsa :
            print("Transaksi", jumlahPulsa,"berhasil")
            break