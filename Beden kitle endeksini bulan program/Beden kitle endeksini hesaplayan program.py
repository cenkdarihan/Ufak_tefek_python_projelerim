print("Beden kitle endeksini hesaplayan programa hoşgeldiniz, lütfen kilo ve boy değerlerini giriniz.\n")

kilo=float(input("Kilo değeri: "))
boy=float(input("Boy değeri (metre cinsinden): "))
BKI = kilo / (boy ** 2)
print("{}" "{:.2f}".format("Beden kitle endeksi: ", BKI))

if BKI < 18.5 :
    print("Zayıfsınız.")

elif 18.5 < BKI < 24.9 :
    print("Beden kitle indeksiniz normal duzeydedir..")

elif 25 < BKI < 29.9 :
    print("Beden kitle indeksinde ortalama uzerindesiniz..")

elif 30 < BKI < 34.9 :
    print("Beden kitle indeksine gore birinci derece obezsiniz.")

elif 35 < BKI < 39.9 :
    print("Beden kitle indeksine gore ikinci derece obezsiniz.")

elif BKI > 40 :
    print("Beden kitle indeksine gore ucuncu derece obezsiniz.")
