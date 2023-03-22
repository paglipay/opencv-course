#pylint:disable=no-member

import cv2 as cv

# img = cv.imread('./Resources/Photos/cats.jpg')
# cv.imshow('Cats', img)

# cv.waitKey(0)

# Reading Videos
# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
# capture = cv.VideoCapture('rtsp://admin:admin@192.168.36.224/user=admin_password=admin_channel=1_stream=0.sdp')
capture = cv.VideoCapture(0)
# haar_cascade = cv.CascadeClassifier('./haar_face.xml')
while True:
    isTrue, frame = capture.read()
    
    # frame = cv.imread('./Resources/Photos/lady.jpg')
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        
        
        # cv.imshow('Group of 5 people', frame)

        # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
        # # cv.imshow('Gray People', gray)


        # faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

        # print(f'Number of faces found = {len(faces_rect)}')

        # for (x,y,w,h) in faces_rect:
        #     cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
        
        
        
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break            
    else:
        break

capture.release()
cv.destroyAllWindows()
