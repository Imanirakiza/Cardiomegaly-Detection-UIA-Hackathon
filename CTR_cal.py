import matplotlib.pyplot as plt
import numpy as np
import cv2
import os
import cv2


def load(filename):
    np_image = Image.open(filename)
    np_image = np.array(np_image).astype('float32')/255
    np_image = transform.resize(np_image, (512, 512, 1))
    np_image = np.expand_dims(np_image, axis=0)
    return np_image
 
# Read the original image
# img = cv2.imread('/content/CHNCXR_0026_0_mask.png') 


def compute(img):
  lung_mask_gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
  a =0
  b = 0
  c= 0 
  d=0
  a,b,c,d = cv2.boundingRect(lung_mask_gray)
  thresh = cv2.threshold(lung_mask_gray,128,255,cv2.THRESH_BINARY)[1]
  lung_mask_gray = cv2.resize(lung_mask_gray, (2000, 2000))


  result = lung_mask_gray.copy()
  contours = cv2.findContours(thresh, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)
  contours = contours[0] if len(contours) == 2 else contours[1]
  val=[]
  # c=0
  for cntr in contours:
   
    x,y,w,h = cv2.boundingRect(cntr)
    val.append(x)
    # print(val)
    cv2.rectangle(result, (x, y), (x+w, y+h), (0, 0, 255), 2)
    # print("x,y,w,h:",x,y,w,h)

  # x,y,w,h = cv2.boundingRect(lung_mask_gray)
  
  # print(a,b, c, d)
  heart_diameter = w -((x)+(0.85*x))
  
  c1 = (w-(val[0]+val[1]))/w
  # (heart_diameter/w 
  
  if c1>0.5:
    print("The cardiothoracic ratio is ", c1 ,"Therefore, Cardiomegaly is present.")
  elif c1<0.5:
    print(" The CTR is less than 0.5", c1 , "No cardiomegaly present.")

    return None