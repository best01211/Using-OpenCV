import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
imgBGR = cv2.imread('cat.bmp')
# imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

plt.axis('off')
plt.imshow(cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB))
plt.show()

# gray scale 영상 출력
imgGray = cv2.imread('cat.bmp',cv2.IMREAD_GRAYSCALE)

plt.axis('off')
plt.imshow(imgGray,cmap='gray')
plt.show()

# 두개의 영상을 함께 출력
plt.subplot(121), plt.axis('off'), plt.imshow(cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB))
plt.subplot(122), plt.axis('off'), plt.imshow(imgGray, cmap='gray')

plt.show()