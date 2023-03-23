import numpy as np
import cv2 as cv

rpath = "pose.png"

img = cv.imread(rpath, cv.IMREAD_GRAYSCALE)
h, w = img.shape

'''
(0, 0)    (0, w-1)
  +-------->
  |
  |
  |
  v
(0, h-1)
'''

A = np.sum(img==255)
cr = 0
cc = 0

for r in range(h):
    for c in range(w):
        if img[r, c] == 255:
            cr += r
            cc += c

output = cv.cvtColor(img, cv.COLOR_GRAY2RGB)
cv.circle(output, center=[cc//A, cr//A], radius=10, color=[0, 0, 255], thickness=4)
# output[cx//A, cy//A] = [255, 255, 255]

# [0][0] is the top left corner
# print(cx//A, cy//A)

# print(img[0][0])

cv.imshow("centroid in green", output)
cv.waitKey(0)