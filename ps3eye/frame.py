import cv2
import numpy
import subprocess

img = numpy.zeros([800,800,3])

img[:,:,0] = numpy.ones([800,800])*1
img[:,:,1] = numpy.ones([800,800])*1
img[:,:,2] = numpy.ones([800,800])*1
x=0
cv2.imwrite('color_img.jpg', img)
i=1
cap = cv2.VideoCapture(0) 

# set the exposure after opening the capture to
# avoid opencv modifying settings
#cap.set(cv2.CV_CAP_PROP_FPS, 15)
fps = "v4l2-ctl --device=/dev/video0 -p 15"
menu = "v4l2-ctl --device=/dev/video2 --set-ctrl auto_exposure=1"
exposure = "v4l2-ctl --device=/dev/video2 --set-ctrl exposure=255"
output1 = subprocess.call(fps, shell=True)
output2 = subprocess.call(menu, shell=True)
output3 = subprocess.call(exposure, shell=True)

#cv2.circle(img, (400,400), 20, (0,0,255), -1)
cv2.putText(img,"text", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0),2)
cv2.imshow("image", img);
#cv2.waitKey();
if( cv2.waitKey(0) & 0xFF == ord('s') ): 
	while(True):
		cv2.circle(img, ((x%800),400), 20, (255,255,255), -1)
		cv2.circle(img, ((x%800)+40,400), 20, (0,0,255), -1)
		cv2.waitKey(10)
		x=x+10;
		ret, frame = cap.read() 
        cv2.imshow('frame', frame)
        cv2.imwrite('15fps/test%02d.jpg'%i,frame)
        i=i+1;
		cv2.imshow("image", img);
		if(cv2.waitKey(1) & 0xFF == ord('q') ): 
			cv2.destroyAllWindows()
			exit();
		if(i=90)
			exit();
			break;

    
if(cv2.waitKey(0) & 0xFF == ord('q') ): 
	cv2.destroyAllWindows()

cap.release() 
cv2.destroyAllWindows()