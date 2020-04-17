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
import time

'''
    check_file takes a fileName and checks if the file contains "test" in the 
    name and if the file has a size >460
    
    @Params:
        fileName - the file wanted to be checked
        
    @Returns:
        ret - Boolean
            True - if file does not contain "test" and if it's >460
            False - if file contains test or is <460
'''
def check_file(fileName):
    ret = False
    if ('test' not in fileName.lower()) and (os.path.getsize(fileName) > 460):
        ret = True
    return ret

'''
    adds the path to the list of unwanted paths
    
    @Params:
        unwanted - a list of unwanted paths (user selects in GUI)
        path - a path to be added to the list of unwanted
'''
def add_unwanted_path(unwanted, path):
    unwanted.append(path)
    
'''
    checks if the file is in the list of unwanted
    
    @Params:
        filename - the name of the file to be checked
        unwanted - list of directories and files wanted to be skipped
    @Returns:
        ret - A boolean
            True - if file is not in unwanted
            False - if file is in unwanted
'''
def check_file_name(filename, unwanted):
    ret = True
    # loops through unwanted paths and skips over file in dir in apart of file name
    for dir in unwanted:
        if dir in filename:
            ret = False
    
    return ret

'''
    returns a list of all valid csv files
    
    @Params:
        myPath - the path to the directory
        unwanted - a list from the user of all unwanted files or directories
    @Returns:
        
'''
def get_files(myPath, unwanted, signal):
    progressCap = 30
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

    for x in range(0, progressCap):
        time.sleep(0.01)
        signal.progress2.emit(1)
                 
    return files

'''
    individually reads the csv files, turns them into pandas dataframes and
    returns them in a list
    @Params:
        files - a list of all files to be read
    @Returns:
        readFiles - a list of all newly created pandas dataframes
'''
def get_data_frames(files, signal):
    progressCap = 25
    increment = progressCap//len(files)
    remainder = progressCap%len(files)
    readFiles = []
   
    for file in files:
        readFiles.append(pd.read_csv(file))
        signal.progress2.emit(increment)
    signal.progress2.emit(remainder)

    return readFiles

'''
    Seperate looping function to return removed items as it iterates.
    
    @Params:
        frames - a list of dataframes
    @Returns:
        the removed dataframe
'''
def recursive_concat(frames):
    for frame in frames:
        frames.remove(frame)
        return(frame)
        
'''
    concatenates all dataframes into one single dataframe to be used
    
    @Params:
        frames - a list of all dataframes
    @Returns:
        finalFrame - one dataframe made up of all the dataframes in frames
'''
def concat_data_frames(frames, files, signal):
    size = len(frames)
    progressCap = 45
    
    #Return the single frame on one file selected.
    if size == 1:
        signal.progress2.emit(45)
        return frames[0]
    
    if size > 5:
        increment = progressCap//len(frames)
        remainder = progressCap%(len(frames))
        firstThird = round(size/3)
        secondThird = round(2*size/3)
        frames1 = frames[:firstThird]
        frames2 = frames[firstThird:secondThird]
        frames3 = frames[secondThird:-1]
        files1 = files[:firstThird]
        files2 = files[firstThird:secondThird]
        files3 = files[secondThird:] 
        concatFrames1 = pd.concat(frames1, sort = False, keys = files1)
    
    #For each deleted frame, concat to the new frame.
        for delFrame in frames1:
            recursive_concat(frames1)
        signal.progress2.emit(increment)
        concatFrames2 = pd.concat(frames2, sort = False, keys = files2)
        for delFrame in frames2:
            recursive_concat(frames2)
        signal.progress2.emit(increment)
        concatFrames3 = pd.concat(frames3, sort = False, keys = files3)
        for delFrame in frames3:
            recursive_concat(frames3)
        signal.progress2.emit(increment)
        allFrames = [concatFrames1, concatFrames2, concatFrames3]
        finalFrame = pd.concat(allFrames, sort = False)
        signal.progress2.emit(remainder)
    else:
        finalFrame = pd.concat(frames, sort = False, keys = files)
        for delFrame in frames:
            recursive_concat(frames)
            signal.progress2.emit(increment)
        signal.progress2.emit(remainder)
    return finalFrame

'''
    Accepts a path and a list of directories and files that are unwanted and
    calls get_files, get_data_frames and concat_data_frames to read the files,
    turn them into pandas data frames and then concat all the frames into one
    data frame
    
    @Params:
        path - a path to the directory with csv files
        unwanted - a list of directories or files that the user does NOT want
                    to be read
    @Returns:
        ret - the combined data frame of all the files
                (if directory is empty, returns empty data frame)
'''
def execute(path, unwanted, signal):
    ret = pd.DataFrame()
    files = get_files(path, unwanted, signal) 
    if(len(files) == 0):
        print(SYSTEM.noFilesFound)   
    else:
        readFiles = get_data_frames(files, signal)
        ret = concat_data_frames(readFiles, files, signal)
    return ret
