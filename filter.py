# import cv2
# import numpy as np

# image=cv2.imread('scenery.jpg')
# image=cv2.resize(image,(1000,500))
# # build filters

# kernel1=np.array([
#     [0,0,0],
#     [0,1,0],
#     [0,0,0]
# ])
# kernel2=np.ones((3,3),np.float32)/9.0
# kernel3=np.ones((11,11),np.float32)/121.0

# #applying the filters

# filter1=cv2.filter2D(image,-1,kernel1)
# filter2=cv2.filter2D(image,-1,kernel2)
# filter3=cv2.filter2D(image,-1,kernel3)

# cv2.imshow('image_filter1',filter1)
# cv2.imshow('image_filter2',filter2)
# cv2.imshow('image_filter3',filter3)

# cv2.waitKey(0)

#-----------------------------------------------------------------------------------------------
#motion blurring 
# import cv2
# import numpy as np

# image=cv2.imread('harry potter.jpg')
# image=cv2.resize(image,(1000,600))

# #motion blurring filter
# size=15

# kernel=np.zeros((size,size))
# kernel[int((size-1)/2),:]=1
# kernel=kernel/size

# # applying the filter
# final=cv2.filter2D(image,-1,kernel)

# cv2.imshow('original',image)
# cv2.imshow('final',final)

# cv2.waitKey(0)

#-------------------------------------------------------------------------------------------------
#diffrent prebuilt filters
import cv2
import numpy as np

image=cv2.imread('harry potter.jpg')
image=cv2.resize(image,(1000,600))

# blur and boxfilter
output_blur=cv2.blur(image,(25,25))
output_box=cv2.boxFilter(image,-1,(5,5))

#gaussian bluring

output_gaussian=cv2.GaussianBlur(image,(5,5),0)
#median blur
output_median=cv2.medianBlur(image,5)
#bilateral blur
output_bil=cv2.bilateralFilter(image,5,5000,5)
cv2.imshow('blur',output_blur)
cv2.imshow('boxFilter',output_box)
cv2.imshow('gaussian',output_gaussian)
cv2.imshow('median',output_median)
cv2.imshow('bilateral',output_bil)
cv2.waitKey()
