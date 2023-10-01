"""
@file test_lock_mode.py
@Description: This is a test script for using the SIYI SDK Python implementation to set Lock mode
@Author: Mohamed Abdelkader
@Contact: mohamedashraf123@gmail.com
All rights reserved 2022
"""

import sys
import os
from time import sleep

from ultralytics import YOLO

model = YOLO('yolov8n.pt')
#model = YOLO('Memorex USB/yolov8/best.pt')
  
current = os.path.dirname(os.path.realpath(__file__))
parent_directory = os.path.dirname(current)
  
sys.path.append(parent_directory)

from siyi_sdk import SIYISDK
#from stream import SIYIRTSP
import cv2
import numpy as np

def test():
    cam = SIYISDK(server_ip="192.168.144.25", port=37260)	

    #rtsp = SIYIRTSP(rtsp_url="rtsp://192.168.144.25:8554/main.264",debug=False)
    #rtsp.setShowWindow(True)
    
    if not cam.connect():
        print("No connection ")
        exit(1)

    yaw = 20
    pitch = 180

    gain = 4

    while(True):
        cam.requestGimbalAttitude()
        if cam._att_msg.seq==cam._last_att_seq:
            cam._logger.info("Did not get new attitude msg")
            cam.requestGimbalSpeed(0,0)
            continue

        cam._last_att_seq = cam._att_msg.seq

        pitchWrapped = angleWrap(cam._att_msg.pitch)

        yaw_err = -yaw + cam._att_msg.yaw # NOTE for some reason it's reversed!!
        pitch_err = pitch - pitchWrapped

        cam._logger.debug("yaw_err= %s", yaw_err)
        cam._logger.debug("pitch_err= %s", pitch_err)

        print(pitchWrapped)

        
        if (abs(pitch_err) <= 1 and abs(yaw_err)<=1):
            cam.requestGimbalSpeed(0, 0)
            cam._logger.info("Goal rotation is reached")
            break

        #print(pitch_err)
        y_speed_sp = max(min(100, int(gain*yaw_err)), -100)
        p_speed_sp = max(min(100, int(gain*pitch_err)), -100)
        cam._logger.debug("yaw speed setpoint= %s", y_speed_sp)
        #cam._logger.debug("pitch speed setpoint= %s", p_speed_sp)
        #print("yaw speed setpoint= %s", y_speed_sp)
        cam.requestGimbalSpeed(-y_speed_sp, -p_speed_sp)

        sleep(0.1) # command frequency'''
    
    capture = cv2.VideoCapture("rtsp://192.168.144.25:8554/main.264")


    counter = 0
    annotated_image = np.zeros((10, 10, 3), np.uint8)
    while(True):
        print("flag")
        ret, img = capture.read()
        print("flag2")
        if ret == True: 
            if counter == 20:
                counter = 0
                result = model(img)
                annotated_image = result[0].plot()
            print("flag3")
            cv2.imshow('video output', annotated_image)
            counter += 1
            print(counter)
            k = cv2.waitKey(10)
            if k==27:
                break
        else:
            print("ERROR")
    
    capture.release()
    cv2.destroyAllWindows()

    cam.disconnect()

def angleWrap(angle):
    if(angle < 0):
        return 360 + angle
    return angle

if __name__ == "__main__":
    test()
