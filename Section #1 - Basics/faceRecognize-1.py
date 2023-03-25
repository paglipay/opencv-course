import face_recognition
import cv2
print(cv2.__version__)
image=face_recognition.load_image_file('./Resources/Photos/group 2.jpg')
face_locations=face_recognition.face_locations(image)
print(face_locations)
