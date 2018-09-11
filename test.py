import cv2
import numpy as np
from matplotlib import pyplot as plt

img_rgb = cv2.imread('Untitled.png')
img_gray = cv2.cvtColor(img_rgb, cv2.COLOR_BGR2GRAY)

temp = cv2.imread('Capture.PNG')
template = cv2.cvtColor(temp, cv2.COLOR_BGR2GRAY)

lap_img = cv2.Laplacian(img_gray, cv2.CV_32F)
lap_temp = cv2.Laplacian(template, cv2.CV_32F)

cv2.imshow("test", lap_img)
cv2.waitKey(0)
cv2.imshow("test", lap_temp)
cv2.waitKey(0)

#
## cv2.imshow("test", template)
## cv2.waitKey()
## cv2.imshow("test", temp_gray)
## cv2.waitKey(0)


w, h = lap_temp.shape[::-1]

res = cv2.matchTemplate(lap_img, lap_temp, cv2.TM_CCOEFF_NORMED)
threshold = .9
loc = np.where(res >= threshold)

counter = 0
for pt in zip(*loc[::-1]):
    cv2.rectangle(img_rgb, pt, (pt[0] + w, pt[1] + h), (0,255,255), 2)
    print loc[0], loc[1]
    counter += 1

print "Number of matches: %s" % counter
cv2.imshow('Detected', img_rgb)
cv2.waitKey(0)


cv2.destroyAllWindows()
