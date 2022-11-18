import cv2 as cv
import face_recognition
from simple_facerec import SimpleFacerec

# img = cv.imread('./storage/obama/1.jpg')
# img_rgb = cv.cvtColor(img, cv.COLOR_BGR2RGB)
# img_encoding = face_recognition.face_encodings(img_rgb)[0]


# img2 = cv.imread('./storage/obama/3.jpg')
# img2_rgb = cv.cvtColor(img2, cv.COLOR_BGR2RGB)
# img2_encoding = face_recognition.face_encodings(img2_rgb)[0]

# result = face_recognition.compare_faces([img_encoding], img2_encoding)

# print('>>>>',result[0])

# cv.imshow('Obama', img2)
# cv.imshow('Obamaa', img)
# cv.waitKey(0)


video = cv.VideoCapture('./storage/obama/video.mp4')
sfr = SimpleFacerec()
sfr.load_encoding_images("storage/example/")

while True:
    isTrue, frame = video.read()

    # Detect
    face_locations, face_names = sfr.detect_known_faces(frame)
    for face_loc, name in zip(face_locations, face_names):
        y1, x2, y2, x1 = face_loc[0], face_loc[1], face_loc[2], face_loc[3]
        cv.rectangle(frame, (x1, y1), (x2, y2), (255, 0, 0), 2)
        cv.putText(frame, name, (x1, y1-3),
                   cv.FONT_HERSHEY_SIMPLEX, 0.75, (0,0,255),2)
        
        
    cv.imshow('Obama', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

cv.destroyAllWindows()
