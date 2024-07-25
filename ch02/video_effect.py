import sys
import numpy as np
import cv2

# 두 개의 동영상을 열어서 cap1, cap2로 지정
cap1 = cv2.VideoCapture(r'C:\Users\c\Desktop\Git\Using-OpenCV\ch02\video1.mp4')
cap2 = cv2.VideoCapture(r'C:\Users\c\Desktop\Git\Using-OpenCV\ch02\video2.mp4')

# 동영상 열기 실패 시 메시지를 출력하고 프로그램을 종료합니다.
if not cap1.isOpened() or not cap2.isOpened():
    print('video open failed!')
    sys.exit()

# 두 동영상의 프레임 수, FPS를 가져옵니다. (두 동영상의 크기와 FPS는 같다고 가정)
frame_cnt1 = round(cap1.get(cv2.CAP_PROP_FRAME_COUNT))
frame_cnt2 = round(cap2.get(cv2.CAP_PROP_FRAME_COUNT))
fps = cap1.get(cv2.CAP_PROP_FPS)
effect_frames = int(fps * 2)  # 2초 동안의 효과 프레임 수

# 프레임 수와 FPS 출력
print('frame_cnt1:', frame_cnt1)
print('frame_cnt2:', frame_cnt2)
print('FPS:', fps)

# 프레임 간 지연 시간 (밀리초) 계산
delay = int(1000 / fps)

# 동영상의 프레임 너비와 높이를 가져옵니다.
w = round(cap1.get(cv2.CAP_PROP_FRAME_WIDTH))
h = round(cap1.get(cv2.CAP_PROP_FRAME_HEIGHT))
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # 비디오 코덱 설정

# 출력 동영상 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 1번 동영상을 복사
for i in range(frame_cnt1 - effect_frames):
    ret1, frame1 = cap1.read()

    if not ret1:
        print('frame read error!')
        sys.exit()

    out.write(frame1)  # 출력 동영상에 프레임을 작성
    print('.', end='')

    cv2.imshow('output', frame1)  # 프레임을 출력 창에 표시
    cv2.waitKey(delay)

# 1번 동영상 뒷부분과 2번 동영상 앞부분을 합성
for i in range(effect_frames):
    ret1, frame1 = cap1.read()
    ret2, frame2 = cap2.read()

    if not ret1 or not ret2:
        print('frame read error!')
        sys.exit()

    dx = int(w / effect_frames) * i  # 프레임 간 변환할 영역 계산

    frame = np.zeros((h, w, 3), dtype=np.uint8)  # 빈 프레임 생성
    frame[:, 0:dx, :] = frame2[:, 0:dx, :]  # frame2의 일부를 합성
    frame[:, dx:w, :] = frame1[:, dx:w, :]  # frame1의 나머지를 합성

    # alpha = i / effect_frames
    # frame = cv2.addWeighted(frame1, 1 - alpha, frame2, alpha, 0)  # 페이드 효과

    out.write(frame)  # 출력 동영상에 프레임을 작성
    print('.', end='')

    cv2.imshow('output', frame)  # 프레임을 출력 창에 표시
    cv2.waitKey(delay)

# 2번 동영상을 복사
for i in range(effect_frames, frame_cnt2):
    ret2, frame2 = cap2.read()

    if not ret2:
        print('frame read error!')
        sys.exit()

    out.write(frame2)  # 출력 동영상에 프레임을 작성
    print('.', end='')

    cv2.imshow('output', frame2)  # 프레임을 출력 창에 표시
    cv2.waitKey(delay)

print('\noutput.avi file is successfully generated!')

# 자원 해제 및 창 닫기
cap1.release()
cap2.release()
out.release()
cv2.destroyAllWindows()
