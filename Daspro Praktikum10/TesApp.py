from MyLib import *

def main () :
    data = "balonku ada lima, rupa-rupa warnanya"
    print("data : ",data)
    #buat inputan untuk variabel c1,c2, dan p
    c1 = input("c1 : ")
    c2 = input("c2 : ")
    p = input("p : ")

    print(panjangString(data))
    cariKarakter(c1,data)
    print(frekuensiKarakter(c2,data))

    if cekPalindrom(p) :
        print("Palindrom")
    else :
        print("Bukan palindrom")
        
if __name__ == "__main__" :
    main()