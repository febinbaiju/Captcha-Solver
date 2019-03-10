import cv2
import numpy
import os

def fetch_datasets(folder):
    ch = os.scandir(folder)
    outer_loop = 1
    for file in ch:
        
        filepath = os.path.abspath(file)
        print(filepath)

        imread = cv2.imread(filepath,0)
        #convert to black and white
        mat,bnw = cv2.threshold(imread,127,255,cv2.THRESH_BINARY)
        contours,hierarchy = cv2.findContours(bnw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
        #get individual datasets
        for index in range(1,len(contours)):
            draw = numpy.zeros(imread.shape,dtype="uint8")
            draw.fill(255)
            cv2.drawContours(draw,contours,index,(0,0,0),1)
            (x,y,w,h) = cv2.boundingRect(contours[index])
            cropped = imread[y:y+h,x:x+w]
            cv2.imwrite("datasets/{0}-{1}.png".format(str(outer_loop),str(index)),cropped)
            break
        outer_loop+=1

#fetch_datasets("cut/")

