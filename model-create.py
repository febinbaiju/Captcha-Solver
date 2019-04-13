import cv2
import numpy as np
import csv
import os

fields = ["Digit","X","Y"]
dataset_file = "dataset.csv"
for iterate in range(1,10):
    read = cv2.imread("datasets/{0}.png".format(iterate),0)
    mat,converted = cv2.threshold(read,127,255,cv2.THRESH_BINARY)
    
    matrix = np.array(converted)
    column_values = np.sum(matrix,axis=1)
    row_values = np.sum(matrix,axis=0)
    
    x=0
    for index in range(0,row_values.shape[0]):
        x+=row_values[index]
        
    y=0
    for index in range(0,column_values.shape[0]):
        y+=column_values[index]

    field = [iterate,x,y]
    if iterate<=1:
        if os.path.exists(dataset_file):
            os.remove(dataset_file)
    with open(dataset_file,'a') as fh:
        writer = csv.writer(fh)
        if iterate<=1:
            writer.writerow(fields)
            print(fields)
            writer.writerow(field)
            print(field)
        else:
            writer.writerow(field)
            print(field)

print("Dataset Generated")