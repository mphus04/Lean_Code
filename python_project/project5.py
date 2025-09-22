'''App nhận diện khuôn mặt  trên ảnh'''

import cv2
import dlib

#read the image
img = cv2.imread("blackpink-stars-hd-wallpaper-preview.jpg")

# resized_img = cv2.resize(img, (1920, 1080))  # Thay đổi kích thước ảnh thành theo ý muốn

# convert img to graycale :3d ->2d
gray = cv2.cvtColor(src=img, code =cv2.COLOR_BGR2GRAY) # chuyển hình thành màu trắng đen

#dlib: Load Face Recognition Detector
face_detector = dlib.get_frontal_face_detector() # load hàm nhận diện khuôn mặt

#load the predictor:
predictor = dlib.shape_predictor("shape_predictor_68_face_landmarks.dat") 
# load từ thư viện tự train của explore nhận diện 68 điểm


# Use detector to find face lammark
faces = face_detector(gray)

for face in faces :
    x1 = face.left() # left Point
    y1 = face.top() # top point
    x2 = face.right() # right point
    y2 = face.bottom() # bottom point
    #lấy tọa độ các điểm trên khuôn mặt
    cv2.rectangle(img = img, pt1=(x1,y1),pt2=(x2,y2),
                  color = (0 ,255, 0), thickness=3) # vẽ hình vuông lên hình trắng đen

    face_features = predictor(image = gray ,box = face) # lên hình trắng đen
    # loop through all 86 point :
    for n in range(0, 68):
        x = face_features.part(n).x
        y = face_features.part(n).y

        #draw circle
        cv2.circle(img=img , center=(x,y), radius=2 ,color=(0, 0, 255), thickness= 1)

#show the image
cv2.imshow(winname="Face Recognition App", mat=img)

#wait for a key press to exist
cv2.waitKey(delay=0) 

#close all window
cv2.destroyAllWindows()
