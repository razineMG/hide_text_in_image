import cv2
import numpy as np


image_path= "/mnt/c/Users/gr009/Desktop/s3/vision/tp/img/cr7.jpg"
image=cv2.imread(image_path,1)
h,w,c=image.shape
userinput=input("enter your text: ")
def string2bits(s=''):
    return [bin(ord(x))[2:].zfill(8) for x in s]

def bits2string(b=None):
    return ''.join([chr(int(x, 2)) for x in b])

bitsOftext = string2bits(userinput)
#s2 = bits2string(b)
print(len(bitsOftext))
#print(s2)
currentBitoftextPosition=-1
bitsOftextLock=False
wordIndexPosition=0
end=False
for y in range(h):
    for x in range(w):
        tempPixel=np.binary_repr(image[y,x,0], width=8)
        if currentBitoftextPosition < len(bitsOftext) and bitsOftextLock==False :
            currentBitoftextPosition=currentBitoftextPosition+1
        if wordIndexPosition < 8 :
            bitsOftextLock=True
            #print(tempPixel)
            tempString=list(tempPixel)
            tempString[7]=bitsOftext[currentBitoftextPosition][wordIndexPosition]
            wordIndexPosition=wordIndexPosition+1
            #print(tempString)
            #print(''.join(tempString))
            image[y,x,0]=np.uint8(int("".join(tempString),2))
        elif currentBitoftextPosition+1 < len(bitsOftext) :
            currentBitoftextPosition=currentBitoftextPosition+1
            tempString=list(tempPixel)
            tempString[7]=bitsOftext[currentBitoftextPosition][0]
            wordIndexPosition=1
            image[y,x,0]=np.uint8(int("".join(tempString),2))
        elif currentBitoftextPosition+1 == len(bitsOftext) and end==False:
            end=True
            print('y ',y,' x',x,' image ',image[y,x-1,0])
            image[y,x,0]=255
        
cv2.imwrite('secret.png',image)            
