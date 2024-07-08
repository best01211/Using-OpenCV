import sys
import glob
import cv2

# 이미지 파일을 모두 img_files 리스트에 추가
img_files = glob.glob('.\\images\\*.jpg')

if not img_files:
    print("There are no jpg in 'images' folder")
    sys.exit()

for f in img_files:
    print(f)