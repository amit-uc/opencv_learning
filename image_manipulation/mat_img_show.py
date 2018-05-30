import cv2
import numpy as np
from matplotlib import pyplot as plt

# Load an image in grayscale
img = cv2.imread('football.jpg', cv2.IMREAD_GRAYSCALE)

# Displaying an Image
plt.imshow(img, cmap='gray', interpolation='bicubic')
plt.xticks([]), plt.yticks([]) # Hiding tick values on X and Y axis
plt.show()
