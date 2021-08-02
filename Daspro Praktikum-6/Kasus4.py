#Program untuk menghitung rata - rata nilai dari nilai yang diinputkan
#Kamus
a = 0
n = 0.0
sum = 0
i = 0
rata2 = 0

#Algoritma
a = int(input("Masukkan jumlah bilangan :"))
while True :
    n = float(input("Masukkan bilangan :"))
    sum = sum + n 
    i = i + 1
    if i >= a :
        break
rata2 = int(sum/i)
print("Rata - rata bilangan :", rata2)
