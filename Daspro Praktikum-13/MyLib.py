from Globals import *

#Kasus 1
def inpNilai(nama, angka, huruf) :
    global mataKuliah
    global nilaiAngka
    global nilaiHuruf

    mataKuliah.append(nama)
    nilaiAngka.append(angka)
    nilaiHuruf.append(huruf)
# def kasusPertama() :
#     NIM = input("Masukkan NIM mahasiswa : ")
#     namaMhs = input("Masukkan nama mahasiswa : ")
#     jumlahMataKuliah = int(input("Jumlah Mata kuliah yang ingin dihitung : "))


#     n = 0
#     IPK = 0
#     while n < jumlahMataKuliah :
#         a = input("Masukkan Mata Kuliah : ")
#         x = int(input("Masukkan nilai dari mata kuliah yang diinputkan : "))
#         if x >= 85 and x <= 100 :
#             nilai(a, x, 'A')
#             IPK += 4
#             n += 1
#         elif x >= 70 :
#             nilai(a, x, 'B')
#             IPK += 3
#             n += 1
#         elif x >= 60 :
#             nilai(a, x, 'C')
#             IPK += 2
#             n += 1
#         elif x >= 50 :
#             nilai(a, x, 'D')
#             IPK += 1
#             n += 1
#         elif x >= 0 :
#             nilai(a, x, 'E')
#             IPK += 0
#             n += 1
#         else :
#             print("Nilai yang anda inputkan salah")
#     #output
#     print("NIM : ", NIM)
#     print("Nama : ", namaMhs)

#     # global.nilai
#     for i in range (jumlahMataKuliah) :
#         print("Mata Kuliah ",nilai[0][i], "dengan Nilai Angka ",nilai[1][i], "dan dengan Nilai Huruf ",nilai[2][i] )

#     #Menghitung IPK
#     IPK = IPK / jumlahMataKuliah
#     print ("IPK : ", IPK)
#     if IPK >= 3.5 :
#         print("Cumlaude")
#     else :
#         print("Tidak Cumlaude")

#Kasus 2
def kasusKedua() :
    nilai = list(input("Masukkan nilai huruf :").split())
    if len (nilai) < 5 or 'E' in nilai:
        print("Tidak Lulus")
    else :
        print("Lulus")