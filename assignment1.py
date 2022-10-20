# importing Modules
from asyncio.windows_events import NULL
import cv2 as cv
import numpy as np
import datetime

# Capturing Video
cap=cv.VideoCapture(0)
fourcc = cv.VideoWriter_fourcc(*'XVID')
out = cv.VideoWriter('output.avi', fourcc, 20.0, (640, 480))

flagrec=False
starttime=NULL
font = cv.FONT_HERSHEY_SIMPLEX
flagshow=True

def mouse_click(event,x ,y , flags, param):
    global flagshow
    if x<=370 and x>270 and y<=290 and y>190:
        if event == cv.EVENT_RBUTTONDOWN:
            flagshow=False

# Recording 
while(flagshow):
    ret, frame = cap.read()
    if ret == True: 
        if cv.waitKey(1) & 0xFF == ord('p'):
            flagrec=True
            starttime=datetime.datetime.now()
        if starttime:
            if starttime.time().second+5<=datetime.datetime.now().time().second:
                frame=cv.rectangle(frame,(270,190),(370,290),(0,0,255),-1)
                frame=cv.putText(frame,'Paridhi',(290,240) ,font ,0.5 ,(255,255,255) ,1 ,cv.LINE_AA)
        if cv.waitKey(1) & 0xFF == ord('l'): 
            break
        if flagrec:
            out.write(frame)
        cv.imshow('frame',frame)
        cv.setMouseCallback('frame',mouse_click)
    else:
        break 

cap.release()
out.release()
cv.destroyAllWindows()