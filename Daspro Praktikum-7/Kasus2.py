#Kasus2 Copy Cat
#Kamus
n = 0

#Algoritma
n = int(input())
for i in range (n) :
    t = int(input())
    for num in range(t+1) :
        for j in range (num) :
            print(num, end=" ") #print number
        #supaya membuat garis baru pada segitiga
        print("\n")
        