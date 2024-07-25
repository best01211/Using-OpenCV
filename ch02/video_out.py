import sys
import cv2

# 기본 카메라 열기
cap = cv2.VideoCapture(0)

# 카메라 열기 실패 시 메시지를 출력하고 프로그램을 종료합니다.
if not cap.isOpened():
    print("Camera open failed!")
    sys.exit()

# 카메라 프레임 너비와 높이, FPS를 가져옵니다.
w = round(cap.get(cv2.CAP_PROP_FRAME_WIDTH))  # 프레임 너비
h = round(cap.get(cv2.CAP_PROP_FRAME_HEIGHT))  # 프레임 높이
fps = cap.get(cv2.CAP_PROP_FPS)  # 프레임 속도

# 비디오 코덱 설정
fourcc = cv2.VideoWriter_fourcc(*'DIVX')  # *'DIVX'는 'D', 'I', 'V', 'X'를 의미합니다.
delay = round(1000 / fps)  # 프레임 간 지연 시간 (밀리초)

# 비디오 파일 쓰기를 위한 VideoWriter 객체 생성
out = cv2.VideoWriter('output.avi', fourcc, fps, (w, h))

# 비디오 파일 열기 실패 시 메시지를 출력하고 프로그램을 종료합니다.
if not out.isOpened():
    print('File open failed!')
    cap.release()
    sys.exit()

# 무한 루프를 시작합니다.
while True:
    ret, frame = cap.read()  # 프레임을 읽습니다.

    # 프레임 읽기 실패 시 루프를 종료합니다.
    if not ret:
        break

    inversed = ~frame  # 프레임을 반전시킵니다.

    out.write(inversed)  # 반전된 프레임을 비디오 파일에 씁니다.

    # 원본 프레임과 반전된 프레임을 각각 창에 출력합니다.
    cv2.imshow('frame', frame)
    cv2.imshow('inversed', inversed)

    # delay 시간 동안 키 입력을 대기하고, ESC 키(27번)가 입력되면 루프를 종료합니다.
    if cv2.waitKey(delay) == 27:
        break

# 카메라 자원 해제 및 비디오 파일 닫기, 모든 창 닫기
cap.release()
out.release()
cv2.destroyAllWindows()
