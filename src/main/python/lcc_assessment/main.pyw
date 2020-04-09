from PyQt5 import QtWidgets, QtCore
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView, QVBoxLayout, QFileDialog, QMainWindow
from PyQt5.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot
from lcc_assessment.gui import Ui_MainWindow
from lcc_assessment.system import main, cleaned_data
import sys, os
import lcc_assessment.getFiles as getFiles
import lcc_assessment.system as system
import lcc_assessment.output as output
from fbs_runtime.application_context.PyQt5 import ApplicationContext
from messages.system import SYSTEM

import sys

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
        self.ui.pushButton_4.clicked.connect(self.setup_output)

        self.ui.pushButton.clicked.connect(self.start_up) #Reset the program flow when data is re-selected.
        self.ui.pushButton.clicked.connect(self.get_path) #Browse button
        self.ui.buttonBox.clicked.connect(self.apply_discard_buttons) #Apply/discard button
        
        #Configuring the "output" window buttons
        self.ui.pushButton_2.clicked.connect(self.db_connect)
        self.ui.DBLoadButton.clicked.connect(self.db_load)
        
        self.ui.outputBrowseButton.clicked.connect(self.get_out_path)
        
    def item_3_click(self, item):
        index = self.ui.listWidget_3.row(item)
        self.ui.listWidget_4.addItem(self.ui.listWidget_3.takeItem(index))

    def item_4_click(self, item):
        index = self.ui.listWidget_4.row(item)
        self.ui.listWidget_3.addItem(self.ui.listWidget_4.takeItem(index))
       
    def all_columns_button(self):
        x  = self.ui.listWidget_3.count()
        while(x >= 0):
            oneItem = self.ui.listWidget_3.takeItem(x)
            self.ui.listWidget_4.addItem(oneItem)
            x -= 1
        
    def start_up(self):
        self.ui.tabWidget.setTabEnabled(1, False)
        self.ui.tabWidget.setTabEnabled(2, False)
        self.ui.tabWidget.setTabEnabled(3, False)
        self.ui.buttonBox.setEnabled(False)
        
        self.ui.buttonBox.setEnabled(False)
        self.ui.lineEdit.clear()
        self.ui.listWidget.clear()
        self.ui.listWidget_2.clear()
        self.ui.treeWidget.clear()
        self.ui.label.setText("Instructors:")
        self.ui.label_2.setText("Terms:")
        self.ui.label_3.setText("Files Found:")
        self.ui.label_4.setText("Items Selected:")
        
        self.ui.treeWidget.resizeColumnToContents(0)
        
        self.df = None
        self.output = None
        self.outPath = None
    
    def validate_button(self):
        self.threadpool = QThreadPool()
        theColumns = []
        x = self.ui.listWidget_4.count()-1
        while(x >= 0):
            theColumns.append(self.ui.listWidget_4.item(x).text())
            x -= 1                         

        worker = Worker(main, theColumns, self.df)
        worker.signals.returnVal.connect(self.displayFeedBack)
        self.threadpool.start(worker)
              
        
    def count_checked_treeWidget(self):
        #Get the count of checked items
        treeItemIterator = QtWidgets.QTreeWidgetItemIterator(self.ui.treeWidget, QtWidgets.QTreeWidgetItemIterator.Checked)
        
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
        self.tree_dict = {}
        self.ui.item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
        try:
            _translate = QtCore.QCoreApplication.translate
        
            self.path = QFileDialog.getExistingDirectory(None, 'Open File')
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
        self.unwanted = []
        for path in self.tree_dict:
            if self.tree_dict[path].checkState(0) == 0:
                getFiles.add_unwanted_path(self.unwanted, path)

    def apply_discard_buttons(self, button): 
        try:
            sb = self.ui.buttonBox.standardButton(button)
            _translate = QtCore.QCoreApplication.translate
            if sb == QtWidgets.QDialogButtonBox.Apply: #APPLY CLICKED
                self.check_state()
                self.df = getFiles.execute(self.path, self.unwanted)
            
                self.print_instructors()
                self.print_termcodes()    
            
                self.ui.tabWidget.setTabEnabled(1, True)
            elif sb == QtWidgets.QDialogButtonBox.Discard: #DISCARD CLICKED
                #Reset flow
                self.start_up()
        except AttributeError:
            return
            
    def print_instructors(self):
        _translate = QtCore.QCoreApplication.translate
        index = 0
        
        self.ui.listWidget.clear()
        instructorList = system.get_instructors(self.df)
        
        if(instructorList == None):
            instructorList = []
            
        for instructor in instructorList:
            item = QtWidgets.QListWidgetItem()
            self.ui.listWidget.addItem(item)
            item = self.ui.listWidget.item(index)
            item.setText(_translate("MainWindow", str(instructor)))
            index = index + 1
           
        self.ui.label.setText("Instructors ({})".format(len(instructorList)))
        
    def print_termcodes(self):
        _translate = QtCore.QCoreApplication.translate
        index = 0
        
        self.ui.listWidget_2.clear()
        termList = system.get_termcodes(self.df)
        
        if(termList == None):
            termList = []
            
        for term in termList:
            item = QtWidgets.QListWidgetItem()
            self.ui.listWidget_2.addItem(item)
            item = self.ui.listWidget_2.item(index)
            item.setText(_translate("MainWindow", str(term)))
            index = index + 1
            
        self.ui.label_2.setText("Terms ({})".format(len(termList)))
            
    def build_tree(self):
        _translate = QtCore.QCoreApplication.translate
        self.ui.item.setText(0, _translate("MainWindow", os.path.basename(self.path)))
        self.ui.item.setCheckState(0, QtCore.Qt.Checked)
        self.ui.item.setFlags(self.ui.item.flags() | QtCore.Qt.ItemIsTristate | QtCore.Qt.ItemIsUserCheckable)
    
        self.tree_dict[self.path] = self.ui.item
        self.recurr(self.path, self.ui.item)
        
        #Set the event listener for further checkbox changes.
        self.ui.treeWidget.itemClicked.connect(self.count_checked_treeWidget)
       

    def recurr(self,path, parent):
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

        
    def setup_output(self, configs):
        #Get a file writer object
        self.output = output.FILE_WRITER()
                
        #Get the found configurations
        configs = self.output.get_db_config()
        
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


    def displayFeedBack(self, theInfo):

        #Initialize variables
        self.x = 0
        header = list()
        vBox1 = QVBoxLayout()
    
        #Create the feedback tab with a table widget and list widget
        self.ui.tabWidget.insertTab(2, self.ui.tab_2, "Feedback")
        self.ui.tableWidget = QtWidgets.QTableWidget(self.ui.tab_2)
        self.ui.tableWidget.setObjectName("tableWidget")
        self.ui.tableWidget.setMinimumSize(500, 195)
        self.ui.tableWidget.setColumnCount(1)
        self.ui.tableWidget.setRowCount(2)
        self.ui.tableWidget.move(130, 20)
        self.ui.checkBox_2 = QtWidgets.QCheckBox(self.ui.tab_2)
        self.ui.checkBox_2.setObjectName("checkBox_2")
        self.ui.checkBox_2.setText("Clean")
        self.ui.checkBox_2.move(130, 230)
        self.ui.pushButton_5 = QtWidgets.QPushButton(self.ui.tab_2)
        self.ui.pushButton_5.setObjectName("pushButton_5")
        self.ui.pushButton_5.setText("Next")
        self.ui.pushButton_5.move(520, 230)
        self.ui.pushButton_6 = QtWidgets.QPushButton(self.ui.tab_2)
        self.ui.pushButton_6.setObjectName("pushButton_6")
        self.ui.pushButton_6.setText("Warnings")
        self.ui.pushButton_6.move(40,350)
        self.ui.pushButton_7 = QtWidgets.QPushButton(self.ui.tab_2)
        self.ui.pushButton_7.setObjectName("pushButton_7")
        self.ui.pushButton_7.setText("Errors")
        self.ui.pushButton_7.move(40, 390)
        self.ui.exceptionsList = QtWidgets.QListWidget(self.ui.tab_2)
        self.ui.exceptionsList.setObjectName("exceptionsList")
        self.ui.exceptionsList.move(150, 330)
        self.ui.exceptionsList.setMinimumSize(550, 150)
       
        header.append(str(theInfo[0]).split('>')[1])
        
        self.ui.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        

        #Construct the table using the values
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(theInfo[0]).split('>')[2]))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(theInfo[0]).split('>')[3]))
        vBox1.addWidget(self.ui.tableWidget)
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        

        self.ui.tableWidget.setVerticalHeaderLabels(['Validator:', 'Info:'])
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(0, QHeaderView.Stretch)
         
       
        #Enable this, and the output tab for the user
        self.ui.tabWidget.setTabEnabled(2, True)
        self.ui.tabWidget.setTabEnabled(3, True)
        
        #Force the view to the feedback screen
        self.ui.tabWidget.setCurrentIndex(2)
        
        #connect the buttons to their functions
        self.ui.pushButton_5.clicked.connect(lambda: self.getNextColumn(self.x, theInfo))
        self.ui.pushButton_6.clicked.connect(lambda: self.seeExceptions(theInfo[self.x], 0))
        self.ui.pushButton_7.clicked.connect(lambda: self.seeExceptions(theInfo[self.x], 1))




    def seeExceptions(self, columnInfo, buttonId):

        self.ui.exceptionsList.clear()
        i = 0
        if(buttonId == 0):
            for element in columnInfo[1].warn:
                self.ui.exceptionsList.insertItem(i, element)
                i += 1
        else:
            for element in columnInfo[1].err:
                self.ui.exceptionsList.insertItem(i, element)
                i += 1


    def getNextColumn(self, x, theInfo):
        
        self.ui.exceptionsList.clear()

        if(self.x < len(theInfo)-1):    
            self.x += 1
            if(self.ui.checkBox_2.isChecked() == True):
                self.ui.checkBox_2.toggle()
                #TODO: add code for preserving info or cleaning column
            
            header = list()
            header.append(str(theInfo[self.x]).split('>')[1])
           
            #Construct the table using the values
            self.ui.tableWidget.setHorizontalHeaderLabels(header)
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(theInfo[self.x]).split('>')[2]))
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(theInfo[self.x]).split('>')[3]))
            
        else:
            self.ui.pushButton_5.setEnabled(False)
        
    def setup_output(self):
        #Get a file writer object
        self.output = output.FILE_WRITER()
                
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
        self.df = cleaned_data(self.df)    
        
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
        try:
            _translate = QtCore.QCoreApplication.translate
            
            self.outPath = QFileDialog.getSaveFileName(self, self.output.outName, '', 'CSV(*.csv)')[0] #Save only the output path
            self.ui.outputBrowseBox.setText(_translate("MainWindow", self.outPath))
            
            self.output.set_path(self.outPath)
            self.output.write_csv(self.df)
        
        except FileNotFoundError:
            print('FileNotFound') #CHANGE TO LOG FILE?
        
class WorkerSignals(QObject):
    #
    returnVal = pyqtSignal(object)
    

               
class Worker(QRunnable):

    def __init__(self, fn, selectedColumns, df):
        super(Worker, self).__init__()
        self.fn = fn
        self.theColumns = selectedColumns
        self.signals = WorkerSignals()
        self.theData = df

    @pyqtSlot()
    def run(self):

        theInfo = self.fn(self.theColumns, self.theData)
        
        #send the info returned from validators back to the GUI from worker thread
        self.signals.returnVal.emit(theInfo)
        
    
if __name__ == "__main__":       
    appctxt = ApplicationContext()       # 1. Instantiate ApplicationContext
    #app = QtWidgets.QApplication([])
    application = mywindow()
    application.resize(800, 600)
    application.show()
    exit_code = appctxt.app.exec_()      # 2. Invoke appctxt.app.exec_()
    sys.exit(exit_code)        
