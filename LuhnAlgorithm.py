kartno = input("Kartin on yuzunde bulunanan 16 sayiyi gir:") #string ifadeyi alÄ±yoruz

cifttop = 0
tektop = 0

kart = list(kartno.strip(" ")) #tip dÃ¶nÃ¼ÅÃ¼mÃ¼ type casting (string to list)
#kart = ['1','3','5','1','3','5','1','3','5','1','3','5','1','3','5','1'] #string listesi
#kart = [1,3,5,1,3,5,1,3,5,1,3,5,1]#int listesi

#kart listesinin uzunluÄunu hesaplar
for j in range(0, len(kart)): #len fonksiyonu uzunluÄu
    kart[j] = int(kart[j])

#kart = [3254 3298 2853 1293]
'''
Önce çift haneleri toplayalım.
2+4+2+8+8+3+2+3 = 32

Tek hanede ki rakamları 2’ye çarparak sonuç olarak çıkan sayıların tekrardan rakamlarını toplayalım.
3×2 = 6         5×2 = 10          3×2= 6       9×2 = 18     2×2 = 4     5×2 = 10     1×2 = 2       9×2 = 18

Şimdi bu sayıların rakamlarını toplayalım.

6 + 1 + 0 + 6 + 1 + 8 + 4 + 1 + 0 + 2 + 1 + 8 = 38

Çift hanede ki rakamlara uygulanan işlem sonrası sonuç = 32

Tek hanede ki rakamlara uygulanan işlem sonrası sonuç = 38

Çift ve tek hanelere uygulanan işlem sonucu elde ettiğimiz 2 farklı sayıyı toplayıp 10’a göre mod alıyoruz.Eğer ki kalan sıfırsa yani 10’a tam bölünüyorsa kredi kartı numarası doğrudur.
32 + 38 = x(mod10)     x 0’a eşit olduğundan görüldüğü gibi bu kredi kartı numarası doğrudur.

'''
for i in range(0,16):
    if i%2 == 0: #tek indisler
    
        if (kart[i]*2) >= 10:
            islem = 1 + (kart[i]*2)%10
            tektop = tektop + islem
        else:
            tektop = tektop + (kart[i]*2) 
            print(tektop)
    
    else: #cift indisler
        cifttop = cifttop + kart[i]

if((cifttop+tektop) % 10 == 0):
    print("kart numarasi dogrudur")
else:   
    print("kart numarasi yanlistir")    

print(cifttop)
print(tektop)