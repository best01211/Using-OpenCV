import matplotlib.pyplot as plt
import cv2

# 컬러 영상 출력
# BGR 형식으로 이미지를 로드합니다.
imgBGR = cv2.imread('cat.bmp')

# BGR 이미지를 RGB 형식으로 변환합니다.
imgRGB = cv2.cvtColor(imgBGR, cv2.COLOR_BGR2RGB)

# 축 라벨을 끕니다.
plt.axis('off')

# RGB 이미지를 출력합니다.
plt.imshow(imgRGB)
plt.show()

# 그레이스케일 영상 출력
# 이미지를 그레이스케일 형식으로 로드합니다.
imgGray = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

# 축 라벨을 끕니다.
plt.axis('off')

# 그레이스케일 이미지를 회색 컬러맵으로 출력합니다.
plt.imshow(imgGray, cmap='gray')
plt.show()

# 두 개의 영상을 함께 출력
# 1행 2열의 서브플롯을 생성하고 첫 번째 서브플롯을 현재 축으로 설정합니다.
plt.subplot(121)

# 축 라벨을 끕니다.
plt.axis('off')

# 첫 번째 서브플롯에 RGB 이미지를 출력합니다.
plt.imshow(imgRGB)

# 두 번째 서브플롯을 현재 축으로 설정합니다.
plt.subplot(122)

# 축 라벨을 끕니다.
plt.axis('off')

# 두 번째 서브플롯에 그레이스케일 이미지를 회색 컬러맵으로 출력합니다.
plt.imshow(imgGray, cmap='gray')

# 결합된 플롯을 출력합니다.
plt.show()
