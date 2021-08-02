import MyLib as b

def main() :
    minimum_nilaiHuruf = 5
    nilai = list(map(str,input("Masukkan nilai huruf (pisahkan dengan spasi) : ").split(" ")))
    if len(nilai) < minimum_nilaiHuruf or 'E' in nilai :
        print("Tidak Lulus")
    else :
        print("Lulus")

if __name__ == "__main__" :
    main()