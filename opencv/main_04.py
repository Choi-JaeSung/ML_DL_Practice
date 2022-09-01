import os
import cv2

os.chdir(os.path.dirname(os.path.abspath(__file__)))



img = cv2.imread('./data/cat.jpg')
cv2.imshow('cat', img)
print(img.shape)
h, w, c = img.shape

img_resized = cv2.resize(img, (int(h * 0.5), int(w * 0.5)))
cv2.imshow('resize', img_resized)

img_flip = cv2.flip(img_resized, 0)
cv2.imshow('flip', img_flip)

cv2.waitKey(0)
cv2.destroyAllWindows()