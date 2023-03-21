
import dlib
# import face_recognition
import os
import cv2

# KNOWN_FACES_DIR =  "../known_faces" # training data
# TOLERANCE = 0.7
# FRAME_THICKNESS = 3 # rectangle thickness
# FONT_THICKNESS = 2 # font thickness
# MODEL = "cnn" # convolutional
# video = cv2.VideoCapture(0) # use webcan as input (source of test images)
# print("loading known faces")
# known_faces = [] # store known faces here
# known_names = [] # store name of them here

print(dlib.DLIB_USE_CUDA) # ture, if cuda is enabled.