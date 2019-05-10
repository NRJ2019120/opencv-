#1、读取图像，并把图像转换为灰度图像并显示
import cv2
im = cv2.imread("cat.jpg")  #读取图片
im_gray = cv2.cvtColor(im, cv2.COLOR_BGR2GRAY)   #转换了灰度化
cv2.imshow("gray",im_gray)  #显示图片
cv2.waitKey(0)

#2、固定阈值二值化
retval, im_at_fixed = cv2.threshold(im_gray, 50, 255, cv2.THRESH_BINARY)
#将阈值设置为50，阈值类型为cv2.THRESH_BINARY，则灰度在大于50的像素其值将设置为255，其它像素设置为0
cv2.imshow("im_at_fixed",im_at_fixed)
cv2.waitKey(0)

#附：固定阈值二值化处理利用cv2.threshold函数，此函数的原型为：
# cv2.threshold(src, thresh, maxval, type[, dst]) -> retval, dst
# 其中:
# 1、src 为输入图像；
# 2、thresh 为阈值；
# 3、maxval 为输出图像的最大值；
# 4、type 为阈值的类型；
# 5、dst 为目标图像。

# #附cv2.threshold函数的常用参数
# 1、cv2.THRESH_BINARY（黑白二值）
# 2、cv2.THRESH_BINARY_INV（黑白二值反转）
# 3、cv2.THRESH_TRUNC （得到的图像为多像素值）
# 4、cv2.THRESH_TOZERO
# 5、cv2.THRESH_TOZERO_INV

#3、算术平法的自适应二值化
im_at_mean = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_MEAN_C, cv2.THRESH_BINARY, 5, 10)
#上面我们将b设置为5，常数设置为10。
cv2.imshow("im_at_mean",im_at_mean)
cv2.waitKey(0)
#附：算术平均法的自适应二值化利用cv2.adaptiveThreshold实现，此函数的原型为：
# cv2.adaptiveThreshold(src, maxValue, adaptiveMethod, thresholdType, blockSize, C[, dst]) -> dst
# 其中:
# 1、src 为输入图像；
# 2、maxval 为输出图像的最大值；
# 3、adaptiveMethod 设置为cv2.ADAPTIVE_THRESH_MEAN_C表示利用算术均值法，设置为cv2.ADAPTIVE_THRESH_GAUSSIAN_C表示用高斯权重均值法；
# 4、thresholdType: 阈值的类型；
# 5、blockSize: b的值；
# 6、C 为从均值中减去的常数，用于得到阈值；
# 7、dst 为目标图像。

#4、高斯加权均值法自适应二值化
im_gaussion_mean = cv2.adaptiveThreshold(im_gray, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, 5, 7)
cv2.imshow("gaussion_mean",im_gaussion_mean)
cv2.waitKey(0)
cv2.destroyAllWindows()
#附：高斯加权均值法自适应二值化也是利用cv2.adaptiveThreshold， 此函数的原型与上述相同：



