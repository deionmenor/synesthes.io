#for image segmentation
import os
import imageio

#for HSL extraction
import cv2
import numpy as np

#slice image into 3 overlapping parts
def sliceImage(filename):
    img = imageio.imread(filename+".png")
    
    height = img.shape[0]
    width = img.shape[1]
    #get 1/3 of the image
    third = width//3
    
    #get 1/9 of the image
    ninth = width//9
    
    #get partition width
    partitionWidthOne = third+ninth
    partitionWidthTwo = third+third+ninth
    partitionWidthThree = third+third-ninth
    
    #3 sections
    sectionOne = img[:, :partitionWidthOne ]
    sectionTwo = img[:,third:partitionWidthTwo ]
    sectionThree = img[:,partitionWidthThree:]
    
    
    
    newpath = filename 
    if not os.path.exists(newpath):
        os.makedirs(newpath)
    os.chdir(newpath)
    imageio.imsave(filename+"1.png",sectionOne)
    imageio.imsave(filename+"2.png",sectionTwo)
    imageio.imsave(filename+"3.png",sectionThree)
    #image_slicer.save_tiles(partitions,directory=newpath,prefix=filename)

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
    for i in range(3):
        HSLPartitionList.append(getHSL(images[i]))
        print("analyzing partition #",i)
    return HSLPartitionList

#get HSL values of an image's partitions      
def analyzePartitionsSequentially(filename):
    sliceImage(filename)
    images = []
    print("filename:",filename)
    print(os.listdir())

    for i in range(3):
        img = cv2.imread(filename+str(i+1)+".png") 
        images.append(img)
    print(images)
    xxx = createHSLPartitionList(images)
    print(xxx)
    return xxx
