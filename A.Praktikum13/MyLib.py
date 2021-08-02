def inputMatkul(mataKuliah) :
    for i in range(len(mataKuliah)) :
        inputMatkul = input("Masukkan Nama Mata Kuliah : ")
        mataKuliah[i] = inputMatkul
    return mataKuliah

def inputNilai(nilai) :
    for i in range(len(nilai)) :
        inputNilai = int(input("Masukkan Nilai dari Mata Kuliah yang sudah diinputkan : "))
        nilai[i] = inputNilai
    return nilai

def displayTranscript(nim, nama, mataKuliah, nilai) :
    ipk = 0
    print("NIM : ", nim)
    print("Nama : ", nama)
    for i in range(len(mataKuliah)) :
        huruf = hsl_nilaiHuruf(nilai[i])
        ipk += hsl_IPK(huruf)
        print("Mata Kuliah ", mataKuliah[i], "dengan Nilai Angka", str(nilai[i]), "dan Nilai Huruf", huruf)

    rataRataIPK = ipk /len(mataKuliah)
    print("IPK : ", str(rataRataIPK))
    if rataRataIPK >= 3.5 :
        print("Keterangan : Cumlaude")
    else :
        print("Keterangan : Tidak Cumlaude")

def hsl_nilaiHuruf(nilaiAngka) :
    if nilaiAngka >= 85 and nilaiAngka < 100 :
        nilaiHuruf = 'A'
    elif nilaiAngka >= 70 :
        nilaiHuruf = 'B'
    elif nilaiAngka >= 60 :
        nilaiHuruf = 'C'
    elif nilaiAngka >= 50 :
        nilaiHuruf = 'D'
    elif nilaiAngka >= 0 :
        nilaiHuruf = 'E'
    else :
        print("Input tidak valid")
    return nilaiHuruf

def hsl_IPK(nilaiHuruf) :
    ipk = 0
    if nilaiHuruf == 'A' :
        ipk = 4
    elif nilaiHuruf == 'B' :
        ipk = 3
    elif nilaiHuruf == 'C' :
        ipk = 2
    elif nilaiHuruf == 'D' :
        ipk = 1
    elif nilaiHuruf == 'E' :
        ipk = 0
    return ipk