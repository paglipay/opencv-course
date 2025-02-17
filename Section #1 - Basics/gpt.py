import cv2 as cv
import time
import numpy as np

# CUDA enabled libraries
cv.cuda.setDevice(0)
cuda = cv.cuda


# Load the Haar cascade classifier for face detection
haar_cascade = cv.cuda_CascadeClassifier('./haar_face.xml')
# haar_cascade = cv.cuda.CascadeClassifier_create('./haar_face.xml')
GSTREAMER_PIPELINE = 'nvarguscamerasrc ! video/x-raw(memory:NVMM), width=3280, height=2464, format=(string)NV12, framerate=21/1 ! nvvidconv flip-method=0 ! video/x-raw, width=960, height=616, format=(string)BGRx ! videoconvert ! video/x-raw, format=(string)BGR ! appsink'

capture = cv.VideoCapture(0, cv.CAP_GSTREAMER)
while True:
    isTrue, frame = capture.read()
    if isTrue:
        # Convert the input frame to grayscale
        gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)

        # Create CUDA matrices for input and output
        gray_gpu = cuda_GpuMat = cv.cuda_GpuMat(gray)
        # # gray_gpu = cv.cuda_GpuMat(gray)
        faces_rect_gpu = cv.cuda_GpuMat()

        # Perform face detection using CUDA
        # faces_rect_gpu = haar_cascade.detectMultiScale(gray_gpu, scaleFactor=1.1, minNeighbors=1)
        # faces_rect_gpu = haar_cascade.detectMultiScale(gray_gpu, faces_rect_gpu)
        faces_rect_gpu = haar_cascade.detectMultiScale(gray_gpu)

        # Download the output from GPU to CPU memory
        faces_rect = faces_rect_gpu.download()

        # print(f'Number of faces found = {len(faces_rect)}')

        # for (x,y,w,h) in faces_rect:
        #     cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

        # Show
        cv.imshow('Video', frame)


        if cv.waitKey(20) & 0xFF==ord('d'):
            break       
    else:
        break
     

capture.release()
cv.destroyAllWindows()
