import os
import cv2

os.chdir(os.path.dirname(os.path.abspath(__file__)))



no = 0

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        if ret:
            cv2.imshow('camera', img)
            key = cv2.waitKey(0) & 0xFF
            if key == ord('s'):
                cv2.imwrite(f'./data/no_mask/no_mask_{no}.jpg', img)
                no = no + 1
            else:
                break
            
        else:
            print('Error!')

else:
    print('Camera Error!')

cap.release()
cv2.destroyAllWindows()