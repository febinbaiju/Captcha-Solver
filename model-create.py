import cv2
import numpy as np

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
    
    print(x,y)
    cv2.imshow("image",converted)
    cv2.waitKey(0)
cv2.destroyAllWindows()