# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'window_suministro.ui'
##
## Created by: Qt User Interface Compiler version 6.8.1
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
from PySide6.QtWidgets import (QApplication, QDialog, QFormLayout, QGridLayout,
    QLabel, QLineEdit, QPushButton, QSizePolicy,
    QWidget)

class Ui_Window(object):
    def setupUi(self, Window):
        if not Window.objectName():
            Window.setObjectName(u"Window")
        Window.resize(458, 420)
        Window.setStyleSheet(u"")
        self.gridLayout_2 = QGridLayout(Window)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.formLayout = QFormLayout()
        self.formLayout.setObjectName(u"formLayout")
        self.formLayout.setVerticalSpacing(7)
        self.label = QLabel(Window)
        self.label.setObjectName(u"label")
        font = QFont()
        font.setPointSize(12)
        font.setBold(True)
        self.label.setFont(font)
        self.label.setStyleSheet(u"")

        self.formLayout.setWidget(0, QFormLayout.LabelRole, self.label)

        self.label_2 = QLabel(Window)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setStyleSheet(u"")

        self.formLayout.setWidget(1, QFormLayout.LabelRole, self.label_2)

        self.lineEdit = QLineEdit(Window)
        self.lineEdit.setObjectName(u"lineEdit")
        self.lineEdit.setStyleSheet(u"")

        self.formLayout.setWidget(2, QFormLayout.LabelRole, self.lineEdit)

        self.label_3 = QLabel(Window)
        self.label_3.setObjectName(u"label_3")
        self.label_3.setStyleSheet(u"")

        self.formLayout.setWidget(3, QFormLayout.LabelRole, self.label_3)

        self.lineEdit_2 = QLineEdit(Window)
        self.lineEdit_2.setObjectName(u"lineEdit_2")
        self.lineEdit_2.setStyleSheet(u"")

        self.formLayout.setWidget(4, QFormLayout.LabelRole, self.lineEdit_2)

        self.label_4 = QLabel(Window)
        self.label_4.setObjectName(u"label_4")
        self.label_4.setStyleSheet(u"")

        self.formLayout.setWidget(5, QFormLayout.LabelRole, self.label_4)

        self.lineEdit_3 = QLineEdit(Window)
        self.lineEdit_3.setObjectName(u"lineEdit_3")
        self.lineEdit_3.setStyleSheet(u"")

        self.formLayout.setWidget(6, QFormLayout.LabelRole, self.lineEdit_3)

        self.label_5 = QLabel(Window)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setStyleSheet(u"")

        self.formLayout.setWidget(7, QFormLayout.LabelRole, self.label_5)

        self.lineEdit_4 = QLineEdit(Window)
        self.lineEdit_4.setObjectName(u"lineEdit_4")

        self.formLayout.setWidget(8, QFormLayout.LabelRole, self.lineEdit_4)

        self.pushButton = QPushButton(Window)
        self.pushButton.setObjectName(u"pushButton")
        font1 = QFont()
        font1.setBold(True)
        self.pushButton.setFont(font1)
        self.pushButton.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.formLayout.setWidget(9, QFormLayout.SpanningRole, self.pushButton)


        self.gridLayout_2.addLayout(self.formLayout, 0, 0, 1, 1)


        self.retranslateUi(Window)

        QMetaObject.connectSlotsByName(Window)
    # setupUi

    def retranslateUi(self, Window):
        Window.setWindowTitle(QCoreApplication.translate("Window", u"Dialog", None))
        self.label.setText(QCoreApplication.translate("Window", u"Crear nuevo suministro", None))
        self.label_2.setText(QCoreApplication.translate("Window", u"Nombre:", None))
        self.label_3.setText(QCoreApplication.translate("Window", u"Ubicaci\u00f3n", None))
        self.label_4.setText(QCoreApplication.translate("Window", u"Stock", None))
        self.label_5.setText(QCoreApplication.translate("Window", u"Peso", None))
        self.pushButton.setText(QCoreApplication.translate("Window", u"Crear suministro", None))
    # retranslateUi

