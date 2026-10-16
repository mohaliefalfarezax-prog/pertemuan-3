sisi = int(input("masukan sisi persegi: "))
pilihan = (input("pilih luas/keliling: "))
sisi_persegi = sisi*sisi
keliling_persegi = 4*sisi

dict = {"luas": sisi_persegi, "keliling": keliling_persegi}
print(dict[pilihan])

