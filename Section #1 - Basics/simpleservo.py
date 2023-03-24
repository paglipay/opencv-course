from adafruit_servokit import ServoKit
import time, keyboard

myKit= ServoKit(channels=16)
p_angle  = 90
t_angle = 90

old_p_angle = p_angle
old_t_angle = t_angle

myKit.servo[0].angle=p_angle
myKit.servo[1].angle=t_angle
while True:
    if keyboard.is_pressed('a') and p_angle < 180:
        print('a pressed')
        p_angle += 1
        # myKit.servo[0].angle=p_angle
    if keyboard.is_pressed('d') and p_angle > 0:
        print('d pressed')
        p_angle -= 1
        # myKit.servo[0].angle=p_angle
        
    if keyboard.is_pressed('w') and t_angle < 180:
        print('w pressed')
        t_angle += 1
        # myKit.servo[1].angle=t_angle
        
    if keyboard.is_pressed('s') and t_angle > 0:
        print('s pressed')
        t_angle -= 1
        # myKit.servo[1].angle=t_angle
    if old_p_angle != p_angle or old_t_angle != t_angle:
        old_p_angle = p_angle
        old_t_angle = t_angle
        print(p_angle, " ",  t_angle)
        
    time.sleep(.01)
    
    myKit.servo[0].angle=p_angle
    myKit.servo[1].angle=t_angle
    # for i in range(0,180,1):
    #     myKit.servo[0].angle=i
    #     myKit.servo[1].angle=i
    #     time.sleep(0.01)
    
    # for j in range(180,0,-1):
    #     myKit.servo[0].angle=j
    #     myKit.servo[1].angle=j
    #     time.sleep(0.01)
        
    # for i in range(0,180,1):
    #     myKit.servo[1].angle=i
    #     time.sleep(0.01)
    
    # for j in range(180,0,-1):
    #     myKit.servo[1].angle=j
    #     time.sleep(0.01)