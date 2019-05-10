"""OpenCV Python教程之图像元素的访问、通道分离与合并"""
import cv2
import numpy as np

#访问像素
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

if __name__ == '__main__':
    img = cv2.imread("cat.jpg")
    saltImage = salt(img, 500)
    cv2.imshow("Salt", saltImage)
    print(np.random.random())
    cv2.waitKey(0)
    cv2.destroyAllWindows()

#分离合并channl   spilt()

img = cv2.imread("cat.jpg")
b, g, r = cv2.split(img)
cv2.imshow("Blue", r)
cv2.imshow("Red", g)
cv2.imshow("Green", b)
cv2.waitKey(0)
cv2.destroyAllWindows()
#合并通道
merged = cv2.merge([b,g,r])
# mergedByNp = np.stack()