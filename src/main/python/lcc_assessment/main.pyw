from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView, QVBoxLayout, QFileDialog, QMainWindow
from PyQt5.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot
from lcc_assessment.gui import Ui_MainWindow
import re
import sys, os
import lcc_assessment.getFiles as getFiles
import lcc_assessment.system as system
import lcc_assessment.output as output
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from messages.system import SYSTEM


class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Modify any starting UI parameters
        self.start_up()
        
        #Set up any event listeners
        self.ui.treeWidget.expanded.connect(self.resize_treeWidget)
        
        #Code for handling widgets on "column configuration" window
        self.ui.listWidget_3.itemClicked.connect(self.item_3_click)
        self.ui.listWidget_4.itemClicked.connect(self.item_4_click)
        self.ui.pushButton_3.clicked.connect(self.all_columns_button)
        self.ui.pushButton_4.clicked.connect(self.validate_button)

        self.ui.pushButton.clicked.connect(self.start_up) #Reset the program flow when data is re-selected.
        self.ui.pushButton.clicked.connect(self.get_path) #Browse button
        self.ui.buttonBox.clicked.connect(self.apply_discard_buttons) #Apply/discard button
        
        #Configuring the "output" window buttons
        self.ui.pushButton_2.clicked.connect(self.db_connect)
        self.ui.DBLoadButton.clicked.connect(self.db_load)
        
        self.ui.outputBrowseButton.clicked.connect(self.get_out_path)

        
    def fill_columns_list(self): 
        """
            Gets all the column names from dataframe to add to listWidget_3
        """
            
        for i, columnName in enumerate(self.df.columns):
            if columnName is not None:
                self.ui.listWidget_3.addItem(columnName)
                
    def item_3_click(self, item):
        """
            Adds [item] from listWidget_3 to listWidget_4
            (**selecting the column name in the GUI)
            @Params:
                item - the column name to be added to the list
        """
        index = self.ui.listWidget_3.row(item)
        self.ui.listWidget_4.addItem(self.ui.listWidget_3.takeItem(index))

    def item_4_click(self, item):
        """
            Adds [item] from listWidget_4 to listWidget_3 
            (**unselecting the column name in the GUI)
            @Params:
                item - the column name to be deselected from the list and added
                back to original column
        """
        index = self.ui.listWidget_4.row(item)
        self.ui.listWidget_3.addItem(self.ui.listWidget_4.takeItem(index))
       
    def all_columns_button(self):
        """
            Adds all columns to list
        """
        x  = self.ui.listWidget_3.count()
        while(x >= 0):
            oneItem = self.ui.listWidget_3.takeItem(x)
            self.ui.listWidget_4.addItem(oneItem)
            x -= 1
        
    def start_up(self):
        """
            Runs on startup to clear all widgets and labels to generate a clean
            'new' GUI
        """
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.buttonBox.setEnabled(False)
        
        self.ui.buttonBox.setEnabled(False)
        self.ui.lineEdit.clear()
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        self.ui.listWidget_3.clear()
        self.ui.listWidget_4.clear()
        self.ui.treeWidget.clear()
        self.ui.label.setText("Instructors:")
        self.ui.label_2.setText("Terms:")
        self.ui.label_3.setText("Files Found:")
        self.ui.label_4.setText("Items Selected:")
        
        self.ui.treeWidget.resizeColumnToContents(0)
        
        self.df = None
        self.output = None
        self.outPath = None
        self.applyFlag = 0
        
        self.ui.progressBar.setValue(0)
        self.ui.progressBar_2.setValue(0)
        
        self.ui.pushButton_5.setText("Next")
        try:
            self.ui.pushButton_5.clicked.disconnect()
        except TypeError:
            pass

    #functions for updating the progress bars
    def validatorProgress(self, n):
        self.currentValue1 += n
        self.ui.progressBar.setValue(self.currentValue1)
        
    #function for updating progress bar for getFiles
    def getFilesProgress(self, n):
        self.currentValue2 += n
        self.ui.progressBar_2.setValue(self.currentValue2)
        
    #function for updating progress bar for cleaners
    def cleanerProgress(self, n):
        self.currentValue3 += n
        self.ui.progressBar_3.setValue(self.currentValue3)

        if(self.currentValue3 == 100):
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
            self.ui.progressBar_3.setValue(0)
            self.ui.label_8.setText("")


    #catches the signal from BCselector and getFiles, assigns the returned frame to self.df
    def setFrame(self, dataframe):
        self.df = dataframe

    #Runs when validate button is clinked in GUI
    def validate_button(self):
        self.threadpool = QThreadPool()
        self.currentValue1 = 0 #holds current value of progress bar for validator thread
        theColumns = []
        x = self.ui.listWidget_4.count()-1
        while(x >= 0):
            theColumns.append(self.ui.listWidget_4.item(x).text())
            x -= 1                         

        worker = Worker(system.main, theColumns, self.df)
        worker.signals.returnVal.connect(self.displayFeedBack)
        worker.signals.progress2.connect(self.validatorProgress)
        worker.signals.dataframe.connect(self.setFrame)
        self.threadpool.start(worker)
              
        
    def count_checked_treeWidget(self):
        #Get the count of checked items
        treeItemIterator = QtWidgets.QTreeWidgetItemIterator(self.ui.treeWidget, QtWidgets.QTreeWidgetItemIterator.Checked)
        self.applyFlag = 0
        checkedItemCount = 0
        while treeItemIterator.value():
            checkedItemCount += 1
            treeItemIterator += 1
        
        #Update the label
        self.ui.label_4.setText("Items Selected: {}".format(checkedItemCount))
    
    
    def resize_treeWidget(self):
        #Set the column width
        self.ui.treeWidget.resizeColumnToContents(0)
    
    def get_path(self):
        '''
         Runs when 'Browse' button is clicked and gets the directory path and calls build_tree
         to build the tree in the GUI
         - Sets self.path to specified directory path
         - Prints the path in self.ui.lineEdit (path line in GUI)
         - Calls build_tree
         - Prints number of files found and selected in GUI
         @Params:
             self
         @Returns:
             self.path - user specified directory path to all the files
        '''
        self.tree_dict = {}
        self.ui.item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
        try:
            _translate = QtCore.QCoreApplication.translate
        
            self.path = QFileDialog.getExistingDirectory(None, 'Select Directory')
            self.ui.lineEdit.setText(_translate("MainWindow", self.path))
            self.countFiles = 0
            self.numFiles = self.build_tree()
            self.ui.label_3.setText(_translate("MainWindow",('Files Found: '+str(self.countFiles))))
            self.ui.label_4.setText("Items Selected: {}".format(str(self.countFiles)))  
                        
            self.ui.buttonBox.setEnabled(True)
            
        except FileNotFoundError:
            print(SYSTEM.noFilesFound)
            
        return self.path
    
    def check_state(self):
        '''
        Ckecks if a subfolder or file is unchecked in the GUI
        If it is unchecked, the path is added to self.unwanted and will be skipped
        @Params:
            self
        @Returns:
            
        '''
        self.unwanted = []
        for path in self.tree_dict:
            if self.tree_dict[path].checkState(0) == 0:
                getFiles.add_unwanted_path(self.unwanted, path)

    def apply_discard_buttons(self, button): 
        '''
        Called when apply or discard button is clicked
        Apply - builds the dataframe by calling getFiles.execute, and prints the
                instructors and term codes found
        Discard - Resets the GUI by calling start_up
        @Params:
            self
            button - states if apply or discard is clicked
        @Returns:
            
        '''
        try:
            self.threadpool = QThreadPool()
            self.currentValue2 = 0 #current value for progress of apply_button thread
            sb = self.ui.buttonBox.standardButton(button)
            if sb == QtWidgets.QDialogButtonBox.Apply: #APPLY CLICKED
                if self.applyFlag == 0: #If 0 apply has not been clicked already
                    self.check_state()
                    worker3 = Worker3(getFiles.execute, self.path, self.unwanted)
                    worker3.signals.dataframe.connect(self.setFrame)
                    worker3.signals.finished1.connect(self.print_instructors)
                    worker3.signals.finished2.connect(self.print_termcodes)
                    worker3.signals.progress2.connect(self.getFilesProgress)
                    worker3.signals.finished2.connect(self.fill_columns_list)
                    self.threadpool.start(worker3)
                    self.applyFlag = 1 # Set to 1 - Apply cannot be clicked until GUI is reset
            elif sb == QtWidgets.QDialogButtonBox.Discard: #DISCARD CLICKED
                #Reset flow
                self.start_up()
        except AttributeError:
            return
            
    def print_instructors(self):
        '''
        Gets the instructors found in the dataframe from system.get_instructors
        and creates listWidgetItems and prints them in GUI.
        @Params:
            self
        @Returns:
            
        '''
        _translate = QtCore.QCoreApplication.translate
        index = 0
        
        self.ui.listWidget.clear()
        instructorList = system.get_instructors(self.df) # Gets a list of instructors sorted by last name
        
        if(instructorList == None):
            instructorList = []
        # For an instructor in the list, build a listWidgetItem print it in listWidget
        for instructor in instructorList:
            item = QtWidgets.QListWidgetItem()
            self.ui.listWidget.addItem(item)
            item = self.ui.listWidget.item(index)
            item.setText(_translate("MainWindow", str(instructor)))
            index = index + 1
        #prints the number of instructors found
        self.ui.label.setText("Instructors ({})".format(len(instructorList)))
        
    def print_termcodes(self):
        '''
        Gets the term codes found in the dataframe from system.get_termcodes
        and creates listWidgetItems and prints them in GUI.
        @Params:
            self
        @Returns:
                   
        '''
        _translate = QtCore.QCoreApplication.translate
        index = 0
        
        self.ui.listWidget_2.clear()
        termList = system.get_termcodes(self.df) # Gets a list of term codes
        
        if(termList == None):
            termList = []
        # For a term in the list, build a listWidgetItem print it in listWidget_2    
        for term in termList:
            item = QtWidgets.QListWidgetItem()
            self.ui.listWidget_2.addItem(item)
            item = self.ui.listWidget_2.item(index)
            item.setText(_translate("MainWindow", str(term)))
            index = index + 1
        self.ui.tabWidget.setTabEnabled(1, True)
        #prints the number of term codes found
        self.ui.label_2.setText("Terms ({})".format(len(termList)))
            
    def build_tree(self):
        '''
        Creates the first 'node' of the tree but getting the basename of the path
        the user selected, sets the checkState to checked, and then calls recurr
        to recursively traverse the directory and build the tree
        @Params:
            self
        @Returns:
            
        '''
        _translate = QtCore.QCoreApplication.translate
        self.ui.item.setText(0, _translate("MainWindow", os.path.basename(self.path)))
        self.ui.item.setCheckState(0, QtCore.Qt.Checked)
        self.ui.item.setFlags(self.ui.item.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
    
        self.tree_dict[self.path] = self.ui.item
        self.recurr(self.path, self.ui.item)
        
        #Set the event listener for further checkbox changes.
        self.ui.treeWidget.itemClicked.connect(self.count_checked_treeWidget)
       

    def recurr(self,path, parent):
        '''
        Recursively walks through the directory
            - if it is a csv file, it will create a node under its parent and 
                adds the file to self.tree_dict
            - if it is not a file(a directory), it will create a node under its parent
                and then call recurr to traverse into the directory
        *All nodes are set to checked when created
        @Params:
            self
            path - the path of the node to be investigated(file or directory?)
            parent - the node above the current path
        @Returns:
            
        '''
        _translate = QtCore.QCoreApplication.translate
        for folder in os.listdir(path):
            if os.path.isfile(os.path.join(path, folder)):
                if '.csv' in folder:
                    if getFiles.check_file(os.path.join(path, folder)):
                        child = QtWidgets.QTreeWidgetItem(parent)
                        child.setText(0, _translate("MainWindow", folder))
                        child.setCheckState(0, QtCore.Qt.Checked)
                        child.setFlags(child.flags() | QtCore.Qt.ItemIsUserCheckable)               
                        self.countFiles = self.countFiles + 1
                        self.tree_dict[os.path.join(path, folder)] = child
                    continue
            else:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setText(0, _translate("MainWindow", folder))
                child.setCheckState(0, QtCore.Qt.Checked)
                child.setFlags(child.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
    
                self.tree_dict[os.path.join(path, folder)] = child
                p = os.path.join(path, folder)
                self.recurr(p, child)


    def displayFeedBack(self, theInfo):
        """
            Displays feedback in GUI
            @Params:
                theInfo - info for the given column
        """

        #Initialize variables
        self.x = 0
        header = list()
        self.cleanersList = system.get_cleaners_list()
       
        header.append(str(theInfo[0]).split('>')[1])
        
        self.ui.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        
        # # Construct the table using the values
        application.resize(800, 800)
        self.ui.tableWidget.setVerticalHeaderLabels(['Validator:', 'Info:'])
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(theInfo[0]).split('>')[2]))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(theInfo[0]).split('>')[3]))
        
        
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        
        
        # Enable this tab
        
        self.ui.tabWidget.setTabEnabled(2, True)
        # Force the view to the feedback screen
        self.ui.tabWidget.setCurrentIndex(2)
        
        # connect the buttons to their functions
        self.ui.pushButton_5.clicked.connect(lambda: self.getNextColumn(self.x, theInfo))#next button
        self.ui.pushButton_7.clicked.connect(lambda: self.seeExceptions(theInfo[self.x], 0))#see warnings button
        self.ui.pushButton_6.clicked.connect(lambda: self.seeExceptions(theInfo[self.x], 1))#see errors button


    def seeExceptions(self, columnInfo, buttonId):

        self.ui.listWidget_5.clear()
        i = 0
        if(buttonId == 0):
            for element in columnInfo[1].warn:
                self.ui.listWidget_5.insertItem(i, element)
                i += 1
        else:
            for element in columnInfo[1].err:
                self.ui.listWidget_5.insertItem(i, element)
                i += 1


    def cleanColumn(self, columnName):
        self.threadpool = QThreadPool()
        columnName = re.findall(r'\[([^][]*[^][]*)]', columnName)
        self.currentValue3 = 0
        wholeColumn = self.df.loc[ :,columnName]
        worker2 = Worker2(system.clean, wholeColumn)
        worker2.signals.cleanedColumn.connect(self.assign_cleaned)
        worker2.signals.progress3.connect(self.cleanerProgress)
        self.threadpool.start(worker2)
        
        
        
    
    def assign_cleaned(self, cleanedColumn):
        if(cleanedColumn is not None):
            self.df[cleanedColumn.name] = cleanedColumn
        
        #Enable buttons after cleaner finishes.
        self.ui.pushButton_5.setEnabled(True)
        self.ui.pushButton_6.setEnabled(True)
        self.ui.pushButton_7.setEnabled(True)


    def getNextColumn(self, x, theInfo):
        
        self.ui.listWidget_5.clear() #clear the listWidget_5 box before moving to next column

        if(self.x < len(theInfo)-1):           
            
            if(self.ui.checkBox.isChecked() == True):
                #Disable the buttons while the cleaner runs
                self.ui.pushButton_5.setEnabled(False)
                self.ui.pushButton_6.setEnabled(False)
                self.ui.pushButton_7.setEnabled(False)

                self.cleanColumn(str(theInfo[self.x]).split('>')[1])
                self.ui.checkBox.toggle()
            else:
                self.ui.label_8.setText("")
                
            
            self.x += 1
            header = list()
            header.append(str(theInfo[self.x]).split('>')[1])
           
            #Construct the table using the values
            self.ui.tableWidget.setHorizontalHeaderLabels(header)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(theInfo[self.x]).split('>')[2]))
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(theInfo[self.x]).split('>')[3]))
            
        else:
            self.ui.pushButton_5.setText("Continue")
            self.ui.pushButton_5.clicked.disconnect()
            self.ui.pushButton_5.clicked.connect(self.setup_output)
        
            
        #Show which cleaners are applied to the column
        try:
            #Get a list of cleaners for this column.
            columnName = re.findall(r'\[([^][]*[^][]*)]', str(theInfo[self.x]).split('>')[1])[0]
            cleanerList = ', '.join(self.cleanersList[columnName])
            self.ui.label_8.setText("Cleaners Applied: {}".format(cleanerList))
        except KeyError:
            self.ui.label_8.setText("No Cleaners Available")
            self.ui.pushButton_5.setEnabled(True)
            self.ui.pushButton_6.setEnabled(True)
            self.ui.pushButton_7.setEnabled(True)
        self.ui.label_8.adjustSize()     
    
        
    def setup_output(self):
        #Enable the tab
        self.ui.tabWidget.setTabEnabled(3, True)
        self.ui.tabWidget.setCurrentIndex(3) # Force the view to the output screen
        application.resize(800, 600)
        #Get a file writer object
        self.output = output.FILE_WRITER()
        
        #Perform final processing of data frame for output.
        self.df = system.cleaned_data(self.df)
                
        #Get FBS connection resource location
        ini = appctxt.get_resource('connection.ini')
        ini = open(ini)
    
        #Read DB configurations
        configs = self.output.get_db_config(ini)
        
        if(configs != None):
            #Display the found configurations
            self.ui.usernameLabel.setText("Username: {}".format(configs["user"]))
            self.ui.TNSLabel.setText("TNS Name: {}".format(configs["tns"]))
            #Fallback configuration
            self.ui.serviceLabel.setText("Service: {}".format(configs["service"]))
            self.ui.hostnameLabel.setText("Hostname: {}".format(configs["hostname"]))
            self.ui.portLabel.setText("Port: {}".format(configs["port"]))
            
        
        #DB Status Message
        self.ui.DBConnectionStatusLabel.setText("Status: {}".format(self.output.dbStatus))
        
        #While validation and cleaning are coupled, get final df here
        # self.df = system.cleaned_data(self.df)    
        
    def db_connect(self):
        #Get FBS connection resource location
        ini = appctxt.get_resource('connection.ini')
        ini = open(ini)
    
        #Read DB configurations
        configs = self.output.get_db_config(ini)
        
        if(configs != None):
            self.db_connection = self.output.connect(configs)
        
        #DB Status Message
        self.ui.DBConnectionStatusLabel.setText("Status: {}".format(self.output.dbStatus))
    
    def db_load(self):
        #Check connection status
        if(self.output.dbStatus == "Connected!"):
            #Do the DB Load
            pass
            
    def get_out_path(self):  
        #Gets the location of where the user would like to save the data
        try:
            _translate = QtCore.QCoreApplication.translate
            
            self.outPath = QFileDialog.getSaveFileName(self, self.output.outName, '', 'CSV(*.csv)')[0] #Save only the output path
            self.ui.outputBrowseBox.setText(_translate("MainWindow", self.outPath))
            
            self.output.set_path(self.outPath)
            self.output.write_csv(self.df)
        
        except FileNotFoundError:
            print('FileNotFound')
        
