import cv2
import numpy as np

A = cv2.imread('cat.jpg',cv2.IMREAD_COLOR)
B = cv2.imread('dog.jpg',cv2.IMREAD_COLOR)
# A = np.resize(A,new_shape=(400,600))
# print(A.shape)
# exit()
# generate Gaussian pyramid for A
G = A.copy()
gpA = [G]
for i in np.arange(6):     #将苹果进行高斯金字塔处理，总共六级处理
    G = cv2.pyrDown(G)
    print(G.shape)
    gpA.append(G)
# generate Gaussian pyramid for B
# exit()

G = B.copy()
gpB = [G]
for i in np.arange(6):  # #将橘子进行高斯金字塔处理，总共六级处理
    G = cv2.pyrDown(G)
    gpB.append(G)

# generate Laplacian Pyramid for A
lpA = [gpA[5]]
for i in np.arange(5,0,-1):    #将苹果进行拉普拉斯金字塔处理，总共5级处理
    GE = cv2.pyrUp(gpA[i])
    # print(GE.shape)
    # print(gpA[i-1].shape)
    # exit()
    L = cv2.subtract(gpA[i-1],GE)  #(30, 44, 3),(29, 44, 3)
    lpA.append(L)
# generate Laplacian Pyramid for B
lpB = [gpB[5]]
for i in np.arange(5,0,-1):    #将橘子进行拉普拉斯金字塔处理，总共5级处理
    GE = cv2.pyrUp(gpB[i])
    L = cv2.subtract(gpB[i-1],GE) #注意图像相减操作，尺寸必须一致
    lpB.append(L)
# Now add left and right halves of images in each level
#numpy.hstack(tup)
#Take a sequence of arrays and stack them horizontally
#to make a single array.
LS = []
for la,lb in zip(lpA,lpB):
    rows,cols,dpt = la.shape
    ls = np.hstack((la[:,0:cols//2], lb[:,cols//2:]))    #将两个图像的矩阵的左半部分和右半部分拼接到一起
    LS.append(ls)
# now reconstruct
ls_ = LS[0]   #这里LS[0]为高斯金字塔的最小图片
for i in range(1,6):                        #第一次循环的图像为高斯金字塔的最小图片，依次通过拉普拉斯金字塔恢复到大图像
    ls_ = cv2.pyrUp(ls_)
    ls_ = cv2.add(ls_, LS[i])                #采用金字塔拼接方法的图像
# image with direct connecting each half
real = np.hstack((A[:,:cols//2],B[:,cols//2:]))   #直接的拼接

# cv2.imwrite('C:\\Users\\WLX\\Desktop\\Pyramid_blending2.jpg',ls_)
# cv2.imwrite('C:\\Users\\WLX\\Desktop\\Direct_blending.jpg',real)