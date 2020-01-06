# This script removes all the empty and duplicate files from the directory
# and loads the csv data into a pandas dataframe

import os
import pandas as pd

#Progress Bar
from tqdm import tqdm

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

    print("Found %i files!" % len(files))                    
                    
    return files

 #individually reads the csv files and creates a list(files) of all dataframes
def getDataFrames(files):
    readFiles = []
    #Iterate using tqdm to show a progress bar.
    for file in tqdm(files, total=len(files)):
        readFiles.append(pd.read_csv(file))
    
    return readFiles
#Recursion function to remove items from a loop while iterating.
def recConcat(frames, concatFrame):
    print(len(concatFrame))
    if len(frames) > 1:
        for frame in frames:
            concatFrameNew = pd.concat([concatFrame, frame], sort=False)
            del concatFrame
            frames.remove(frame)
            recConcat(frames, concatFrameNew)
    else:
        concatFrame = pd.concat([concatFrame,frames[0]], sort=False)
    return(concatFrame)

#concatenates all dataframes into one single dataframe to be used
def concatDataFrames(frames):
    concatFrame = pd.DataFrame()

    for dframe in tqdm(frames, total=len(frames)):
        recConcat(frames, concatFrame)

    return concatFrame
    

if __name__ == '__main__':
    path = r'./D2L Data'
    files = getFiles(path)
    
    readFiles = getDataFrames(files)
   
    data = concatDataFrames(readFiles)
    
    
     
    
    
    
    
    
    
        





        