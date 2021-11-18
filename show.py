import cv2
import numpy as np


image_path= "/mnt/c/Users/gr009/Desktop/s3/vision/secret.png"
image=cv2.imread(image_path,1)
h,w,c=image.shape

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])
finalListWord=[]
wordIndexPosition=0
tempWord=[]
exitSecondLoop=False
for y in range(h):
    for x in range(w):
        tempPixel=np.binary_repr(image[y,x,0], width=8)
        if wordIndexPosition < 8 :
    
            tempString=list(tempPixel)
            tempWord.append(tempString[7])
            wordIndexPosition=wordIndexPosition+1
        if wordIndexPosition == 8 and tempWord != ['1','1','1','1','1','1','1','1'] :
            finalListWord.append(''.join(tempWord))
            wordIndexPosition=0
            #print(tempWord)
            tempWord=[]
        if image[y,x,0] == 255 :
            exitSecondLoop=True
            break    
    if exitSecondLoop == True :
        break    
print(bits2string(finalListWord))