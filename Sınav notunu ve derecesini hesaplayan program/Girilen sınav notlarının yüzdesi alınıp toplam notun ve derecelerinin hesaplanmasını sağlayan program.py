# Kullanıcının girdiği 1.vize 2.vize ve final sınavlarının sonucuna göre aldığı not ve derecesini hesaplayan program.
# 1. ve 2. vizenin %30'u, final sınavının ise %40'ı alınacak.
# Not sınırları ve dereceleri Dokuz Eylül Üniversitesinin kendi sitesinden alınmıştır.

print("Sınavlarınızın sonucuna göre notunuzu ve derecenizi hesaplayan programa hoşgeldiniz.\n")

a=float(input("1.vize sınavınızın sonucu: "))

b=float(input("2.vize sınavınızın sonucu: "))

c=float(input("Final sınavınızın sonucu: "))

totalNote= a*3/10 + b*3/10 + c*4/10

if totalNote >= 90:
    
    print("Toplam notunuz: {} ve dereceniz 'AA'".format(totalNote))
    
elif totalNote >= 85:
    
    print("Toplam notunuz: {} ve dereceniz 'BA'".format(totalNote))
    
elif totalNote >= 80:
    
    print("Toplam notunuz: {} ve dereceniz 'BB'".format(totalNote))
    
elif totalNote >= 75:
    
    print("Toplam notunuz: {} ve dereceniz 'CB'".format(totalNote))
    
elif totalNote >= 70:
    
    print("Toplam notunuz: {} ve dereceniz 'CC'".format(totalNote))
    
elif totalNote >= 65:
    
    print("Toplam notunuz: {} ve dereceniz 'DC'".format(totalNote))
    
elif totalNote >= 60:
    
    print("Toplam notunuz: {} ve dereceniz 'DD'".format(totalNote))
    
elif totalNote >= 50:
    
    print("Toplam notunuz: {} ve dereceniz 'FD'".format(totalNote))
    
elif totalNote < 50:
    
    print("Toplam notunuz: {} ve dereceniz 'FF'".format(totalNote))
    
    
    