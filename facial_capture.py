import cv2, sys, numpy

face_cascade = cv2.CascadeClassifier('haarcascade_frontalface_alt.xml')
eye_cascade = cv2.CascadeClassifier('haarcascade_eye.xml')

cam=cv2.VideoCapture(0)

id = raw_input('enter user id  ')
samplenum = 0

while(True):
	ret,frame=cam.read()
	gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
	faces=face_cascade.detectMultiScale(gray,1.3,5)
	for(x,y,w,h) in faces:
		samplenum = samplenum + 1
		cv2.rectangle(frame,(x,y),(x+w,y+h),(0,0,255),2)
		font = cv2.FONT_HERSHEY_SIMPLEX
		cv2.putText(frame, 'Daniel', ((x+w)/2, (y+h)), font, 2, (0,255,255), 2, cv2.LINE_AA)
	
		eyes=eye_cascade.detectMultiScale(gray,1.3,5)
		for (ex,ey,ew,eh) in eyes:
			cv2.rectangle(frame,(ex,ey), (ex+ew,ey+eh), (0,250,0), 2)
	#cv2.imwrite(str(id)+str(samplenum)+".jpg",gray)
	cv2.imshow("Geta",frame)
	cv2.waitKey(100)
	#if(cv2.waitKey(30) & 0xFF == 27):
	if(samplenum>20):
		break
cam.release()
cv2.DestroyAllWindows()

