from Globals import *

def inputMatkul(a) :
    for __ in range (10) :
        Globals.nm_mataKuliah = str(input("Masukkan nama matkul : ")) #jika sudah selesai ketik "end" untuk keluar
        if Globals.nm_mataKuliah == "end" :
            break
        Globals.mataKuliah.append(Globals.nm_mataKuliah)

def inputNilai(n) :
    x = 0
    for __ in range (len(Globals.mataKuliah)) :
        Globals.nilai_input = int(input("Masukkan nilai "+Globals.mataKuliah[0+x] +" : "))
        x += 1
        Globals.nilai.append(Globals.nilai_input)
        if Globals.nilai_input >= 85 and Globals.nilai_input <100 :
            Globals.nilai_huruf = 'A'
            Globals.keterangan = 4
        elif Globals.nilai_input >= 70 :
            Globals.nilai_huruf = 'B'
            Globals.keterangan = 3
        elif Globals.nilai_input >= 60 :
            Globals.nilai_huruf = 'C'
            Globals.keterangan = 2
        elif Globals.nilai_input < 50 :
            Globals.nilai_huruf = 'D'
            Globals.keterangan = 1
        elif Globals.nilai_input >= 0 :
            Globals.nilai_huruf = 'E'
            Globals.keterangan = 0
        else :
            print("Nilai yang anda inputkan salah")

        Globals.keterangan_full.append(Globals.keterangan)
        Globals.huruf.append(Globals.nilai_huruf)
    
    Globals.ipk = sum(Globals.keterangan_full) / len(Globals.mataKuliah)
    if Globals.ipk >= 3.5 :
        Globals.ipk_keterangan = "Cumlaude"
    else :
        Globals.ipk_keterangan = "Tidak Cumlaude"

def DisplayTranskrip(o,p,q,r) :
    y = 0
    print("NIM : ", o)
    print("Nama : ", p)
    for __ in range (len(Globals.mataKuliah)) :
        print("Mata Kuliah", Globals.mataKuliah[0+y], "dengan Nilai Angka", str(Globals.nilai[0+y]), "dan dengan Nilai Huruf", Globals.huruf[o+y])
        y +=1
    print("IPK : ", Globals.ipk)
    print("Keterangan : ", Globals.ipk_keterangan)