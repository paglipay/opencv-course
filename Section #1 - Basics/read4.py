import cv2

img = cv2.imread('./lady.jpg')
cascade = cv2.cuda_CascadeClassifier.create('./haarcascade_frontalface_alt.xml')
gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
cuFrame = cv2.cuda_GpuMat(gray_img)
result = cascade.detectMultiScale(cuFrame).download() # download() gets the result as UMat

if result is not None:
    print(result[0])
    print(f'Number of faces found = {len(result[0])}')

    for (x,y,w,h) in result[0]:
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), thickness=2)
    cv2.imshow('Video', img)
    
    cv2.waitKey(0)
    