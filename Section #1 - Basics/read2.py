import cv2 as cv
import nanocamera as nano

# cam_pipeline_str = 'nvarguscamerasrc sensor-id=0 ! video/x-raw(memory:NVMM),format=NV12,width=1280,height=720,framerate=30/1 ! nvvidconv ! video/x-raw,format=BGRx ! videoconvert ! video/x-raw,format=BGR ! appsink drop=1'
# vod = cv.VideoCapture(cam_pipeline_str, cv.CAP_GSTREAMER)
# vod = cv.VideoCapture('../Resources/Videos/dog.mp4')
# Create the Camera instance for No rotation (flip=0) with size of 640 by 480
vod = nano.Camera(camera_type=1, device_id=0, width=640, height=480, fps=30)

# ret, frame = vod.read()

scale = 0.5
# CUDA enabled libraries
# cv.cuda.setDevice(0)
# cuda = cv.cuda

gpu_frame = cv.cuda_GpuMat()

# Load the Haar cascade classifier for face detection
HAAR_CASCADE_XML_FILE_FACE = "./haarcascade_frontalface_alt.xml"
# haar_cascade = cv.CascadeClassifier(HAAR_CASCADE_XML_FILE_FACE)
# haar_cascade = cv.cuda_CascadeClassifier('./haar_face.xml')
# haar_cascade = cv.cuda.CascadeClassifier.create(HAAR_CASCADE_XML_FILE_FACE)
haar_cascade = cv.cuda_CascadeClassifier.create('./haarcascade_frontalface_alt.xml')

# frame = cv.imread('./Resources/Photos/cat.jpg')
while vod.isReady():

    frame = vod.read()
    #Convert the input frame to grayscale
    # gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
    gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)


    # Create CUDA matrices for input and output
    # gray_gpu = cuda_GpuMat = cv.cuda_GpuMat(gray)
    gray_gpu = cv.cuda_GpuMat(gray)
    # faces_rect_gpu = cv.cuda_GpuMat()

    # Perform face detection using CUDA
    # faces_rect_gpu = haar_cascade.detectMultiScale(gray_gpu, scaleFactor=1.1, minNeighbors=1)
    # faces_rect_gpu = haar_cascade.detectMultiScale(gray_gpu, faces_rect_gpu)
    faces_rect_gpu = haar_cascade.detectMultiScale(gray_gpu)

    # Download the output from GPU to CPU memory
    # faces_rect = faces_rect_gpu.download()
    result = haar_cascade.detectMultiScale(gray_gpu).download()
    if result is not None:
         
        print(f'Number of faces found = {len(result[0])}')
        for (x,y,w,h) in result[0]:
            cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)

    # gpu_frame.upload(frame)

    # resized = cv.cuda.resize(gpu_frame, (int(1280 * scale), int(720 * scale)))

    # luv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2LUV)
    # hsv = cv.cuda.cvtColor(resized, cv.COLOR_BGR2HSV)
    # gray = cv.cuda.cvtColor(resized, cv.COLOR_BGR2GRAY)
    
    # faces_rect_gpu = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)


    # Download the output from GPU to CPU memory
    # faces_rect = faces_rect_gpu.download()

    # # download new image(s) from GPU to CPU (cv2.cuda_GpuMat -> numpy.ndarray)
    # resized = resized.download()
    # luv = luv.download()
    # hsv = hsv.download()
    # gray = gray.download()q

    # cv.imshow('resized', resized)
    # cv.imshow('luv', luv)
    # cv.imshow('hsv', hsv)
    # cv.imshow('gray', gray)
    cv.imshow('Video', frame)
    if cv.waitKey(20) & 0xFF==ord('d'):
        break  
    
vod.release()
del vod