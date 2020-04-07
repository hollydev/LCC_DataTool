"""
    Filename: output.py
    Programmer: Holly Locke
    Date Created: 01/13/2020
    Last Update: File Created

    Description: This script provides functionality for saving a data frame to a memory object.
    Available memory types include: CSV, (Excel?), Oracle SQL

"""

import pandas as pd
import numpy as np
import csv
import pickle
import os
import cx_Oracle

from messages.system import SYSTEM, LOG

# class InvalidPathError(Error):
#     def __init__(self, expression, message):
#         self.expression = expression
#         self.messages = message

class FILE_WRITER():
    messages = []
    log = []
    dbStatus = "Disconnected"

    def __init__(self, outPath=None, outName=None):
        """ Writer init function. Handles all file writing capabilites. Performs path validation
        on each instance. 

        @Params:
            self  - self object allows access to set path and outName.
            outPath - A path indicating the output location.
            outName (optional) - A string indicating the name of the output file.
            
        @Raises:
            FileNotFoundError - Indicates the given path does not point to a valid file or directory.
        """
        if outName == None:
            self.outName = "combined_gradebook"
        else:
            self.outName = outName

        #Validate the path on initialization.
        if outPath == None:
            #Get the current path as output path
            self.outPath = os.getcwd()
        elif self.validate_path(outPath):
            #Check to make sure that the path includes a '/' or '\'
            if(outPath.endswith("\\") == False or outPath.endswith("/") == False):
                outPath = outPath + "\\" #Assign the windows slash to paths that need it.

            #Use the defined path given a passing validation.
            self.outPath = outPath


        else:
            raise FileNotFoundError(SYSTEM.FileNotFoundException.format(outPath)) #{} pathValue
        
        

    def validate_path(cls, checkPath):
        """ Check if the given path is valid. Checks emptp paths and path.exists() errors.

        @Params:
            cls - self object allows access to set path and outName.
            checkPath - A string indicating the path to check for validity.
            

        @Returns:
            BOOLEAN - Indicates whether new path is valid.
            
        @Raises:
            TypeError - Indicates the given path variable is not a string.
        """
        #Check type
        if(not isinstance(checkPath, str)):
            raise TypeError(SYSTEM.TypeException.format(type(str), type(checkPath))) #{} Expected, {} Got
        
        #Validate empty path, trim extra spaces and see if the path minimized to empty.
        if(checkPath.strip() == ''):
            cls.messages.append(SYSTEM.emptyPath)
            cls.log.append(LOG.emptyPath)
            return False

        #Check if the path exists
        if(not os.path.exists(checkPath)):
            try:
                os.stat(checkPath)
            except:
                cls.log.append(LOG.notPath_stat)
                return False
        
            cls.messages.append(SYSTEM.notPath)
            cls.log.append(LOG.notPath)
            return False

        return True
    
    def get_path(cls):
        """ Get a path to initialize the writer or return the current path"""
        if cls.outPath == None:
            return input("No Path provided. Enter a path: ")
        else:
            return cls.outPath

    def set_path(cls, newPath):
        """ Setter method ensuring that new path is valid.

        @Params:
            cls - self object allows access to set path and outName.
            newPath - A string indicating the new path given

        @Returns:
            BOOLEAN - Indicates whether new path was set.
        """
        if(not isinstance(newPath, str)):
            raise TypeError(SYSTEM.TypeException.format(type(str), type(newPath)))
        
        if(cls.outPath == newPath):
            cls.log.append(SYSTEM.newPathSame.format(newPath))
            return True

        if(cls.validate_path(newPath)):
            #Check to make sure that the path includes a '/' or '\'
            if(newPath.endswith("\\") == False or newPath.endswith("\/") == False):
                #Check if the path has a file name associated
                if(newPath.endswith(".csv")):
                    splitPath = newPath.rsplit("/", 1) #Split on the last slash
                    cls.outPath = splitPath[0] + "\\" #Assign the windows slash
                    cls.outName = splitPath[1]
                else:
                    cls.outPath = newPath + "\\" #Assign the windows slash to paths that need it.
            return True
        else:        
            #Check if the path has a file name associated
            if(newPath.endswith(".csv")):
                splitPath = newPath.rsplit("/", 1) #Split on the last slash
                cls.outPath = splitPath[0] + "\\" #Assign the windows slash
                cls.outName = splitPath[1]
            return False

        print("uncaught case")
        return False

    
    def check_overwrite(cls):
        """ Check if the path points to an existing file. If so verify if okay to overwrite.

        @Params:
            cls - self object allows access to set path and outName.

        @Returns:
            BOOLEAN - Indicates whether okay to overwrite. True = okay.
        """
        
        #Get the path and name lengths
        nameLength = len(cls.outName)
        pathLength = len(cls.outPath)

        #Get the start and end index. 4 indicates a file type .XXX
        iStart = pathLength - nameLength - 4
        iEnd = pathLength - 4

        #Check if path points to a file.
        if(os.outPath.isfile(cls.outPath)):
            """TODO: When GUI change overwrite handler to Windows"""
            #Check if the file has the same name, check overwrite ok.
            if(cls.outPath.endswith(cls.outName, iStart, iEnd)):
                overwriteOkay = input(SYSTEM.overwrite.format(cls.outName).lower())
                if (overwriteOkay == "yes" or\
                    overwriteOkay == "y"):
                    return True
                elif (overwriteOkay == "no" or\
                      overwriteOkay == "n"):
                    return False
                else:
                    return False

            cls.messages.append(SYSTEM.existingFile)
        else:
            return True


    def available_types(cls, file):
        """ Provide a list of file types which are available to save.
            TODO: Provide a list based on the filetype of the parameter.

            @Params:
                cls - self object allows access to set path and outName.
                file - The file to be saved. For file type checking.

            @Returns:
                types - A list of file types which are available for the file.
        """

        #If the file is a data frame
        if(isinstance(file, pd.DataFrame)):
            return(["CSV, XLSX, Pickle"])
        else:
            return(["Pickle"])

    
    def write_csv(cls, file):
        """ Saving of csv files for files produced by
        the application.

        @Params:
            cls - self object allows access to set path and outName.
            file - The file to be saved.
            outPath - The path where the file should be saved.
        
        @Returns:
            Saved - Boolean - Indicates whether the file was saved successfully.
        """

        #Save Pandas DF using Pandas
        if(isinstance(file, pd.DataFrame)):
            keptColumns = ["username",
                           "firstname",
                           "lastname",
                           "courseofferingname",
                           "coursesectioncode",
                           "gradeitemcategoryname",
                           "gradeitemname",
                           "pointsnumerator",
                           "pointsdenominator",
                           "gradecomments"]
                           
            cleanFile = file[keptColumns]
            
            #Check if the filename has an extension
            if(cls.outName.endswith(".csv")):
                cleanFile.to_csv(cls.outPath + cls.outName, index=False)
            else:
                cleanFile.to_csv(cls.outPath + cls.outName + ".csv", index=False)
        
        #Save dict object using CSV
        elif (isinstance(file, dict)):
            #Use the csv package to handle writing dicts to files.
            writer = csv.Writer(cls.outPath)

            for row in file:
                writer.WriteRow(line)

    def write_pickle(cls, file):
        """ Saving of pickle objects for later use by the python program.

        @Params:
            file - The file to be pickled.
        """

        #Save the pickle object, a serialized representation.
        if(isinstance(file, pd.DataFrame)):
            cls.fileName = cls.fileName + "_pandasDataFrame"
        elif (isinstance(file, pd.Series)):
            cls.fileName = cls.fileName + "_pandasSeries"
        
        if(check_overwrite(cls.outPath) == True):
            try:
                outFile = open(cls.outPath + cls.fileName, 'rw')
                pickle.dump(file, outFile)
                outFile.close()

            except OSError as e:
                print("Unable to open file, please try again.", e)
                
    ######################################################
    ############## DB Connection Code ####################
    ######################################################

    def get_db_config(cls, config_file):
        """ Read the configuration file to get the database connection details. This allows the GUI to hide necessary information.
        
        @Returns:
            configs - A map of with named configurations. Keys are the DB info, values are the specified configs. Returns None on invalid config.
        """

        user = ""
        password = ""
        tnsName = ""
        service = ""
        hostname = ""
        port = None

        if(config_file == None):
            cls.dbStatus = "Connection file not found!"
            return None
        
        lines = config_file.readlines()
        for line in lines:
            if('#' not in line and len(line) > 1):
                cleanLine = line.replace('\n','')
                splitLine = cleanLine.split('=')
                
                id = splitLine[0].lower()
                value = splitLine[1]
                
                if(id == 'username'):
                    user = value

                if(id == 'password'):
                    password = value
                    
                if(id == 'connection'):
                    tnsName = value
                    
                if(id == 'service'):
                    service = value

                if(id == 'hostname'):
                    hostname = value
                    
                if(id == 'port'):
                    port = value
            
        configs = {"user": user
             , "password": password
             , "tns": tnsName
             , "service": service
             , "hostname":hostname
             , "port": port}
             
        return configs
        
    def connect(cls, configs):
        try:
            connection = cx_Oracle.connect(configs["user"], configs["password"], configs["tns"])
            cls.dbStatus  = "Connected!"
            
            return connection

        except cx_Oracle.DatabaseError:
            print("TNS connection failed. Using fallback configuration.")
            
            try:
                connection = cx_Oracle.connect(configs["user"], configs["password"], configs["hostname"] + ':' + configs["port"] + '/' + configs["service"])
                cls.dbStatus  = "Connected!"
                return connection
            except cx_Oracle.DatabaseError:
                cls.dbStatus = "Unable to Connect"
                return None
