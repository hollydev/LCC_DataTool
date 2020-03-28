"""
    Filename: getFiles.py
    Programmer: 
    Date Created: 01/03/2020
    Last Update: File Created

    Description: This script removes all the empty and duplicate files from the directory
    and loads the csv data into a pandas dataframe

"""

from messages.system import SYSTEM
import os
import pandas as pd


#Progress Bar
from tqdm import tqdm


# returns True if the file is not a duplicate or empty.
def check_file(fileName):
    ret = False
    if ('test' not in fileName.lower()) and (os.path.getsize(fileName) > 460):
        ret = True
    
    return ret

def add_unwanted_path(unwanted, path):
    unwanted.append(path)
    

# returns True if the file is in an acceptable directory.
def check_file_name(filename, unwanted):
    ret = True
    # loops through unwanted paths and skips over file in dir in apart of file name
    for dir in unwanted:
        if dir in filename:
            ret = False
    
    return ret

# returns a list of all 'good' csv files
def get_files(myPath, unwanted):

    files = []
    skippedFiles = 0

    for root, dirs, f in os.walk(myPath):
        for file in f:
            if '.csv' in file:
                fileName = os.path.join(root, file)
                
                if check_file_name(fileName, unwanted):
                
                    if check_file(fileName) == True:
                        files.append(fileName)
                    else:
                        skippedFiles += 1
                else:
                    skippedFiles += 1

    print("Found {} files. ({} skipped)".format(len(files), skippedFiles))
                    
    return files


 #individually reads the csv files and creates a list(files) of all dataframes
def get_data_frames(files):
    readFiles = []
    #Iterate using tqdm to show a progress bar.
    for file in tqdm(files, total=len(files)):
        readFiles.append(pd.read_csv(file))
    
    return readFiles

#Seperate looping function to return removed items as it iterates.
def recursive_concat(frames):
    for frame in frames:
        frames.remove(frame)
        return(frame)

#concatenates all dataframes into one single dataframe to be used
def concat_data_frames(frames):
    size = len(frames)
    progressBar = tqdm(total=3)

    firstThird = round(size/3)
    secondThird = round(2*size/3)
    frames1 = frames[:firstThird]
    frames2 = frames[firstThird:secondThird]
    frames3 = frames[secondThird:-1]
    
    concatFrames1 = pd.concat(frames1, sort = False)
    
    
    #For each deleted frame, concat to the new frame.
    for delFrame in frames1:
        recursive_concat(frames1)
    progressBar.update(1)
    progressBar.display()
    
    concatFrames2 = pd.concat(frames2, sort = False)
    
    for delFrame in frames2:
        recursive_concat(frames2)
    progressBar.update(1)
    progressBar.display()

    concatFrames3 = pd.concat(frames3, sort = False)
    
    for delFrame in frames3:
        recursive_concat(frames3)
    progressBar.update(1)
    progressBar.display()

    allFrames = [concatFrames1, concatFrames2, concatFrames3]
    finalFrame = pd.concat(allFrames, sort = False)
    progressBar.close()

    return finalFrame

# unwanted is a list of all unchecked dirs and files from GUI
def execute(path, unwanted):
    ret = pd.DataFrame()
    files = get_files(path, unwanted)
    
    if(len(files) == 0):
        print(SYSTEM.noFilesFound)
        
    else:
        readFiles = get_data_frames(files)
        ret = concat_data_frames(readFiles)
        
    return ret


if __name__ == "__main__": 
    path = r'../../D2L data'
    unwanted = ['A&S', 'Gradebook Downloads', 'HHS', 'Archived']
    pd = execute(path, unwanted)
    l = pd['GradeValue']
    index = 0
    for i in l:
        
        print(i, ' -- ', pd['CourseOfferingCode'][index])
            
        index = index + 1
    
   
    
    
    

    
    
    
     
    
    
    
    
    
    
        





        