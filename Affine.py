import cv2
import numpy as np

img=cv2.imread('harry potter.jpg')
rows,cols=img.shape[:2]
print(img.shape)
print(rows)
print(cols)

src_points=np.float32([
    [0,0],
    [cols-1,0],
    [0,rows-1]
])

dst_points=np.float32([
    [0,0],
    [int(0.6*(cols-1)),0],
    [int(0.4*(cols-1)),rows-1]
])

affine_matrix=cv2.getAffineTransform(src_points,dst_points)
img_output=cv2.warpAffine(img,affine_matrix,(cols,rows))
resize=cv2.resize(img_output,(800,400))
cv2.imshow("window",resize)

cv2.waitKey()