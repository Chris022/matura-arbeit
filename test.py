import numpy as np
import cv2 as cv
import math

img = np.zeros((900,900,3))

filter = [[0,0,0],
          [0,0,1],
          [0,1,0]]

size = 300

for y in range(0, len(img)):
    for x in range(0, len(img[y])):

        color = filter[math.floor(x/300)][math.floor(y/300)]

        img[y][x] = 255-color*255

color = 70
for y in range(0, len(img)):

    img[y][299] = color
    img[y][300] = color
    #img[y][298] = color
    #img[y][301] = color
    img[y][599] = color
    img[y][600] = color
    #img[y][598] = color
    #img[y][601] = color

    if y%5 == 0:
        color = 255-color

color = 70
for x in range(0, len(img[0])):

    img[299][x] = color
    img[300][x] = color
    #img[298][x] = color
    #img[301][x] = color
    img[599][x] = color
    img[600][x] = color
    #img[598][x] = color
    #img[601][x] = color

    if x%5 == 0:
        color = 255-color

cv.imwrite("test.png", img)