# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'gui.ui'
#
# Created by: PyQt5 UI code generator 5.14.1
#
# WARNING! All changes made in this file will be lost!


from PyQt5 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(891, 668)
        self.centralwidget = QtWidgets.QWidget(MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.horizontalLayout = QtWidgets.QHBoxLayout(self.centralwidget)
        self.horizontalLayout.setObjectName("horizontalLayout")
        self.tabWidget = QtWidgets.QTabWidget(self.centralwidget)
        self.tabWidget.setEnabled(True)
        self.tabWidget.setTabPosition(QtWidgets.QTabWidget.North)
        self.tabWidget.setTabShape(QtWidgets.QTabWidget.Rounded)
        self.tabWidget.setIconSize(QtCore.QSize(16, 16))
        self.tabWidget.setTabsClosable(False)
        self.tabWidget.setTabBarAutoHide(False)
        self.tabWidget.setObjectName("tabWidget")
        self.tab = QtWidgets.QWidget()
        self.tab.setObjectName("tab")
        self.verticalLayout_6 = QtWidgets.QVBoxLayout(self.tab)
        self.verticalLayout_6.setObjectName("verticalLayout_6")
        self.groupBox = QtWidgets.QGroupBox(self.tab)
        self.groupBox.setTitle("")
        self.groupBox.setObjectName("groupBox")
        self.horizontalLayout_2 = QtWidgets.QHBoxLayout(self.groupBox)
        self.horizontalLayout_2.setObjectName("horizontalLayout_2")
        self.lineEdit = QtWidgets.QLineEdit(self.groupBox)
        self.lineEdit.setEnabled(True)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.lineEdit.sizePolicy().hasHeightForWidth())
        self.lineEdit.setSizePolicy(sizePolicy)
        self.lineEdit.setMinimumSize(QtCore.QSize(400, 0))
        self.lineEdit.setObjectName("lineEdit")
        self.horizontalLayout_2.addWidget(self.lineEdit)
        self.pushButton = QtWidgets.QPushButton(self.groupBox)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Expanding, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton.sizePolicy().hasHeightForWidth())
        self.pushButton.setSizePolicy(sizePolicy)
        self.pushButton.setMinimumSize(QtCore.QSize(80, 0))
        self.pushButton.setMaximumSize(QtCore.QSize(80, 16777215))
        self.pushButton.setObjectName("pushButton")
        self.horizontalLayout_2.addWidget(self.pushButton)
        self.verticalLayout_6.addWidget(self.groupBox)
        self.groupBox_5 = QtWidgets.QGroupBox(self.tab)
        self.groupBox_5.setObjectName("groupBox_5")
        self.gridLayout_5 = QtWidgets.QGridLayout(self.groupBox_5)
        self.gridLayout_5.setObjectName("gridLayout_5")
        self.groupBox_3 = QtWidgets.QGroupBox(self.groupBox_5)
        self.groupBox_3.setMinimumSize(QtCore.QSize(61, 100))
        self.groupBox_3.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.groupBox_3.setObjectName("groupBox_3")
        self.verticalLayout_2 = QtWidgets.QVBoxLayout(self.groupBox_3)
        self.verticalLayout_2.setObjectName("verticalLayout_2")
        self.groupBox_6 = QtWidgets.QGroupBox(self.groupBox_3)
        self.groupBox_6.setTitle("")
        self.groupBox_6.setObjectName("groupBox_6")
        self.gridLayout_2 = QtWidgets.QGridLayout(self.groupBox_6)
        self.gridLayout_2.setObjectName("gridLayout_2")
        self.label_4 = QtWidgets.QLabel(self.groupBox_6)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.label_4.sizePolicy().hasHeightForWidth())
        self.label_4.setSizePolicy(sizePolicy)
        self.label_4.setObjectName("label_4")
        self.gridLayout_2.addWidget(self.label_4, 0, 0, 1, 1)
        self.label_3 = QtWidgets.QLabel(self.groupBox_6)
        self.label_3.setAlignment(QtCore.Qt.AlignRight|QtCore.Qt.AlignTrailing|QtCore.Qt.AlignVCenter)
        self.label_3.setObjectName("label_3")
        self.gridLayout_2.addWidget(self.label_3, 0, 1, 1, 1)
        self.verticalLayout_2.addWidget(self.groupBox_6)
        self.label = QtWidgets.QLabel(self.groupBox_3)
        self.label.setObjectName("label")
        self.verticalLayout_2.addWidget(self.label)
        self.listWidget = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget.setObjectName("listWidget")
        self.verticalLayout_2.addWidget(self.listWidget)
        self.label_2 = QtWidgets.QLabel(self.groupBox_3)
        self.label_2.setObjectName("label_2")
        self.verticalLayout_2.addWidget(self.label_2)
        self.listWidget_2 = QtWidgets.QListWidget(self.groupBox_3)
        self.listWidget_2.setObjectName("listWidget_2")
        self.verticalLayout_2.addWidget(self.listWidget_2)
        self.gridLayout_5.addWidget(self.groupBox_3, 0, 1, 1, 1)
        self.treeWidget = QtWidgets.QTreeWidget(self.groupBox_5)
        self.treeWidget.viewport().setProperty("cursor", QtGui.QCursor(QtCore.Qt.ArrowCursor))
        self.treeWidget.setAutoFillBackground(False)
        self.treeWidget.setHorizontalScrollBarPolicy(QtCore.Qt.ScrollBarAsNeeded)
        self.treeWidget.setSizeAdjustPolicy(QtWidgets.QAbstractScrollArea.AdjustIgnored)
        self.treeWidget.setEditTriggers(QtWidgets.QAbstractItemView.CurrentChanged|QtWidgets.QAbstractItemView.DoubleClicked|QtWidgets.QAbstractItemView.EditKeyPressed|QtWidgets.QAbstractItemView.SelectedClicked)
        self.treeWidget.setProperty("showDropIndicator", True)
        self.treeWidget.setDragEnabled(True)
        self.treeWidget.setAlternatingRowColors(True)
        self.treeWidget.setSelectionMode(QtWidgets.QAbstractItemView.ExtendedSelection)
        self.treeWidget.setSelectionBehavior(QtWidgets.QAbstractItemView.SelectItems)
        self.treeWidget.setAutoExpandDelay(-1)
        self.treeWidget.setUniformRowHeights(True)
        self.treeWidget.setWordWrap(False)
        self.treeWidget.setHeaderHidden(False)
        self.treeWidget.setObjectName("treeWidget")
        self.gridLayout_5.addWidget(self.treeWidget, 0, 0, 1, 1)
        self.verticalLayout_6.addWidget(self.groupBox_5)
        self.buttonBox = QtWidgets.QDialogButtonBox(self.tab)
        self.buttonBox.setOrientation(QtCore.Qt.Horizontal)
        self.buttonBox.setStandardButtons(QtWidgets.QDialogButtonBox.Apply|QtWidgets.QDialogButtonBox.Discard)
        self.buttonBox.setObjectName("buttonBox")
        self.verticalLayout_6.addWidget(self.buttonBox)
        self.tabWidget.addTab(self.tab, "")
        self.Column = QtWidgets.QWidget()
        self.Column.setObjectName("Column")
        self.gridLayout = QtWidgets.QGridLayout(self.Column)
        self.gridLayout.setObjectName("gridLayout")
        self.listWidget_3 = QtWidgets.QListWidget(self.Column)
        self.listWidget_3.setObjectName("listWidget_3")
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        item = QtWidgets.QListWidgetItem()
        self.listWidget_3.addItem(item)
        self.gridLayout.addWidget(self.listWidget_3, 1, 0, 3, 2)

        self.progressBar = QtWidgets.QProgressBar(self.tab) #PROGRESS BAR
        self.progressBar.setObjectName("progressBar")
        self.gridLayout.addWidget(self.progressBar)


        self.label_5 = QtWidgets.QLabel(self.Column)
        self.label_5.setObjectName("label_5")
        self.gridLayout.addWidget(self.label_5, 0, 0, 1, 1)
        self.listWidget_4 = QtWidgets.QListWidget(self.Column)
        self.listWidget_4.setObjectName("listWidget_4")
        self.gridLayout.addWidget(self.listWidget_4, 1, 2, 1, 1)
        self.pushButton_3 = QtWidgets.QPushButton(self.Column)
        self.pushButton_3.setObjectName("pushButton_3")
        self.gridLayout.addWidget(self.pushButton_3, 0, 1, 1, 1)
        self.label_6 = QtWidgets.QLabel(self.Column)
        self.label_6.setObjectName("label_6")
        self.gridLayout.addWidget(self.label_6, 0, 2, 1, 1)
        self.pushButton_4 = QtWidgets.QPushButton(self.Column)
        self.pushButton_4.setObjectName("pushButton_4")
        self.gridLayout.addWidget(self.pushButton_4, 4, 2, 1, 1)
        self.tabWidget.addTab(self.Column, "")
        self.tab_2 = QtWidgets.QWidget()
        self.tab_2.setObjectName("tab_2")
        self.formLayout = QtWidgets.QFormLayout(self.tab_2)
        self.formLayout.setObjectName("formLayout")
        self.tableWidget = QtWidgets.QTableWidget(self.tab_2)
        self.tableWidget.setObjectName("tableWidget")
        self.tableWidget.setMinimumSize(500, 195)
        self.tableWidget.setColumnCount(1)
        self.tableWidget.setRowCount(2)
        self.tableWidget.move(130, 20)
        self.checkBox_2 = QtWidgets.QCheckBox(self.tab_2)
        self.checkBox_2.setObjectName("checkBox_2")
        self.checkBox_2.setText("Clean")
        self.checkBox_2.move(130, 230)
        self.pushButton_5 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_5.setObjectName("pushButton_5")
        self.pushButton_5.setText("Next")
        self.pushButton_5.move(520, 230)
        self.pushButton_6 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_6.setObjectName("pushButton_6")
        self.pushButton_6.setText("Warnings")
        self.pushButton_6.move(10,330)
        self.pushButton_7 = QtWidgets.QPushButton(self.tab_2)
        self.pushButton_7.setObjectName("pushButton_7")
        self.pushButton_7.setText("Errors")
        self.pushButton_7.move(10, 390)
        self.exceptionsList = QtWidgets.QListWidget(self.tab_2)
        self.exceptionsList.setObjectName("exceptionsList")
        self.exceptionsList.move(130, 330)
        self.exceptionsList.setMinimumSize(500, 195)
        self.tabWidget.addTab(self.tab_2, "")
        self.tab_3 = QtWidgets.QWidget()
        self.tab_3.setObjectName("tab_3")
        self.verticalLayout = QtWidgets.QVBoxLayout(self.tab_3)
        self.verticalLayout.setObjectName("verticalLayout")
        self.groupBox_2 = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Expanding)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_2.sizePolicy().hasHeightForWidth())
        self.groupBox_2.setSizePolicy(sizePolicy)
        self.groupBox_2.setObjectName("groupBox_2")
        self.verticalLayout_5 = QtWidgets.QVBoxLayout(self.groupBox_2)
        self.verticalLayout_5.setObjectName("verticalLayout_5")
        self.DBConnection = QtWidgets.QGroupBox(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DBConnection.sizePolicy().hasHeightForWidth())
        self.DBConnection.setSizePolicy(sizePolicy)
        self.DBConnection.setObjectName("DBConnection")
        self.verticalLayout_3 = QtWidgets.QVBoxLayout(self.DBConnection)
        self.verticalLayout_3.setObjectName("verticalLayout_3")
        self.usernameLabel = QtWidgets.QLabel(self.DBConnection)
        self.usernameLabel.setObjectName("usernameLabel")
        self.verticalLayout_3.addWidget(self.usernameLabel)
        self.TNSLabel = QtWidgets.QLabel(self.DBConnection)
        self.TNSLabel.setObjectName("TNSLabel")
        self.verticalLayout_3.addWidget(self.TNSLabel)
        self.fallbackConnection = QtWidgets.QGroupBox(self.DBConnection)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Ignored, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.fallbackConnection.sizePolicy().hasHeightForWidth())
        self.fallbackConnection.setSizePolicy(sizePolicy)
        self.fallbackConnection.setObjectName("fallbackConnection")
        self.verticalLayout_4 = QtWidgets.QVBoxLayout(self.fallbackConnection)
        self.verticalLayout_4.setObjectName("verticalLayout_4")
        self.serviceLabel = QtWidgets.QLabel(self.fallbackConnection)
        self.serviceLabel.setObjectName("serviceLabel")
        self.verticalLayout_4.addWidget(self.serviceLabel)
        self.hostnameLabel = QtWidgets.QLabel(self.fallbackConnection)
        self.hostnameLabel.setObjectName("hostnameLabel")
        self.verticalLayout_4.addWidget(self.hostnameLabel)
        self.portLabel = QtWidgets.QLabel(self.fallbackConnection)
        self.portLabel.setObjectName("portLabel")
        self.verticalLayout_4.addWidget(self.portLabel)
        self.verticalLayout_3.addWidget(self.fallbackConnection)
        self.verticalLayout_5.addWidget(self.DBConnection)
        self.DBConnectionStatusLabel = QtWidgets.QLabel(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DBConnectionStatusLabel.sizePolicy().hasHeightForWidth())
        self.DBConnectionStatusLabel.setSizePolicy(sizePolicy)
        self.DBConnectionStatusLabel.setObjectName("DBConnectionStatusLabel")
        self.verticalLayout_5.addWidget(self.DBConnectionStatusLabel)
        self.label_7 = QtWidgets.QLabel(self.groupBox_2)
        self.label_7.setObjectName("label_7")
        self.verticalLayout_5.addWidget(self.label_7)
        self.pushButton_2 = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.pushButton_2.sizePolicy().hasHeightForWidth())
        self.pushButton_2.setSizePolicy(sizePolicy)
        self.pushButton_2.setObjectName("pushButton_2")
        self.verticalLayout_5.addWidget(self.pushButton_2)
        self.DBLoadButton = QtWidgets.QPushButton(self.groupBox_2)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Minimum, QtWidgets.QSizePolicy.Fixed)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.DBLoadButton.sizePolicy().hasHeightForWidth())
        self.DBLoadButton.setSizePolicy(sizePolicy)
        self.DBLoadButton.setMaximumSize(QtCore.QSize(16777215, 16777215))
        self.DBLoadButton.setObjectName("DBLoadButton")
        self.verticalLayout_5.addWidget(self.DBLoadButton)
        self.verticalLayout.addWidget(self.groupBox_2)
        self.groupBox_4 = QtWidgets.QGroupBox(self.tab_3)
        sizePolicy = QtWidgets.QSizePolicy(QtWidgets.QSizePolicy.Preferred, QtWidgets.QSizePolicy.Minimum)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.groupBox_4.sizePolicy().hasHeightForWidth())
        self.groupBox_4.setSizePolicy(sizePolicy)
        self.groupBox_4.setObjectName("groupBox_4")
        self.gridLayout_3 = QtWidgets.QGridLayout(self.groupBox_4)
        self.gridLayout_3.setObjectName("gridLayout_3")
        self.outputBrowseBox = QtWidgets.QLineEdit(self.groupBox_4)
        self.outputBrowseBox.setObjectName("outputBrowseBox")
        self.gridLayout_3.addWidget(self.outputBrowseBox, 0, 0, 1, 1)
        self.outputBrowseButton = QtWidgets.QPushButton(self.groupBox_4)
        self.outputBrowseButton.setObjectName("outputBrowseButton")
        self.gridLayout_3.addWidget(self.outputBrowseButton, 0, 1, 1, 1)
        self.verticalLayout.addWidget(self.groupBox_4)
        self.tabWidget.addTab(self.tab_3, "")
        self.horizontalLayout.addWidget(self.tabWidget)
        MainWindow.setCentralWidget(self.centralwidget)
        self.statusbar = QtWidgets.QStatusBar(MainWindow)
        self.statusbar.setObjectName("statusbar")
        MainWindow.setStatusBar(self.statusbar)

        self.retranslateUi(MainWindow)
        self.tabWidget.setCurrentIndex(0)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "LCC Assessment Data Tool"))
        self.lineEdit.setText(_translate("MainWindow", "C:\\Users\\razzi\\Desktop\\D2L Data"))
        self.pushButton.setText(_translate("MainWindow", "Browse..."))
        self.groupBox_5.setTitle(_translate("MainWindow", "Select Data"))
        self.groupBox_3.setTitle(_translate("MainWindow", "Statistics"))
        self.label_4.setText(_translate("MainWindow", "Files Selected"))
        self.label_3.setText(_translate("MainWindow", "Files Found"))
        self.label.setText(_translate("MainWindow", "Instructors:"))
        self.label_2.setText(_translate("MainWindow", "Term Range:"))
        self.treeWidget.headerItem().setText(0, _translate("MainWindow", "Gradebook Data"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Gradebook Data"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.tab), _translate("MainWindow", "Select gradebook information"))
        __sortingEnabled = self.listWidget_3.isSortingEnabled()
        self.listWidget_3.setSortingEnabled(False)
        item = self.listWidget_3.item(0)
        item.setText(_translate("MainWindow", "Username"))
        item = self.listWidget_3.item(1)
        item.setText(_translate("MainWindow", "FirstName"))
        item = self.listWidget_3.item(2)
        item.setText(_translate("MainWindow", "LastName"))
        item = self.listWidget_3.item(3)
        item.setText(_translate("MainWindow", "RoleId"))
        item = self.listWidget_3.item(4)
        item.setText(_translate("MainWindow", "RoleName"))
        item = self.listWidget_3.item(5)
        item.setText(_translate("MainWindow", "CourseOfferingId"))
        item = self.listWidget_3.item(6)
        item.setText(_translate("MainWindow", "CourseOfferingCode"))
        item = self.listWidget_3.item(7)
        item.setText(_translate("MainWindow", "CourseOfferingName"))
        item = self.listWidget_3.item(8)
        item.setText(_translate("MainWindow", "CourseSectionCode"))
        item = self.listWidget_3.item(9)
        item.setText(_translate("MainWindow", "GradeItemCategoryId"))
        item = self.listWidget_3.item(10)
        item.setText(_translate("MainWindow", "GradeItemCategoryName"))
        item = self.listWidget_3.item(11)
        item.setText(_translate("MainWindow", "GradeItemId"))
        item = self.listWidget_3.item(12)
        item.setText(_translate("MainWindow", "GradeItemName"))
        item = self.listWidget_3.item(13)
        item.setText(_translate("MainWindow", "GradeItemWeight"))
        item = self.listWidget_3.item(14)
        item.setText(_translate("MainWindow", "PointsNumerator"))
        item = self.listWidget_3.item(15)
        item.setText(_translate("MainWindow", "PointsDenominator"))
        item = self.listWidget_3.item(16)
        item.setText(_translate("MainWindow", "GradeValue"))
        item = self.listWidget_3.item(17)
        item.setText(_translate("MainWindow", "GradeLastModified"))
        self.listWidget_3.setSortingEnabled(__sortingEnabled)
        self.label_5.setText(_translate("MainWindow", "Select the columns you want or click all columns"))
        self.pushButton_3.setText(_translate("MainWindow", "All columns"))
        self.label_6.setText(_translate("MainWindow", "Selected Columns:"))
        self.pushButton_4.setText(_translate("MainWindow", "Validate"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Column), _translate("MainWindow", "Validate"))
        self.tabWidget.setTabToolTip(self.tabWidget.indexOf(self.Column), _translate("MainWindow", "Configure column settings"))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), _translate("MainWindow", "Feedback"))
        self.groupBox_2.setTitle(_translate("MainWindow", "Load to Database"))
        self.DBConnection.setTitle(_translate("MainWindow", "Connection Information"))
        self.usernameLabel.setText(_translate("MainWindow", "Username: "))
        self.TNSLabel.setText(_translate("MainWindow", "TNS Name:"))
        self.fallbackConnection.setTitle(_translate("MainWindow", "Fallback Connection"))
        self.serviceLabel.setText(_translate("MainWindow", "Service:"))
        self.hostnameLabel.setText(_translate("MainWindow", "Hostname:"))
        self.portLabel.setText(_translate("MainWindow", "Port:"))
        self.DBConnectionStatusLabel.setText(_translate("MainWindow", "Status: "))
        self.label_7.setText(_translate("MainWindow", "Task:"))
        self.pushButton_2.setText(_translate("MainWindow", "Connect"))
        self.DBLoadButton.setText(_translate("MainWindow", "Load to Database"))
        self.groupBox_4.setTitle(_translate("MainWindow", "Write CSV File"))
        self.outputBrowseButton.setText(_translate("MainWindow", "Browse..."))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_3), _translate("MainWindow", "Output"))