class WorkerSignals(QObject):
    
    returnVal = pyqtSignal(object) #Signal to return the information from the validators run
    cleanedColumn = pyqtSignal(object) #Signal to return the cleaned column from the cleaner function

    progress1 = pyqtSignal(int)#signal for updating apply button progress bar
    progress2 = pyqtSignal(int)#signal for updating validator progress bar
    progress3 = pyqtSignal(int)#signal for updating cleaner progress bar

    dataframe = pyqtSignal(object)

    finished1 = pyqtSignal()#for print_instructors()
    finished2 = pyqtSignal()#for print_termcodes()


#thread for validating columns
class Worker(QRunnable):

    def __init__(self, fn, selectedColumns, df):
        super(Worker, self).__init__()
        self.fn = fn
        self.theColumns = selectedColumns
        self.signals = WorkerSignals()
        self.theData = df

    @pyqtSlot()
    def run(self):

        theInfo = self.fn(self.theColumns, self.theData, self.signals)
        
        #send the info returned from validators back to the GUI from worker thread
        self.signals.returnVal.emit(theInfo)
        
#thread for cleaning columns
class Worker2(QRunnable):
    def __init__(self, fn, columntoclean):
        super(Worker2, self).__init__()
        self.fn = fn
        self.columntoclean = columntoclean
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):

        cleanedColumn = self.fn(self.columntoclean, self.signals)
        if(cleanedColumn is not None):
            cleanedColumn.name = cleanedColumn.name + "_cleaned"
            self.signals.cleanedColumn.emit(cleanedColumn)
        else:
            print("No default cleaner set")

class Worker3(QRunnable):
    def __init__(self, fn, path, unwanted):
        super(Worker3, self).__init__()
        self.fn = fn
        self.path = path
        self.unwanted = unwanted
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):

        # self.signals.dataframe.emit(self.fn(self.path, self.unwanted))
        theFiles = self.fn(self.path, self.unwanted, self.signals)
        self.signals.dataframe.emit(theFiles)
        self.signals.finished1.emit()
        self.signals.finished2.emit()

        return

    
if __name__ == "__main__":       
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #app = QtWidgets.QApplication([])
    application = mywindow()
    application.resize(800, 600)
    application.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)        
