import numpy as np
import scipy.ndimage as ndimage
import matplotlib.pyplot as plt
import cv2
import math
from scipy import misc
np.seterr(over='ignore')

# đọc ảnh 
img = cv2.imread('tit.jpg')
# tạo ma trận c có kích thước bằng ảnh
c = np.zeros((len(img), len(img[0])))
#chuyển ảnh về ảnh xám
img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
#làm mờ ảnh bằng gauss để giảm nhiễu
img = ndimage.gaussian_filter(img, sigma=2, order=0)
# hàm chuyển ma trận thành ảnh 
def convertArraytoImage(Array):
	flatNumpyArray = np.array(Array)
	print("kich thuoc anh: " + str(len(Array)) + " x " + str(len(Array[0])))
	# Convert the array to make grayscale image.
	grayImage = flatNumpyArray.reshape(len(Array), len(Array[0]))
	cv2.imwrite('output.png', grayImage)
#xuat ma tran
def xuatmang(a):
     for i in range(len(a)):
                for j in range(len(a[0])):
                    print(a[i][j])
#hàm tính WLD của 1 ảnh xám và trả ma trận mới vào ma trận c
def wld(a):
         for i in range(len(a)):
                for j in range(len(a[0])):
                    if(i!=0 and i!=len(a)-1 and j!=0 and j != len(a[0])-1):            
                        c[i][j] = int(math.atan(2*((a[i][j]-a[i-1][j-1])+(a[i][j]-a[i-1][j])+(a[i][j]-a[i-1][j+1])+(a[i][j]-a[i][j-1])+(a[i][j]-a[i][j+1])+(a[i][j]-a[i+1][j-1])+(a[i][j]-a[i+1][j])+(a[i][j])-a[i+1][j+1])/(a[i][j])))
#nomarlize
def nomalize(a):
    max_matrix= max(max(x) for x in a)
    min_matrix = min(min(x) for x in a)
    for i in range(len(a)):
        for j in range(len(a[0])):
            a[i][j] = ((a[i][j]-min_matrix)/(max_matrix-min_matrix))*255
wld(img)
nomalize(c)
convertArraytoImage(c)



