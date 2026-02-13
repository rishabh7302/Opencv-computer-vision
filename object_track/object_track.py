import cv2
import numpy as np

#defining called tracker function
def setValues(x):
    print("")

#creating the trackbars needed for adjusting the marker colour
cv2.namedWindow("color detector")
cv2.createTrackbar("upper hue","color detector",153,180,setValues)
cv2.createTrackbar("upper saturation","color detector",255,255,setValues)
cv2.createTrackbar("upper value","color detector",255,255,setValues)
cv2.createTrackbar("lower hue","color detector",64,180,setValues)
cv2.createTrackbar("lower saturation","color detector",72,255,setValues)
cv2.createTrackbar("lower value","color detector",49,255,setValues)

#capture the inpur frame from webcam
def get_frame(cap,scaling_factor):
    ret,frame=cap.read()
    # resize the input frame
    frame=cv2.resize(frame,None,fx=scaling_factor,fy=scaling_factor,interpolation=cv2.INTER_AREA)
    return frame

if __name__=='__main__':
    cap=cv2.VideoCapture(0)
    scaling_factor=0.9
    #Iterate until the use presses ESC key
    while True:
        frame=get_frame(cap,scaling_factor)

        #convert the HSV colorSpace
        hsv=cv2.cvtColor(frame,cv2.COLOR_BGR2HSV)
        u_hue=cv2.getTrackbarPos("upper hue","color detector")
        u_saturation=cv2.getTrackbarPos("upper saturation","color detector")
        u_value=cv2.getTrackbarPos("upper value","color detector")
        l_hue=cv2.getTrackbarPos("lower hue","color detector")
        l_saturation=cv2.getTrackbarPos("lower saturation","color detector")
        l_value=cv2.getTrackbarPos("lower value","color detector")

        #Define 'color' range in HSV colorSpace

        upper_hsv=np.array([u_hue,u_saturation,u_value])
        lower_hsv=np.array([l_hue,l_saturation,l_value])

        #Threshold the HSV image to get only selected color

        mask=cv2.inRange(hsv,lower_hsv,upper_hsv)
        #Bitwise AND mask and original image

        res=cv2.bitwise_and(frame,frame,mask=mask)
        res=cv2.medianBlur(res,5)

        cv2.imshow('Orginal image',frame)
        cv2.imshow('Color Detector',res)

        #check if the user pressed ESC key
        c=cv2.waitKey(5)
        if c==27:
            break

cv2.destroyAllWindows()