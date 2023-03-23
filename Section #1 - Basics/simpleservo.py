from adafruit_servokit import ServoKit
import time

myKit= ServoKit(channels=16)

while True:
    for i in range(0,180,1):
        myKit.servo[0].angle=i
        myKit.servo[1].angle=i
        time.sleep(0.01)
    
    for j in range(180,0,-1):
        myKit.servo[0].angle=j
        myKit.servo[1].angle=j
        time.sleep(0.01)
        
    # for i in range(0,180,1):
    #     myKit.servo[1].angle=i
    #     time.sleep(0.01)
    
    # for j in range(180,0,-1):
    #     myKit.servo[1].angle=j
    #     time.sleep(0.01)