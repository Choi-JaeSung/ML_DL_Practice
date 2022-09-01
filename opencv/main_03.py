import os
import cv2
import matplotlib.pyplot as plt



os.chdir(os.path.dirname(os.path.abspath(__file__)))

img = cv2.imread('./data/cat.jpg')
cv2.imshow('cat', img)

img2 = img[0:150, 0:150].copy()
cv2.line(img2, (0, 0), (100, 100), (0, 0, 255), 8)
cv2.imshow('crop', img2)
cv2.imshow('cat', img)


img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
plt.imshow(img)
plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()