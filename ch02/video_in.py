import sys
import cv2

# 비디오 파일 열기
cap = cv2.VideoCapture(r'C:\Users\c\Desktop\Git\Using-OpenCV\ch02\video1.mp4')  # 'video1.mp4' 파일을 엽니다.

# 비디오 파일 열기 실패 시 메시지를 출력하고 프로그램을 종료합니다.
if not cap.isOpened():
    print("Video open failed!")
    sys.exit()

# 비디오 프레임 크기, 전체 프레임 수, FPS 등 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))  # 프레임 너비 출력
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 프레임 높이 출력
print('Frame count:', int(cap.get(cv2.CAP_PROP_FRAME_COUNT)))  # 전체 프레임 수 출력

fps = cap.get(cv2.CAP_PROP_FPS)  # FPS (초당 프레임 수) 가져오기
print('FPS:', fps)

delay = round(1000 / fps)  # 프레임 간 지연 시간 (밀리초) 계산

# 비디오 매 프레임 처리
while True:
    ret, frame = cap.read()  # 프레임을 읽습니다.

    # 프레임 읽기 실패 시 루프를 종료합니다.
    if not ret:
        break

    inversed = ~frame  # 프레임을 반전시킵니다.

    # 원본 프레임과 반전된 프레임을 각각 창에 출력합니다.
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    # delay 시간 동안 키 입력을 대기하고, ESC 키(27번)가 입력되면 루프를 종료합니다.
    if cv2.waitKey(delay) == 27:
        break

# 비디오 자원 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
