#Program Bug Fixing
#Kamus
ipk = 0
counter = 0
n = int(input("Masukkan batas makul"))
while counter < n :
    nilai = int(input("nilai makul ke-" +str(counter+1)+":"))
#Algoritma
n = int(input("Masukkan batas makul :"))
while counter < n :
    
    nilai = int(input("nilai makul ke-" +str(counter+1)+":"))
    if nilai >= 85 :
        ipk += 4 #samadengan ipk = ipk+4
    elif nilai >= 70 and nilai <85 :
        ipk += 3
    elif nilai >= 60 and nilai <70 :
        ipk += 2
    elif nilai >= 50 and nilai <60 :
        ipk += 1
    counter += 1
print("ipk :", ipk / counter)