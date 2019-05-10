"""image show，read,save"""

import cv2
import numpy as np
#读取显示图像

img = cv2.imread("cat.jpg")
cv2.imshow("cat",img)
#获取图片属性
print(img.shape)
print(img.size)
print(img.dtype)
# exit()
#创建复制图像
# emptymage = np.zeros(img.shape, np.uint8)

emptymage = img.copy()
emptymage3=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
#emptyImage3[...]=0
cv2.imshow("empty1",emptymage)
cv2.imshow("empty2",emptymage3)

#保存图像
cv2.imwrite("cat2.jpg",img)
cv2.imwrite("cat3.jpg", img, [int(cv2.IMWRITE_JPEG_QUALITY), 5])
cv2.imwrite("./cat.png", img, [int(cv2.IMWRITE_PNG_COMPRESSION), 0])
cv2.waitKey(0)
cv2.destroyAllWindows()

#输出文本
frame = cv2.imread("country.jpg")
cv2.putText(frame, 'Hello World', (300,100), 0, 0.5, (0,0,255),2)
cv2.imshow("puttext",frame)
cv2.waitKey(0)
cv2.destroyAllWindows()
# exit()
#缩放图片

img = cv2.imread('country.jpg')
res = cv2.resize(img, None, fx=2, fy=2, interpolation=cv2.INTER_CUBIC)
#or
# height, width = img.shape[:2]
# res = cv2.resize(img, (2 * width, 2 * height), interpolation=cv2.INTER_CUBIC)
cv2.imshow("resize",res)
cv2.waitKey(0)
cv2.destroyAllWindows()
# exit()
#裁剪图片
img = cv2.imread("cat.jpg")
print(img.shape)
cropped = img[128:300, 256:512]  # 裁剪坐标为[y0:y1, x0:x1]
cv2.imshow("orgion",img)
cv2.imshow("cropped",cropped)
cv2.imwrite("cat_crop.jpg", cropped)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()
#图像平移

img = cv2.imread('country.jpg', 0)
rows, cols = img.shape

M = np.float32([[1, 0, 100], [0, 1, 50]])
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
# exit()
#图像旋转
img = cv2.imread('cat.jpg')
print(img.shape)
rows,cols,_ = img.shape

M = cv2.getRotationMatrix2D((cols / 2, rows / 2), 90, 1)
dst = cv2.warpAffine(img, M, (cols, rows))
cv2.imshow('img', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
# exit()
#仿射变换

img = cv2.imread('cat.jpg')
rows, cols, ch = img.shape

pts1 = np.float32([[50, 50], [200, 50], [50, 200]])
pts2 = np.float32([[10, 100], [200, 50], [100, 250]])

M = cv2.getAffineTransform(pts1, pts2)

dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('image', dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
exit()

#颜色变换
#cv2.cvtColor(input_image, flag)函数实现图片颜色空间的转换，flag 参数决定变换类型
# cv.Convert()：将图片从一个颜色空间转到另一个颜色空间
# cv.CvtColor(src, dst, code)

#下面的代码实现识别摄像视频中蓝色的部分
cap = cv2.VideoCapture(0)
while (1):
    # 读取视频的每一帧
    _, frame = cap.read()

    # 将图片从 BGR 空间转换到 HSV 空间
    hsv = cv2.cvtColor(frame, cv2.COLOR_BGR2HSV)

    # 定义在HSV空间中蓝色的范围
    lower_blue = np.array([110, 50, 50])
    upper_blue = np.array([130, 255, 255])

    # 根据以上定义的蓝色的阈值得到蓝色的部分
    mask = cv2.inRange(hsv, lower_blue, upper_blue)

    res = cv2.bitwise_and(frame, frame, mask=mask)

    cv2.imshow('frame', frame)
    cv2.imshow('mask', mask)
    cv2.imshow('res', res)
    k = cv2.waitKey(5) & 0xFF
    if k == 27:
        break
cv2.destroyAllWindows()