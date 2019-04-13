import cv2
import csv
import numpy as np
import math

captcha_identified = []
dataset_file = "dataset.csv"

filepath = "/home/febin/Downloads/otp.png"

imread = cv2.imread(filepath,0)
height,width = imread.shape
roi = imread[0:16,0:width]
imread=roi 
#convert to black and white
mat,bnw = cv2.threshold(imread,127,255,cv2.THRESH_BINARY)
contours,hierarchy = cv2.findContours(bnw,cv2.RETR_TREE,cv2.CHAIN_APPROX_SIMPLE)
#get individual datasets
for index in range(1,len(contours)):
    draw = np.zeros(imread.shape,dtype="uint8")
    draw.fill(255)
    cv2.drawContours(draw,contours,index,(0,0,0),1)
    (x,y,w,h) = cv2.boundingRect(contours[index])
    cropped = imread[y:y+h,x:x+w]
    mar2,bnww = cv2.threshold(cropped,127,255,cv2.THRESH_BINARY)
    cropped = bnww
        
    matrix = np.array(cropped)
    column_values = np.sum(matrix,axis=1)
    row_values = np.sum(matrix,axis=0)
    
    x=0
    for index in range(0,row_values.shape[0]):
        x+=row_values[index]
        
    y=0
    for index in range(0,column_values.shape[0]):
        y+=column_values[index]

    eucs = []

    #read datasets from csv
    with open(dataset_file,'r') as fh:
        csvreader = csv.reader(fh)
        iter=0
        for row in csvreader:
            iter+=1
            if iter<=1:
                continue
            row[1] = float(row[1])
            row[2] = float(row[2])

    #Euclidean distance Formula
            q1 = (row[1]-x)*(row[1]-x)
            q2 = (row[2]-y)*(row[2]-y)

            euc = math.sqrt(q1+q2)
            eucs.append(euc)
    
    temp_store = eucs.copy()
    temp_store.sort()
    min_euc = temp_store[0]

    if min_euc>x:
        continue

    #finding the index of euclidean distance
    index = eucs.index(min_euc)+1
    captcha_identified.append(index)
    print("identified: "+str(index))

captcha_identified.reverse()
if len(captcha_identified)>0:
    print("\n")
    print("CAPTCHA DECODED: ")
    print(captcha_identified[:len(captcha_identified)])
else:
    print("CAPTCHA DECODING FAILED")        
cv2.imshow("image",cv2.imread(filepath))
cv2.waitKey(0)

cv2.destroyAllWindows()