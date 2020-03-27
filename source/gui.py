from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QTableWidgetItem, QTableWidget, QHeaderView
from PyQt5.QtCore import QRunnable, QThreadPool, QObject, pyqtSignal, pyqtSlot
from .gradebook_tool import Ui_MainWindow
from source.system import main
import sys, traceback

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)


        #Code for handling widgets on "column configuration" window
        self.ui.listWidget_3.itemClicked.connect(self.item_3_click)
        self.ui.listWidget_4.itemClicked.connect(self.item_4_click)
        self.ui.pushButton_3.clicked.connect(self.all_columns_button)
        self.ui.pushButton_4.clicked.connect(self.validate_button)

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
        

    def validate_button(self):
        self.threadpool = QThreadPool()
        theColumns = []
        x = self.ui.listWidget_4.count()-1
        while(x >= 0):
            theColumns.append(self.ui.listWidget_4.item(x).text())
            x -= 1

        worker = Worker(main, theColumns)
        worker.signals.returnVal.connect(self.displayFeedBack)
        self.threadpool.start(worker)

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
        self.ui.tabWidget.addTab(self.ui.tab_2, "feedback")
        self.ui.tableWidget = QtWidgets.QTableWidget(self.ui.tab_2)
        self.ui.tableWidget.setObjectName("tableWidget")
        self.ui.tableWidget.setMinimumSize(505, 195)
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
        # self.ui.pushButton_6 = QtWidgets.QPushButton(self.ui.tab_2)
        # self.ui.pushButton_6.setObjectName("pushButton_6")
        # self.ui.pushButton_6.setText("Exceptions")
        # self.ui.pushButton_6.move(320, 230)
       
        #create strings from the validator info returned from main 
        self.x = 0
        header = list()
        validator = list()
        stats = list()
        warnings = list()
        errors = list()

        header.append(str(theInfo[self.x]).split('>')[1])
        validator.append(str(theInfo[self.x]).split('>')[2])
        stats.append(str(theInfo[self.x]).split('>')[3])
        warnings.append(str(theInfo[self.x]).split('>')[5])

        #Construct the table using the values
        self.ui.tableWidget.setItem(0, 0, QTableWidgetItem(str(validator[self.x])))
        self.ui.tableWidget.setItem(1, 0, QTableWidgetItem(str(stats[self.x])))
        self.ui.tableWidget.resizeRowsToContents()
        self.ui.tableWidget.resizeColumnsToContents()
        

        self.ui.tableWidget.setVerticalHeaderLabels(['Validator:', 'Info:'])
        self.ui.tableWidget.setHorizontalHeaderLabels(header)
        self.ui.tableWidget.horizontalHeader().setSectionResizeMode(QHeaderView.ResizeToContents)
       
        self.ui.pushButton_5.clicked.connect(lambda: self.getNextColumn(self.x, theInfo, validator, stats, warnings, errors))
        
        


class WorkerSignals(QObject):

    returnVal = pyqtSignal(object)

               
class Worker(QRunnable):

    def __init__(self, fn, selectedColumns):
        super(Worker, self).__init__()
        self.fn = fn
        self.theColumns = selectedColumns
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):

        theInfo = self.fn(self.theColumns)
        self.signals.returnVal.emit(theInfo)
        

        


    

        
                
if __name__ == "__main__":       
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.resize(800, 600)
    application.show()
    sys.exit(app.exec())        
