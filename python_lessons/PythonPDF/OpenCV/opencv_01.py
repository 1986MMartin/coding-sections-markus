import cv2
import numpy as np

image=cv2.imread("Foto2_3.jpg")
image=cv2.resize(image,(1300,800))
orig=image.copy()

gray=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
cv2.imshow("Title",gray)
