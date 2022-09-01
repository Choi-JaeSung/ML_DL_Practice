import os
import cv2
import numpy as np

from tensorflow import keras

os.chdir(os.path.dirname(os.path.abspath(__file__)))



size = (128, 128)

model = keras.models.load_model('./mask_model.h5')

cap = cv2.VideoCapture(0)

if cap.isOpened():
    while True:
        ret, img = cap.read()
        img_orig = img.copy()

        if ret:
            img = cv2.resize(img, dsize=size)
            img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
            img = img / 255.
            img = img.reshape(-1, 128, 128, 3)
            
            y_pred = model.predict(img)
            
            if y_pred < 0.5:
                y_pred = 0
            else:
                y_pred = 1
            
            if y_pred == 0:
                cv2.putText(img_orig, 'MASK', (50, 100), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 255, 0))
            else:
                cv2.putText(img_orig, 'NO MASK', (50, 100), cv2.FONT_HERSHEY_DUPLEX, 2, (0, 0, 255))
            
            cv2.imshow('camera', img_orig)
            
            if cv2.waitKey(1) != -1:
                break
            
        else:
            print('Error!')

else:
    print('Camera Error!')

cap.release()
cv2.destroyAllWindow()