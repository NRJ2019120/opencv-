"""计算并显示直方图"""

# cv2.calcHist()
import cv2
import numpy as np

def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0, 255])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    print(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)

    return histImg

image = cv2.imread("cat.jpg")
b, g, r = cv2.split(image)
hist = cv2.calcHist([image], [0],  # 使用的通道
                    None,  # 没有使用mask
                    [256],  # HistSize
                    [0.0, 255.0])  # 直方图柱的范围

b, g, r = cv2.split(image)

histImgB = calcAndDrawHist(b, [255, 0, 0])
histImgG = calcAndDrawHist(g, [0, 255, 0])
histImgR = calcAndDrawHist(r, [0, 0, 255])

cv2.imshow("histImgB", histImgB)
cv2.imshow("histImgG", histImgG)
cv2.imshow("histImgR", histImgR)
cv2.imshow("Img", image)
cv2.waitKey(0)
cv2.destroyAllWindows()

#反向投影
"""
反向投影可以用来做图像分割，寻找感兴趣区间。它会输出与输入图像大小相同的图像，每一个像素值代表了输入图像上对应点属于目标对象的概率，简言之，输出图像中像素值越高的点越可能代表想要查找的目标。直方图投影经常与camshift（追踪算法）算法一起使用。

算法实现的方法，首先要为包含我们感兴趣区域的图像建立直方图（样例要找一片草坪，其他的不要）。被查找的对象最好是占据整个图像（图像里全是草坪）。最好使用颜色直方图，物体的颜色信息比灰度图像更容易被分割和识别。再将颜色直方图投影到输入图像查找目标，也就是找到输入图像中每一个像素点的像素值在直方图中对应的概率，这样就得到一个概率图像，最后设置适当的阈值对概率图像进行二值化。
"""
import cv2
import numpy as np
from matplotlib import pyplot as plt
"""
函数 cv2.calcBackProject()直接实现反向投影，参数与cv2.calcHist基本一致。其中一个参数是要查找的目标的直方图。在使用目标直方图反向投赢钱应该进行归一化处理。返回结果是一个概率图像，然后进行圆盘形状卷积操作，再二值化。
"""

# roi是我们需要找到的对象或区域
roi = cv2.imread('cat_crop.jpg')
hsv = cv2.cvtColor(roi, cv2.COLOR_BGR2HSV)

# target是我们搜索的图像
target = cv2.imread('cat.jpg')
hsvt = cv2.cvtColor(target, cv2.COLOR_BGR2HSV)

# 计算对象的直方图
roihist = cv2.calcHist([hsv], [0,1], None, [180,256], [0,180,0,256])

# 标准化直方图，并应用投影
cv2.normalize(roihist, roihist, 0, 255, cv2.NORM_MINMAX)
dst = cv2.calcBackProject([hsvt], [0,1], roihist, [0,180,0,256], 1)

# 与磁盘内核进行卷积
disc = cv2.getStructuringElement(cv2.MORPH_ELLIPSE, (5,5))
cv2.filter2D(dst, -1, disc, dst)

# 阈值、二进制按位和操作
ret, thresh = cv2.threshold(dst, 50, 255, 0)
thresh = cv2.merge((thresh, thresh, thresh))
res = cv2.bitwise_and(target, thresh)

res = np.vstack((target, thresh, res))
cv2.imshow('res', res)
cv2.waitKey()