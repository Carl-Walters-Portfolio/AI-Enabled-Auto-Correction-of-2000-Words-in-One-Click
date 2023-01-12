# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
##
## Created by: Qt User Interface Compiler version 6.3.2
##
## WARNING! All changes made in this file will be lost when recompiling UI file!
################################################################################

from PySide6.QtCore import (QCoreApplication, QDate, QDateTime, QLocale,
    QMetaObject, QObject, QPoint, QRect,
    QSize, QTime, QUrl, Qt)
from PySide6.QtGui import (QBrush, QColor, QConicalGradient, QCursor,
    QFont, QFontDatabase, QGradient, QIcon,
    QImage, QKeySequence, QLinearGradient, QPainter,
    QPalette, QPixmap, QRadialGradient, QTransform)
from PySide6.QtWidgets import (QApplication, QGraphicsView, QLabel, QLineEdit,
    QMainWindow, QPushButton, QSizePolicy, QWidget)

class Ui_controller_text_state(object):
    def setupUi(self, controller_text_state):
        if not controller_text_state.objectName():
            controller_text_state.setObjectName(u"controller_text_state")
        controller_text_state.resize(1728, 986)
        controller_text_state.setToolButtonStyle(Qt.ToolButtonIconOnly)
        controller_text_state.setDockNestingEnabled(True)
        self.centralWidget = QWidget(controller_text_state)
        self.centralWidget.setObjectName(u"centralWidget")
        self.centralWidget.setFocusPolicy(Qt.NoFocus)
        self.centralWidget.setContextMenuPolicy(Qt.DefaultContextMenu)
        self.graphicsView = QGraphicsView(self.centralWidget)
        self.graphicsView.setObjectName(u"graphicsView")
        self.graphicsView.setGeometry(QRect(-50, 0, 2051, 191))
        self.graphicsView.setStyleSheet(u"background-color: rgb(0, 0, 0);")
        self.textWords = QLabel(self.centralWidget)
        self.textWords.setObjectName(u"textWords")
        self.textWords.setGeometry(QRect(810, 10, 561, 111))
        self.textWords.setStyleSheet(u"font: 16pt \"MS Shell Dlg 2\";\n"
"color: rgb(255, 255, 255);")
        self.speedButton = QPushButton(self.centralWidget)
        self.speedButton.setObjectName(u"speedButton")
        self.speedButton.setGeometry(QRect(130, 40, 131, 41))
        self.setSpeed = QLineEdit(self.centralWidget)
        self.setSpeed.setObjectName(u"setSpeed")
        self.setSpeed.setGeometry(QRect(10, 40, 113, 41))
        self.lineButton = QPushButton(self.centralWidget)
        self.lineButton.setObjectName(u"lineButton")
        self.lineButton.setGeometry(QRect(130, 90, 131, 41))
        self.lineInput = QLineEdit(self.centralWidget)
        self.lineInput.setObjectName(u"lineInput")
        self.lineInput.setGeometry(QRect(10, 90, 113, 41))
        self.lineLengthInput = QLineEdit(self.centralWidget)
        self.lineLengthInput.setObjectName(u"lineLengthInput")
        self.lineLengthInput.setGeometry(QRect(10, 140, 113, 41))
        self.lineLengthButton = QPushButton(self.centralWidget)
        self.lineLengthButton.setObjectName(u"lineLengthButton")
        self.lineLengthButton.setGeometry(QRect(130, 140, 131, 41))
        self.pauseButton = QPushButton(self.centralWidget)
        self.pauseButton.setObjectName(u"pauseButton")
        self.pauseButton.setGeometry(QRect(1000, 120, 181, 51))
        font = QFont()
        font.setPointSize(25)
        font.setBold(True)
        self.pauseButton.setFont(font)
        self.betweenWordButton = QPushButton(self.centralWidget)
        self.betweenWordButton.setObjectName(u"betweenWordButton")
        self.betweenWordButton.setGeometry(QRect(390, 40, 131, 41))
        self.betweenWordInput = QLineEdit(self.centralWidget)
        self.betweenWordInput.setObjectName(u"betweenWordInput")
        self.betweenWordInput.setGeometry(QRect(270, 40, 113, 41))
        controller_text_state.setCentralWidget(self.centralWidget)

        self.retranslateUi(controller_text_state)

        QMetaObject.connectSlotsByName(controller_text_state)
    # setupUi

    def retranslateUi(self, controller_text_state):
        controller_text_state.setWindowTitle(QCoreApplication.translate("controller_text_state", u"MainWindow", None))
        self.textWords.setText(QCoreApplication.translate("controller_text_state", u"<html><head/><body><p align=\"center\">peaker and best selling author of</p></body></html>", None))
        self.speedButton.setText(QCoreApplication.translate("controller_text_state", u"Speed", None))
        self.lineButton.setText(QCoreApplication.translate("controller_text_state", u"Per Line", None))
        self.lineLengthButton.setText(QCoreApplication.translate("controller_text_state", u"Line Length", None))
        self.pauseButton.setText(QCoreApplication.translate("controller_text_state", u"Pause", None))
        self.betweenWordButton.setText(QCoreApplication.translate("controller_text_state", u"Between word", None))
    # retranslateUi

