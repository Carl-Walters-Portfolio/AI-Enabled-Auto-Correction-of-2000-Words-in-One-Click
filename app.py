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
        
        """change grammar
        
        """
        uic.loadUi('GUI/mainwindow.ui', self)
        
        self.setWindowTitle("AI-Enabled-Auto-Correction-of-2000-Words-in-One-Click")
        
        self.RemoveWhiteSpace = True
        self.removeWhiteSpaceButton.setStyleSheet("background-color: Green")
        
        self.api = Api()
        self.files = File()
        
        self.removeWhiteSpaceButton.pressed.connect(lambda: self.toggleWhiteSpace())

        self.sumbitButton_2.pressed.connect(lambda: self.sumbitText())
        self.sumbitButton_2.setShortcut("Ctrl+f")

        self.exportToText.pressed.connect(lambda: self.exportToTextFile())
        
        self.setAiContextBox()

    def setAiContextBox(self):
        self.aiPromptBox.setPlainText("Correct the spelling and grammar of the following text.")

    
    def toggleWhiteSpace(self):
        if self.RemoveWhiteSpace == False:
            self.RemoveWhiteSpace = True
        elif self.RemoveWhiteSpace == True:
            self.RemoveWhiteSpace = False
            
        if self.RemoveWhiteSpace == False:
            self.removeWhiteSpaceButton.setStyleSheet("background-color: red")
        elif self.RemoveWhiteSpace == True:
            self.removeWhiteSpaceButton.setStyleSheet("background-color: Green")


    def sumbitText(self):
        self.userInputText.toPlainText()
        userText = str(self.userInputText.toPlainText())
        
        aiPromptText = self.aiPromptBox.toPlainText()
        
        correctedText = self.api.call(aiPromptText, userText)
        
        if self.RemoveWhiteSpace == True:
            correctedText = correctedText.strip()

        self.userInputText.setPlainText(correctedText)
        self.copyToClipBoard(correctedText)
        

    def exportToTextFile(self):
        fileName = "SavedTextFile/" + str(self.textForFile.toPlainText())
        userText = str(self.userInputText.toPlainText())
        self.files.createTextFile(fileName, userText)
        
    def copyToClipBoard(self, text):
        QApplication.clipboard().setText(text)


import sys
app = QApplication([])
window = MainWindow()
window.show()
app.exec()
state = False
