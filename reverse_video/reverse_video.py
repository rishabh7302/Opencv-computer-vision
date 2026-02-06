#import the library
import cv2

#video Capture Instance
cap=cv2.VideoCapture('Tom and jerry.mp4')

#Properties of Video

#Total number of frames in video
frames=cap.get(cv2.CAP_PROP_FRAME_COUNT)

#Frames per second of video
fps=cap.get(cv2.CAP_PROP_FPS)

# Height and width of video
height=cap.get(cv2.CAP_PROP_FRAME_HEIGHT)
width=cap.get(cv2.CAP_PROP_FRAME_WIDTH)

#Intiating the output writer for video

fourcc=cv2.VideoWriter_fourcc(*'MPEG')
out=cv2.VideoWriter('reverse.avi',fourcc,fps,(int(width*0.5),int(height*0.5)))

print("NO.of frames are :{}",format(frames))
print("FPS is :{}",format(fps))

#we get the index of the last frame of  the video file
frame_index=frames-1

#Checking if the video instance is ready

if(cap.isOpened()):
    #Reading till the end of the video
    while(frame_index>=0):
        #we set the current frame position to last frame
        cap.set(cv2.CAP_PROP_POS_FRAMES,frame_index)
        ret,frame=cap.read()


        #Resize the frame
        frame=cv2.resize(frame,(int(width*0.5),int(height*0.5)))

        #optional :to show the reversing video
        #cv2.imshow('winname',frame)

        #writing the reversed video
        out.write(frame)
        #Decrementing frame index at each step
        frame_index=frame_index-1

        #printing the progress
        if(frame_index%100==0):
            print(frame_index)
        #if(cv2.waitKey(2)==ord('q')):
        #    break

out.release()
cap.release()
cv2.destroyAllWindows()