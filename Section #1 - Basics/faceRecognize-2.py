import cv2 as cv
import face_recognition
capture = cv.VideoCapture(0)
while True:
    isTrue, image = capture.read()
    if isTrue:
        # image=face_recognition.load_image_file('./Resources/Photos/group 2.jpg')
        fr_image=cv.cvtColor(image,cv.COLOR_BGR2RGB)
        face_locations=face_recognition.face_locations(fr_image)
        print(face_locations)
        if face_locations is not None:
            # print(f'Number of faces found = {len(face_locations)}')
            for (row1,col1,row2,col2) in face_locations:
                cv.rectangle(image, (col1,row1), (col2,row2), (0,255,0), thickness=2)

        cv.imshow('Video', image)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break  
    
capture.release()
del capture