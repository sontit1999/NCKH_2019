import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
import cv2
import math
from scipy import misc
img = [
            [23,12,18],
            [21,17,17],
            [19,10,18],
            [19,15,18]
      ]
# tim max cua ma tran img  -- true
max_img= max(max(x) for x in img)
min_img= min(min(x) for x in img)
#hàm tính WLD cua 1 toa do -- true
def wld(x,y):
     data=0
     if x!=0 and x!=len(img)-1 and y!=0 and y!= len(img[0])-1:
         for i in range(x-1,x+2):
                for j in range(y-1,y+2):
                    data=data+(img[x][y]-img[i][j])
         #return math.atan(2*data/img[x][y])
         return math.atan(2*data/img[x][y])
     else:
         return 0

# hàm nomernize của 1 điểm trong ma trận
def nomalize(a):
    max_matrix= max(max(x) for x in a)
    min_matrix = min(min(x) for x in a)
    for i in range(len(a)):
        for j in range(len(a[0])):
             a[i][j]= wld(i,j)
    print('image a')         
    print(a)
    #new_value = ((wld(1,1)-min_matrix)/(min_matrix-max_matrix))*255
    #print(new_value)

