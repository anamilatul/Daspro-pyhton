#Program menentukan predikat kelulusan berdasarkan IPK mahasiswa
#Kamus
ipk = 0.0

#Algoritma
ipk = float(input("Masukkan ipk :"))
if (ipk >= 3.5 and ipk <= 4.0) :
    print("Dengan pujian/Cumlaud")
elif (ipk >= 3.0 and ipk < 3.5) :
    print("Sangat memuaskan/Very Good")
elif (ipk >= 2.75 and ipk < 3.0) :
    print("Memuaskan/Good")
else :
    print("Inputan salah, ulangi kembali")