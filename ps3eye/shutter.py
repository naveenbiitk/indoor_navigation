import cv2 
import subprocess
import time

# open the capture
cap = cv2.VideoCapture(2) 
i=0
# set the exposure after opening the capture to
# avoid opencv modifying settings
#cap.set(cv2.CV_CAP_PROP_FPS, 15)
fps = "v4l2-ctl --device=/dev/video2 -p 15"
menu = "v4l2-ctl --device=/dev/video2 --set-ctrl auto_exposure=1"
exposure = "v4l2-ctl --device=/dev/video2 --set-ctrl exposure=255"
output1 = subprocess.call(fps, shell=True)
output2 = subprocess.call(menu, shell=True)
output3 = subprocess.call(exposure, shell=True)

# watch your changes!
while (True):
	if(int(time.time())==1547355802): 
		while(True):
			ret, frame = cap.read() 
        	cv2.imshow('frame', frame)
        	cv2.imwrite('15fps/test%02d.jpg'%i,frame)
        	i=i+1;
			#cv2.imshow("image", img);
			if(i=100)
				exit();
				break;
			if(cv2.waitKey(1) & 0xFF == ord('q') ): 
				cv2.destroyAllWindows()
				exit();

    
if(cv2.waitKey(0) & 0xFF == ord('q') ): 
	cv2.destroyAllWindows()


cap.release() 
cv2.destroyAllWindows()
