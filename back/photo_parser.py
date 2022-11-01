#! /usr/bin/env python
# -*- coding: utf-8 -*-
import cv2


class ParsPhoto(object):
    def __init__(self, image):
        self.img = cv2.imread(image) 

    def output(self, text,scale_percent = 60):#Вывод картинки ужатой на 50%
        width = int(self.img.shape[1] * scale_percent / 100)
        height = int(self.img.shape[0] * scale_percent / 100)
        dim = (width, height)
        resized = cv2.resize(self.img, dim, interpolation = cv2.INTER_AREA)
        cv2.imshow(text, resized)
        cv2.waitKey(0)
        cv2.destroyAllWindows()
    
    def find_contours_main(self):#Поиск всех контуров на исходном фото
        blurred = cv2.GaussianBlur(self.img, (3, 3), 0)#размытие //blurred = cv2.GaussianBlur(self.img, (3, 3), 0)#размытие
        gray = cv2.cvtColor(blurred, cv2.COLOR_BGR2GRAY)#оттенки серого
        T, thresh_img = cv2.threshold(gray, 200, 255, cv2.THRESH_BINARY)#монохром#T, thresh_img = cv2.threshold(gray, 220, 255, cv2.THRESH_BINARY)#монохром
        contours, hierarchy  = cv2.findContours(thresh_img, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_TC89_KCOS)#контуры
        cv2.drawContours( thresh_img, contours, -1, (255,255,255), 50, cv2.LINE_AA, hierarchy)#обводка
        return contours

    def find_coordinates_main(self, cnts):#Поиск самого большого контура на исходном фото
        P_max =0 
        P_arr = 0
        coord_max = 0,0,1,1
        for i in range(0, len(cnts)):
            x, y, w, h = cv2.boundingRect(cnts[i])
            if w > 20 and h > 30:
                P_arr = (w)*(h)
                if P_max < P_arr or i==0:
                    coord_max = x, y, x+w, y+h
                    P_max = P_arr
                    i_max = i
        return coord_max

    def all_white_local (self, arr):#убираем фон
        i = 0
        min_img = self.img[arr[1]:arr[3], arr[0]:arr[2]]
        gray = cv2.cvtColor(min_img, cv2.COLOR_BGR2GRAY)

        blurred = cv2.blur(gray, (7, 7))
        T, img_t = cv2.threshold(blurred, 210, 255, cv2.THRESH_BINARY)
        flag_r = (arr[2]-arr[0])/(arr[3]-arr[1])
        if(flag_r < 1.3 and flag_r > 0.7):
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (1, 25))
        else:
            kernel = cv2.getStructuringElement(cv2.MORPH_RECT, (25, 1))
        closed = cv2.morphologyEx(img_t, cv2.MORPH_OPEN, kernel)
        contours, hierarchy  = cv2.findContours(closed, cv2.RETR_CCOMP, cv2.CHAIN_APPROX_TC89_KCOS)#контуры
        cont_ret = []
        coord_work = []
    
        for i in range(0 ,len(contours)):#удаление слоев побочного уровня 
            if(hierarchy[0][i][3]!=-1):
                cont_ret.append(contours[i])
                coord_work.append(cv2.boundingRect(contours[i]))

        return cont_ret, coord_work

    def find_coordinates_local (self, cnts, arr):#находим все на трафорете и выводим на основное фото
        for i in range(0, len(cnts)):
            x, y, w, h = cv2.boundingRect(cnts[i])
            self.img = cv2.rectangle(self.img, (arr[0]+x,arr[1]+y), (arr[0]+x+w,arr[1]+y+h), (0, 0, 255), 5) 
