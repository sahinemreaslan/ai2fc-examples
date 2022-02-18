import numpy as np
from PIL import Image
#Author = @voidstring
imageAdrr = "C:/Users/Emre/Desktop/Deneme.jpg"
myİmageOne = Image.open(imageAdrr)
myİmage = np.array(myİmageOne)

robertCrossX = np.array([[1,0],[0,-1]])
robertCrossy = np.array([[0,1],[-1,0]])


#numpy nedir ? Matris üzerinde işlem yapmamızı KOLAYLAŞTIRAN kütüphanedir.

def Compute_P(i, j):
    RenkR = int(myİmage[i][j][0])#8 BİT 0-255
    RenkG = int(myİmage[i][j][1])#8 BİT 0-255
    RenkB = int(myİmage[i][j][2])#8 BİT 0-255
    #+
    #------------------------------------------
    #24 BİT
    P = (RenkR + RenkG + RenkB)/3 # 8 BİT 0-255
    return P


for i in range(0,myİmage.shape[0]-1):
    for j in range(0,myİmage.shape[1]-1):
            #x,y
        p1 = Compute_P(i,j)#(x,y)
        p2 = Compute_P(i+1,j)#(x+1,y)
        p3 = Compute_P(i,j+1)#(x,y+1)
        p4 = Compute_P(i+1,j+1)##(x+1,y+1)
        x = abs(p1-p4)
        y = abs(p2-p3)
        robertCrossVal = x + y
        
        
        if robertCrossVal > 255: robertCrossVal = 255
        myİmage[i][j] = np.array([robertCrossVal])
            
resultMyİmage = Image.fromarray(myİmage)
resultMyİmage.save('resultMyİmage2.png')
