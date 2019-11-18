import sys
import os
import dlib
import glob
from skimage import io
import numpy as np
import cv2
from scipy.spatial import distance as dist #입술 사이 거리 계산 위해
import math
import pygame
from game import *

class face():
    def __init__(self,game):
        super().__init__()
        self.game=game

        self.cap = cv2.VideoCapture(0)
        self.fourcc = cv2.VideoWriter_fourcc(*'XVID')
        #self.out = cv2.VideoWriter('output.avi',self.fourcc, 20.0, (1280, 720))
        self.predictor_path = 'shape_predictor_81_face_landmarks.dat'
        self.detector = dlib.get_frontal_face_detector() #INITIALIZE FACE PROTECTOR
        self.predictor = dlib.shape_predictor(self.predictor_path) #LANDMARK PREDICTOR

        self.ret,self.frame = self.cap.read() #영상 읽어들임
        self.frame = cv2.flip(self.frame, 1)
        self.dets = self.detector(self.frame, 0) #rects
        (self.mStart,self.mEnd)=(48,54) #mouth의 시작점, 끝점 번호
        self.MOUTH_AR_THRESH = 0.1

    def __call__(self):
        print (" ")

    def face_recognition(self,screen):
        self.ret,self.frame = self.cap.read() #영상 읽어들임
        self.frame = cv2.flip(self.frame, 1)
        #self.dets = self.detector(self.frame, 0) #rects

        for k, d in enumerate(self.dets):
            shape = self.predictor(self.frame, d)
            landmarks = np.matrix([[p.x, p.y] for p in shape.parts()])
            for num in range(shape.num_parts):
                cv2.circle(self.frame, (shape.parts()[num].x, shape.parts()[num].y), 3, (0,255,0), -1)
            A=dist.euclidean((shape.parts()[61].x,shape.parts()[61].y),(shape.parts()[67].x,shape.parts()[67].y))
            B=dist.euclidean((shape.parts()[63].x,shape.parts()[63].y),(shape.parts()[65].x,shape.parts()[65].y))
            C=dist.euclidean((shape.parts()[48].x,shape.parts()[48].y),(shape.parts()[54].x,shape.parts()[54].y))
            mar=(A+B)/(2.0*C)
            mar=round(mar,5)

            if mar>self.MOUTH_AR_THRESH:
                #cv2.putText(self.frame,"MOUTH IS OPEN!",(30,60),cv2.FONT_HERSHEY_SIMPLEX,0.7,(0,0,255),2)
                print("mouth is open")
                return True
            else:
                print("closed")
                return False

        #cv2.imshow("Frame", self.frame)
        self.cap.release()
        #self.out.release()
        cv2.destroyAllWindows()
