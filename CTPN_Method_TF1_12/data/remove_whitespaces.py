import numpy as np
import cv2

img = cv2.imread('X51006414429_res.jpg') # Read in the image and convert to grayscale
cv2.imshow('X51006414429_res.jpg',img)
#img = img[:-20,:-20] # Perform pre-cropping
gray = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
gray = 255*(gray < 128).astype(np.uint8) # To invert the text to white
gray = cv2.morphologyEx(gray, cv2.MORPH_OPEN, np.ones((2, 2), dtype=np.uint8)) # Perform noise filtering
coords = cv2.findNonZero(gray) # Find all non-zero points (text)
x, y, w , h = cv2.boundingRect(coords) # Find minimum spanning bounding box
x = x-16
y=y-16
w= w+32
h=h+32
rect = img[y:y+h, x:x+w] # Crop the image - note we do this on the original image
cv2.imshow("Cropped", rect) # Show it
cv2.waitKey(0)
cv2.destroyAllWindows()
cv2.imwrite("rect.png", rect) # Save the image