#Program tukar tambah motor
#Kamus
tahunMotor = 0

#Algoritma
tahunMotor = int(input("Masukkan tahun motor anda :"))
if (tahunMotor >= 2020) :
    print("Motor sudah tahun 2020")
else :
    selisih = 2020 - tahunMotor
    bayar = selisih * 2000000
    print("Biaya tambahan yang harus dibayarkan :" , bayar)