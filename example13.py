import cv2
import numpy as np

img = cv2.imread(r'C:\Users\ASSAF\Documents\Program\opencv\OpenCV2-Python-Tutorials\messi5.jpg');

#res = cv2.resize(img,None,fx=2, fy=2, interpolation = cv2.INTER_LINEAR);
#cv2.imshow("messy_small", res);cv2.waitKey(0);

rows,cols,_ = img.shape

#M = np.float32([[1,0,100],[0,1,50]])
#dst = cv2.warpAffine(img,M,(cols+100,rows+100))

M = cv2.getRotationMatrix2D((cols / 4, rows / 2), 50, 1)
dst = cv2.warpAffine(img, M, (cols, rows))

cv2.imshow('img',dst)
cv2.waitKey(0)
cv2.destroyAllWindows()
