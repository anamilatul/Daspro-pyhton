import MyLib as n

def main() :
    nana = 0
    nana = int(input("Panjang array yang diinginkan : "))
    arr = [float]*nana
    for i in range(0,nana) :
        arr[i] = float(input("Masukkan angka untuk Indeks ke-"+str(i)+" : "))

    jmlTotal = n.Hsljumlah(arr,nana)
    print("Jumlah totalnya : "+str(jmlTotal))

    average = n.Hslaverage(arr,nana)
    print("Rata - ratanya : "+str(average))

    median = n.Hslmedian(arr,nana)
    print("Mediannya : "+str(median))

    nilaiTerkecil = n.HslNilaiTerkecil(arr,nana)
    print("Nilai terkecilnya : "+str(nilaiTerkecil))

    nilaiTerbesar = n.HslNilaiTerbesar(arr,nana)
    print("Nilai terbesarnya : "+str(nilaiTerbesar))

if __name__ == "__main__" :
    main()