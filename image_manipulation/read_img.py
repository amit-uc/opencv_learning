import cv2
import numpy as np

# Load an image in grayscale
img = cv2.imread('football.jpg', cv2.IMREAD_GRAYSCALE)

# Displaying an Image
cv2.imshow("Football Picha", img)
cv2.waitKey(0)
cv2.destroyAllWindows()
