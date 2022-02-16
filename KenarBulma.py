#Kenar Bulma Algoritmalarının Uygulanması - RobertCross Aİ2FC TEAM App
import numpy as np
from PIL import Image
#Author = @voidstring
imageAdrr = "C:/Users/Emre/Desktop/Deneme.jpg"
myİmage = Image.open(imageAdrr)
myİmage = np.array(myİmage)

robertCrossX = np.array([[1,0],[0,-1]])
robertCrossy = np.array([[0,1],[-1,0]])


def Compute(i, j):
    RenkR = int(myİmage[i][j][0])
    RenkG = int(myİmage[i][j][1])
    RenkB = int(myİmage[i][j][2])
    P = (RenkR + RenkG + RenkB)/3
    return P


for i in range(0,myİmage.shape[0]-1):
    for j in range(0,myİmage.shape[1]-1):
            #x,y
        p1 = Compute(i,j)
        p2 = Compute(i+1,j)
        p3 = Compute(i,j+1)
        p4 = Compute(i+1,j+1)
        x = abs(p1-p4)
        y = abs(p2-p3)
        robertCrossVal = x + y
        if robertCrossVal > 255: robertCrossVal = 255
        myİmage[i][j] = np.array([robertCrossVal,robertCrossVal,robertCrossVal])
            
resultMyİmage = Image.fromarray(myİmage)
resultMyİmage.save('resultMyİmage.png')