from PyQt5 import QtWidgets
from PyQt5.QtCore import QRunnable, QThreadPool
from .gradebook_tool import Ui_MainWindow
from source.system import main
import sys

class mywindow(QtWidgets.QMainWindow):
    def __init__(self):
        super(mywindow, self).__init__()
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        

        #Code for handling widgets on "column configuration" window
        self.ui.listWidget_3.itemClicked.connect(self.item_3_click)
        self.ui.listWidget_4.itemClicked.connect(self.item_4_click)
        self.ui.pushButton_3.clicked.connect(self.all_columns_button)
        self.ui.pushButton_2.clicked.connect(self.continue_button)

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
