import os
from PIL import Image
import cv2
def resize_pic(path):
    files=os.listdir(path)
    for file in files:
        if str(file).split('.')[0]=='0003':
            print(file)
            #img=cv2.imread(path+file)
            img=Image.open(path+file)
            img=img.resize((10, 10),Image.ANTIALIAS)
            #cv2.imwrite(path+file,img)
            img.save(path+file)


path='./tmp/'
resize_pic(path)