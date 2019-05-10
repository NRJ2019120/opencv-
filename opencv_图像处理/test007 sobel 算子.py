"""
Sobel算子依然是一种过滤器，只是其是带有方向的。在OpenCV-Python中，使用Sobel的算子的函数原型如下：
dst = cv2.Sobel(src, ddepth, dx, dy[, dst[, ksize[, scale[, delta[, borderType]]]]])

"""

import cv2
import numpy as np

img = cv2.imread("cat.jpg")

x = cv2.Sobel(img, cv2.CV_16S, 1, 0)
y = cv2.Sobel(img, cv2.CV_16S, 0, 1)

absX = cv2.convertScaleAbs(x)  # 转回uint8
absY = cv2.convertScaleAbs(y)

dst = cv2.addWeighted(absX, 0.5, absY, 0.5, 0)

cv2.imshow("absX", absX)
cv2.imshow("absY", absY)
cv2.imshow("orgion",img)
cv2.imshow("Result", dst)

cv2.waitKey(0)
cv2.destroyAllWindows()

"""
图像中的边缘区域，像素值会发生“跳跃”，对这些像素求导，在其一阶导数在边缘位置为极值，这就是Sobel算子使用的原理——极值处就是边缘
Laplace函数实现的方法是先用Sobel 算子计算二阶x和y导数，再求和
dst = cv2.Laplacian(src, ddepth[, dst[, ksize[, scale[, delta[, borderType]]]]])"""

import cv2
import numpy as np

img = cv2.imread("cat.jpg", 0)

gray_lap = cv2.Laplacian(img, cv2.CV_16S, ksize=3)
dst = cv2.convertScaleAbs(gray_lap)

cv2.imshow('laplacian', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()