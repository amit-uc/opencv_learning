import cv2
import numpy as np

img = cv2.imread('messi.jpg')

px = img[100, 100]

print(px)

# Accessing only blue pixels
blue = img[100, 100, 0]
print(blue)

# Modifiying the pixel values
img[100, 100] = [255, 255, 255]

print(img[100, 100])

cv2.rectangle(img, (330, 280), (390, 340), (0, 255, 0), 2)
#img = cv2.rectangle(img, (384, 0), (510, 128), (0, 255, 0), 3)
#ball = img[280:340, 330:390]
#img[273:333, 100:160] = ball

cv2.imshow('img', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
