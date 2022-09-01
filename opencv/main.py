import cv2
import os

os.chdir(os.path.dirname(os.path.abspath(__file__)))

image_path = './data/cat.jpg'

img = cv2.imread(image_path)
img2 = cv2.imread(image_path, cv2.IMREAD_GRAYSCALE)

print(type(img))
print(img.shape)

if img is not None:
    cv2.imshow('dog', img)
    cv2.imshow('gray', img2)
    
    cv2.waitKey(0)
    # save to img
    cv2.imwrite('./data/cat_gray.jpg', img2)
    cv2.destroyAllWindows()
else:
    print("Error!")
