import cv2
import numpy as np

"""
膨胀、腐蚀、开、闭运算是数学形态学最基本的变换。
本文主要针对二值图像的形态学
膨胀：把二值图像各1像素连接成分的边界扩大一层（填充边缘或0像素内部的孔）；
腐蚀：把二值图像各1像素连接成分的边界点去掉从而缩小一层（可提取骨干信息，去掉毛刺，去掉孤立的0像素）；
开：先腐蚀再膨胀，可以去掉目标外的孤立点
闭：先膨胀再腐蚀，可以去掉目标内的孔。

cv2.erode()
cv2.dilate()
cv2.morphologyEx()
cv2.getStructuringElement()
"""

#十字形结构元素
element = cv2.getStructuringElement(cv2.MORPH_CROSS,(5,5))
element2 = cv2.getStructuringElement(cv2.MORPH_ELLIPSE,(5,5))
# NpKernel = np.uint8(np.zeros((5,5)))
# for i in range(5):
# 	NpKernel[2, i] = 1
# 	NpKernel[i, 2] = 1
print(element2)
print(element)

#腐蚀和膨胀

img = cv2.imread('cat.jpg')
# OpenCV定义的结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))

# 腐蚀图像
eroded = cv2.erode(img,kernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded Image", eroded)

# 膨胀图像
dilated = cv2.dilate(img, kernel)
# 显示膨胀后的图像
cv2.imshow("Dilated Image", dilated)
# 原图像
cv2.imshow("Origin", img)

# NumPy定义的结构元素
NpKernel = np.uint8(np.ones((3, 3)))
Nperoded = cv2.erode(img, NpKernel)
# 显示腐蚀后的图像
cv2.imshow("Eroded by NumPy kernel", Nperoded)

cv2.waitKey(0)
cv2.destroyAllWindows()


img = cv2.imread('cat.jpg', 0)
# 定义结构元素
kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))

# 闭运算
closed = cv2.morphologyEx(img, cv2.MORPH_CLOSE, kernel)
# 显示腐蚀后的图像
cv2.imshow("Close", closed)

# 开运算
opened = cv2.morphologyEx(img, cv2.MORPH_OPEN, kernel)
# 显示腐蚀后的图像
cv2.imshow("Open", opened)

cv2.waitKey(0)
cv2.destroyAllWindows()