import matplotlib
import numpy as nm
import cv2
import os, sys
import FeatureDetection

#print sys.argv[0]
# print sys.path
projectDir = sys.path[0]

image = "moduleSA3D-icon48.png"
imageDir = "/imageDatabase/icons/modulebuttons/%s" % image
template = "Untitled.png"

feature = cv2.imread('C:\Moe-Repo\OpenCV\src\Capture.PNG')
# cv2.imshow("Test", feature)
# cv2.waitKey(0)

window = cv2.imread(template)
# cv2.imshow("cvi42 Window Snapshot", window)
# cv2.waitKey(0)

FeatureDetection.compareDetectionMeth(feature, window)
exit(0)
