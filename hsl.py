
#for image segmentation
import image_slicer
import os

#for HSL extraction
import cv2
import numpy as np

#slice image into 9 equal parts
def sliceImage(filename):
    partitions = image_slicer.slice(filename+".png",9,save=False)
    newpath = filename 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    image_slicer.save_tiles(partitions,directory=newpath,prefix=filename)

#convert rgb to hsl   
def hsl(r,g,b):
    
    r=r/255
    g=g/255
    b=b/255
    vmax = max(r,g,b)
    vmin = min(r,g,b)
    vsum = vmax + vmin
    hsllist = []
    l = vsum/2
    h=0
    s=0

    if vmax != vmin:
        vdiff = vmax - vmin
        if l >= 0.5:
            s = vdiff/(2-vsum)
        else:
            s = vdiff/vsum
            if vmax == r:
                h = 60*(g-b)/vdiff
            elif vmax == g:
                h = 120+60*(b-r)/vdiff
            elif vmax == b:
                h = 240 + 60*(r-g)/vdiff

    if h<0:
        h = h+360

    hsllist.append(h)
    hsllist.append(s)
    hsllist.append(l)
    return hsllist

#get mean of numbers
def mean(numbers):
    return float(sum(numbers))/max(len(numbers),1)

#get mean HSL values of an image
def getHSL(image):
    pixels = np.asarray(image.shape)
    rows = pixels[0]
    columns = pixels[1]
    hlist = []
    slist = []
    llist = []
    
    for i in range(rows):
        for j in range(columns):
            r=image[i,j,0]
            g=image[i,j,1]
            b=image[i,j,2]
            hsllist = hsl(r,g,b)
            hlist.append(hsllist[0])
            slist.append(hsllist[1])
            llist.append(hsllist[2])

    output=[mean(hlist),mean(slist),mean(llist)]
    return output

#get HSL values of multiple images
def createHSLPartitionList(images):
    HSLPartitionList = []
    for i in range(9):
        HSLPartitionList.append(getHSL(images[i]))
        print("analyzing partition #",i)
    return HSLPartitionList

#get HSL values of an image's partitions      
def analyzePartitions(filename):
    sliceImage(filename)
    images = []

    for files in os.listdir(filename):
        img = cv2.imread(filename+"/"+files)
        images.append(img)
    
    xxx = createHSLPartitionList(images)
    print(xxx)
    return xxx
