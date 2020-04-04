from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView, QVBoxLayout
from PyQt5.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot
from .gradebook_tool import Ui_MainWindow
from source.system import main
import sys,os
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
from source import getFiles
from source import system
from source import output

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)

        #Modify any starting UI parameters
        self.start_up()
        
        #Code for handling widgets on "column configuration" window
        self.ui.listWidget_3.itemClicked.connect(self.item_3_click)
        self.ui.listWidget_4.itemClicked.connect(self.item_4_click)
        self.ui.pushButton_3.clicked.connect(self.all_columns_button)
        self.ui.pushButton_4.clicked.connect(self.validate_button)
        self.ui.pushButton_4.clicked.connect(self.setup_output)

        self.ui.pushButton.clicked.connect(self.getPath)
        self.ui.buttonBox.clicked.connect(self.apply_button)
        
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
        
    def update_selected_text(self):
        selectedCount = len(self.ui.treeWidget.selectedItems())
        print(selectedCount)
        self.ui.label_4.setText("{} selected".format(selectedCount))
        
    def getPath(self):
        self.tree_dict = {}
        self.ui.item = QtWidgets.QTreeWidgetItem(self.ui.treeWidget)
        try:
            _translate = QtCore.QCoreApplication.translate
        
            self.path = QFileDialog.getExistingDirectory(None, 'Open File')
            self.ui.lineEdit.setText(_translate("MainWindow", self.path))
            self.countFiles = 0
            self.numFiles = self.build_tree()
            self.ui.label_3.setText(_translate("MainWindow",('Files Found: '+str(self.countFiles))))
            
            self.ui.treeWidget.itemSelectionChanged.connect(self.update_selected_text)
            
            self.ui.buttonBox.setEnabled(True)
            
        except FileNotFoundError:
            print('FileNotFound') #CHANGE TO LOG FILE?
            
        return self.path
    
    def check_state(self):
        self.unwanted = []
        for path in self.tree_dict:
            if self.tree_dict[path].checkState(0) == 0:
                getFiles.add_unwanted_path(self.unwanted, path)
                
    
    def apply_button(self): 
        if self.path != None:
            self.check_state()
            self.df = getFiles.execute(self.path, self.unwanted)
            
            self.print_instructors()
            self.print_termcodes()
            
            self.ui.tabWidget.setTabEnabled(1, True)
            
            
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
    
        self.tree_dict[self.path] = self.ui.item
        self.recurr(self.path, self.ui.item)
       

    def recurr(self,path, parent):
        _translate = QtCore.QCoreApplication.translate
        for folder in os.listdir(path):
            if os.path.isfile(os.path.join(path, folder)):
                if '.csv' in folder:
                    if getFiles.check_file(os.path.join(path, folder)):
                        child = QtWidgets.QTreeWidgetItem(parent)
                        child.setText(0, _translate("MainWindow", folder))
                        child.setCheckState(0, QtCore.Qt.Checked)
                        self.countFiles = self.countFiles + 1
                        self.tree_dict[os.path.join(path, folder)] = child
                    continue
            else:
                child = QtWidgets.QTreeWidgetItem(parent)
                child.setText(0, _translate("MainWindow", folder))
                child.setCheckState(0, QtCore.Qt.Checked)
                self.tree_dict[os.path.join(path, folder)] = child
                p = os.path.join(path, folder)
                self.recurr(p, child)

    def getNextColumn(self, x, theInfo, validator, stats, warnings, errors):
        
        if(self.x < len(theInfo)-1):    
            self.x += 1
            if(self.ui.checkBox_2.isChecked() == True):
                self.ui.checkBox_2.toggle()
                #TODO: add code for preserving info or cleaning column
            

            header = list()
            header.append(str(theInfo[self.x]).split('>')[1])
            validator.append(str(theInfo[self.x]).split('>')[2])
            stats.append(str(theInfo[self.x]).split('>')[3])
            warnings.append(str(theInfo[self.x]).split('>')[5])

            #Construct the table using the values
            self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(validator[self.x])))
            self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(stats[self.x])))
            

            self.ui.tableWidget.setHorizontalHeaderLabels(header)
            
        else:
            self.x = -1
            validator.clear()
            stats.clear()
            warnings.clear()

    def displayFeedBack(self, theInfo):
    
        #Create the feedback tab with a table widget
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
        self.ui.pushButton_5.setText("Continue")
        self.ui.pushButton_5.move(520, 230)
       
        #create strings from the validator info returned from main 
        self.x = 0
        header = list()
        validator = list()
        stats = list()
        warnings = list()
        errors = list()
        vBox = QVBoxLayout()

        header.append(str(theInfo[self.x]).split('>')[1])
        validator.append(str(theInfo[self.x]).split('>')[2])
        stats.append(str(theInfo[self.x]).split('>')[3])
        warnings.append(str(theInfo[self.x]).split('>')[5])

        self.ui.tableWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustToContents)
        

        #Construct the table using the values
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(validator[self.x])))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(stats[self.x])))
        vBox.addWidget(self.ui.tableWidget)
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
        
        #connect continue button to function that cycles through the validated columns
        self.ui.pushButton_5.clicked.connect(lambda: self.getNextColumn(self.x, theInfo, validator, stats, warnings, errors))
        
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

class WorkerSignals(QObject):
    #
    returnVal = pyqtSignal(object)
    
    
    # dbConfigs = pyqtSignal(object)

               
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

    # @pyqtSlot()
    # def save(self):
    
        # configs = self.fn(self.theData)
        
        # Send the connection configurations read to the GUI
        # self.signals.dbConfigs.emit(configs)
        
    
if __name__ == "__main__":       
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.resize(800, 600)
    application.show()
    sys.exit(app.exec())        
