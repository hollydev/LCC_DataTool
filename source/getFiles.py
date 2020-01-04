# This script removes all the empty and duplicate files from the directory
# and loads the csv data into a pandas dataframe

import os
import pandas as pd

# returns True if the file is not a duplicate or empty.
def checkFile(fileName):
    ret = False
    if ('test' not in fileName.lower()) and (os.path.getsize(fileName) > 460):
        ret = True
    
    return ret

# returns a list of all 'good' csv files
def getFiles(myPath):

    files = []

    for root, dirs, f in os.walk(myPath):
        for file in f:
            if '.csv' in file:
                fileName = os.path.join(root, file)
                
                if checkFile(fileName) == True:
                    files.append(fileName)
                    
                    
    return files

 #individually reads the csv files and creates a list(readFiles) of all dataframes
def getDataFrames(files):
    readFiles = []
    for file in files:
        readFiles.append(pd.read_csv(file))
        
    return readFiles

#concatenates all dataframes into one single dataframe to be used
def concatDataFrames(files):
    return pd.concat(files, sort=False)
    

if __name__ == '__main__':
    path = r'./D2L Data'
    files = getFiles(path)
    
    readFiles = getDataFrames(files)
   
    data = concatDataFrames(readFiles)
    
    
     
    
    
    
    
    
    
        





        