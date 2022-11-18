import cv2 as cv

img = cv.imread('./storage/trump/trump1.jpg')




def rescaleFrame(frame,scale=0.75):
    width = int(frame.shape[1] * scale)
    height = int(frame.shape[0] * scale)
    dimansions = (width,height)

    return cv.resize(frame,dimansions, interpolation=cv.INTER_AREA)

# img_resize = rescaleFrame(img)
# cv.imshow('Trump',img)
# cv.imshow('Trump',img_resize)

# cv.waitKey(0)



video = cv.VideoCapture('storage/trump/video.mp4')

while True:
    print('...')
    isTrue, frame = video.read()
    frame_resize = rescaleFrame(frame,0.2)
    # cv.imshow('Video',frame)
    cv.imshow('Video',frame_resize)

    if cv.waitKey(20) & 0xFF==ord('d'):
        break

video.release()
cv.destroyAllWindows()