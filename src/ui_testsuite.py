# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file 'testsuite.ui'
#
# Created by: PyQt4 UI code generator 4.11.4
#
# WARNING! All changes made in this file will be lost!

from PyQt4 import QtCore, QtGui

try:
    _fromUtf8 = QtCore.QString.fromUtf8
except AttributeError:
    def _fromUtf8(s):
        return s

try:
    _encoding = QtGui.QApplication.UnicodeUTF8
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig, _encoding)
except AttributeError:
    def _translate(context, text, disambig):
        return QtGui.QApplication.translate(context, text, disambig)

class Ui_TestSuite(object):
    def setupUi(self, TestSuite):
        TestSuite.setObjectName(_fromUtf8("TestSuite"))
        TestSuite.resize(695, 640)
        TestSuite.setAcceptDrops(True)
        icon = QtGui.QIcon()
        icon.addPixmap(QtGui.QPixmap(_fromUtf8("images/applications_games.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        TestSuite.setWindowIcon(icon)
        self.centralwidget = QtGui.QWidget(TestSuite)
        self.centralwidget.setObjectName(_fromUtf8("centralwidget"))
        self.gridLayout_5 = QtGui.QGridLayout(self.centralwidget)
        self.gridLayout_5.setObjectName(_fromUtf8("gridLayout_5"))
        self.horizontalLayout_5 = QtGui.QHBoxLayout()
        self.horizontalLayout_5.setObjectName(_fromUtf8("horizontalLayout_5"))
        self.gridLayout_5.addLayout(self.horizontalLayout_5, 0, 0, 1, 1)
        self.verticalLayout_3 = QtGui.QVBoxLayout()
        self.verticalLayout_3.setObjectName(_fromUtf8("verticalLayout_3"))
        self.groupBox = QtGui.QGroupBox(self.centralwidget)
        self.groupBox.setObjectName(_fromUtf8("groupBox"))
        self.verticalLayout_5 = QtGui.QVBoxLayout(self.groupBox)
        self.verticalLayout_5.setObjectName(_fromUtf8("verticalLayout_5"))
        self.horizontalLayout = QtGui.QHBoxLayout()
        self.horizontalLayout.setObjectName(_fromUtf8("horizontalLayout"))
        self.verticalLayout_5.addLayout(self.horizontalLayout)
        self.horizontalLayout_7 = QtGui.QHBoxLayout()
        self.horizontalLayout_7.setObjectName(_fromUtf8("horizontalLayout_7"))
        self.listTestCollection = QtGui.QListWidget(self.groupBox)
        self.listTestCollection.setProperty("showDropIndicator", True)
        self.listTestCollection.setDragEnabled(False)
        self.listTestCollection.setDragDropOverwriteMode(False)
        self.listTestCollection.setDragDropMode(QtGui.QAbstractItemView.NoDragDrop)
        self.listTestCollection.setSelectionMode(QtGui.QAbstractItemView.ExtendedSelection)
        self.listTestCollection.setObjectName(_fromUtf8("listTestCollection"))
        self.horizontalLayout_7.addWidget(self.listTestCollection)
        self.verticalLayout = QtGui.QVBoxLayout()
        self.verticalLayout.setObjectName(_fromUtf8("verticalLayout"))
        self.buttonAdd = QtGui.QPushButton(self.groupBox)
        self.buttonAdd.setText(_fromUtf8(""))
        icon1 = QtGui.QIcon()
        icon1.addPixmap(QtGui.QPixmap(_fromUtf8("images/add.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonAdd.setIcon(icon1)
        self.buttonAdd.setObjectName(_fromUtf8("buttonAdd"))
        self.verticalLayout.addWidget(self.buttonAdd)
        self.buttonEdit = QtGui.QPushButton(self.groupBox)
        self.buttonEdit.setEnabled(False)
        self.buttonEdit.setText(_fromUtf8(""))
        icon2 = QtGui.QIcon()
        icon2.addPixmap(QtGui.QPixmap(_fromUtf8("images/edit.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonEdit.setIcon(icon2)
        self.buttonEdit.setObjectName(_fromUtf8("buttonEdit"))
        self.verticalLayout.addWidget(self.buttonEdit)
        self.buttonRemove = QtGui.QPushButton(self.groupBox)
        self.buttonRemove.setEnabled(False)
        self.buttonRemove.setText(_fromUtf8(""))
        icon3 = QtGui.QIcon()
        icon3.addPixmap(QtGui.QPixmap(_fromUtf8("images/remove.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRemove.setIcon(icon3)
        self.buttonRemove.setObjectName(_fromUtf8("buttonRemove"))
        self.verticalLayout.addWidget(self.buttonRemove)
        self.buttonRemoveAll = QtGui.QPushButton(self.groupBox)
        self.buttonRemoveAll.setEnabled(False)
        self.buttonRemoveAll.setText(_fromUtf8(""))
        icon4 = QtGui.QIcon()
        icon4.addPixmap(QtGui.QPixmap(_fromUtf8("images/remove_all.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonRemoveAll.setIcon(icon4)
        self.buttonRemoveAll.setObjectName(_fromUtf8("buttonRemoveAll"))
        self.verticalLayout.addWidget(self.buttonRemoveAll)
        spacerItem = QtGui.QSpacerItem(20, 40, QtGui.QSizePolicy.Minimum, QtGui.QSizePolicy.Expanding)
        self.verticalLayout.addItem(spacerItem)
        self.horizontalLayout_7.addLayout(self.verticalLayout)
        self.verticalLayout_5.addLayout(self.horizontalLayout_7)
        self.verticalLayout_3.addWidget(self.groupBox)
        self.gridLayout_5.addLayout(self.verticalLayout_3, 0, 1, 2, 1)
        self.groupBox_3 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_3.setObjectName(_fromUtf8("groupBox_3"))
        self.gridLayout = QtGui.QGridLayout(self.groupBox_3)
        self.gridLayout.setObjectName(_fromUtf8("gridLayout"))
        self.buttonClearLog = QtGui.QPushButton(self.groupBox_3)
        self.buttonClearLog.setText(_fromUtf8(""))
        icon5 = QtGui.QIcon()
        icon5.addPixmap(QtGui.QPixmap(_fromUtf8("images/clear_log.png")), QtGui.QIcon.Normal, QtGui.QIcon.Off)
        self.buttonClearLog.setIcon(icon5)
        self.buttonClearLog.setObjectName(_fromUtf8("buttonClearLog"))
        self.gridLayout.addWidget(self.buttonClearLog, 1, 0, 1, 1)
        spacerItem1 = QtGui.QSpacerItem(232, 20, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout.addItem(spacerItem1, 1, 1, 1, 1)
        self.textBrowserLog = QtGui.QTextBrowser(self.groupBox_3)
        self.textBrowserLog.setObjectName(_fromUtf8("textBrowserLog"))
        self.gridLayout.addWidget(self.textBrowserLog, 0, 0, 1, 2)
        self.gridLayout_5.addWidget(self.groupBox_3, 1, 2, 3, 1)
        self.groupBox_4 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_4.setMaximumSize(QtCore.QSize(16777215, 90))
        self.groupBox_4.setObjectName(_fromUtf8("groupBox_4"))
        self.gridLayout_4 = QtGui.QGridLayout(self.groupBox_4)
        self.gridLayout_4.setObjectName(_fromUtf8("gridLayout_4"))
        self.pushButton = QtGui.QPushButton(self.groupBox_4)
        self.pushButton.setEnabled(False)
        self.pushButton.setObjectName(_fromUtf8("pushButton"))
        self.gridLayout_4.addWidget(self.pushButton, 0, 1, 1, 1)
        self.buttonStop = QtGui.QPushButton(self.groupBox_4)
        self.buttonStop.setEnabled(False)
        self.buttonStop.setObjectName(_fromUtf8("buttonStop"))
        self.gridLayout_4.addWidget(self.buttonStop, 0, 2, 1, 1)
        self.buttonExecute = QtGui.QPushButton(self.groupBox_4)
        self.buttonExecute.setEnabled(False)
        self.buttonExecute.setObjectName(_fromUtf8("buttonExecute"))
        self.gridLayout_4.addWidget(self.buttonExecute, 0, 0, 1, 1)
        self.buttonExecuteAll = QtGui.QPushButton(self.groupBox_4)
        self.buttonExecuteAll.setEnabled(False)
        self.buttonExecuteAll.setObjectName(_fromUtf8("buttonExecuteAll"))
        self.gridLayout_4.addWidget(self.buttonExecuteAll, 1, 0, 1, 1)
        self.buttonExecuteFailed = QtGui.QPushButton(self.groupBox_4)
        self.buttonExecuteFailed.setEnabled(False)
        self.buttonExecuteFailed.setObjectName(_fromUtf8("buttonExecuteFailed"))
        self.gridLayout_4.addWidget(self.buttonExecuteFailed, 1, 1, 1, 1)
        self.buttonExecuteUntested = QtGui.QPushButton(self.groupBox_4)
        self.buttonExecuteUntested.setEnabled(False)
        self.buttonExecuteUntested.setObjectName(_fromUtf8("buttonExecuteUntested"))
        self.gridLayout_4.addWidget(self.buttonExecuteUntested, 1, 2, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_4, 2, 0, 1, 2)
        self.groupBox_2 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_2.setMaximumSize(QtCore.QSize(16777215, 100))
        self.groupBox_2.setObjectName(_fromUtf8("groupBox_2"))
        self.gridLayout_2 = QtGui.QGridLayout(self.groupBox_2)
        self.gridLayout_2.setObjectName(_fromUtf8("gridLayout_2"))
        self.horizontalLayout_3 = QtGui.QHBoxLayout()
        self.horizontalLayout_3.setObjectName(_fromUtf8("horizontalLayout_3"))
        self.label_2 = QtGui.QLabel(self.groupBox_2)
        self.label_2.setObjectName(_fromUtf8("label_2"))
        self.horizontalLayout_3.addWidget(self.label_2)
        self.gridLayout_2.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)
        self.horizontalLayout_4 = QtGui.QHBoxLayout()
        self.horizontalLayout_4.setObjectName(_fromUtf8("horizontalLayout_4"))
        self.label_3 = QtGui.QLabel(self.groupBox_2)
        self.label_3.setObjectName(_fromUtf8("label_3"))
        self.horizontalLayout_4.addWidget(self.label_3)
        self.sliderSpeed = QtGui.QSlider(self.groupBox_2)
        self.sliderSpeed.setLayoutDirection(QtCore.Qt.LeftToRight)
        self.sliderSpeed.setMaximum(1000)
        self.sliderSpeed.setSingleStep(200)
        self.sliderSpeed.setPageStep(200)
        self.sliderSpeed.setProperty("value", 200)
        self.sliderSpeed.setSliderPosition(200)
        self.sliderSpeed.setTracking(False)
        self.sliderSpeed.setOrientation(QtCore.Qt.Horizontal)
        self.sliderSpeed.setTickPosition(QtGui.QSlider.TicksAbove)
        self.sliderSpeed.setTickInterval(200)
        self.sliderSpeed.setObjectName(_fromUtf8("sliderSpeed"))
        self.horizontalLayout_4.addWidget(self.sliderSpeed)
        self.label_4 = QtGui.QLabel(self.groupBox_2)
        self.label_4.setObjectName(_fromUtf8("label_4"))
        self.horizontalLayout_4.addWidget(self.label_4)
        self.gridLayout_2.addLayout(self.horizontalLayout_4, 0, 1, 1, 1)
        spacerItem2 = QtGui.QSpacerItem(123, 18, QtGui.QSizePolicy.Expanding, QtGui.QSizePolicy.Minimum)
        self.gridLayout_2.addItem(spacerItem2, 0, 2, 1, 1)
        self.checkBoxStopWhenFailed = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxStopWhenFailed.setObjectName(_fromUtf8("checkBoxStopWhenFailed"))
        self.gridLayout_2.addWidget(self.checkBoxStopWhenFailed, 1, 0, 1, 2)
        self.checkBoxStopOnError = QtGui.QCheckBox(self.groupBox_2)
        self.checkBoxStopOnError.setObjectName(_fromUtf8("checkBoxStopOnError"))
        self.gridLayout_2.addWidget(self.checkBoxStopOnError, 2, 0, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_2, 3, 1, 1, 1)
        self.groupBox_5 = QtGui.QGroupBox(self.centralwidget)
        self.groupBox_5.setMaximumSize(QtCore.QSize(16777215, 180))
        self.groupBox_5.setObjectName(_fromUtf8("groupBox_5"))
        self.gridLayout_3 = QtGui.QGridLayout(self.groupBox_5)
        self.gridLayout_3.setObjectName(_fromUtf8("gridLayout_3"))
        self.label = QtGui.QLabel(self.groupBox_5)
        self.label.setObjectName(_fromUtf8("label"))
        self.gridLayout_3.addWidget(self.label, 0, 0, 1, 1)
        self.labelName = QtGui.QLabel(self.groupBox_5)
        self.labelName.setText(_fromUtf8(""))
        self.labelName.setObjectName(_fromUtf8("labelName"))
        self.gridLayout_3.addWidget(self.labelName, 0, 1, 1, 1)
        self.label_5 = QtGui.QLabel(self.groupBox_5)
        self.label_5.setObjectName(_fromUtf8("label_5"))
        self.gridLayout_3.addWidget(self.label_5, 1, 0, 1, 1)
        self.labelHand = QtGui.QLabel(self.groupBox_5)
        self.labelHand.setText(_fromUtf8(""))
        self.labelHand.setObjectName(_fromUtf8("labelHand"))
        self.gridLayout_3.addWidget(self.labelHand, 1, 1, 1, 1)
        self.label_6 = QtGui.QLabel(self.groupBox_5)
        self.label_6.setObjectName(_fromUtf8("label_6"))
        self.gridLayout_3.addWidget(self.label_6, 2, 0, 1, 1)
        self.labelStatus = QtGui.QLabel(self.groupBox_5)
        self.labelStatus.setText(_fromUtf8(""))
        self.labelStatus.setObjectName(_fromUtf8("labelStatus"))
        self.gridLayout_3.addWidget(self.labelStatus, 2, 1, 1, 1)
        self.label_7 = QtGui.QLabel(self.groupBox_5)
        self.label_7.setObjectName(_fromUtf8("label_7"))
        self.gridLayout_3.addWidget(self.label_7, 3, 0, 1, 1)
        self.textInfo = QtGui.QTextBrowser(self.groupBox_5)
        self.textInfo.setEnabled(True)
        self.textInfo.setObjectName(_fromUtf8("textInfo"))
        self.gridLayout_3.addWidget(self.textInfo, 3, 1, 1, 1)
        self.gridLayout_5.addWidget(self.groupBox_5, 0, 2, 1, 1)
        TestSuite.setCentralWidget(self.centralwidget)
        self.menubar = QtGui.QMenuBar(TestSuite)
        self.menubar.setGeometry(QtCore.QRect(0, 0, 695, 21))
        self.menubar.setObjectName(_fromUtf8("menubar"))
        self.menuFile = QtGui.QMenu(self.menubar)
        self.menuFile.setObjectName(_fromUtf8("menuFile"))
        TestSuite.setMenuBar(self.menubar)
        self.statusbar = QtGui.QStatusBar(TestSuite)
        self.statusbar.setAutoFillBackground(True)
        self.statusbar.setSizeGripEnabled(True)
        self.statusbar.setObjectName(_fromUtf8("statusbar"))
        TestSuite.setStatusBar(self.statusbar)
        self.actionNew = QtGui.QAction(TestSuite)
        self.actionNew.setObjectName(_fromUtf8("actionNew"))
        self.actionOpen = QtGui.QAction(TestSuite)
        self.actionOpen.setObjectName(_fromUtf8("actionOpen"))
        self.actionSave = QtGui.QAction(TestSuite)
        self.actionSave.setObjectName(_fromUtf8("actionSave"))
        self.actionSaveAs = QtGui.QAction(TestSuite)
        self.actionSaveAs.setObjectName(_fromUtf8("actionSaveAs"))
        self.actionExit = QtGui.QAction(TestSuite)
        self.actionExit.setObjectName(_fromUtf8("actionExit"))
        self.menuFile.addAction(self.actionNew)
        self.menuFile.addAction(self.actionOpen)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionSave)
        self.menuFile.addAction(self.actionSaveAs)
        self.menuFile.addSeparator()
        self.menuFile.addAction(self.actionExit)
        self.menubar.addAction(self.menuFile.menuAction())

        self.retranslateUi(TestSuite)
        QtCore.QMetaObject.connectSlotsByName(TestSuite)

    def retranslateUi(self, TestSuite):
        TestSuite.setWindowTitle(_translate("TestSuite", "TestSuite", None))
        self.groupBox.setTitle(_translate("TestSuite", "Test Collection", None))
        self.buttonAdd.setToolTip(_translate("TestSuite", "Add test case", None))
        self.buttonEdit.setToolTip(_translate("TestSuite", "Edit test case", None))
        self.buttonRemove.setToolTip(_translate("TestSuite", "Remove test case", None))
        self.buttonRemoveAll.setToolTip(_translate("TestSuite", "Remove all test cases", None))
        self.groupBox_3.setTitle(_translate("TestSuite", "Log", None))
        self.buttonClearLog.setToolTip(_translate("TestSuite", "Clear log", None))
        self.groupBox_4.setTitle(_translate("TestSuite", "Execution", None))
        self.pushButton.setText(_translate("TestSuite", "Pause", None))
        self.buttonStop.setText(_translate("TestSuite", "Stop", None))
        self.buttonExecute.setText(_translate("TestSuite", "Execute", None))
        self.buttonExecuteAll.setText(_translate("TestSuite", "Execute All", None))
        self.buttonExecuteFailed.setText(_translate("TestSuite", "Execute Failed", None))
        self.buttonExecuteUntested.setText(_translate("TestSuite", "Execute Untested", None))
        self.groupBox_2.setTitle(_translate("TestSuite", "Options", None))
        self.label_2.setText(_translate("TestSuite", "Execution Speed:", None))
        self.label_3.setText(_translate("TestSuite", "0 ms", None))
        self.label_4.setText(_translate("TestSuite", "1000 ms", None))
        self.checkBoxStopWhenFailed.setText(_translate("TestSuite", "Stop when test case fails", None))
        self.checkBoxStopOnError.setText(_translate("TestSuite", "Stop on error", None))
        self.groupBox_5.setTitle(_translate("TestSuite", "Test Case Info", None))
        self.label.setText(_translate("TestSuite", "Name:", None))
        self.label_5.setText(_translate("TestSuite", "Hand:", None))
        self.label_6.setText(_translate("TestSuite", "Status:", None))
        self.label_7.setText(_translate("TestSuite", "Info:", None))
        self.menuFile.setTitle(_translate("TestSuite", "File", None))
        self.actionNew.setText(_translate("TestSuite", "New...", None))
        self.actionNew.setShortcut(_translate("TestSuite", "Ctrl+N", None))
        self.actionOpen.setText(_translate("TestSuite", "Open...", None))
        self.actionSave.setText(_translate("TestSuite", "Save", None))
        self.actionSave.setShortcut(_translate("TestSuite", "Ctrl+S", None))
        self.actionSaveAs.setText(_translate("TestSuite", "Save as...", None))
        self.actionExit.setText(_translate("TestSuite", "Exit", None))

