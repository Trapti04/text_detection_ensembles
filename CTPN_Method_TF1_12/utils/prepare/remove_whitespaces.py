import numpy as np
import cv2
import os
import sys
from tqdm import tqdm

cur_dir = os.getcwd()

DATA_FOLDER = '/data/res_image/bad_quality/'
OUTPUT = '/data/demo/white_space_samples/'
ORIGINAL_FOLDER = '/data/demo/'

im_fns = os.listdir(cur_dir + DATA_FOLDER)

for im_fn in tqdm(im_fns):
    try:
        _, fn = os.path.split(im_fn)
        bfn, ext = os.path.splitext(fn)
        if bfn.endswith('_res'):
            bfn = bfn[:-4]
        im_fn = bfn + ext
        img_path = cur_dir + ORIGINAL_FOLDER + im_fn
        img = cv2.imread(img_path) # Read in the image and convert to grayscale
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
        #cv2.waitKey(0)
        #cv2.destroyAllWindows()
        out_path = cur_dir + OUTPUT + im_fn
        cv2.imwrite(out_path, rect) # Save the image
    except Exception as e:
        print("Error processing {} has exception {}".format(im_fn, e))





