#Kasus1 Copy Cat
#Kamus
n = 0

#Algoritma
n = int(input())
for i in range (n) :
    a,b = map(int,input().split())
    if a > b:
        print(">")
    elif a < b:
        print("<")
    else :
        print("=")