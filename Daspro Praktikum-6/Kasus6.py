#Program uang anak kos
#Kamus
saldoAwal = 0
saldoAkhir = 0
pengeluaran = 0
i = 0

#Algoritma
saldoAwal = int(input("Masukkan saldo awal :"))
saldoAkhir = saldoAkhir + saldoAwal
while ( pengeluaran != -1):
    pengeluaran = int(input("Pengeluaran Soni hari ini (isikan -1 untuk keluar) :"))
    if (saldoAkhir < pengeluaran):
        print("Saldo tidak cukup")
        break
    elif (saldoAkhir >= pengeluaran and pengeluaran != -1):
        saldoAkhir = saldoAkhir - pengeluaran
print("Sisa saldo", saldoAkhir)