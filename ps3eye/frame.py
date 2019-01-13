import cv2
import numpy
import time

img = numpy.zeros([800,800,3])

img[:,:,0] = numpy.ones([800,800])*1
img[:,:,1] = numpy.ones([800,800])*1
img[:,:,2] = numpy.ones([800,800])*1
x=0

cv2.putText(img,"text", (50, 50), cv2.FONT_HERSHEY_SIMPLEX, 2.0, (0,0,0),2)
cv2.imshow("image", img);

while (True):
	if(int(time.time())==1547355802): 
		while(True):
			cv2.circle(img, ((x%800),400), 10, (255,255,255), -1)
			cv2.circle(img, ((x%800)+10,400), 10, (0,0,255), -1)
			cv2.waitKey(10)
			x=x+10;
			cv2.imshow("image", img);
			if(cv2.waitKey(1) & 0xFF == ord('q') ): 
				cv2.destroyAllWindows()
				exit();

    
if(cv2.waitKey(0) & 0xFF == ord('q') ): 
	cv2.destroyAllWindows()

cap.release() 
cv2.destroyAllWindows()