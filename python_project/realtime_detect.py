'''App nhận diện khuôn mặt trên cam trực tiếp'''

import cv2
import dlib
import time
# Load the detector
detector = dlib.get_frontal_face_detector()

# Load the predictor
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat")

# read the image
cap = cv2.VideoCapture(0)
start_time = time.time() # bắt đầu ghi thời gian


while True:
    _, frame = cap.read()  # đọc khung hình _, 
    # Convert image into grayscale
    gray = cv2.cvtColor(src=frame, code=cv2.COLOR_BGR2GRAY)

    # Use detector to find landmarks
    faces = detector(gray)

    for face in faces:
        x1 = face.left()  # left point
        y1 = face.top()  # top point
        x2 = face.right()  # right point
        y2 = face.bottom()  # bottom point
        # Draw a rectangle
        cv2.rectangle(img=frame, pt1=(x1, y1), pt2=(
            x2, y2), color=(0, 255, 0), thickness=4)

    # show the image
    cv2.imshow(winname="Face", mat=frame)

    # Exit when escape is pressed
    if cv2.waitKey(delay=1) == 27 or time.time() - start_time > 20: # cách thoát là nhấn phím esc hoặc sau 20 giây sẽ tự thoát khỏi vòng lặp
        break

# When everything done, release the video capture and video write objects
cap.release()
# Close all windows
cv2.destroyAllWindows()