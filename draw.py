import cv2 as cv
import numpy as np

blank = np.zeros((500,500,3),dtype='uint8')
# cv.imshow('Blank',blank)

# img = cv.imread('./storage/trump/trump1.jpg')
# cv.imshow('Trump',img)

# blank[100:102,300:400]=0,0,255
# cv.imshow('Red',blank)


cv.rectangle(blank,(0,0),(blank.shape[1]//2,100),(0,0,255), thickness=cv.FILLED)
cv.line(blank,(0,0),(300,100),(0,255,0),thickness=2)
cv.putText(blank,'Hello',(300,200), cv.FONT_HERSHEY_SIMPLEX, 1.0,(0,220,0),1)
cv.imshow('Reactagle',blank)


cv.waitKey(0)