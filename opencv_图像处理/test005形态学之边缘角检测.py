"""里通过一个较复杂的例子介绍如何用形态学算子检测图像中的边缘和拐角（这里只是作为介绍形态学处理例子，
实际使用时请用Canny或Harris等算法）"""
"""
形态学检测边缘的原理很简单，
在膨胀时，图像中的物体会想周围“扩张”；腐蚀时，
图像中的物体会“收缩”。比较这两幅图像，
由于其变化的区域只发生在边缘。
所以这时将两幅图像相减，得到的就是图像中物体的边缘"""

import cv2
import numpy
#边缘检测
image = cv2.imread("cat.jpg",2)
# 构造一个3×3的结构元素
element = cv2.getStructuringElement(cv2.MORPH_RECT, (3, 3))
dilate = cv2.dilate(image, element)
erode = cv2.erode(image, element)

# 将两幅图像相减获得边，第一个参数是膨胀后的图像，第二个参数是腐蚀后的图像
result = cv2.absdiff(dilate, erode)

# 上面得到的结果是灰度图，将其二值化以便更清楚的观察结果
retval, result = cv2.threshold(result, 40, 255, cv2.THRESH_BINARY);
# 反色，即对二值图每个像素取反
result = cv2.bitwise_not(result)
# 显示图像
cv2.imshow("result", result)
cv2.waitKey(0)
cv2.destroyAllWindows()
#拐角检测
"""与边缘检测不同，拐角的检测的过程稍稍有些复杂。但原理相同，所不同的是先用十字形的结构元素膨胀像素，这种情况下只会在边缘处“扩张”，角点不发生变化。接着用菱形的结构元素腐蚀原图像，导致只有在拐角处才会“收缩”，而直线边缘都未发生变化。

第二步是用X形膨胀原图像，角点膨胀的比边要多。这样第二次用方块腐蚀时，角点恢复原状，而边要腐蚀的更多。所以当两幅图像相减时，只保留了拐角处"""

image = cv2.imread("cat.jpg", 0)
origin = cv2.imread("cat.jpg")
# 构造5×5的结构元素，分别为十字形、菱形、方形和X型
cross = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# 菱形结构元素的定义稍麻烦一些
diamond = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
diamond[0, 0] = 0
diamond[0, 1] = 0
diamond[1, 0] = 0
diamond[4, 4] = 0
diamond[4, 3] = 0
diamond[3, 4] = 0
diamond[4, 0] = 0
diamond[4, 1] = 0
diamond[3, 0] = 0
diamond[0, 3] = 0
diamond[0, 4] = 0
diamond[1, 4] = 0
square = cv2.getStructuringElement(cv2.MORPH_RECT, (5, 5))
x = cv2.getStructuringElement(cv2.MORPH_CROSS, (5, 5))
# 使用cross膨胀图像
result1 = cv2.dilate(image, cross)
# 使用菱形腐蚀图像
result1 = cv2.erode(result1, diamond)

# 使用X膨胀原图像
result2 = cv2.dilate(image, x)
# 使用方形腐蚀图像
result2 = cv2.erode(result2, square)

# result = result1.copy()
# 将两幅闭运算的图像相减获得角
result = cv2.absdiff(result2, result1)
# 使用阈值获得二值图
retval,result = cv2.threshold(result,40,255, cv2.THRESH_BINARY)
print(result.shape)
# 在原图上用半径为5的圆圈将点标出。
for j in range(result.size):
    y = j // result.shape[0]#   / ???
    x = j % result.shape[0]

    if result[x,y] == 255:
        cv2.circle(image, (y, x), 5, (255, 0, 0))

cv2.imshow("Result", image)
cv2.waitKey(0)
cv2.destroyAllWindows()
