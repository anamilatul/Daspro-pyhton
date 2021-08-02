def Hsljumlah(arr,N) :
    total = 0
    for i in range(0,N):
        total += arr[i]
    return total

def Hslaverage(arr,N) :
    total = Hsljumlah(arr,N)
    return total / N

def Hslmedian(arr,N) :
    x = [float]*N
    for i in range (0,N) :
        x[i] = arr[i]
    x = sorted(x)
    print("Sorted array : ",x)
    if N % 2 == 0 : #genap
        dat1 = N / 2
        dat2 = dat1 + 1
        nilai1 = x[int(dat1) - 1]
        nilai2 = x[int(dat2) - 1]
        median = (nilai1 + nilai2) / 2
        return median
    else : #ganjil
        dat = (N / 2) + 0.5
        median = x[int(dat) - 1]
        return median

def HslNilaiTerkecil(arr,N) :
    nilaiTerkecil = arr[0]
    for i in range (1,N) :
        if arr[i] < nilaiTerkecil :
            nilaiTerkecil = arr[i]
    return nilaiTerkecil

def HslNilaiTerbesar(arr,N) :
    nilaiTerbesar = arr[0]
    for i in range(1,N) :
        if arr[i] > nilaiTerbesar :
            nilaiTerbesar = arr[i]
    return nilaiTerbesar
    