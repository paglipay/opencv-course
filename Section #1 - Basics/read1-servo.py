import cv2 as cv
import datetime

from adafruit_servokit import ServoKit
# import time, keyboard

fps_start = datetime.datetime.now()
fps = 0
total_frames = 0

myKit= ServoKit(channels=16)
p_angle  = 90
t_angle = 90

old_p_angle = p_angle
old_t_angle = t_angle

myKit.servo[0].angle=p_angle
myKit.servo[1].angle=t_angle
# Reading Videos
# capture = cv.VideoCapture('./Resources/Videos/dog.mp4')
# capture = cv.VideoCapture('rtsp://admin:admin@192.168.36.224/user=admin_password=admin_channel=1_stream=0.sdp')
capture = cv.VideoCapture(0)
haar_cascade = cv.CascadeClassifier('./haar_face.xml')
while True:
    isTrue, frame = capture.read()
    total_frames += 1
    fps_end = datetime.datetime.now()
    time_diff = fps_end - fps_start
    if time_diff.seconds ==0:
        fps = 0.0
    else:
        fps = (total_frames / time_diff.seconds)
    fps_text = "FPS: {:.2f}".format(fps)
    
    cv.putText(frame, fps_text,(5,30),cv.FONT_HERSHEY_COMPLEX_SMALL, 1, (0,0,255), 1)
    
    
    # frame = cv.imread('./Resources/Photos/lady.jpg')
    # if cv.waitKey(20) & 0xFF==ord('d'):
    # This is the preferred way - if `isTrue` is false (the frame could 
    # not be read, or we're at the end of the video), we immediately
    # break from the loop. 
    if isTrue:    
        
        if total_frames % 2 != 0:
            # cv.imshow('Group of 5 people', frame)

            gray = cv.cvtColor(frame, cv.COLOR_BGR2GRAY)
            # cv.imshow('Gray People', gray)


            faces_rect = haar_cascade.detectMultiScale(gray, scaleFactor=1.1, minNeighbors=1)

            # print(f'Number of faces found = {len(faces_rect)}')

        for idx, (x,y,w,h) in enumerate(faces_rect):
            if idx == 0:
                cv.rectangle(frame, (x,y), (x+w,y+h), (0,255,0), thickness=2)
            else:
                cv.rectangle(frame, (x,y), (x+w,y+h), (255,0,0), thickness=2)
            break
        
        
        cv.imshow('Video', frame)
        if cv.waitKey(20) & 0xFF==ord('q'):
            break  
        
        if cv.waitKey(10) & 0xFF==ord('a') and p_angle < 180:
            print('a pressed')
            p_angle += 10
        if cv.waitKey(10) & 0xFF==ord('d') and p_angle > 0:
            print('d pressed')
            p_angle -= 10
              
        if cv.waitKey(10) & 0xFF==ord('w') and t_angle < 180:
            print('w pressed')
            t_angle += 10
              
        if cv.waitKey(10) & 0xFF==ord('s') and t_angle > 0:
            print('s pressed')
            t_angle -= 10
                        
    else:
        break

    # if keyboard.is_pressed('a') and p_angle < 180:
    #     print('a pressed')
    #     p_angle += 1
    #     # myKit.servo[0].angle=p_angle
    # if keyboard.is_pressed('d') and p_angle > 0:
    #     print('d pressed')
    #     p_angle -= 1
    #     # myKit.servo[0].angle=p_angle
        
    # if keyboard.is_pressed('w') and t_angle < 180:
    #     print('w pressed')
    #     t_angle += 1
    #     # myKit.servo[1].angle=t_angle
        
    # if keyboard.is_pressed('s') and t_angle > 0:
    #     print('s pressed')
    #     t_angle -= 1
    #     # myKit.servo[1].angle=t_angle
    if old_p_angle != p_angle or old_t_angle != t_angle:
        old_p_angle = p_angle
        old_t_angle = t_angle
        print(p_angle, " ",  t_angle)
        
    # time.sleep(.01)
    
    myKit.servo[0].angle=p_angle
    myKit.servo[1].angle=t_angle

capture.release()
cv.destroyAllWindows()
