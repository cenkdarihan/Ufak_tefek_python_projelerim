#Bu program dik kenarları girilen dik üçgenin hipotenüsünü bulur.
while True :
 print(" ")
 print("Dik kenarları girilen dik üçgenin hipotenüsünü bulan programa hoşgeldiniz, lütfen istenilen değerleri giriniz.")
 print(" ")
 dik1=int(input("1. dik kenarı giriniz: "))
 dik2=int(input("2. dik kenarı giriniz: "))
 print(" ")
 hipotenüs= dik1 ** 2 + dik2 ** 2
 print(" ")
 print("Hipotenüsün uzunluğu: ", hipotenüs ** 0.5)
