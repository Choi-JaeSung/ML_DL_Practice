import cv2


cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            cv2.line(img, (50, 50), (150, 150), (255, 0, 0), 8)
            cv2.rectangle(img, (150, 150), (400, 400), (0, 0, 255), 8)
            cv2.putText(img, 'NO MASK', (50, 100), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))
            cv2.imshow('line', img)
            
            if cv2.waitKey(1) != -1:
                break
            
        else:
            print('Error!')

else:
    print('Camera Error!')

cap.release()
cv2.destroyAllWindow()