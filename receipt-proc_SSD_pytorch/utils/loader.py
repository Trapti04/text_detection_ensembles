import os
import glob
from cv2 import cv2 as cv
import numpy as np
#import plotly.express as px

class image_reader:

    def __init__(self):
        self.current_directory = os.getcwd()
        self.image_list = []
        self.object_list = []
        self.n_objects = 0
        self.path = '/0325updated_task1train_626p'

    """
    from zipfile import ZipFile

    traindata_filename = "0325train_626p_data.zip"
    # below code unzips all files in folder 0325updated.task1train(626p)
    with ZipFile(traindata_filename, 'r') as zip: 
        # printing all the contents of the zip file 
        zip.printdir() 
  
        # extracting all the files 
        print('Extracting all the files now...') 
        zip.extractall() 
    print('Done!') 
    """
     
    def parse_annotation(self,annotation_path):
        boxes = list()
        labels = list()
        label_map = {'background': 0, 'text': 1}
        f_txt = open(annotation_path)

        # In ICDAR case, the first line is our ROI coordinate (xmin, ymin)
        line_txt = f_txt.readline()
        coor = line_txt.split(',')
        ROI_x = int(coor[0].strip('\''))
        ROI_y = int(coor[1].strip('\''))

        line_txt = f_txt.readline()

        while line_txt:
            coor = line_txt.split(',')
            #print(coor[0])
            #print(annotation_path)
            if coor[0] !='"\r\n':
                xmin = int(coor[0].strip('\'')) - ROI_x
                ymin = int(coor[1].strip('\'')) - ROI_y
                xmax = int(coor[4].strip('\'')) - ROI_x
                ymax = int(coor[5].strip('\'')) - ROI_y
                # text = coor[8].strip('\n').strip('\'')
                boxes.append([xmin, ymin, xmax, ymax])
                labels.append(label_map['text'])

            line_txt = f_txt.readline()

        return {'bboxes': boxes, 'labels': labels}

    def create_dataset(self,path):
        for filepath in glob.glob(self.current_directory + '/' + path +  '/*.txt'):

            filename = filepath.rsplit('\\', 1)[-1]
            
            objects = self.parse_annotation(filepath)
            if len(objects) == 0:
                continue
            self.n_objects += 1
            self.object_list.append(objects)
            self.image_list.append(filename[:-3] + 'jpg')
            
        #print(n_objects, len(object_list))
        assert len(self.object_list) == len(self.image_list), 'mismatch between no. of .txt & .jpg'
        return self.object_list, self.image_list

    def create_unified_dataset(self):


    '''
        print('sample object:' ,object_list[1], ' sample image-Name:', image_list[1])
        path = current_directory + '/' + path + '/' + image_list[1]
        print(path)
        SAMPLE_IMAGE = cv.imread(path)
        fig = px.imshow(SAMPLE_IMAGE)
        #cv.imshow('image',SAMPLE_IMAGE)
        fig.show()
    '''

                       



