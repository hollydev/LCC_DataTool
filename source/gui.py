from PyQt5 import QtWidgets
from PyQt5.QtCore import QRunnable, QThreadPool
from .gradebook_tool import Ui_MainWindow
from source.system import main
import sys,os
from PyQt5.QtWidgets import QFileDialog
from PyQt5 import QtCore
import getFiles, system

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        #Code for handling widgets on "column configuration" window
        self.ui.listWidget_3.itemClicked.connect(self.item_3_click)
        self.ui.listWidget_4.itemClicked.connect(self.item_4_click)
        self.ui.pushButton_3.clicked.connect(self.all_columns_button)
        self.ui.pushButton_4.clicked.connect(self.continue_button)
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
        self.ui.listWidget_4.repaint()

    def continue_button(self):
        self.threadpool = QThreadPool()
        theColumns = []
        x = self.ui.listWidget_4.count()-1
        while(x >= 0):
            theColumns.append(self.ui.listWidget_4.item(x).text())
            x -= 1
        worker = Worker(main, theColumns)
        self.threadpool.start(worker)
        
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
            
            
            
    def print_instructors(self):
        _translate = QtCore.QCoreApplication.translate
        index = 0
        for instructor in system.get_instructors(self.df):
            item = QtWidgets.QListWidgetItem()
            self.ui.listWidget.addItem(item)
            item = self.ui.listWidget.item(index)
            item.setText(_translate("MainWindow", instructor))
            index = index + 1
            
    def print_termcodes(self):
        _translate = QtCore.QCoreApplication.translate
        index = 0
        for term in system.get_termcodes(self.df):
            item = QtWidgets.QListWidgetItem()
            self.ui.listWidget_2.addItem(item)
            item = self.ui.listWidget_2.item(index)
            item.setText(_translate("MainWindow", term))
            index = index + 1
            
            
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


class Worker(QRunnable):

    def __init__(self, fn, selectedColumns):
        super(Worker, self).__init__()
        self.fn = fn
        self.theColumns = selectedColumns

    def run(self):
        
        self.fn(self.theColumns)
                
if __name__ == "__main__":       
    app = QtWidgets.QApplication([])
    application = mywindow()
    application.resize(800, 600)
    application.show()
    sys.exit(app.exec())        
