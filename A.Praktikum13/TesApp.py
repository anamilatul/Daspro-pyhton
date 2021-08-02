import MyLib as b

def main() :
    nim = input("NIM : ")
    nama = input("Nama : ")
    mataKuliah = [str]*10
    nilai = [int]*10
    b.inputMatkul(mataKuliah)
    b.inputNilai(nilai)
    b.displayTranscript(nim, nama, mataKuliah, nilai)

if __name__ == "__main__" :
    main()