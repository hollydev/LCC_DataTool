# The fuction takes a pulls all the non-empty and non-duplicate files out.
#   empty files: files with a size of 460 Bytes.
#   duplicate files: files with 'Test' in the name.

import os

# returns True if the file is not a duplicate or empty.
def checkFile(fileName):
    ret = False
    if ('test' not in fileName.lower()) and (os.path.getsize(fileName) > 460):
        ret = True
    
    return ret

# returns a list of all good files.
def getFiles(myPath):

    files = []

    for root, dirs, f in os.walk(myPath):
        for file in f:
            if '.csv' in file:
                fileName = os.path.join(root, file)
                
                if checkFile(fileName) == True:
                    files.append(fileName)
    return files




        