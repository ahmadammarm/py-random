total_harta = int(input("Masukkan total harta Anda: "))

if total_harta <= 0:
    print("Tolong masukkan harta Anda dengan valid!")
    exit()

warisan_istri = total_harta / 8

print("Jumlah harta warisan untuk istri adalah Rp", warisan_istri)

sisa_harta = total_harta - warisan_istri

print("Jumlah sisa harta sekarang adalah Rp", sisa_harta)

jumlah_anak_laki = int(input("Masukkan jumlah anak laki-laki Anda: "))
jumlah_anak_perempuan = int(input("Masukkan jumlah anak perempuan Anda: "))

total_unit = (jumlah_anak_laki * 2) + (jumlah_anak_perempuan * 1)

if total_unit == 0:
    print("Tidak ada anak jadi tidak perlu pembagian lagi")
    exit()

else:
    unit = sisa_harta / total_unit

    print("1 unit warisan: Rp", unit)

    warisan_anak_laki = jumlah_anak_laki * (unit * 2)
    warisan_anak_perempuan = jumlah_anak_perempuan * unit

    print("Jumlah warisan yang didapatkan anak laki", warisan_anak_laki)
    print("Jumlah warisan yang didapatkan anak perempuan", warisan_anak_perempuan)