import cv2
import numpy as np


def main():
	image=cv2.imread('Foto2.jpeg')
	#image=cv2.resize(image,(1300,800))
	orig=image.copy()
	
	cv2.imshow('Origin',image)
#	cv2.waitKey(0)
#	cv2.destroyAllWindows()


main()