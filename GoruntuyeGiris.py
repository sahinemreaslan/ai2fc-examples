import cv2
import numpy as np

resim= cv2.imread("deneme.jpg")

#cv2.imshow("kus resmi",resim)
# resim[100,100]= [255,255,255]   # belirlediğimiz kordinatlarda gridiğimiz rgb piksel değerleri ile değiştirdik

# resim[x_eksein][y_ekseni][kanalı_Belirtir] = 255
# 3 kanallı ve her kanal 8 bit ile ifade ediliyorsa 
# 24 bitlik bir görüntü

#     R           G           B
# 1111 1111 + 1111 1111 + 1111 1111 =
#2^0*1+2^1*1+...2^7*1 = 128+64+32+16+8+4+2+1 = 255
# [x][y][0] = 255
# [x][y][1] = 255
# [x][y][2] = 255



x_ekseni, y_ekseni, kanal_sayisi = resim.shape
print(kanal_sayisi)
print(x_ekseni)
print(y_ekseni)


for i in range(648):
    for j in range(624):
        for k in range(0,3):
            resim[x_ekseni][y_ekseni][kanali belirtir] = (0-255 arasinda deger)
            
for i in range(648):
    for j in range(624):     
        resim[x_ekseni][y_ekseni] = (0-255,0-255,0-255)

#cv2.imshow("kus resmi",resim)
cv2.waitKey(0)
cv2.destroyAllWindows()