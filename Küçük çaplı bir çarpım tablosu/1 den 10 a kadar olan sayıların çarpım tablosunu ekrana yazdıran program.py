# 1'den 10'a kadar olan sayıların çarpım tablosunu ekrana yazdıran program.

for x in range(1,11):
    
    print("********************")
    
    for y in range(1,11):
        
        print("{} x {} = {}".format(x,y,x*y))