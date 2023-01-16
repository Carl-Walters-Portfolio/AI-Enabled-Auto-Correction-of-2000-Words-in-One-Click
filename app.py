from PyQt6.QtWidgets import QApplication, QMainWindow
from PyQt6 import uic
from PyQt6.QtGui import *
from PyQt6.QtWidgets import *
from PyQt6.QtCore import *
from PyQt6 import QtWidgets, QtGui, QtCore

from PyQt6.QtGui import  *
from PyQt6.QtWidgets import *
from PyQt6 import *
from PyQt6 import QtWidgets, QtGui, QtCore
from PyQt6 import QtWidgets, QtCore
from PyQt6.QtMultimedia import *
from PyQt6 import QtMultimedia
from PyQt6.uic import loadUi
from PyQt6.QtWidgets import QApplication, QWidget, QLabel
from PyQt6.QtGui import QIcon, QPixmap
from PyQt6 import QtWidgets

from PyQt6.QtWidgets import (QWidget, QTabWidget, QGridLayout, QApplication, QMainWindow, QStatusBar, QTableView)
from PyQt6.QtCore import (Qt, QTimer, QAbstractTableModel, QThread, QVariant, QObject, QRect, pyqtSlot, pyqtSignal)

import numpy
import os

# x = json.loads(document_name)

import time
import random
import datetime
import json

from Files import File
from api import Api
import json
# path = "E:\Brain\Self\dev\Latest2022"

state = True

class WorkerSignals(QObject):
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QRunnable):
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot()
    def run(self):
        pass    

class MainWindow(QMainWindow):

    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        uic.loadUi('GUI/mainwindow.ui', self)
        
        self.api = Api()
        self.files = File()
        self.sumbitButton_2.pressed.connect(lambda: self.sumbitText())
        self.exportToText.pressed.connect(lambda: self.exportToTextFile())

    def sumbitText(self):
        self.userInputText.toPlainText()
        userText = str(self.userInputText.toPlainText())
        corrected = self.api.call(userText)
        self.userInputText.setPlainText(corrected.strip())
    
    def exportToTextFile(self):
        fileName = "SavedTextFile/" + str(self.textForFile.toPlainText())
        userText = str(self.userInputText.toPlainText())
        self.files.createTextFile(fileName, userText)

import sys
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
state = False
