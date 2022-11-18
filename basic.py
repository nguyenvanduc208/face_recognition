import cv2 as cv

img = cv.imread('storage/trump/trump2.jpg')
cv.imshow('Trump',img)

# gray = cv.cvtColor(img, cv.COLOR_BGR2GRAY)
# cv.imshow('ddd',gray)

# Blur 
# blur = cv.GaussianBlur(img,(5,7), cv.BORDER_ISOLATED)
# cv.imshow('dfa',blur)

# Canny

canny = cv.Canny(img,125,175)
cv.imshow('fdas',canny)


cv.waitKey(0)