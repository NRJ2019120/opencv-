"""过滤是信号和图像处理中基本的任务。其目的是根据应用环境的不同，选择性的提取图像中某些认为是重要的信息。
过滤可以移除图像中的噪音、提取感兴趣的可视特征、允许图像重采样，等等。其源自于一般的信号和系统理论，这里将不介绍该理论的细节。但本章会介绍关于过滤的基本概念，
以及如何在图像处理程序中使用滤波器

根据灰度分布的不同来区分不同的图像。但还有其他方面可以对图像进行分析。
我们可以观察图像中灰度的变化

，观察图像中这些变化的频率就构成了另一条分类图像的方法。这个观点称为频域。
而通过观察图像灰度分布来分类图像称为空间域。

频域分析将图像分成从低频到高频的不同部分。低频对应图像强度变化小的区域，
而高频是图像强度变化非常大的区域

，观察图像中这些变化的频率就构成了另一条分类图像的方法。这个观点称为频域。
而通过观察图像灰度分布来分类图像称为空间域。

滤波器是一个用来增强图像中某个波段或频率并阻塞（或降低）其他频率波段的操作。低通滤波器是消除图像中高频部分，
但保留低频部分。高通滤波器消除低频部分


result = cv2.medianBlur(image,5)
dst = cv2.blur(image,(5,5));
gaussianResult = cv2.GaussianBlur(img,(5,5),1.5)"""
#用低通滤波来平滑图像,低通滤波器的目标是降低图像的变化率。如将每个像素替换为该像素周围像素的均值
import cv2
import numpy as np
img = cv2.imread("cat.jpg", 0)
result = cv2.blur(img, (5, 5))
# result1 = cv2.boxFilter(img, -1, (5, 5))
gaussianResult = cv2.GaussianBlur(img,(5,5),1.5)#高斯模糊

cv2.imshow("Origin", img)
cv2.imshow("Blur", result)
cv2.imshow("gaussianresult",gaussianResult)

cv2.waitKey(0)
cv2.destroyAllWindows()

#中值滤波器 消除噪点

def salt(img, n):
    for k in range(n):
        i = int(np.random.random() * img.shape[1]);
        j = int(np.random.random() * img.shape[0]);
        if img.ndim == 2:
            img[j, i] = 255
        elif img.ndim == 3:
            img[j, i, 0] = 255
            img[j, i, 1] = 255
            img[j, i, 2] = 255
    return img


img = cv2.imread("cat.jpg", 0)
result = salt(img, 500)
median = cv2.medianBlur(result, 5)

cv2.imshow("Salt", result)
cv2.imshow("Median", median)

cv2.waitKey(0)
cv2.destroyAllWindows()