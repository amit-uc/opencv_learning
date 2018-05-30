import cv2
import numpy as np

img = cv2.imread('football.jpg', cv2.IMREAD_GRAYSCALE)

cv2.namedWindow('football', cv2.WINDOW_NORMAL)
cv2.imshow('football', img)
key_pressed = cv2.waitKey(0)

if key_pressed == 27:
    cv2.destroyAllWindows()
elif key_pressed == ord('s'):
    cv2.imwrite('footballgrey.png', img)
    cv2.destroyAllWindows()
