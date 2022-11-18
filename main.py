# import cv2 as cv

# # Read image
# # img = cv.imread('./storage/trump/trump1.jpg')
# # cv.imshow('Trump',img)

# # cv.waitKey(0)


# # Read video

# video = cv.VideoCapture('storage/trump/video.mp4')

# while True:
#     print('...')
#     isTrue, frame = video.read()
#     cv.imshow('Video', frame)

#     if cv.waitKey(20) & 0xFF == ord('d'):
#         break

# video.release()
# cv.destroyAllWindows()

numberList = [1, 2, 3]
 
strList = ['one', 'two', 'three']
 
# Không truyền iterable
 
result = zip()
 
# Chuyển đổi iterator thành list
 
resultList = list(result)
 
print(resultList)
 
# Truyền 2 iterator 
 
result = zip(numberList, strList)
 
# Chuyển đổi iterator thành set
 
resultSet = set(result)
 
for (a, b) in result:
    print(f'>>>>> {a}')
    print(f'>>>>> {b}')
