import cv2
import numpy as np

# Create a black image
img = np.zeros((512, 512, 3), np.uint8)

# Draw a diagonal blue line with thickness of 5 px
img = cv2.line(img, (0,0), (511, 511), (255, 0, 0), 5)
img = cv2.line(img, (0,511), (511, 0), (255, 0, 0), 5)
img = cv2.line(img, (255,0), (255, 511), (255, 0, 0), 5)

cv2.imshow('img', img)

cv2.waitKey(0)
cv2.destroyAllWindows()
