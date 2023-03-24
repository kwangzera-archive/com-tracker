import numpy as np
import cv2 as cv
import os

poses = "./poses"

for img_path in os.listdir(poses):
    print(img_path)
    img = cv.imread(os.path.join(poses, img_path), cv.IMREAD_GRAYSCALE)
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

    cv.imshow("", output)
    cv.waitKey(0)