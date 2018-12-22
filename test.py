
import numpy as np
import cv2 as cv
import os
 
def create_HSL_image(hsl_values,image):

    src = image+".png"
    img = cv.imread(src)
    height, width = img.shape[:2]

    font = cv.FONT_HERSHEY_SIMPLEX

    hsl = hsl_values


    ## draw panelist
    img = cv.line(img, (0,int(height/3)), (width,int(height/3)), (50,50,50),4)
    img = cv.line(img, (0,int(height/3*2)), (width,int(height/3*2)), (50,50,50),4)
    img = cv.line(img, (int(width/3),0), (int(width/3),height), (50,50,50),4)
    img = cv.line(img, (int(width/3*2),0), (int(width/3*2),height), (50,50,50),4, lineType=8)

    x = 10
    y = 15
    partition = 0
    for i in range(3):
        for j in range(3):
            cv.putText(img, "H:"+ str(hsl[partition][0]) + " S:"+ str(hsl[partition][1]) + " L:" + str(hsl[partition][2]) , (x, y), font, 0.8, (255,50, 200), 2)
            x = x + int(width/3)
            partition = partition+1
        x = 10
        y=y+int(height/3)+10

    print("Saving image.")
    cv.imwrite( "reef_HSL.png", img )

    # cv.imshow('Draw01',img)
    # cv.waitKey(0)

