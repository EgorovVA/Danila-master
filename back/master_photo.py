#! /usr/bin/env python
# -*- coding: utf-8 -*-
from os import system 
import cv2
import queue
import urllib
import math as m
import numpy as np
from back.photo_parser import ParsPhoto
import eel

class Param_Move:
    def __init__(self): 
        self.head_size = 8 #Диаметр распыла
        self.factor_img_mm = float(100.0/45.0) #Коэфицент перевода 
        sqrt_two = m.sqrt(2)
        sqrt_three = m.sqrt(3)
        self.cos_rotete = [ -0.5, -sqrt_two/2, -sqrt_three/2, -1.0, -sqrt_three/2,-sqrt_two/2, -0.5]
        self.sin_rotete = [ sqrt_three/2, sqrt_two/2, 0.5, 0, -0.5, -sqrt_two/2, -sqrt_three/2]

def ParserPhoto(pp):        
    cnts= pp.find_contours_main() 
    arr= pp.find_coordinates_main(cnts)#область поиска букв
    cnts, coord_work = pp.all_white_local (arr)
    pp.find_coordinates_local(cnts, arr)
    #pp.output("black_white") 
    return  cnts, coord_work, arr

@eel.expose
def go():

    #работа с изоброжением 
    image_file = r'C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/photo.jpg' 

    pp = ParsPhoto(image_file) 
    cnts, coord_work, arr = ParserPhoto(pp)
    #работа с закраской 

    Mimg = queue.Queue()
    param = Param_Move()
    #for i in range(0 ,len(cnts)):
    #x, y, w, h  = coord_work[0]
    
    #Mimg.put( [0, x, y, w, h])
#    step =  m.floor ((h*param.factor_img_mm)/(param.head_size*2)) /2
  #  k = step
    with open("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/comand/gcode.txt", 'r+') as f:
        f.truncate(0)
    gcode_f = open("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/comand/gcode.txt", "a")
    flag_cos = 1
    color_k = True
    color = [0, 255, 0]
    
    start = [0,0]
    for count_cont in range(0, len(cnts)):
        x, y, w, h = cv2.boundingRect(cnts[count_cont])
        step =  m.floor ((h*param.factor_img_mm)/(param.head_size*2)) /2
        k = step
        i=h+step
        r = step/2
        gcode_f.write("G0 X"+str(start[0])+" Y" + str(start[1])+ '\n')
        cv2.line(pp.img, (start[0] ,start[1] ), (arr[0]+x,arr[1]+y+h), color, 1)
        while(i>0):

            coord = [arr[0]+x,arr[1]+y+int(i-k),arr[0]+x+w,arr[1]+y+h-int(i-k)]
            
            if(color_k):
                color = [0, 255, 0]
                color_k = False
                flag_cos = -1
                x_ = coord[2]     
            else:
                color = [255, 0, 255]
                color_k = True
                flag_cos = 1
                x_ = coord[0]

            y_ = coord[1]-r
            x0 = x_
            y0 = coord[1]
            gcode_f.write("G1 X"+str(coord[2])+" Y" + str(coord[1])+ '\n')
            #img = cv2.rectangle(pp.img , (coord[0],coord[1]), (coord[2],coord[3]), color, 1)
            cv2.line(pp.img, (coord[0] ,coord[1]), (coord[2],coord[1]), color, 1)
            for i_rot in range(0, 7):
                x1 =int(flag_cos*r*(param.cos_rotete[i_rot])+x_)
                y1 =int(r*(param.sin_rotete[i_rot])+y_)
                gcode_f.write("G2 X"+str(x1)+" Y" + str(y1)+ '\n')
                cv2.line(pp.img, (x0 ,y0), (x1,y1), color, 1)
                x0 = x1
                y0 = y1
            start = [x0, y0]
            i-=k

    cv2.imwrite(image_file, pp.img)
    cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/lupe_1.jpg", pp.img)
    cv2.imwrite("C:/Users/vlade/Desktop/test_eel-master/Danila-master/front/images/lupe_0.jpg", pp.img)  
    cv2.waitKey(0)
