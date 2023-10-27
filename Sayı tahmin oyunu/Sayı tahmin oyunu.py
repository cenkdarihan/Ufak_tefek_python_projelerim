# Sayı tahmin oyunu.

print("Sayı tahmin etme oyununa hoşgeldiniz, bakalım bilgisayarın tuttuğu sayıyı kısa sürede bulabilecek misiniz :)\n")


import random

sayi=random.randint(1,100)

tahmin=int(input("1 ile 100 arasında bir sayı tahmin ediniz: "))

while tahmin!=sayi:
    
    if sayi<tahmin:
        
        print("Girdiğiniz sayı tutulan sayıdan büyük.")
        
    elif sayi>tahmin:
        
        print("Girdiğiniz sayı tutulan sayıdan küçük.")
        
    tahmin=int(input("1 ile 100 arasında bir sayı tahmin ediniz: "))
    
print("Tebrikler bildiniz! Tutulan sayı: {} idi".format(sayi))