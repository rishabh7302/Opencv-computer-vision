import cv2
import numpy as np

image=cv2.imread('fantasy.jpg')
image=cv2.resize(image,(600,500))
image=cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
sobel_x=cv2.Sobel(image,-1,1,0)
sobel_y=cv2.Sobel(image,-1,0,1)

sobel_xy=cv2.addWeighted(sobel_x,0.5,sobel_y,0.5,0)

# apply laplacian
laplacian=cv2.Laplacian(image,-1)

#now canny edge detection

canny=cv2.Canny(image,80,150)

cv2.imshow("sobelx",sobel_x)
cv2.imshow("sobely",sobel_y)
cv2.imshow("sobelxy",sobel_xy)
cv2.imshow("laplacian",laplacian)
cv2.imshow("canny",canny)

cv2.waitKey()
cv2.destroyAllWindows()