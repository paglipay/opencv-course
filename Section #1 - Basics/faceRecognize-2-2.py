import cv2 as cv
import face_recognition
capture = cv.VideoCapture(0)

Encodings = []
face_pic = face_recognition.load_image_file('./Resources/Faces/train/Ben Afflek/2.jpg')
Encodings.append(face_recognition.face_encodings(face_pic)[0])

# Encodings=faces
Names=['Ben Afflek']
font = cv.FONT_HERSHEY_SIMPLEX

while True:
    isTrue, image = capture.read()
    if isTrue:
        # image=face_recognition.load_image_file('./Resources/Photos/group 2.jpg')
        fr_image=cv.cvtColor(image,cv.COLOR_BGR2RGB)
        face_locations=face_recognition.face_locations(fr_image)
        allEncodings=face_recognition.face_encodings(fr_image, face_locations)
        # print(face_locations)
        if face_locations is not None:
            # print(f'Number of faces found = {len(face_locations)}')
            # for (row1,col1,row2,col2) in face_locations:
            #     cv.rectangle(image, (col1,row1), (col2,row2), (0,255,0), thickness=2)
            for (top,right,bottom,left), face_encoding in zip(face_locations, allEncodings):
                name='Unknown Person'
                matches=face_recognition.compare_faces(Encodings, face_encoding)
                # print('matches', matches)
                if True in matches:
                    first_match_index=matches.index(True)
                    name=Names[first_match_index]
                
                cv.rectangle(image, (left, top), (right,bottom), (0,255,0), thickness=2)
                cv.putText(image,name, (left,top-6),font,.75,(255,0,255),1)
                

        cv.imshow('Video', image)
        if cv.waitKey(20) & 0xFF==ord('d'):
            break  
    
capture.release()
del capture