import cv2
import numpy as np

img = cv2.imread('football.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('football_picha', cv2.WINDOW_NORMAL)
cv2.imshow('football_picha', img)
cv2.waitKey(0)
cv2.destroyAllWindows()
