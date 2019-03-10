import cv2
import os

def image_crop(img,folder):
    imr = cv2.imread(img,0)
    height,width = imr.shape
    roi = imr[0:16,0:width]
    base = os.path.basename(img) 
    cv2.imwrite(folder+base,roi)