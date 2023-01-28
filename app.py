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
    """ 
    defines and emit signals for a worker thread.
    Args:
        QObject cointains signals
    """
    finished = pyqtSignal()
    error = pyqtSignal(tuple)
    result = pyqtSignal(object)
    progress = pyqtSignal(int)

class Worker(QRunnable):
    """
    Provides event handling for multiple signals to be handled this class is not 
    currently being utilised but would be useful to have from the beginning in anticipation 
    for more complex features.

    Args:
        QRunnable: helps manage a pool of worker threads 
    """
    def __init__(self, fn, *args, **kwargs):
        super(Worker, self).__init__()
        self.fn = fn
        self.args = args
        self.kwargs = kwargs
        self.signals = WorkerSignals()

    @pyqtSlot() 
    def run(self):
        """can be used for multithreading"""   

class MainWindow(QMainWindow):
    """
    MainWindow contains logic that enables and controls various elements within the GUI 
    """
    def __init__(self, *args, **kwargs):
        super(MainWindow, self).__init__(*args, **kwargs)
        
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
        """
        Set weather the return later presented to the user has white space.
        """
        if self.RemoveWhiteSpace == False:
            self.RemoveWhiteSpace = True
        elif self.RemoveWhiteSpace == True:
            self.RemoveWhiteSpace = False
            
        if self.RemoveWhiteSpace == False:
            self.removeWhiteSpaceButton.setStyleSheet("background-color: red")
        elif self.RemoveWhiteSpace == True:
            self.removeWhiteSpaceButton.setStyleSheet("background-color: Green")


    def sumbitText(self):
        """
        After the submit button has been pressed userText is assigned the text users input 
        text and aiPromptText Is set to the Ai prompt text
        """
        self.userInputText.toPlainText()
        aiPromptText = self.aiPromptBox.toPlainText()

        userText = str(self.userInputText.toPlainText())
        
        correctedText = self.api.call(aiPromptText, userText)
        
        if self.RemoveWhiteSpace == True:
            correctedText = correctedText.strip()

        self.userInputText.setPlainText(correctedText)
        self.copyToClipBoard(correctedText)
        

    def exportToTextFile(self):
        """
        The Ai output can be exported to a text document by pressing the export button.
        """
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
