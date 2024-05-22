import cv2
import numpy as np
black = np.zeros([1400,1401])
black[200:400, 200:400] = 101
print(black)
cv2.imshow("Black Picture", black)
cv2.waitKey(0)