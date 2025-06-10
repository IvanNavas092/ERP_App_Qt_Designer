# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_filtrar.ui'
##
## Created by: Qt User Interface Compiler version 6.8.0
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
from PySide6.QtWidgets import (QApplication, QCheckBox, QDialog, QGridLayout,
    QLabel, QPushButton, QSizePolicy, QWidget)

class Ui_Dialog_F(object):
    def setupUi(self, Dialog):
        if not Dialog.objectName():
            Dialog.setObjectName(u"Dialog")
        Dialog.resize(410, 376)
        self.gridLayout_2 = QGridLayout(Dialog)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.gridLayout = QGridLayout()
        self.gridLayout.setObjectName(u"gridLayout")
        self.checkBox_2 = QCheckBox(Dialog)
        self.checkBox_2.setObjectName(u"checkBox_2")
        self.checkBox_2.setMaximumSize(QSize(16777215, 100))
        font = QFont()
        font.setPointSize(12)
        self.checkBox_2.setFont(font)

        self.gridLayout.addWidget(self.checkBox_2, 2, 0, 1, 1)

        self.label = QLabel(Dialog)
        self.label.setObjectName(u"label")
        font1 = QFont()
        font1.setPointSize(12)
        font1.setBold(True)
        self.label.setFont(font1)

        self.gridLayout.addWidget(self.label, 0, 0, 1, 1)

        self.checkBox_3 = QCheckBox(Dialog)
        self.checkBox_3.setObjectName(u"checkBox_3")
        self.checkBox_3.setMaximumSize(QSize(16777215, 100))
        self.checkBox_3.setFont(font)

        self.gridLayout.addWidget(self.checkBox_3, 1, 0, 1, 1)

        self.checkBox = QCheckBox(Dialog)
        self.checkBox.setObjectName(u"checkBox")
        self.checkBox.setMaximumSize(QSize(16777215, 100))
        self.checkBox.setFont(font)

        self.gridLayout.addWidget(self.checkBox, 3, 0, 1, 1)

        self.pushButton = QPushButton(Dialog)
        self.pushButton.setObjectName(u"pushButton")
        font2 = QFont()
        font2.setBold(True)
        self.pushButton.setFont(font2)
        self.pushButton.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.gridLayout.addWidget(self.pushButton, 4, 0, 1, 1)


        self.gridLayout_2.addLayout(self.gridLayout, 0, 0, 1, 1)


        self.retranslateUi(Dialog)

        QMetaObject.connectSlotsByName(Dialog)
    # setupUi

    def retranslateUi(self, Dialog):
        Dialog.setWindowTitle(QCoreApplication.translate("Dialog", u"Dialog", None))
        self.checkBox_2.setText(QCoreApplication.translate("Dialog", u"Ordenar por n\u00famero de stock", None))
        self.label.setText(QCoreApplication.translate("Dialog", u"Filtrar", None))
        self.checkBox_3.setText(QCoreApplication.translate("Dialog", u"Ordenar alfab\u00e9ticamente (A-Z o Z-A)", None))
        self.checkBox.setText(QCoreApplication.translate("Dialog", u" Ordenar por precio", None))
        self.pushButton.setText(QCoreApplication.translate("Dialog", u"Filtrar", None))
    # retranslateUi

