pelanggaran_haji = {
    "a": "Dam Haji Tamattu' dan Qiran",
    "hukuman_a": "Menyembelih seekor kambing / puasa 10 hari (lihat ketentuannya terlebih dahulu)",
    "b" : "Dam karena Melanggar Larangan Ihram (Takhyir dan Taqdir/Ta'dil)",
    "hukuman_b" : {
        "pilihan_1" : "Sembelih 1 kambing",
        "pilihan_2" : "Sedekah 3 sha' makanan kepada 6 orang fakir miskin (masing-masing ½ sha')",
        "pilihan_3" : "Puasa 3 hari"
    }
}

print("JENIS PELANGGARAN HAJI: \n" )
print("a.", pelanggaran_haji["a"])
print("Hukuman:", pelanggaran_haji["hukuman_a"], "\n")
print("b.", pelanggaran_haji["b"])
print("Pilihan hukuman:")
print("Pilihan 1", pelanggaran_haji["hukuman_b"]["pilihan_1"])
print("Pilihan 2", pelanggaran_haji["hukuman_b"]["pilihan_2"])
print("Pilihan 3", pelanggaran_haji["hukuman_b"]["pilihan_3"], "\n")

hukuman_jamaah = input("Apa pelanggaran Anda? Pilih salah satu dari di atas (cukup jawab a / b): ").lower()

if hukuman_jamaah == "a":
    print("Anda telah melakukan pelanggaran", pelanggaran_haji["a"])
    print("Hukuman Anda adalah", pelanggaran_haji["hukuman_a"])
elif hukuman_jamaah == "b":
    print("Anda telah melakukan pelanggaran", pelanggaran_haji["b"])
    pilihan_hukuman_b = input("Masukkan pilihan untuk hukuman Anda (cukup jawab dengan 1 atau 2 atau 3): ").lower()

    if pilihan_hukuman_b == "1":
        print("Hukuman Anda adalah", pelanggaran_haji['hukuman_b']['pilihan_1'])
    elif pilihan_hukuman_b == "2":
        print("Hukuman Anda adalah", pelanggaran_haji['hukuman_b']['pilihan_2'])
    elif pilihan_hukuman_b == "3":
        print("Hukuman Anda adalah", pelanggaran_haji['hukuman_b']['pilihan_3'])
    else:
        print("Maaf pilihan Anda tidak valid!")
else:
    print("Maaf masukan Anda tidak valid. Tolong masukkan a atau b")
