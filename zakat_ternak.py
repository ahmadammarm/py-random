hewan_ternak = int(input("Masukkan jumlah hewan ternak Anda (satuan ekor): "))

if 0 <= hewan_ternak < 40:
    zakat = 0
    print("Anda belum diwajibkan membayar zakat")
elif 40 <= hewan_ternak <= 120:
    zakat = 1
    print("Anda diwajibkan berzakat sebanyak", zakat, "ekor hewan ternak Anda")
elif 121 <= hewan_ternak <= 200:
    zakat = 2
    print("Anda diwajibkan berzakat sbanyak", zakat, "ekor hewan ternak Anda")
elif 201 <= hewan_ternak <= 300:
    zakat = 3
    print("Anda diwajibkan berzakat sebanyak", zakat, "ekor hewan ternak Anda")
elif hewan_ternak > 300:
    zakat = 3 + ((hewan_ternak - 300) // 100)
    print("Anda diwajibkan berzakat sebanyak", zakat, "ekor hewan ternak Anda")
else:
    print("Masukan tidak valid")
