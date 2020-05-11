import os
from zipfile import ZipFile

class zip_extractor:
    
    @classmethod
    def __init__(self,filePath):
        self.zipfilename = filePath

    def expand_zip(self):
        #current_directory = os.getcwd()
        traindata_filename = "0325train_626p_data.zip" # filepath
        # below code unzips all files in folder 0325updated.task1train(626p)
        with ZipFile(traindata_filename, 'r') as zip: 
            # printing all the contents of the zip file 
            #zip.printdir() 
            # extracting all the files 
            print('Extracting all the files now...') 
            zip.extractall() 
        print('Done!') 
