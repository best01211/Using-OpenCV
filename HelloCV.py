import cv2
import sys

print('Hello OpenCV', cv2.__version__)

# cv2.imread(filename, flags=None)
# filename은 파일명, flag는 영상 불러오는 옵션(gray, color)
img = cv2.imread('cat.bmp', cv2.IMREAD_GRAYSCALE)

if img is None:
    print('image load failed!')
    sys.exit()

# cv2.imwrite(filename, img,params=None)
# params은 파일 저장옵션이다 -> [cv2.IMWRITE_JPEG_QUALITY,80] : JPG 파일 압축률을 90%로 지정
cv2.imwrite('cat_gray.jpg',img)

# cv2.namedWindow(winname, flags=None)
# cv2.WINDOW_NORMAL : 영상 크기를 창 크기에 맞게 지정
# cv2.WINDOW_AUTOSIZE (기본) : 창 크기를 영상 크기에 맞게 지정
cv2.namedWindow('image',cv2.WINDOW_NORMAL)

# cv2.resizeWindow(winname, width, height)
# cv2.WINDOW_NORMAL로 생성해야 동작
cv2.resizeWindow('image', 500,500)

# cv2.imshow(window, mat)
# mat : 출력할 영상 데이터
cv2.imshow('image', img)

# cv2.waitKey()에 도달해야 영상 출력이 됨
while True:
    if cv2.waitKey() == 27:
        # esc키로만 나가기 가능
        # cv2.waitKey() == ord('q):
        break


cv2.destroyWindow('image')
# cv2.destroyAllWindows()
