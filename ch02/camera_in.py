import sys
import cv2

# 카메라 열기
cap = cv2.VideoCapture(0)  # 기본 카메라를 엽니다.

# 카메라 열기 실패 시 메시지를 출력하고 프로그램을 종료합니다.
if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 크기 출력
print('Frame width:', int(cap.get(cv2.CAP_PROP_FRAME_WIDTH)))  # 프레임 너비를 출력합니다.
print('Frame height:', int(cap.get(cv2.CAP_PROP_FRAME_HEIGHT)))  # 프레임 높이를 출력합니다.

# 카메라 프레임 처리
while True:
    ret, frame = cap.read()  # 프레임을 읽습니다.

    # 프레임 읽기 실패 시 루프를 종료합니다.
    if not ret:
        break

    inversed = ~frame  # 프레임을 반전시킵니다.

    # 원본 프레임과 반전된 프레임을 각각 창에 출력합니다.
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    # 10ms 동안 키 입력을 대기하고, ESC 키(27번)가 입력되면 루프를 종료합니다.
    if cv2.waitKey(10) == 27:
        break

# 카메라 자원 해제 및 모든 창 닫기
cap.release()
cv2.destroyAllWindows()
