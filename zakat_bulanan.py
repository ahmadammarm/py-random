harga_emas = 1200000

nisab_bulanan = 85 * (harga_emas / 12)

print(nisab_bulanan)

gaji_bulanan = int(input("Masukkan gaji bulanan Anda: "))

if gaji_bulanan <= 0:
    print("Masukan Anda tidak valid")
    exit()

zakat = 2.5/100 * gaji_bulanan

if gaji_bulanan < nisab_bulanan:
    print("Anda belum diwajibkan mengeluarkan zakat")
elif gaji_bulanan >= nisab_bulanan:
    print("Anda wajib mengeluarkan zakat sebesar", zakat)
