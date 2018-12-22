
#for image segmentation
import image_slicer
import os

#for HSL extraction
import cv2 
import numpy as np

#slice image into 9 equal parts
def sliceImage(filename):
    partitions = image_slicer.slice("img/"+filename+".png",9,save=False)
    newpath = filename 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    image_slicer.save_tiles(partitions,directory=newpath,prefix=filename)


def create_HSL_image(hsl_values,image):

    src = image+".png"
    img = cv2.imread(src)
    height, width = img.shape[:2]

    font = cv2.FONT_HERSHEY_SIMPLEX

    hsl = hsl_values


    ## draw panelist
    img = cv2.line(img, (0,int(height/3)), (width,int(height/3)), (50,50,50),4)
    img = cv2.line(img, (0,int(height/3*2)), (width,int(height/3*2)), (50,50,50),4)
    img = cv2.line(img, (int(width/3),0), (int(width/3),height), (50,50,50),4)
    img = cv2.line(img, (int(width/3*2),0), (int(width/3*2),height), (50,50,50),4, lineType=8)

    x = 10
    y = 15
    partition = 0
    for i in range(3):
        for j in range(3):
            text = "H:"+ str(round(hsl[partition][0],2)) + " S:"+ str(round(hsl[partition][1],2)) + " L:" + str(round(hsl[partition][2],2))
            cv2.putText(img,text,(x, y), font, 0.4, (255,50, 200), 2)
            x = x + int(width/3)
            partition = partition+1
        x = 10
        y=y+int(height/3)+10

    print("Saving image.")
    cv2.imwrite( image+"_hsl_map.png", img )
   
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

def mean(numbers):
    return float(sum(numbers))/max(len(numbers),1)

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

def createHSLPartitionList(images):
    HSLPartitionList = []
    for i in range(9):
        HSLPartitionList.append(getHSL(images[i]))
        print("analyzing partition #",i)
    return HSLPartitionList
        
def analyzePartitions(filename):
    print("this is the filename",filename)
    sliceImage(filename)
    images = []
    print(os.listdir())
    print(os.listdir(filename))
    for files in os.listdir(filename):
        img = cv2.imread(filename+"/"+files)
        images.append(img)
    
    xxx = createHSLPartitionList(images)
    print(xxx)
    return xxx
