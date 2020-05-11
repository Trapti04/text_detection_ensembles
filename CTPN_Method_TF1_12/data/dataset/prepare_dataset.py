import csv
import glob
import os
import random
import shutil
#from PIL import Image
#from skimage import io
import cv2
import sys

# This class is to prepare the data. It retrieves x0,y0 and x3,y3 co-ordinates from original txt file
# copies to a new label file in mlt/label directory and stores the correspouning image in mlt/image


def get_data():
    home_path = "/home/trapti_kalra/receipt-processing/CTPN_Method_TF1_12/data/dataset/"
    filenames = [os.path.splitext(os.path.basename(f))[0] for f in glob.glob(home_path + "original/*.jpg")]
    
    jpg_files = [s + ".jpg" for s in filenames]
    txt_files = [s + ".txt" for s in filenames]

    for file in txt_files:
        boxes = []
       # with open(file, "r", encoding="utf-8", newline="") as lines: # to work with python2.7
        try:
            with open(home_path + "original/" + file, "r") as lines:
                for line in csv.reader(lines):
                    boxes.append([line[0], line[1], line[6], line[7]])
        
            with open(home_path + "mlt/label/" + file, "w+") as labelFile:
                wr = csv.writer(labelFile)
                wr.writerows(boxes)
        except IOError:
            print(file + " not found in original")
            img_to_be_rm = file.split('.')[0] + '.jpg'
            jpg_files.remove(img_to_be_rm)

    for jpg in jpg_files:
        shutil.copy(home_path + "original/" + jpg, home_path + "mlt/image/")


if __name__ == "__main__":
    get_data()