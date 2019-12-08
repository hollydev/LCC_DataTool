import pandas as pd 
import glob as glob
#setting for the displayed output
pd.set_option('display.max_columns', None)
pd.set_option('display.width', None)
pd.set_option('display.max_colwidth', -1)

#using glob to find all files in the subdirectory 'GBsample' that have the .csv extension
for file in glob.glob("./GBsample/*.csv"):
       
                                     #targeted columns
    df = pd.read_csv(file, usecols = list(range(0,9)), sep = ',')
    print(file)
    print(df)