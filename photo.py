import numpy
import cv2
import os
for filename in os.listdir('C:\\Users\\'):
img = cv2.imread('C:\\somedirectory\\\\Photo-EA-3.JPG', )
    img = cv2.imread('filename')
    tile = numpy.tile(img, (2, 5, 1));
#    cv2.imshow('Tile', tile)
    cv2.imwrite('filemname', tile)
cv2.waitKey(0)
cv2.destroyAllWindows()
