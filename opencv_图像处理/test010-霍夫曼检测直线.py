"""
Hough变换是经典的检测直线的算法。其最初用来检测图像中的直线，同时也可以将其扩展，以用来检测图像中简单的结构。
"""
import cv2
import numpy as np

img = cv2.imread("road.jpg", 0)

img = cv2.GaussianBlur(img,(3,3) ,0)
edges = cv2.Canny(img, 50, 150, apertureSize = 3)
lines = cv2.HoughLines(edges,1,np.pi/180,118)  # 这里对最后一个参数使用了经验型的值
# print(lines)
lines = lines.reshape((lines.shape[0],lines.shape[2]))
# print(lines.shape)
result = img.copy()
# print(lines)
# exit()
for line in lines:
    rho = line[0]  # 第一个元素是距离rho
    theta = line[1]  # 第二个元素是角度theta

    # print(line.shape)
    # print(rho)
    # print(theta)
    if (theta < (np.pi /4)) or (theta > (3 *np.pi/4.0)):  # 垂直直线
        # 该直线与第一行的交点
        pt1 = (int(rho /np.cos(theta)),0)
        # 该直线与最后一行的焦点
        pt2 = (int((rho -result.shape[0 ] *np.sin(theta) ) /np.cos(theta)) ,result.shape[0])
        # 绘制一条白线
        cv2.line( result, pt1, pt2, (255))
    else:  # 水平直线
        # 该直线与第一列的交点
        pt1 = (0 ,int(rho /np.sin(theta)))
        # 该直线与最后一列的交点
        pt2 = (result.shape[1], int((rho -result.shape[1 ] *np.cos(theta) ) /np.sin(theta)))
        # 绘制一条直线
        cv2.line(result, pt1, pt2, (255), 1)

cv2.imshow('Canny', edges )
cv2.imshow('Result', result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#概率霍夫变换
#观察前面的例子得到的结果图片，其中Hough变换看起来就像在图像中查找对齐的边界像素点集合。但这样会在一些情况下导致虚假检测，如像素偶然对齐或多条直线穿过同样的对齐像素造成的多重检测。

# 要避免这样的问题，并检测图像中分段的直线（而不是贯穿整个图像的直线），就诞生了Hough变化的改进版，即概率Hough变换（Probabilistic Hough）
# coding=utf-8
import cv2
import numpy as np

img = cv2.imread("road.jpg")

img = cv2.GaussianBlur(img, (3, 3), 0)
edges = cv2.Canny(img, 50, 150, apertureSize=3)
lines = cv2.HoughLines(edges, 1, np.pi / 180, 118)
result = img.copy()
lines = lines.reshape((lines.shape[0],lines.shape[2]))
# 经验参数
minLineLength = 200
maxLineGap = 15
lines = cv2.HoughLinesP(edges, 1, np.pi / 180, 80, minLineLength, maxLineGap)

for line in lines:
    for x1, y1, x2, y2  in line:
        cv2.line(img, (x1, y1), (x2, y2), (0, 255, 0), 2)

cv2.imshow('Result', img)
cv2.waitKey(0)
cv2.destroyAllWindows()