import cv2
import numpy as np

image = cv2.imread('test_image.jpg')
lane_image = np.copy(image)
gray = cv2.cvtColor(image, cv2.COLOR_RGB2GRAY)

# cv2.imwrite('test_image_grayscale.jpg', gray)
cv2.imshow("result", gray)
cv2.waitKey(0)
