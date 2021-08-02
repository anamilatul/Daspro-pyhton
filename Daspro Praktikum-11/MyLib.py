from Globals import *
#kasus1
def kasusPertama() :
    global dok
    i = 1
    while True :
        nana = int(input("Elemen list ke-"+str((i))+" : "))
        if nana == 0 :
            break
        else :
            dok.append(nana)
        i+=1

#Kasus2

def sumNana() :
    global dok
    return sum(dok)

def avgNana() :
    global dok
    n = 0
    if dok is not None :
        for i in dok :
            n +=1
    return sumNana()/n

def medianNana() :
    global dok
    n = sorted (dok)
    print("Jika disorted maka : ", n)
    if n is not None:
            if len(n) %2 == 1 :
                return n [int((len(n)/2))]
            else :
                return (n[int((len(n)/2))] + n[int((len(n)/2))-1])/2

def minNana() :
    global dok
    if dok is not None :
        min=dok[0]
        for i in dok :
            if i < min :
                min=i
    return min

def maxNana() :
    global dok
    if len(dok) > 0 :
        max = dok [0]
        for i in dok :
            if i > max :
                max = i
    return max

#Kasus 3
def kasusketiga() :
    dok = list(map(int,input("Masukkan tahun : ").split(" ")))
    menang = 0
    for i in dok :
        if i <1990 or i > 2020 :
            print("input tidak valid")
            return
        if i % 2 != 0 :
                menang += 1
    print("Jumlah kemenangan club SC : "+str(menang))

    
