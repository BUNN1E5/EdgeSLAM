import cv2
import numpy as np

cap = cv2.VideoCapture(0)
ret, frame = cap.read()
ret, last = cap.read()

frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
last = cv2.cvtColor(last, cv2.COLOR_BGR2GRAY) 

orb = cv2.ORB_create()
bf = cv2.BFMatcher(cv2.NORM_HAMMING, crossCheck=True)

kp, des = orb.detectAndCompute(frame, None)
kp_last = kp
des_last = des


while(True):
    ret, frame = cap.read()
    frame = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) 
    #Do the work here!
    
    kp, des = orb.detectAndCompute(frame, None)
    img2 = cv2.drawKeypoints(frame,kp, outImage = None, color=(0,255,0), flags=0)
    matches = bf.match(des, des_last)

    matches = sorted(matches, key = lambda x:x.distance)
    matches.reverse()

    img3 = cv2.drawMatches(frame,kp, last,kp_last, matches[:10], None,flags=2)
    # Display the resulting frame
    cv2.imshow('frame', frame)
    cv2.imshow('kp',img2)

    cv2.imshow('matches',img3)
    
    if cv2.waitKey(1) & 0xFF == ord('q'):
        break
    
    last = frame.copy()
    kp_last = kp
    des_last = des
    
cap.release()
cv2.destroyAllWindows()
