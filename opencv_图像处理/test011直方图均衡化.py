"""
在图像处理中，直方图均衡化一般用来均衡图像的强度，或增加图像的对比度。在介绍使用直方图均衡化来拉伸图像的直方图之前，先介绍使用查询表的方法。

观察上图中原始图像的直方图，很容易发现大部分强度值范围都没有用到。因此先检测图像非0的最低（imin）强度值和最高（imax）强度值。
将最低值imin设为0，最高值imax设为255。中间的按255.0*(i-imin)/(imax-imin)+0.5)的形式设置。

result = cv2.LUT(image, lut)
"""
#使用查找表来拉伸直方图
import cv2
import numpy as np

def calcAndDrawHist(image, color):
    hist = cv2.calcHist([image], [0], None, [256], [0.0, 255.0])
    minVal, maxVal, minLoc, maxLoc = cv2.minMaxLoc(hist)
    histImg = np.zeros([256, 256, 3], np.uint8)
    hpt = int(0.9 * 256)

    for h in range(256):
        intensity = int(hist[h] * hpt / maxVal)
        cv2.line(histImg, (h, 256), (h, 256 - intensity), color)

    return histImg

image = cv2.imread("cat.jpg",0)
# print(type(image))
# exit()
lut = np.zeros(256, dtype=image.dtype)  # 创建空的查找表

hist = cv2.calcHist([image],  # 计算图像的直方图
                    [0],  # 使用的通道
                    None,  # 没有使用mask
                    [256],  # it is a 1D histogram
                    [0.0, 255.0])

minBinNo,maxBinNo = 0,255


histimg = calcAndDrawHist(hist,[255, 0, 0])

# 计算从左起第一个不为0的直方图柱的位置
for binNo, binValue in enumerate(hist):
    if binValue != 0:
        minBinNo = binNo
        break
# 计算从右起第一个不为0的直方图柱的位置
for binNo, binValue in enumerate(reversed(hist)):
    if binValue != 0:
        maxBinNo = 255 - binNo
        break
print(minBinNo, maxBinNo)

#生成查找表，方法来自参考文献1第四章第2节
for i, v in enumerate(lut):
    # print(i)
    if i < minBinNo:
        lut[i] = 0
    elif i > maxBinNo:
        lut[i] = 255
    else:
        lut[i] = int(255.0 * (i - minBinNo) / (maxBinNo - minBinNo) + 0.5)

# 计算
result = cv2.LUT(image, lut)
histresult = cv2.calcHist([image],[0],None,[256],[0.0, 255.0])
histresult = calcAndDrawHist(result,[255, 0, 0])

cv2.imshow("Result", result)
cv2.imshow("orgion",image)
cv2.imshow("histimg",histimg)
cv2.imshow("histresult",histresult)
# cv2.imwrite("LutImage.jpg", result)
cv2.waitKey(0)
cv2.destroyAllWindows()

#直方图均衡化 opencv函数实现
img = cv2.imread('cat.jpg',0)
equ = cv2.equalizeHist(img)

histimg = cv2.calcHist([img],[0],None,[256],[0.0, 255.0])
histequ = cv2.calcHist([equ],[0],None,[256],[0.0, 255.0])
hist1 = calcAndDrawHist(histimg,[255, 0, 0])
hist2 = calcAndDrawHist(histequ,[255, 0, 0])

cv2.imshow("histimg",hist1)
cv2.imshow("histequ",hist2)
cv2.imshow('equ',equ)
cv2.waitKey(0)
cv2.destroyAllWindows()

#直方图均衡化之NumPy函数实现

image = cv2.imread("country.jpg",0)
# print(type(image))
# exit()
lut = np.zeros(256)  # 创建空的查找表

hist, bins = np.histogram(image.flatten(),256, [0, 256])
cdf = hist.cumsum()  # 计算累积直方图
cdf_m = np.ma.masked_equal(cdf, 0)  # 除去直方图中的0值
cdf_m = (cdf_m - cdf_m.min()) * 255 / (cdf_m.max() - cdf_m.min())  # 等同于前面介绍的lut[i] = int(255.0 *p[i])公式
cdf = np.ma.filled(cdf_m, 0).astype('uint8')  # 将掩模处理掉的元素补为0

# 计算
result2 = cdf[image]
result = cv2.LUT(image, cdf)

cv2.imshow("OpenCVLUT", result)
cv2.imshow("NumPyLUT", result2)
cv2.waitKey(0)
cv2.destroyAllWindows()