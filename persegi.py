sisi = int(input("Masukkan sisi persegi: "))
pilihan = input("pilih luas/keliling: ")

luas = sisi * sisi
keliling = 4 * sisi

hasil = {"luas": luas, "keliling": keliling}
pesan_error = 'Oops, hanya bisa input "luas" atau "keliling". Periksa kembali input-an Anda'

print(hasil.get(pilihan, pesan_error))