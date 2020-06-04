# encoding:utf-8
import os
import time

import cv2
import matplotlib

import matplotlib.pyplot as plt
import numpy as np


DATA_FOLDER = "/data/res/"
RES_FOLDER = "/data/res_image/" 
cur_dir =os.getcwd()

def get_training_data():
    img_files = []
    exts = ['jpg', 'png', 'jpeg', 'JPG']
    for parent, dirnames, filenames in os.walk((cur_dir + DATA_FOLDER)):
        for filename in filenames:
            for ext in exts:
                if filename.endswith(ext):
                    img_files.append(os.path.join(parent, filename))
                    break
    print('Find {} images'.format(len(img_files)))
    return img_files


def load_annotation(p):
    bbox = []
    with open(p, "r") as f:
        lines = f.readlines()
    for line in lines:
        line = line.strip().split(",")[0:8]
        x_1, y_1, x_2, y_2,x_3, y_3, x_4, y_4 = map(int, line)
        bbox.append([x_1, y_1, x_2, y_2,x_3, y_3, x_4, y_4, 1])
    return bbox


def print_output():
    image_list = np.array(get_training_data())
    print('{} training images in {}'.format(image_list.shape[0], DATA_FOLDER))
    index = np.arange(0, image_list.shape[0])
    
    for i in index:
        im_fn = image_list[i]
        im = cv2.imread(im_fn)
        h, w, c = im.shape
        im_info = np.array([h, w, c]).reshape([1, 3])
                
        _, fn = os.path.split(im_fn)
        fn, _ = os.path.splitext(fn)
                
        txt_fn = os.path.join((cur_dir + DATA_FOLDER), fn + '.txt')
        if not os.path.exists(txt_fn):
            print("Ground truth for image {} not exist!".format(im_fn))
            continue
        bbox = load_annotation(txt_fn)
        if len(bbox) == 0:
            print("Ground truth for image {} empty!".format(im_fn))
            continue

               
        for p in bbox:
            cv2.rectangle(im, (p[0], p[1]), (p[4], p[5]), color=(0, 0, 255), thickness=1)
        cv2.imwrite((cur_dir + RES_FOLDER + fn + '_res.jpg'), im) # as above
                    

if __name__ == '__main__':
   print_output()
   print('done')
