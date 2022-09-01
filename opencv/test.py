import cv2
import time

video = cv2.VideoCapture(0)			# WebCam의 경우 0 또는 1
						# 비디오 파일의 경우 '경로/파일명.확장자'

prev_time = 0
FPS = 5

while True:

    ret, frame = video.read()
    
    current_time = time.time() - prev_time

    if (ret is True) and (current_time > 1./ FPS) :
    	
        prev_time = time.time()
        
        cv2.imshow('VideoCapture', frame)
    	
        if cv2.waitKey(1) > 0 :
            
            break