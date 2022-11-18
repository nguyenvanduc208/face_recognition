import cv2 as cv


def rescaleFrame(frame, scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimansions = (width, height)

    return cv.resize(frame, dimansions, interpolation=cv.INTER_AREA)


faceCascade = cv.CascadeClassifier(
    cv.data.haarcascades + 'haarcascade_frontalface_default.xml')
# image = cv.imread('storage/obama/6.jpg')
# image = rescaleFrame(image,0.8)
# gray = cv.cvtColor(image,cv.COLOR_BGR2GRAY)

# faces = faceCascade.detectMultiScale(gray,scaleFactor=1.2,minNeighbors=5,minSize=(30,30))
# print(f'Length: {len(faces)}')


# for (x,y,w,h) in faces:
#     cv.rectangle(image, (x,y), (x+w,y+h),(0,255,0),2 )

# cv.imshow('saaa',image)

# cv.waitKey(0)

video = cv.VideoCapture('storage/trump/video.mp4')

while True:
    isTrue, frame = video.read()
    frame = rescaleFrame(frame)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    faces = faceCascade.detectMultiScale(
        gray, scaleFactor=1.3, minNeighbors=5, minSize=(30, 30))
    
    print(f'length: {len(faces)}')
    for (x, y, w, h) in faces:
        cv.rectangle(frame, (x, y), (x+w, y+h), (0, 255, 0), 2)
    cv.imshow('zz', frame)

    if cv.waitKey(20) & 0xFF == ord('d'):
        break

video.release()
cv.destroyAllWindows()
