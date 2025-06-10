# -*- coding: utf-8 -*-

################################################################################
## Form generated from reading UI file 'mainwindow.ui'
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
from PySide6.QtWidgets import (QAbstractItemView, QAbstractScrollArea, QApplication, QCalendarWidget,
    QComboBox, QFormLayout, QFrame, QGridLayout,
    QHBoxLayout, QHeaderView, QLabel, QLineEdit,
    QMainWindow, QProgressBar, QPushButton, QScrollArea,
    QSizePolicy, QTabWidget, QTableWidget, QTableWidgetItem,
    QVBoxLayout, QWidget)

class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        if not MainWindow.objectName():
            MainWindow.setObjectName(u"MainWindow")
        MainWindow.resize(1065, 697)
        MainWindow.setStyleSheet(u"")
        self.centralwidget = QWidget(MainWindow)
        self.centralwidget.setObjectName(u"centralwidget")
        self.gridLayout_2 = QGridLayout(self.centralwidget)
        self.gridLayout_2.setObjectName(u"gridLayout_2")
        self.main_body = QGridLayout()
        self.main_body.setObjectName(u"main_body")
        self.MENU_LATERAL = QFrame(self.centralwidget)
        self.MENU_LATERAL.setObjectName(u"MENU_LATERAL")
        sizePolicy = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Preferred)
        sizePolicy.setHorizontalStretch(0)
        sizePolicy.setVerticalStretch(0)
        sizePolicy.setHeightForWidth(self.MENU_LATERAL.sizePolicy().hasHeightForWidth())
        self.MENU_LATERAL.setSizePolicy(sizePolicy)
        self.MENU_LATERAL.setMaximumSize(QSize(90, 16777215))
        self.MENU_LATERAL.setStyleSheet(u" background-color: #434343")
        self.MENU_LATERAL.setFrameShape(QFrame.Shape.StyledPanel)
        self.MENU_LATERAL.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout = QGridLayout(self.MENU_LATERAL)
        self.gridLayout.setObjectName(u"gridLayout")
        self.verticalLayout_2 = QVBoxLayout()
        self.verticalLayout_2.setSpacing(50)
        self.verticalLayout_2.setObjectName(u"verticalLayout_2")
        self.pushButton_3 = QPushButton(self.MENU_LATERAL)
        self.pushButton_3.setObjectName(u"pushButton_3")
        icon = QIcon()
        icon.addFile(u"icons/menu_1_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_3.setIcon(icon)
        self.pushButton_3.setIconSize(QSize(30, 30))

        self.verticalLayout_2.addWidget(self.pushButton_3)

        self.pushButton_7 = QPushButton(self.MENU_LATERAL)
        self.pushButton_7.setObjectName(u"pushButton_7")
        icon1 = QIcon()
        icon1.addFile(u"icons/menu_2_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_7.setIcon(icon1)
        self.pushButton_7.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_7)

        self.pushButton_6 = QPushButton(self.MENU_LATERAL)
        self.pushButton_6.setObjectName(u"pushButton_6")
        icon2 = QIcon()
        icon2.addFile(u"icons/menu_3_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_6.setIcon(icon2)
        self.pushButton_6.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_6)

        self.pushButton_5 = QPushButton(self.MENU_LATERAL)
        self.pushButton_5.setObjectName(u"pushButton_5")
        icon3 = QIcon()
        icon3.addFile(u"icons/menu_4_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_5.setIcon(icon3)
        self.pushButton_5.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_5)

        self.pushButton_4 = QPushButton(self.MENU_LATERAL)
        self.pushButton_4.setObjectName(u"pushButton_4")
        icon4 = QIcon()
        icon4.addFile(u"icons/menu_5_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_4.setIcon(icon4)
        self.pushButton_4.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_4)

        self.pushButton_2 = QPushButton(self.MENU_LATERAL)
        self.pushButton_2.setObjectName(u"pushButton_2")
        icon5 = QIcon()
        icon5.addFile(u"icons/menu_6_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_2.setIcon(icon5)
        self.pushButton_2.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton_2)

        self.pushButton = QPushButton(self.MENU_LATERAL)
        self.pushButton.setObjectName(u"pushButton")
        icon6 = QIcon()
        icon6.addFile(u"icons/menu_7_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton.setIcon(icon6)
        self.pushButton.setIconSize(QSize(32, 32))

        self.verticalLayout_2.addWidget(self.pushButton)


        self.gridLayout.addLayout(self.verticalLayout_2, 0, 0, 1, 1)


        self.main_body.addWidget(self.MENU_LATERAL, 1, 0, 1, 1)

        self.MENU_SUPERIOR = QFrame(self.centralwidget)
        self.MENU_SUPERIOR.setObjectName(u"MENU_SUPERIOR")
        sizePolicy1 = QSizePolicy(QSizePolicy.Policy.Preferred, QSizePolicy.Policy.Fixed)
        sizePolicy1.setHorizontalStretch(0)
        sizePolicy1.setVerticalStretch(0)
        sizePolicy1.setHeightForWidth(self.MENU_SUPERIOR.sizePolicy().hasHeightForWidth())
        self.MENU_SUPERIOR.setSizePolicy(sizePolicy1)
        self.MENU_SUPERIOR.setMinimumSize(QSize(0, 50))
        self.MENU_SUPERIOR.setMaximumSize(QSize(16777215, 16777215))
        self.MENU_SUPERIOR.setStyleSheet(u" background-color: #23acf9")
        self.MENU_SUPERIOR.setFrameShape(QFrame.Shape.StyledPanel)
        self.MENU_SUPERIOR.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_6 = QGridLayout(self.MENU_SUPERIOR)
        self.gridLayout_6.setObjectName(u"gridLayout_6")
        self.horizontalLayout = QHBoxLayout()
        self.horizontalLayout.setObjectName(u"horizontalLayout")
        self.label = QLabel(self.MENU_SUPERIOR)
        self.label.setObjectName(u"label")

        self.horizontalLayout.addWidget(self.label)

        self.comboBox = QComboBox(self.MENU_SUPERIOR)
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.addItem("")
        self.comboBox.setObjectName(u"comboBox")
        sizePolicy1.setHeightForWidth(self.comboBox.sizePolicy().hasHeightForWidth())
        self.comboBox.setSizePolicy(sizePolicy1)

        self.horizontalLayout.addWidget(self.comboBox)


        self.gridLayout_6.addLayout(self.horizontalLayout, 0, 0, 1, 1)

        self.horizontalLayout_2 = QHBoxLayout()
        self.horizontalLayout_2.setObjectName(u"horizontalLayout_2")
        self.horizontalLayout_2.setContentsMargins(100, -1, 0, -1)
        self.pushButton_9 = QPushButton(self.MENU_SUPERIOR)
        self.pushButton_9.setObjectName(u"pushButton_9")
        self.pushButton_9.setMaximumSize(QSize(100, 16777215))
        icon7 = QIcon()
        icon7.addFile(u"icons/settings_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_9.setIcon(icon7)

        self.horizontalLayout_2.addWidget(self.pushButton_9)

        self.pushButton_10 = QPushButton(self.MENU_SUPERIOR)
        self.pushButton_10.setObjectName(u"pushButton_10")
        self.pushButton_10.setMaximumSize(QSize(100, 16777215))
        icon8 = QIcon()
        icon8.addFile(u"icons/notification_button.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        self.pushButton_10.setIcon(icon8)

        self.horizontalLayout_2.addWidget(self.pushButton_10)

        self.pushButton_8 = QPushButton(self.MENU_SUPERIOR)
        self.pushButton_8.setObjectName(u"pushButton_8")
        self.pushButton_8.setMinimumSize(QSize(30, 30))
        self.pushButton_8.setMaximumSize(QSize(30, 30))
        self.pushButton_8.setStyleSheet(u"border-style: solid;\n"
"border-width: 1px;\n"
"color: rgb(255, 255, 255);\n"
"border-radius: 13px;")

        self.horizontalLayout_2.addWidget(self.pushButton_8)


        self.gridLayout_6.addLayout(self.horizontalLayout_2, 0, 1, 1, 1)


        self.main_body.addWidget(self.MENU_SUPERIOR, 0, 0, 1, 2)

        self.contenido = QFrame(self.centralwidget)
        self.contenido.setObjectName(u"contenido")
        self.contenido.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.contenido.setFrameShape(QFrame.Shape.StyledPanel)
        self.contenido.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_7 = QGridLayout(self.contenido)
        self.gridLayout_7.setObjectName(u"gridLayout_7")
        self.gridLayout_4 = QGridLayout()
        self.gridLayout_4.setObjectName(u"gridLayout_4")
        self.tabWidget = QTabWidget(self.contenido)
        self.tabWidget.setObjectName(u"tabWidget")
        self.tabWidget.setMinimumSize(QSize(30, 30))
        font = QFont()
        font.setBold(True)
        self.tabWidget.setFont(font)
        self.login = QWidget()
        self.login.setObjectName(u"login")
        self.gridLayout_5 = QGridLayout(self.login)
        self.gridLayout_5.setObjectName(u"gridLayout_5")
        self.frame = QFrame(self.login)
        self.frame.setObjectName(u"frame")
        self.frame.setMaximumSize(QSize(399, 300))
        self.frame.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_3 = QVBoxLayout(self.frame)
        self.verticalLayout_3.setObjectName(u"verticalLayout_3")
        self.gridLayout_3 = QGridLayout()
        self.gridLayout_3.setObjectName(u"gridLayout_3")
        self.lineEdit = QLineEdit(self.frame)
        self.lineEdit.setObjectName(u"lineEdit")

        self.gridLayout_3.addWidget(self.lineEdit, 2, 0, 1, 1)

        self.id_label = QLabel(self.frame)
        self.id_label.setObjectName(u"id_label")
        font1 = QFont()
        font1.setFamilies([u"Segoe UI"])
        font1.setBold(True)
        self.id_label.setFont(font1)
        self.id_label.setStyleSheet(u"")
        self.id_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.id_label, 1, 0, 1, 1)

        self.pass_label = QLabel(self.frame)
        self.pass_label.setObjectName(u"pass_label")
        self.pass_label.setFont(font1)
        self.pass_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.pass_label, 5, 0, 1, 1)

        self.Tit = QLabel(self.frame)
        self.Tit.setObjectName(u"Tit")
        font2 = QFont()
        font2.setFamilies([u"Segoe UI"])
        font2.setPointSize(11)
        font2.setBold(True)
        font2.setItalic(False)
        self.Tit.setFont(font2)
        self.Tit.setStyleSheet(u"")
        self.Tit.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.Tit, 0, 0, 1, 1)

        self.user_label = QLabel(self.frame)
        self.user_label.setObjectName(u"user_label")
        self.user_label.setFont(font1)
        self.user_label.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_3.addWidget(self.user_label, 3, 0, 1, 1)

        self.lineEdit_3 = QLineEdit(self.frame)
        self.lineEdit_3.setObjectName(u"lineEdit_3")

        self.gridLayout_3.addWidget(self.lineEdit_3, 6, 0, 1, 1)

        self.lineEdit_2 = QLineEdit(self.frame)
        self.lineEdit_2.setObjectName(u"lineEdit_2")

        self.gridLayout_3.addWidget(self.lineEdit_2, 4, 0, 1, 1)


        self.verticalLayout_3.addLayout(self.gridLayout_3)

        self.entry_button = QPushButton(self.frame)
        self.entry_button.setObjectName(u"entry_button")
        self.entry_button.setFont(font1)

        self.verticalLayout_3.addWidget(self.entry_button)


        self.gridLayout_5.addWidget(self.frame, 0, 0, 1, 1)

        self.tabWidget.addTab(self.login, "")
        self.enter_data = QWidget()
        self.enter_data.setObjectName(u"enter_data")
        self.gridLayout_71 = QGridLayout(self.enter_data)
        self.gridLayout_71.setObjectName(u"gridLayout_71")
        self.frame_20 = QFrame(self.enter_data)
        self.frame_20.setObjectName(u"frame_20")
        self.frame_20.setMaximumSize(QSize(399, 300))
        self.frame_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_20.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_17 = QVBoxLayout(self.frame_20)
        self.verticalLayout_17.setObjectName(u"verticalLayout_17")
        self.descargar_documentacion = QPushButton(self.frame_20)
        self.descargar_documentacion.setObjectName(u"descargar_documentacion")
        self.descargar_documentacion.setMaximumSize(QSize(16777215, 30))
        self.descargar_documentacion.setFont(font)
        self.descargar_documentacion.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")
        icon9 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.Printer))
        self.descargar_documentacion.setIcon(icon9)

        self.verticalLayout_17.addWidget(self.descargar_documentacion)

        self.boton_subir_archivo = QPushButton(self.frame_20)
        self.boton_subir_archivo.setObjectName(u"boton_subir_archivo")
        self.boton_subir_archivo.setMaximumSize(QSize(16777215, 30))
        self.boton_subir_archivo.setFont(font1)
        self.boton_subir_archivo.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")
        icon10 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.DocumentOpen))
        self.boton_subir_archivo.setIcon(icon10)

        self.verticalLayout_17.addWidget(self.boton_subir_archivo)


        self.gridLayout_71.addWidget(self.frame_20, 0, 0, 1, 1)

        self.tabWidget.addTab(self.enter_data, "")
        self.Home = QWidget()
        self.Home.setObjectName(u"Home")
        self.gridLayout_9 = QGridLayout(self.Home)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.GRID = QGridLayout()
        self.GRID.setObjectName(u"GRID")
        self.frame_3 = QFrame(self.Home)
        self.frame_3.setObjectName(u"frame_3")
        self.frame_3.setMaximumSize(QSize(300, 16777215))
        self.frame_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_12 = QGridLayout(self.frame_3)
        self.gridLayout_12.setObjectName(u"gridLayout_12")
        self.gridLayout_11 = QGridLayout()
        self.gridLayout_11.setObjectName(u"gridLayout_11")
        self.pushButton_11 = QPushButton(self.frame_3)
        self.pushButton_11.setObjectName(u"pushButton_11")

        self.gridLayout_11.addWidget(self.pushButton_11, 3, 0, 1, 1)

        self.label_2 = QLabel(self.frame_3)
        self.label_2.setObjectName(u"label_2")
        self.label_2.setFont(font)
        self.label_2.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_11.addWidget(self.label_2, 0, 0, 1, 1)

        self.label_3 = QLabel(self.frame_3)
        self.label_3.setObjectName(u"label_3")
        font3 = QFont()
        font3.setPointSize(20)
        font3.setBold(True)
        self.label_3.setFont(font3)
        self.label_3.setStyleSheet(u"color:green;")
        self.label_3.setTextFormat(Qt.TextFormat.AutoText)
        self.label_3.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)
        self.label_3.setMargin(0)

        self.gridLayout_11.addWidget(self.label_3, 1, 0, 1, 1)


        self.gridLayout_12.addLayout(self.gridLayout_11, 0, 0, 1, 1)


        self.GRID.addWidget(self.frame_3, 1, 0, 1, 1)

        self.graphic = QFrame(self.Home)
        self.graphic.setObjectName(u"graphic")
        self.graphic.setFrameShape(QFrame.Shape.StyledPanel)
        self.graphic.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.graphic)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.grid_graphic = QGridLayout()
        self.grid_graphic.setObjectName(u"grid_graphic")

        self.gridLayout_14.addLayout(self.grid_graphic, 0, 0, 1, 1)


        self.GRID.addWidget(self.graphic, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.Home)
        self.frame_4.setObjectName(u"frame_4")
        self.frame_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_10 = QGridLayout(self.frame_4)
        self.gridLayout_10.setObjectName(u"gridLayout_10")
        self.gridLayout_8 = QGridLayout()
        self.gridLayout_8.setObjectName(u"gridLayout_8")
        self.calendarWidget = QCalendarWidget(self.frame_4)
        self.calendarWidget.setObjectName(u"calendarWidget")

        self.gridLayout_8.addWidget(self.calendarWidget, 0, 0, 1, 1)


        self.gridLayout_10.addLayout(self.gridLayout_8, 0, 0, 1, 1)


        self.GRID.addWidget(self.frame_4, 0, 0, 1, 2)

        self.GRID.setRowStretch(0, 1)
        self.GRID.setRowStretch(1, 1)
        self.GRID.setColumnStretch(0, 1)
        self.GRID.setColumnStretch(1, 1)

        self.gridLayout_9.addLayout(self.GRID, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Home, "")
        self.Inventory = QWidget()
        self.Inventory.setObjectName(u"Inventory")
        self.gridLayout_15 = QGridLayout(self.Inventory)
        self.gridLayout_15.setObjectName(u"gridLayout_15")
        self.gridLayout_13 = QGridLayout()
        self.gridLayout_13.setObjectName(u"gridLayout_13")
        self.frame_2 = QFrame(self.Inventory)
        self.frame_2.setObjectName(u"frame_2")
        self.frame_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_19 = QGridLayout(self.frame_2)
        self.gridLayout_19.setObjectName(u"gridLayout_19")
        self.gridLayout_18 = QGridLayout()
        self.gridLayout_18.setObjectName(u"gridLayout_18")
        self.scrollArea_3 = QScrollArea(self.frame_2)
        self.scrollArea_3.setObjectName(u"scrollArea_3")
        self.scrollArea_3.setWidgetResizable(True)
        self.scrollAreaWidgetContents = QWidget()
        self.scrollAreaWidgetContents.setObjectName(u"scrollAreaWidgetContents")
        self.scrollAreaWidgetContents.setGeometry(QRect(0, 0, 881, 436))
        self.gridLayout_41 = QGridLayout(self.scrollAreaWidgetContents)
        self.gridLayout_41.setObjectName(u"gridLayout_41")
        self.tableWidget = QTableWidget(self.scrollAreaWidgetContents)
        if (self.tableWidget.columnCount() < 7):
            self.tableWidget.setColumnCount(7)
        __qtablewidgetitem = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(0, __qtablewidgetitem)
        __qtablewidgetitem1 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(1, __qtablewidgetitem1)
        __qtablewidgetitem2 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(2, __qtablewidgetitem2)
        __qtablewidgetitem3 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(3, __qtablewidgetitem3)
        __qtablewidgetitem4 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(4, __qtablewidgetitem4)
        __qtablewidgetitem5 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(5, __qtablewidgetitem5)
        __qtablewidgetitem6 = QTableWidgetItem()
        self.tableWidget.setHorizontalHeaderItem(6, __qtablewidgetitem6)
        if (self.tableWidget.rowCount() < 20):
            self.tableWidget.setRowCount(20)
        __qtablewidgetitem7 = QTableWidgetItem()
        self.tableWidget.setItem(0, 0, __qtablewidgetitem7)
        __qtablewidgetitem8 = QTableWidgetItem()
        self.tableWidget.setItem(0, 1, __qtablewidgetitem8)
        __qtablewidgetitem9 = QTableWidgetItem()
        self.tableWidget.setItem(0, 2, __qtablewidgetitem9)
        __qtablewidgetitem10 = QTableWidgetItem()
        self.tableWidget.setItem(0, 3, __qtablewidgetitem10)
        __qtablewidgetitem11 = QTableWidgetItem()
        self.tableWidget.setItem(0, 4, __qtablewidgetitem11)
        icon11 = QIcon()
        if QIcon.hasThemeIcon(QIcon.ThemeIcon.SyncSynchronizing):
            icon11 = QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing)
        else:
            icon11.addFile(u"icons/icons8-automation-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)

        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setIcon(icon11);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem12)
        icon12 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.MailReplied))
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setIcon(icon12);
        self.tableWidget.setItem(0, 6, __qtablewidgetitem13)
        __qtablewidgetitem14 = QTableWidgetItem()
        self.tableWidget.setItem(1, 0, __qtablewidgetitem14)
        __qtablewidgetitem15 = QTableWidgetItem()
        self.tableWidget.setItem(1, 1, __qtablewidgetitem15)
        __qtablewidgetitem16 = QTableWidgetItem()
        self.tableWidget.setItem(1, 2, __qtablewidgetitem16)
        __qtablewidgetitem17 = QTableWidgetItem()
        self.tableWidget.setItem(1, 3, __qtablewidgetitem17)
        __qtablewidgetitem18 = QTableWidgetItem()
        self.tableWidget.setItem(1, 4, __qtablewidgetitem18)
        icon13 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.SyncSynchronizing))
        __qtablewidgetitem19 = QTableWidgetItem()
        __qtablewidgetitem19.setIcon(icon13);
        self.tableWidget.setItem(1, 5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
        __qtablewidgetitem20.setIcon(icon12);
        self.tableWidget.setItem(1, 6, __qtablewidgetitem20)
        __qtablewidgetitem21 = QTableWidgetItem()
        self.tableWidget.setItem(2, 0, __qtablewidgetitem21)
        __qtablewidgetitem22 = QTableWidgetItem()
        self.tableWidget.setItem(2, 1, __qtablewidgetitem22)
        __qtablewidgetitem23 = QTableWidgetItem()
        self.tableWidget.setItem(2, 2, __qtablewidgetitem23)
        __qtablewidgetitem24 = QTableWidgetItem()
        self.tableWidget.setItem(2, 3, __qtablewidgetitem24)
        __qtablewidgetitem25 = QTableWidgetItem()
        self.tableWidget.setItem(2, 4, __qtablewidgetitem25)
        __qtablewidgetitem26 = QTableWidgetItem()
        __qtablewidgetitem26.setIcon(icon13);
        self.tableWidget.setItem(2, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
        __qtablewidgetitem27.setIcon(icon12);
        self.tableWidget.setItem(2, 6, __qtablewidgetitem27)
        __qtablewidgetitem28 = QTableWidgetItem()
        self.tableWidget.setItem(3, 0, __qtablewidgetitem28)
        __qtablewidgetitem29 = QTableWidgetItem()
        self.tableWidget.setItem(3, 1, __qtablewidgetitem29)
        __qtablewidgetitem30 = QTableWidgetItem()
        self.tableWidget.setItem(3, 2, __qtablewidgetitem30)
        __qtablewidgetitem31 = QTableWidgetItem()
        self.tableWidget.setItem(3, 3, __qtablewidgetitem31)
        __qtablewidgetitem32 = QTableWidgetItem()
        self.tableWidget.setItem(3, 4, __qtablewidgetitem32)
        __qtablewidgetitem33 = QTableWidgetItem()
        __qtablewidgetitem33.setIcon(icon13);
        self.tableWidget.setItem(3, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
        __qtablewidgetitem34.setIcon(icon12);
        self.tableWidget.setItem(3, 6, __qtablewidgetitem34)
        __qtablewidgetitem35 = QTableWidgetItem()
        self.tableWidget.setItem(4, 0, __qtablewidgetitem35)
        __qtablewidgetitem36 = QTableWidgetItem()
        self.tableWidget.setItem(4, 1, __qtablewidgetitem36)
        __qtablewidgetitem37 = QTableWidgetItem()
        self.tableWidget.setItem(4, 2, __qtablewidgetitem37)
        __qtablewidgetitem38 = QTableWidgetItem()
        self.tableWidget.setItem(4, 3, __qtablewidgetitem38)
        __qtablewidgetitem39 = QTableWidgetItem()
        self.tableWidget.setItem(4, 4, __qtablewidgetitem39)
        __qtablewidgetitem40 = QTableWidgetItem()
        __qtablewidgetitem40.setIcon(icon13);
        self.tableWidget.setItem(4, 5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
        __qtablewidgetitem41.setIcon(icon12);
        self.tableWidget.setItem(4, 6, __qtablewidgetitem41)
        __qtablewidgetitem42 = QTableWidgetItem()
        self.tableWidget.setItem(5, 0, __qtablewidgetitem42)
        __qtablewidgetitem43 = QTableWidgetItem()
        self.tableWidget.setItem(5, 1, __qtablewidgetitem43)
        __qtablewidgetitem44 = QTableWidgetItem()
        self.tableWidget.setItem(5, 2, __qtablewidgetitem44)
        __qtablewidgetitem45 = QTableWidgetItem()
        self.tableWidget.setItem(5, 3, __qtablewidgetitem45)
        __qtablewidgetitem46 = QTableWidgetItem()
        self.tableWidget.setItem(5, 4, __qtablewidgetitem46)
        __qtablewidgetitem47 = QTableWidgetItem()
        __qtablewidgetitem47.setIcon(icon13);
        self.tableWidget.setItem(5, 5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
        __qtablewidgetitem48.setIcon(icon12);
        self.tableWidget.setItem(5, 6, __qtablewidgetitem48)
        __qtablewidgetitem49 = QTableWidgetItem()
        self.tableWidget.setItem(6, 0, __qtablewidgetitem49)
        __qtablewidgetitem50 = QTableWidgetItem()
        self.tableWidget.setItem(6, 1, __qtablewidgetitem50)
        __qtablewidgetitem51 = QTableWidgetItem()
        self.tableWidget.setItem(6, 2, __qtablewidgetitem51)
        __qtablewidgetitem52 = QTableWidgetItem()
        self.tableWidget.setItem(6, 3, __qtablewidgetitem52)
        __qtablewidgetitem53 = QTableWidgetItem()
        self.tableWidget.setItem(6, 4, __qtablewidgetitem53)
        __qtablewidgetitem54 = QTableWidgetItem()
        __qtablewidgetitem54.setIcon(icon13);
        self.tableWidget.setItem(6, 5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
        __qtablewidgetitem55.setIcon(icon12);
        self.tableWidget.setItem(6, 6, __qtablewidgetitem55)
        __qtablewidgetitem56 = QTableWidgetItem()
        self.tableWidget.setItem(7, 0, __qtablewidgetitem56)
        __qtablewidgetitem57 = QTableWidgetItem()
        self.tableWidget.setItem(7, 1, __qtablewidgetitem57)
        __qtablewidgetitem58 = QTableWidgetItem()
        self.tableWidget.setItem(7, 2, __qtablewidgetitem58)
        __qtablewidgetitem59 = QTableWidgetItem()
        self.tableWidget.setItem(7, 3, __qtablewidgetitem59)
        __qtablewidgetitem60 = QTableWidgetItem()
        self.tableWidget.setItem(7, 4, __qtablewidgetitem60)
        __qtablewidgetitem61 = QTableWidgetItem()
        __qtablewidgetitem61.setIcon(icon13);
        self.tableWidget.setItem(7, 5, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
        __qtablewidgetitem62.setIcon(icon12);
        self.tableWidget.setItem(7, 6, __qtablewidgetitem62)
        __qtablewidgetitem63 = QTableWidgetItem()
        self.tableWidget.setItem(8, 0, __qtablewidgetitem63)
        __qtablewidgetitem64 = QTableWidgetItem()
        self.tableWidget.setItem(8, 1, __qtablewidgetitem64)
        __qtablewidgetitem65 = QTableWidgetItem()
        self.tableWidget.setItem(8, 2, __qtablewidgetitem65)
        __qtablewidgetitem66 = QTableWidgetItem()
        self.tableWidget.setItem(8, 3, __qtablewidgetitem66)
        __qtablewidgetitem67 = QTableWidgetItem()
        self.tableWidget.setItem(8, 4, __qtablewidgetitem67)
        __qtablewidgetitem68 = QTableWidgetItem()
        __qtablewidgetitem68.setIcon(icon13);
        self.tableWidget.setItem(8, 5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
        __qtablewidgetitem69.setIcon(icon12);
        self.tableWidget.setItem(8, 6, __qtablewidgetitem69)
        __qtablewidgetitem70 = QTableWidgetItem()
        self.tableWidget.setItem(9, 0, __qtablewidgetitem70)
        __qtablewidgetitem71 = QTableWidgetItem()
        self.tableWidget.setItem(9, 1, __qtablewidgetitem71)
        __qtablewidgetitem72 = QTableWidgetItem()
        self.tableWidget.setItem(9, 2, __qtablewidgetitem72)
        __qtablewidgetitem73 = QTableWidgetItem()
        self.tableWidget.setItem(9, 3, __qtablewidgetitem73)
        __qtablewidgetitem74 = QTableWidgetItem()
        self.tableWidget.setItem(9, 4, __qtablewidgetitem74)
        __qtablewidgetitem75 = QTableWidgetItem()
        __qtablewidgetitem75.setIcon(icon13);
        self.tableWidget.setItem(9, 5, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
        __qtablewidgetitem76.setIcon(icon12);
        self.tableWidget.setItem(9, 6, __qtablewidgetitem76)
        __qtablewidgetitem77 = QTableWidgetItem()
        self.tableWidget.setItem(10, 0, __qtablewidgetitem77)
        __qtablewidgetitem78 = QTableWidgetItem()
        self.tableWidget.setItem(10, 1, __qtablewidgetitem78)
        __qtablewidgetitem79 = QTableWidgetItem()
        self.tableWidget.setItem(10, 2, __qtablewidgetitem79)
        __qtablewidgetitem80 = QTableWidgetItem()
        self.tableWidget.setItem(10, 3, __qtablewidgetitem80)
        __qtablewidgetitem81 = QTableWidgetItem()
        self.tableWidget.setItem(10, 4, __qtablewidgetitem81)
        __qtablewidgetitem82 = QTableWidgetItem()
        __qtablewidgetitem82.setIcon(icon13);
        self.tableWidget.setItem(10, 5, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
        __qtablewidgetitem83.setIcon(icon12);
        self.tableWidget.setItem(10, 6, __qtablewidgetitem83)
        __qtablewidgetitem84 = QTableWidgetItem()
        self.tableWidget.setItem(11, 0, __qtablewidgetitem84)
        __qtablewidgetitem85 = QTableWidgetItem()
        self.tableWidget.setItem(11, 1, __qtablewidgetitem85)
        __qtablewidgetitem86 = QTableWidgetItem()
        self.tableWidget.setItem(11, 2, __qtablewidgetitem86)
        __qtablewidgetitem87 = QTableWidgetItem()
        self.tableWidget.setItem(11, 3, __qtablewidgetitem87)
        __qtablewidgetitem88 = QTableWidgetItem()
        self.tableWidget.setItem(11, 4, __qtablewidgetitem88)
        __qtablewidgetitem89 = QTableWidgetItem()
        __qtablewidgetitem89.setIcon(icon13);
        self.tableWidget.setItem(11, 5, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
        __qtablewidgetitem90.setIcon(icon12);
        self.tableWidget.setItem(11, 6, __qtablewidgetitem90)
        __qtablewidgetitem91 = QTableWidgetItem()
        self.tableWidget.setItem(12, 0, __qtablewidgetitem91)
        __qtablewidgetitem92 = QTableWidgetItem()
        self.tableWidget.setItem(12, 1, __qtablewidgetitem92)
        __qtablewidgetitem93 = QTableWidgetItem()
        self.tableWidget.setItem(12, 2, __qtablewidgetitem93)
        __qtablewidgetitem94 = QTableWidgetItem()
        self.tableWidget.setItem(12, 3, __qtablewidgetitem94)
        __qtablewidgetitem95 = QTableWidgetItem()
        self.tableWidget.setItem(12, 4, __qtablewidgetitem95)
        __qtablewidgetitem96 = QTableWidgetItem()
        __qtablewidgetitem96.setIcon(icon13);
        self.tableWidget.setItem(12, 5, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
        __qtablewidgetitem97.setIcon(icon12);
        self.tableWidget.setItem(12, 6, __qtablewidgetitem97)
        __qtablewidgetitem98 = QTableWidgetItem()
        self.tableWidget.setItem(13, 0, __qtablewidgetitem98)
        __qtablewidgetitem99 = QTableWidgetItem()
        self.tableWidget.setItem(13, 1, __qtablewidgetitem99)
        __qtablewidgetitem100 = QTableWidgetItem()
        self.tableWidget.setItem(13, 2, __qtablewidgetitem100)
        __qtablewidgetitem101 = QTableWidgetItem()
        self.tableWidget.setItem(13, 3, __qtablewidgetitem101)
        __qtablewidgetitem102 = QTableWidgetItem()
        self.tableWidget.setItem(13, 4, __qtablewidgetitem102)
        __qtablewidgetitem103 = QTableWidgetItem()
        __qtablewidgetitem103.setIcon(icon13);
        self.tableWidget.setItem(13, 5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        __qtablewidgetitem104.setIcon(icon12);
        self.tableWidget.setItem(13, 6, __qtablewidgetitem104)
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget.setItem(14, 0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget.setItem(14, 1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget.setItem(14, 2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget.setItem(14, 3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget.setItem(14, 4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        __qtablewidgetitem110.setIcon(icon13);
        self.tableWidget.setItem(14, 5, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        __qtablewidgetitem111.setIcon(icon12);
        self.tableWidget.setItem(14, 6, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget.setItem(15, 0, __qtablewidgetitem112)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget.setItem(15, 1, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget.setItem(15, 2, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget.setItem(15, 3, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget.setItem(15, 4, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        __qtablewidgetitem117.setIcon(icon13);
        self.tableWidget.setItem(15, 5, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        __qtablewidgetitem118.setIcon(icon12);
        self.tableWidget.setItem(15, 6, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget.setItem(16, 0, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget.setItem(16, 1, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget.setItem(16, 2, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget.setItem(16, 3, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget.setItem(16, 4, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        __qtablewidgetitem124.setIcon(icon13);
        self.tableWidget.setItem(16, 5, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        __qtablewidgetitem125.setIcon(icon12);
        self.tableWidget.setItem(16, 6, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget.setItem(17, 0, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget.setItem(17, 1, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget.setItem(17, 2, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget.setItem(17, 3, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget.setItem(17, 4, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        __qtablewidgetitem131.setIcon(icon13);
        self.tableWidget.setItem(17, 5, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        __qtablewidgetitem132.setIcon(icon12);
        self.tableWidget.setItem(17, 6, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget.setItem(18, 0, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget.setItem(18, 1, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget.setItem(18, 2, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget.setItem(18, 3, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget.setItem(18, 4, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        __qtablewidgetitem138.setIcon(icon13);
        self.tableWidget.setItem(18, 5, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        __qtablewidgetitem139.setIcon(icon12);
        self.tableWidget.setItem(18, 6, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget.setItem(19, 0, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget.setItem(19, 1, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget.setItem(19, 2, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget.setItem(19, 3, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget.setItem(19, 4, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        __qtablewidgetitem145.setIcon(icon13);
        self.tableWidget.setItem(19, 5, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        __qtablewidgetitem146.setIcon(icon12);
        self.tableWidget.setItem(19, 6, __qtablewidgetitem146)
        self.tableWidget.setObjectName(u"tableWidget")
        sizePolicy2 = QSizePolicy(QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Expanding)
        sizePolicy2.setHorizontalStretch(0)
        sizePolicy2.setVerticalStretch(0)
        sizePolicy2.setHeightForWidth(self.tableWidget.sizePolicy().hasHeightForWidth())
        self.tableWidget.setSizePolicy(sizePolicy2)
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setFrameShadow(QFrame.Shadow.Sunken)
        self.tableWidget.setVerticalScrollBarPolicy(Qt.ScrollBarPolicy.ScrollBarAlwaysOn)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(False)
        self.tableWidget.setIconSize(QSize(20, 20))
        self.tableWidget.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget.setShowGrid(True)
        self.tableWidget.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget.setRowCount(20)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_41.addWidget(self.tableWidget, 0, 0, 1, 1)

        self.scrollArea_3.setWidget(self.scrollAreaWidgetContents)

        self.gridLayout_18.addWidget(self.scrollArea_3, 0, 0, 1, 1)


        self.gridLayout_19.addLayout(self.gridLayout_18, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_2, 1, 0, 1, 1)

        self.frame_5 = QFrame(self.Inventory)
        self.frame_5.setObjectName(u"frame_5")
        self.frame_5.setMaximumSize(QSize(16777215, 100))
        self.frame_5.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_5.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_17 = QGridLayout(self.frame_5)
        self.gridLayout_17.setObjectName(u"gridLayout_17")
        self.horizontalLayout_3 = QHBoxLayout()
        self.horizontalLayout_3.setObjectName(u"horizontalLayout_3")
        self.label_4 = QLabel(self.frame_5)
        self.label_4.setObjectName(u"label_4")

        self.horizontalLayout_3.addWidget(self.label_4)

        self.boton_filtrar = QPushButton(self.frame_5)
        self.boton_filtrar.setObjectName(u"boton_filtrar")
        self.boton_filtrar.setMinimumSize(QSize(30, 30))
        self.boton_filtrar.setMaximumSize(QSize(100, 16777215))
        self.boton_filtrar.setFont(font)
        self.boton_filtrar.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_3.addWidget(self.boton_filtrar)

        self.crear_suministro = QPushButton(self.frame_5)
        self.crear_suministro.setObjectName(u"crear_suministro")
        self.crear_suministro.setMinimumSize(QSize(30, 30))
        self.crear_suministro.setMaximumSize(QSize(100, 16777215))
        self.crear_suministro.setFont(font)
        self.crear_suministro.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);")

        self.horizontalLayout_3.addWidget(self.crear_suministro)

        self.crear_informe = QPushButton(self.frame_5)
        self.crear_informe.setObjectName(u"crear_informe")
        self.crear_informe.setMinimumSize(QSize(30, 30))
        self.crear_informe.setMaximumSize(QSize(110, 16777215))
        self.crear_informe.setFont(font)
        self.crear_informe.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);")

        self.horizontalLayout_3.addWidget(self.crear_informe)


        self.gridLayout_17.addLayout(self.horizontalLayout_3, 0, 0, 1, 1)


        self.gridLayout_13.addWidget(self.frame_5, 0, 0, 1, 1)


        self.gridLayout_15.addLayout(self.gridLayout_13, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Inventory, "")
        self.Buys = QWidget()
        self.Buys.setObjectName(u"Buys")
        self.gridLayout_20 = QGridLayout(self.Buys)
        self.gridLayout_20.setObjectName(u"gridLayout_20")
        self.GRID_2 = QGridLayout()
        self.GRID_2.setObjectName(u"GRID_2")
        self.frame_6 = QFrame(self.Buys)
        self.frame_6.setObjectName(u"frame_6")
        self.frame_6.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_6.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout = QFormLayout(self.frame_6)
        self.formLayout.setObjectName(u"formLayout")
        self.gridLayout_16 = QGridLayout()
        self.gridLayout_16.setObjectName(u"gridLayout_16")
        self.frame_8 = QFrame(self.frame_6)
        self.frame_8.setObjectName(u"frame_8")
        self.frame_8.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_8.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_23 = QGridLayout(self.frame_8)
        self.gridLayout_23.setObjectName(u"gridLayout_23")
        self.tableWidget_2 = QTableWidget(self.frame_8)
        if (self.tableWidget_2.columnCount() < 8):
            self.tableWidget_2.setColumnCount(8)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem154)
        if (self.tableWidget_2.rowCount() < 6):
            self.tableWidget_2.setRowCount(6)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem160)
        __qtablewidgetitem161 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem161)
        __qtablewidgetitem162 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem162)
        __qtablewidgetitem163 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem163)
        __qtablewidgetitem164 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem164)
        __qtablewidgetitem165 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem165)
        __qtablewidgetitem166 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, __qtablewidgetitem166)
        __qtablewidgetitem167 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 4, __qtablewidgetitem167)
        __qtablewidgetitem168 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 5, __qtablewidgetitem168)
        __qtablewidgetitem169 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 6, __qtablewidgetitem169)
        __qtablewidgetitem170 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 7, __qtablewidgetitem170)
        __qtablewidgetitem171 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem171)
        __qtablewidgetitem172 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem172)
        __qtablewidgetitem173 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem173)
        __qtablewidgetitem174 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, __qtablewidgetitem174)
        __qtablewidgetitem175 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 4, __qtablewidgetitem175)
        __qtablewidgetitem176 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 5, __qtablewidgetitem176)
        __qtablewidgetitem177 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 6, __qtablewidgetitem177)
        __qtablewidgetitem178 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 7, __qtablewidgetitem178)
        __qtablewidgetitem179 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem179)
        __qtablewidgetitem180 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem180)
        __qtablewidgetitem181 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, __qtablewidgetitem181)
        __qtablewidgetitem182 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 3, __qtablewidgetitem182)
        __qtablewidgetitem183 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 4, __qtablewidgetitem183)
        __qtablewidgetitem184 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 5, __qtablewidgetitem184)
        __qtablewidgetitem185 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 6, __qtablewidgetitem185)
        __qtablewidgetitem186 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 7, __qtablewidgetitem186)
        __qtablewidgetitem187 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem187)
        __qtablewidgetitem188 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem188)
        __qtablewidgetitem189 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, __qtablewidgetitem189)
        __qtablewidgetitem190 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 3, __qtablewidgetitem190)
        __qtablewidgetitem191 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 4, __qtablewidgetitem191)
        __qtablewidgetitem192 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 5, __qtablewidgetitem192)
        __qtablewidgetitem193 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 6, __qtablewidgetitem193)
        __qtablewidgetitem194 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 7, __qtablewidgetitem194)
        __qtablewidgetitem195 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem195)
        __qtablewidgetitem196 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem196)
        __qtablewidgetitem197 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, __qtablewidgetitem197)
        __qtablewidgetitem198 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 3, __qtablewidgetitem198)
        __qtablewidgetitem199 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 4, __qtablewidgetitem199)
        __qtablewidgetitem200 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 5, __qtablewidgetitem200)
        __qtablewidgetitem201 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 6, __qtablewidgetitem201)
        __qtablewidgetitem202 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 7, __qtablewidgetitem202)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_2.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_2.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_2.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_2.setRowCount(6)
        self.tableWidget_2.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_2.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_2.verticalHeader().setVisible(False)

        self.gridLayout_23.addWidget(self.tableWidget_2, 0, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_8, 1, 0, 1, 1)

        self.frame_9 = QFrame(self.frame_6)
        self.frame_9.setObjectName(u"frame_9")
        self.frame_9.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_9.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_24 = QGridLayout(self.frame_9)
        self.gridLayout_24.setObjectName(u"gridLayout_24")
        self.horizontalLayout_5 = QHBoxLayout()
        self.horizontalLayout_5.setObjectName(u"horizontalLayout_5")
        self.frame_10 = QFrame(self.frame_9)
        self.frame_10.setObjectName(u"frame_10")
        self.frame_10.setMaximumSize(QSize(300, 16777215))
        self.frame_10.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_10.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_25 = QGridLayout(self.frame_10)
        self.gridLayout_25.setObjectName(u"gridLayout_25")
        self.gridLayout_22 = QGridLayout()
        self.gridLayout_22.setObjectName(u"gridLayout_22")
        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        font4 = QFont()
        font4.setPointSize(14)
        font4.setBold(True)
        self.label_8.setFont(font4)
        self.label_8.setStyleSheet(u"color: red;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_6.setFont(font5)
        self.label_6.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_22.addWidget(self.label_6, 0, 0, 1, 1)

        self.progressBar = QProgressBar(self.frame_10)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_22.addWidget(self.progressBar, 3, 0, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        font6 = QFont()
        font6.setPointSize(18)
        font6.setBold(True)
        self.label_7.setFont(font6)
        self.label_7.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.label_7, 1, 0, 1, 1)


        self.gridLayout_25.addLayout(self.gridLayout_22, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_10)

        self.frame_lineal = QFrame(self.frame_9)
        self.frame_lineal.setObjectName(u"frame_lineal")
        self.frame_lineal.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_lineal.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_27 = QGridLayout(self.frame_lineal)
        self.gridLayout_27.setObjectName(u"gridLayout_27")
        self.GRID_3 = QGridLayout()
        self.GRID_3.setObjectName(u"GRID_3")
        self.GRID_7 = QGridLayout()
        self.GRID_7.setObjectName(u"GRID_7")

        self.GRID_3.addLayout(self.GRID_7, 0, 0, 1, 1)


        self.gridLayout_27.addLayout(self.GRID_3, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_lineal)


        self.gridLayout_24.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_9, 0, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_16)


        self.GRID_2.addWidget(self.frame_6, 1, 0, 1, 1)

        self.frame_7 = QFrame(self.Buys)
        self.frame_7.setObjectName(u"frame_7")
        self.frame_7.setMaximumSize(QSize(16777215, 100))
        self.frame_7.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_7.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_21 = QGridLayout(self.frame_7)
        self.gridLayout_21.setObjectName(u"gridLayout_21")
        self.horizontalLayout_4 = QHBoxLayout()
        self.horizontalLayout_4.setObjectName(u"horizontalLayout_4")
        self.label_5 = QLabel(self.frame_7)
        self.label_5.setObjectName(u"label_5")
        self.label_5.setFont(font)

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(200, 100))

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.boton_filtrar_2 = QPushButton(self.frame_7)
        self.boton_filtrar_2.setObjectName(u"boton_filtrar_2")
        self.boton_filtrar_2.setMinimumSize(QSize(30, 30))
        self.boton_filtrar_2.setMaximumSize(QSize(100, 16777215))
        self.boton_filtrar_2.setFont(font)
        self.boton_filtrar_2.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_4.addWidget(self.boton_filtrar_2)

        self.crear_recordatorio = QPushButton(self.frame_7)
        self.crear_recordatorio.setObjectName(u"crear_recordatorio")
        self.crear_recordatorio.setMinimumSize(QSize(30, 30))
        self.crear_recordatorio.setMaximumSize(QSize(150, 16777215))
        self.crear_recordatorio.setFont(font)
        self.crear_recordatorio.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_4.addWidget(self.crear_recordatorio)

        self.crear_informe_2 = QPushButton(self.frame_7)
        self.crear_informe_2.setObjectName(u"crear_informe_2")
        self.crear_informe_2.setMinimumSize(QSize(30, 30))
        self.crear_informe_2.setMaximumSize(QSize(150, 16777215))
        self.crear_informe_2.setFont(font)
        self.crear_informe_2.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_4.addWidget(self.crear_informe_2)


        self.gridLayout_21.addLayout(self.horizontalLayout_4, 0, 0, 1, 1)


        self.GRID_2.addWidget(self.frame_7, 0, 0, 1, 1)


        self.gridLayout_20.addLayout(self.GRID_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Buys, "")
        self.sales = QWidget()
        self.sales.setObjectName(u"sales")
        self.gridLayout_28 = QGridLayout(self.sales)
        self.gridLayout_28.setObjectName(u"gridLayout_28")
        self.gridLayout_26 = QGridLayout()
        self.gridLayout_26.setObjectName(u"gridLayout_26")
        self.frame_12 = QFrame(self.sales)
        self.frame_12.setObjectName(u"frame_12")
        self.frame_12.setMaximumSize(QSize(16777215, 450))
        self.frame_12.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_12.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_32 = QGridLayout(self.frame_12)
        self.gridLayout_32.setObjectName(u"gridLayout_32")
        self.horizontalLayout_6 = QHBoxLayout()
        self.horizontalLayout_6.setSpacing(100)
        self.horizontalLayout_6.setObjectName(u"horizontalLayout_6")
        self.frame_13 = QFrame(self.frame_12)
        self.frame_13.setObjectName(u"frame_13")
        self.frame_13.setMaximumSize(QSize(16777215, 16777215))
        self.frame_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_33 = QGridLayout(self.frame_13)
        self.gridLayout_33.setObjectName(u"gridLayout_33")
        self.gridLayout_29 = QGridLayout()
        self.gridLayout_29.setObjectName(u"gridLayout_29")
        self.tableWidget_3 = QTableWidget(self.frame_13)
        if (self.tableWidget_3.columnCount() < 7):
            self.tableWidget_3.setColumnCount(7)
        __qtablewidgetitem203 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(0, __qtablewidgetitem203)
        __qtablewidgetitem204 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(1, __qtablewidgetitem204)
        __qtablewidgetitem205 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(2, __qtablewidgetitem205)
        __qtablewidgetitem206 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(3, __qtablewidgetitem206)
        __qtablewidgetitem207 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(4, __qtablewidgetitem207)
        __qtablewidgetitem208 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(5, __qtablewidgetitem208)
        __qtablewidgetitem209 = QTableWidgetItem()
        self.tableWidget_3.setHorizontalHeaderItem(6, __qtablewidgetitem209)
        if (self.tableWidget_3.rowCount() < 13):
            self.tableWidget_3.setRowCount(13)
        __qtablewidgetitem210 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 0, __qtablewidgetitem210)
        __qtablewidgetitem211 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 1, __qtablewidgetitem211)
        __qtablewidgetitem212 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 2, __qtablewidgetitem212)
        __qtablewidgetitem213 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 3, __qtablewidgetitem213)
        __qtablewidgetitem214 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 4, __qtablewidgetitem214)
        __qtablewidgetitem215 = QTableWidgetItem()
        self.tableWidget_3.setItem(0, 5, __qtablewidgetitem215)
        __qtablewidgetitem216 = QTableWidgetItem()
        __qtablewidgetitem216.setIcon(icon13);
        self.tableWidget_3.setItem(0, 6, __qtablewidgetitem216)
        __qtablewidgetitem217 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 0, __qtablewidgetitem217)
        __qtablewidgetitem218 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 1, __qtablewidgetitem218)
        __qtablewidgetitem219 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 2, __qtablewidgetitem219)
        __qtablewidgetitem220 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 3, __qtablewidgetitem220)
        __qtablewidgetitem221 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 4, __qtablewidgetitem221)
        __qtablewidgetitem222 = QTableWidgetItem()
        self.tableWidget_3.setItem(1, 5, __qtablewidgetitem222)
        __qtablewidgetitem223 = QTableWidgetItem()
        __qtablewidgetitem223.setIcon(icon13);
        self.tableWidget_3.setItem(1, 6, __qtablewidgetitem223)
        __qtablewidgetitem224 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 0, __qtablewidgetitem224)
        __qtablewidgetitem225 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 1, __qtablewidgetitem225)
        __qtablewidgetitem226 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 2, __qtablewidgetitem226)
        __qtablewidgetitem227 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 3, __qtablewidgetitem227)
        __qtablewidgetitem228 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 4, __qtablewidgetitem228)
        __qtablewidgetitem229 = QTableWidgetItem()
        self.tableWidget_3.setItem(2, 5, __qtablewidgetitem229)
        __qtablewidgetitem230 = QTableWidgetItem()
        __qtablewidgetitem230.setIcon(icon13);
        self.tableWidget_3.setItem(2, 6, __qtablewidgetitem230)
        __qtablewidgetitem231 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 0, __qtablewidgetitem231)
        __qtablewidgetitem232 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 1, __qtablewidgetitem232)
        __qtablewidgetitem233 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 2, __qtablewidgetitem233)
        __qtablewidgetitem234 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 3, __qtablewidgetitem234)
        __qtablewidgetitem235 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 4, __qtablewidgetitem235)
        __qtablewidgetitem236 = QTableWidgetItem()
        self.tableWidget_3.setItem(3, 5, __qtablewidgetitem236)
        __qtablewidgetitem237 = QTableWidgetItem()
        __qtablewidgetitem237.setIcon(icon13);
        self.tableWidget_3.setItem(3, 6, __qtablewidgetitem237)
        __qtablewidgetitem238 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 0, __qtablewidgetitem238)
        __qtablewidgetitem239 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 1, __qtablewidgetitem239)
        __qtablewidgetitem240 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 2, __qtablewidgetitem240)
        __qtablewidgetitem241 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 3, __qtablewidgetitem241)
        __qtablewidgetitem242 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 4, __qtablewidgetitem242)
        __qtablewidgetitem243 = QTableWidgetItem()
        self.tableWidget_3.setItem(4, 5, __qtablewidgetitem243)
        __qtablewidgetitem244 = QTableWidgetItem()
        __qtablewidgetitem244.setIcon(icon13);
        self.tableWidget_3.setItem(4, 6, __qtablewidgetitem244)
        __qtablewidgetitem245 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 0, __qtablewidgetitem245)
        __qtablewidgetitem246 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 1, __qtablewidgetitem246)
        __qtablewidgetitem247 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 2, __qtablewidgetitem247)
        __qtablewidgetitem248 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 3, __qtablewidgetitem248)
        __qtablewidgetitem249 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 4, __qtablewidgetitem249)
        __qtablewidgetitem250 = QTableWidgetItem()
        self.tableWidget_3.setItem(5, 5, __qtablewidgetitem250)
        __qtablewidgetitem251 = QTableWidgetItem()
        __qtablewidgetitem251.setIcon(icon13);
        self.tableWidget_3.setItem(5, 6, __qtablewidgetitem251)
        __qtablewidgetitem252 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 0, __qtablewidgetitem252)
        __qtablewidgetitem253 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 1, __qtablewidgetitem253)
        __qtablewidgetitem254 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 2, __qtablewidgetitem254)
        __qtablewidgetitem255 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 3, __qtablewidgetitem255)
        __qtablewidgetitem256 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 4, __qtablewidgetitem256)
        __qtablewidgetitem257 = QTableWidgetItem()
        self.tableWidget_3.setItem(6, 5, __qtablewidgetitem257)
        __qtablewidgetitem258 = QTableWidgetItem()
        __qtablewidgetitem258.setIcon(icon13);
        self.tableWidget_3.setItem(6, 6, __qtablewidgetitem258)
        __qtablewidgetitem259 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 0, __qtablewidgetitem259)
        __qtablewidgetitem260 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 1, __qtablewidgetitem260)
        __qtablewidgetitem261 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 2, __qtablewidgetitem261)
        __qtablewidgetitem262 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 3, __qtablewidgetitem262)
        __qtablewidgetitem263 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 4, __qtablewidgetitem263)
        __qtablewidgetitem264 = QTableWidgetItem()
        self.tableWidget_3.setItem(7, 5, __qtablewidgetitem264)
        __qtablewidgetitem265 = QTableWidgetItem()
        __qtablewidgetitem265.setIcon(icon13);
        self.tableWidget_3.setItem(7, 6, __qtablewidgetitem265)
        __qtablewidgetitem266 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 0, __qtablewidgetitem266)
        __qtablewidgetitem267 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 1, __qtablewidgetitem267)
        __qtablewidgetitem268 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 2, __qtablewidgetitem268)
        __qtablewidgetitem269 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 3, __qtablewidgetitem269)
        __qtablewidgetitem270 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 4, __qtablewidgetitem270)
        __qtablewidgetitem271 = QTableWidgetItem()
        self.tableWidget_3.setItem(8, 5, __qtablewidgetitem271)
        __qtablewidgetitem272 = QTableWidgetItem()
        __qtablewidgetitem272.setIcon(icon13);
        self.tableWidget_3.setItem(8, 6, __qtablewidgetitem272)
        __qtablewidgetitem273 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 0, __qtablewidgetitem273)
        __qtablewidgetitem274 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 1, __qtablewidgetitem274)
        __qtablewidgetitem275 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 2, __qtablewidgetitem275)
        __qtablewidgetitem276 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 3, __qtablewidgetitem276)
        __qtablewidgetitem277 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 4, __qtablewidgetitem277)
        __qtablewidgetitem278 = QTableWidgetItem()
        self.tableWidget_3.setItem(9, 5, __qtablewidgetitem278)
        __qtablewidgetitem279 = QTableWidgetItem()
        __qtablewidgetitem279.setIcon(icon13);
        self.tableWidget_3.setItem(9, 6, __qtablewidgetitem279)
        __qtablewidgetitem280 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 0, __qtablewidgetitem280)
        __qtablewidgetitem281 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 1, __qtablewidgetitem281)
        __qtablewidgetitem282 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 2, __qtablewidgetitem282)
        __qtablewidgetitem283 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 3, __qtablewidgetitem283)
        __qtablewidgetitem284 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 4, __qtablewidgetitem284)
        __qtablewidgetitem285 = QTableWidgetItem()
        self.tableWidget_3.setItem(10, 5, __qtablewidgetitem285)
        __qtablewidgetitem286 = QTableWidgetItem()
        __qtablewidgetitem286.setIcon(icon13);
        self.tableWidget_3.setItem(10, 6, __qtablewidgetitem286)
        __qtablewidgetitem287 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 0, __qtablewidgetitem287)
        __qtablewidgetitem288 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 1, __qtablewidgetitem288)
        __qtablewidgetitem289 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 2, __qtablewidgetitem289)
        __qtablewidgetitem290 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 3, __qtablewidgetitem290)
        __qtablewidgetitem291 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 4, __qtablewidgetitem291)
        __qtablewidgetitem292 = QTableWidgetItem()
        self.tableWidget_3.setItem(11, 5, __qtablewidgetitem292)
        __qtablewidgetitem293 = QTableWidgetItem()
        __qtablewidgetitem293.setIcon(icon13);
        self.tableWidget_3.setItem(11, 6, __qtablewidgetitem293)
        __qtablewidgetitem294 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 0, __qtablewidgetitem294)
        __qtablewidgetitem295 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 1, __qtablewidgetitem295)
        __qtablewidgetitem296 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 2, __qtablewidgetitem296)
        __qtablewidgetitem297 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 3, __qtablewidgetitem297)
        __qtablewidgetitem298 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 4, __qtablewidgetitem298)
        __qtablewidgetitem299 = QTableWidgetItem()
        self.tableWidget_3.setItem(12, 5, __qtablewidgetitem299)
        __qtablewidgetitem300 = QTableWidgetItem()
        __qtablewidgetitem300.setIcon(icon13);
        self.tableWidget_3.setItem(12, 6, __qtablewidgetitem300)
        self.tableWidget_3.setObjectName(u"tableWidget_3")
        self.tableWidget_3.setSizeIncrement(QSize(0, 0))
        self.tableWidget_3.setFocusPolicy(Qt.FocusPolicy.NoFocus)
        self.tableWidget_3.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_3.setIconSize(QSize(20, 20))
        self.tableWidget_3.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_3.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_3.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget_3.setRowCount(13)
        self.tableWidget_3.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_3.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_3.horizontalHeader().setStretchLastSection(False)
        self.tableWidget_3.verticalHeader().setVisible(False)

        self.gridLayout_29.addWidget(self.tableWidget_3, 0, 0, 1, 1)


        self.gridLayout_33.addLayout(self.gridLayout_29, 0, 0, 1, 1)


        self.horizontalLayout_6.addWidget(self.frame_13)


        self.gridLayout_32.addLayout(self.horizontalLayout_6, 0, 1, 1, 1)


        self.gridLayout_26.addWidget(self.frame_12, 1, 0, 1, 1)

        self.frame_11 = QFrame(self.sales)
        self.frame_11.setObjectName(u"frame_11")
        self.frame_11.setMinimumSize(QSize(100, 100))
        self.frame_11.setMaximumSize(QSize(16777215, 149))
        self.frame_11.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_11.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_30 = QGridLayout(self.frame_11)
        self.gridLayout_30.setObjectName(u"gridLayout_30")
        self.horizontalLayout_7 = QHBoxLayout()
        self.horizontalLayout_7.setObjectName(u"horizontalLayout_7")
        self.label_9 = QLabel(self.frame_11)
        self.label_9.setObjectName(u"label_9")
        self.label_9.setFont(font5)

        self.horizontalLayout_7.addWidget(self.label_9)

        self.lineEdit_5 = QLineEdit(self.frame_11)
        self.lineEdit_5.setObjectName(u"lineEdit_5")
        self.lineEdit_5.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_7.addWidget(self.lineEdit_5)

        self.pushButton_15 = QPushButton(self.frame_11)
        self.pushButton_15.setObjectName(u"pushButton_15")
        self.pushButton_15.setMinimumSize(QSize(30, 30))
        self.pushButton_15.setFont(font)
        self.pushButton_15.setStyleSheet(u"background-color: #23acf9;\n"
"color: green\n"
";\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_7.addWidget(self.pushButton_15)

        self.pushButton_14 = QPushButton(self.frame_11)
        self.pushButton_14.setObjectName(u"pushButton_14")
        self.pushButton_14.setMinimumSize(QSize(30, 30))
        self.pushButton_14.setFont(font)
        self.pushButton_14.setStyleSheet(u"background-color: #23acf9;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_7.addWidget(self.pushButton_14)

        self.pushButton_13 = QPushButton(self.frame_11)
        self.pushButton_13.setObjectName(u"pushButton_13")
        self.pushButton_13.setMinimumSize(QSize(30, 30))
        self.pushButton_13.setFont(font)
        self.pushButton_13.setStyleSheet(u"background-color: #23acf9;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_7.addWidget(self.pushButton_13)

        self.pushButton_12 = QPushButton(self.frame_11)
        self.pushButton_12.setObjectName(u"pushButton_12")
        self.pushButton_12.setMinimumSize(QSize(30, 30))
        self.pushButton_12.setFont(font)
        self.pushButton_12.setStyleSheet(u"background-color: #23acf9;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_7.addWidget(self.pushButton_12)


        self.gridLayout_30.addLayout(self.horizontalLayout_7, 1, 0, 1, 1)


        self.gridLayout_26.addWidget(self.frame_11, 0, 0, 1, 1)


        self.gridLayout_28.addLayout(self.gridLayout_26, 0, 0, 1, 1)

        self.tabWidget.addTab(self.sales, "")
        self.finance = QWidget()
        self.finance.setObjectName(u"finance")
        self.gridLayout_116 = QGridLayout(self.finance)
        self.gridLayout_116.setObjectName(u"gridLayout_116")
        self.GRID_18 = QGridLayout()
        self.GRID_18.setObjectName(u"GRID_18")
        self.frame_40 = QFrame(self.finance)
        self.frame_40.setObjectName(u"frame_40")
        self.frame_40.setMaximumSize(QSize(16777215, 16777215))
        self.frame_40.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_40.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_6 = QFormLayout(self.frame_40)
        self.formLayout_6.setObjectName(u"formLayout_6")
        self.gridLayout_61 = QGridLayout()
        self.gridLayout_61.setObjectName(u"gridLayout_61")
        self.frame_48 = QFrame(self.frame_40)
        self.frame_48.setObjectName(u"frame_48")
        self.frame_48.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_48.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_110 = QGridLayout(self.frame_48)
        self.gridLayout_110.setObjectName(u"gridLayout_110")
        self.tableWidget_12 = QTableWidget(self.frame_48)
        if (self.tableWidget_12.columnCount() < 8):
            self.tableWidget_12.setColumnCount(8)
        __qtablewidgetitem301 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(0, __qtablewidgetitem301)
        __qtablewidgetitem302 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(1, __qtablewidgetitem302)
        __qtablewidgetitem303 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(2, __qtablewidgetitem303)
        __qtablewidgetitem304 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(3, __qtablewidgetitem304)
        __qtablewidgetitem305 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(4, __qtablewidgetitem305)
        __qtablewidgetitem306 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(5, __qtablewidgetitem306)
        __qtablewidgetitem307 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(6, __qtablewidgetitem307)
        __qtablewidgetitem308 = QTableWidgetItem()
        self.tableWidget_12.setHorizontalHeaderItem(7, __qtablewidgetitem308)
        if (self.tableWidget_12.rowCount() < 6):
            self.tableWidget_12.setRowCount(6)
        __qtablewidgetitem309 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 0, __qtablewidgetitem309)
        __qtablewidgetitem310 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 1, __qtablewidgetitem310)
        __qtablewidgetitem311 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 2, __qtablewidgetitem311)
        __qtablewidgetitem312 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 3, __qtablewidgetitem312)
        __qtablewidgetitem313 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 4, __qtablewidgetitem313)
        __qtablewidgetitem314 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 5, __qtablewidgetitem314)
        __qtablewidgetitem315 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 6, __qtablewidgetitem315)
        __qtablewidgetitem316 = QTableWidgetItem()
        self.tableWidget_12.setItem(0, 7, __qtablewidgetitem316)
        __qtablewidgetitem317 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 0, __qtablewidgetitem317)
        __qtablewidgetitem318 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 1, __qtablewidgetitem318)
        __qtablewidgetitem319 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 2, __qtablewidgetitem319)
        __qtablewidgetitem320 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 3, __qtablewidgetitem320)
        __qtablewidgetitem321 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 4, __qtablewidgetitem321)
        __qtablewidgetitem322 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 5, __qtablewidgetitem322)
        __qtablewidgetitem323 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 6, __qtablewidgetitem323)
        __qtablewidgetitem324 = QTableWidgetItem()
        self.tableWidget_12.setItem(1, 7, __qtablewidgetitem324)
        __qtablewidgetitem325 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 0, __qtablewidgetitem325)
        __qtablewidgetitem326 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 1, __qtablewidgetitem326)
        __qtablewidgetitem327 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 2, __qtablewidgetitem327)
        __qtablewidgetitem328 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 3, __qtablewidgetitem328)
        __qtablewidgetitem329 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 4, __qtablewidgetitem329)
        __qtablewidgetitem330 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 5, __qtablewidgetitem330)
        __qtablewidgetitem331 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 6, __qtablewidgetitem331)
        __qtablewidgetitem332 = QTableWidgetItem()
        self.tableWidget_12.setItem(2, 7, __qtablewidgetitem332)
        __qtablewidgetitem333 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 0, __qtablewidgetitem333)
        __qtablewidgetitem334 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 1, __qtablewidgetitem334)
        __qtablewidgetitem335 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 2, __qtablewidgetitem335)
        __qtablewidgetitem336 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 3, __qtablewidgetitem336)
        __qtablewidgetitem337 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 4, __qtablewidgetitem337)
        __qtablewidgetitem338 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 5, __qtablewidgetitem338)
        __qtablewidgetitem339 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 6, __qtablewidgetitem339)
        __qtablewidgetitem340 = QTableWidgetItem()
        self.tableWidget_12.setItem(3, 7, __qtablewidgetitem340)
        __qtablewidgetitem341 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 0, __qtablewidgetitem341)
        __qtablewidgetitem342 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 1, __qtablewidgetitem342)
        __qtablewidgetitem343 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 2, __qtablewidgetitem343)
        __qtablewidgetitem344 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 3, __qtablewidgetitem344)
        __qtablewidgetitem345 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 4, __qtablewidgetitem345)
        __qtablewidgetitem346 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 5, __qtablewidgetitem346)
        __qtablewidgetitem347 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 6, __qtablewidgetitem347)
        __qtablewidgetitem348 = QTableWidgetItem()
        self.tableWidget_12.setItem(4, 7, __qtablewidgetitem348)
        __qtablewidgetitem349 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 0, __qtablewidgetitem349)
        __qtablewidgetitem350 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 1, __qtablewidgetitem350)
        __qtablewidgetitem351 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 2, __qtablewidgetitem351)
        __qtablewidgetitem352 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 3, __qtablewidgetitem352)
        __qtablewidgetitem353 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 4, __qtablewidgetitem353)
        __qtablewidgetitem354 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 5, __qtablewidgetitem354)
        __qtablewidgetitem355 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 6, __qtablewidgetitem355)
        __qtablewidgetitem356 = QTableWidgetItem()
        self.tableWidget_12.setItem(5, 7, __qtablewidgetitem356)
        self.tableWidget_12.setObjectName(u"tableWidget_12")
        self.tableWidget_12.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget_12.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget_12.setVerticalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_12.setHorizontalScrollMode(QAbstractItemView.ScrollMode.ScrollPerPixel)
        self.tableWidget_12.setRowCount(6)
        self.tableWidget_12.horizontalHeader().setDefaultSectionSize(200)
        self.tableWidget_12.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget_12.verticalHeader().setVisible(False)

        self.gridLayout_110.addWidget(self.tableWidget_12, 0, 0, 1, 1)


        self.gridLayout_61.addWidget(self.frame_48, 1, 0, 1, 1)

        self.frame_49 = QFrame(self.frame_40)
        self.frame_49.setObjectName(u"frame_49")
        self.frame_49.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_49.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_111 = QGridLayout(self.frame_49)
        self.gridLayout_111.setObjectName(u"gridLayout_111")
        self.horizontalLayout_22 = QHBoxLayout()
        self.horizontalLayout_22.setObjectName(u"horizontalLayout_22")
        self.frame_50 = QFrame(self.frame_49)
        self.frame_50.setObjectName(u"frame_50")
        self.frame_50.setMaximumSize(QSize(16777215, 16777215))
        self.frame_50.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_50.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_112 = QGridLayout(self.frame_50)
        self.gridLayout_112.setObjectName(u"gridLayout_112")
        self.gridLayout_113 = QGridLayout()
        self.gridLayout_113.setSpacing(1)
        self.gridLayout_113.setObjectName(u"gridLayout_113")
        self.label_36 = QLabel(self.frame_50)
        self.label_36.setObjectName(u"label_36")
        self.label_36.setFont(font4)
        self.label_36.setStyleSheet(u"color: red;")
        self.label_36.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_113.addWidget(self.label_36, 2, 0, 1, 1)

        self.label_37 = QLabel(self.frame_50)
        self.label_37.setObjectName(u"label_37")
        self.label_37.setFont(font5)
        self.label_37.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_113.addWidget(self.label_37, 0, 0, 1, 1)

        self.progressBar_7 = QProgressBar(self.frame_50)
        self.progressBar_7.setObjectName(u"progressBar_7")
        self.progressBar_7.setValue(24)

        self.gridLayout_113.addWidget(self.progressBar_7, 3, 0, 1, 1)

        self.label_38 = QLabel(self.frame_50)
        self.label_38.setObjectName(u"label_38")
        self.label_38.setFont(font6)
        self.label_38.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_113.addWidget(self.label_38, 1, 0, 1, 1)


        self.gridLayout_112.addLayout(self.gridLayout_113, 0, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_50)

        self.frame_balance = QFrame(self.frame_49)
        self.frame_balance.setObjectName(u"frame_balance")
        self.frame_balance.setMaximumSize(QSize(16777215, 16777215))
        self.frame_balance.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_balance.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_122 = QGridLayout(self.frame_balance)
        self.gridLayout_122.setObjectName(u"gridLayout_122")

        self.horizontalLayout_22.addWidget(self.frame_balance)

        self.frame_52 = QFrame(self.frame_49)
        self.frame_52.setObjectName(u"frame_52")
        self.frame_52.setMaximumSize(QSize(16777215, 16777215))
        self.frame_52.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_52.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_114 = QGridLayout(self.frame_52)
        self.gridLayout_114.setObjectName(u"gridLayout_114")
        self.gridLayout_117 = QGridLayout()
        self.gridLayout_117.setObjectName(u"gridLayout_117")
        self.gridLayout_117.setVerticalSpacing(1)
        self.label_42 = QLabel(self.frame_52)
        self.label_42.setObjectName(u"label_42")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_42.setFont(font7)
        self.label_42.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_117.addWidget(self.label_42, 4, 0, 1, 1)

        self.label_41 = QLabel(self.frame_52)
        self.label_41.setObjectName(u"label_41")
        self.label_41.setFont(font5)
        self.label_41.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_117.addWidget(self.label_41, 0, 0, 1, 1)

        self.label_49 = QLabel(self.frame_52)
        self.label_49.setObjectName(u"label_49")
        self.label_49.setFont(font7)
        self.label_49.setStyleSheet(u"color: red;")
        self.label_49.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_117.addWidget(self.label_49, 1, 0, 1, 1)

        self.label_50 = QLabel(self.frame_52)
        self.label_50.setObjectName(u"label_50")
        self.label_50.setFont(font5)
        self.label_50.setAlignment(Qt.AlignmentFlag.AlignHCenter|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_117.addWidget(self.label_50, 2, 0, 1, 1)

        self.label_40 = QLabel(self.frame_52)
        self.label_40.setObjectName(u"label_40")
        self.label_40.setFont(font4)
        self.label_40.setStyleSheet(u"color: green;")
        self.label_40.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_117.addWidget(self.label_40, 5, 0, 1, 1)

        self.label_51 = QLabel(self.frame_52)
        self.label_51.setObjectName(u"label_51")
        self.label_51.setFont(font7)
        self.label_51.setStyleSheet(u"color: green;")
        self.label_51.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_117.addWidget(self.label_51, 3, 0, 1, 1)


        self.gridLayout_114.addLayout(self.gridLayout_117, 0, 0, 1, 1)


        self.horizontalLayout_22.addWidget(self.frame_52)

        self.horizontalLayout_22.setStretch(0, 1)
        self.horizontalLayout_22.setStretch(1, 2)
        self.horizontalLayout_22.setStretch(2, 1)

        self.gridLayout_111.addLayout(self.horizontalLayout_22, 1, 0, 1, 1)


        self.gridLayout_61.addWidget(self.frame_49, 0, 0, 1, 1)


        self.formLayout_6.setLayout(0, QFormLayout.FieldRole, self.gridLayout_61)


        self.GRID_18.addWidget(self.frame_40, 1, 0, 1, 1)

        self.frame_51 = QFrame(self.finance)
        self.frame_51.setObjectName(u"frame_51")
        self.frame_51.setMaximumSize(QSize(16777215, 100))
        self.frame_51.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_51.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_115 = QGridLayout(self.frame_51)
        self.gridLayout_115.setObjectName(u"gridLayout_115")
        self.horizontalLayout_23 = QHBoxLayout()
        self.horizontalLayout_23.setObjectName(u"horizontalLayout_23")
        self.label_39 = QLabel(self.frame_51)
        self.label_39.setObjectName(u"label_39")

        self.horizontalLayout_23.addWidget(self.label_39)

        self.boton_filtrar_3 = QPushButton(self.frame_51)
        self.boton_filtrar_3.setObjectName(u"boton_filtrar_3")
        self.boton_filtrar_3.setMinimumSize(QSize(30, 30))
        self.boton_filtrar_3.setMaximumSize(QSize(100, 16777215))
        self.boton_filtrar_3.setFont(font)
        self.boton_filtrar_3.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_23.addWidget(self.boton_filtrar_3)

        self.crear_recordatorio_4 = QPushButton(self.frame_51)
        self.crear_recordatorio_4.setObjectName(u"crear_recordatorio_4")
        self.crear_recordatorio_4.setMinimumSize(QSize(30, 30))
        self.crear_recordatorio_4.setMaximumSize(QSize(150, 16777215))
        self.crear_recordatorio_4.setFont(font)
        self.crear_recordatorio_4.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_23.addWidget(self.crear_recordatorio_4)

        self.crear_informe_4 = QPushButton(self.frame_51)
        self.crear_informe_4.setObjectName(u"crear_informe_4")
        self.crear_informe_4.setMinimumSize(QSize(30, 30))
        self.crear_informe_4.setMaximumSize(QSize(150, 16777215))
        self.crear_informe_4.setFont(font)
        self.crear_informe_4.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_23.addWidget(self.crear_informe_4)


        self.gridLayout_115.addLayout(self.horizontalLayout_23, 0, 0, 1, 1)


        self.GRID_18.addWidget(self.frame_51, 0, 0, 1, 1)


        self.gridLayout_116.addLayout(self.GRID_18, 0, 0, 1, 1)

        self.tabWidget.addTab(self.finance, "")
        self.rrhh = QWidget()
        self.rrhh.setObjectName(u"rrhh")
        self.gridLayout_124 = QGridLayout(self.rrhh)
        self.gridLayout_124.setObjectName(u"gridLayout_124")
        self.gridLayout_123 = QGridLayout()
        self.gridLayout_123.setObjectName(u"gridLayout_123")
        self.gridLayout_125 = QGridLayout()
        self.gridLayout_125.setObjectName(u"gridLayout_125")
        self.frame_53 = QFrame(self.rrhh)
        self.frame_53.setObjectName(u"frame_53")
        self.frame_53.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_53.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_8 = QVBoxLayout(self.frame_53)
        self.verticalLayout_8.setObjectName(u"verticalLayout_8")
        self.scrollArea = QScrollArea(self.frame_53)
        self.scrollArea.setObjectName(u"scrollArea")
        self.scrollArea.setWidgetResizable(True)
        self.scrollAreaWidgetContents_2 = QWidget()
        self.scrollAreaWidgetContents_2.setObjectName(u"scrollAreaWidgetContents_2")
        self.scrollAreaWidgetContents_2.setGeometry(QRect(0, 0, 605, 657))
        self.gridLayout_34 = QGridLayout(self.scrollAreaWidgetContents_2)
        self.gridLayout_34.setObjectName(u"gridLayout_34")
        self.horizontal1_7 = QHBoxLayout()
        self.horizontal1_7.setObjectName(u"horizontal1_7")
        self.cap1_25 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_25.setObjectName(u"cap1_25")
        self.cap1_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_25.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_154 = QGridLayout(self.cap1_25)
        self.gridLayout_154.setObjectName(u"gridLayout_154")
        self.frame_107 = QFrame(self.cap1_25)
        self.frame_107.setObjectName(u"frame_107")
        self.frame_107.setMaximumSize(QSize(80, 16777215))
        self.frame_107.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_107.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_48 = QGridLayout(self.frame_107)
        self.gridLayout_48.setObjectName(u"gridLayout_48")
        self.label_60 = QLabel(self.frame_107)
        self.label_60.setObjectName(u"label_60")
        self.label_60.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_60.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_48.addWidget(self.label_60, 0, 1, 1, 1)


        self.gridLayout_154.addWidget(self.frame_107, 1, 0, 1, 1)

        self.frame_108 = QFrame(self.cap1_25)
        self.frame_108.setObjectName(u"frame_108")
        self.frame_108.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_108.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_31 = QVBoxLayout(self.frame_108)
        self.verticalLayout_31.setObjectName(u"verticalLayout_31")
        self.verticalLayout_32 = QVBoxLayout()
        self.verticalLayout_32.setObjectName(u"verticalLayout_32")
        self.label_61 = QLabel(self.frame_108)
        self.label_61.setObjectName(u"label_61")

        self.verticalLayout_32.addWidget(self.label_61)

        self.label_62 = QLabel(self.frame_108)
        self.label_62.setObjectName(u"label_62")
        font8 = QFont()
        font8.setPointSize(8)
        font8.setBold(False)
        self.label_62.setFont(font8)
        self.label_62.setStyleSheet(u"color: gray;")

        self.verticalLayout_32.addWidget(self.label_62)


        self.verticalLayout_31.addLayout(self.verticalLayout_32)


        self.gridLayout_154.addWidget(self.frame_108, 1, 1, 1, 1)


        self.horizontal1_7.addWidget(self.cap1_25)

        self.cap1_26 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_26.setObjectName(u"cap1_26")
        self.cap1_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_26.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_155 = QGridLayout(self.cap1_26)
        self.gridLayout_155.setObjectName(u"gridLayout_155")
        self.frame_109 = QFrame(self.cap1_26)
        self.frame_109.setObjectName(u"frame_109")
        self.frame_109.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_109.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_33 = QVBoxLayout(self.frame_109)
        self.verticalLayout_33.setObjectName(u"verticalLayout_33")
        self.verticalLayout_34 = QVBoxLayout()
        self.verticalLayout_34.setObjectName(u"verticalLayout_34")
        self.label_63 = QLabel(self.frame_109)
        self.label_63.setObjectName(u"label_63")

        self.verticalLayout_34.addWidget(self.label_63)

        self.label_64 = QLabel(self.frame_109)
        self.label_64.setObjectName(u"label_64")
        self.label_64.setFont(font8)
        self.label_64.setStyleSheet(u"color: gray;")

        self.verticalLayout_34.addWidget(self.label_64)


        self.verticalLayout_33.addLayout(self.verticalLayout_34)


        self.gridLayout_155.addWidget(self.frame_109, 1, 1, 1, 1)

        self.frame_110 = QFrame(self.cap1_26)
        self.frame_110.setObjectName(u"frame_110")
        self.frame_110.setMaximumSize(QSize(80, 16777215))
        self.frame_110.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_110.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_49 = QGridLayout(self.frame_110)
        self.gridLayout_49.setObjectName(u"gridLayout_49")
        self.label_65 = QLabel(self.frame_110)
        self.label_65.setObjectName(u"label_65")
        self.label_65.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_65.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_49.addWidget(self.label_65, 0, 1, 1, 1)


        self.gridLayout_155.addWidget(self.frame_110, 1, 0, 1, 1)


        self.horizontal1_7.addWidget(self.cap1_26)

        self.cap1_27 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_27.setObjectName(u"cap1_27")
        self.cap1_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_27.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_156 = QGridLayout(self.cap1_27)
        self.gridLayout_156.setObjectName(u"gridLayout_156")
        self.frame_111 = QFrame(self.cap1_27)
        self.frame_111.setObjectName(u"frame_111")
        self.frame_111.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_111.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_35 = QVBoxLayout(self.frame_111)
        self.verticalLayout_35.setObjectName(u"verticalLayout_35")
        self.verticalLayout_36 = QVBoxLayout()
        self.verticalLayout_36.setObjectName(u"verticalLayout_36")
        self.label_66 = QLabel(self.frame_111)
        self.label_66.setObjectName(u"label_66")

        self.verticalLayout_36.addWidget(self.label_66)

        self.label_67 = QLabel(self.frame_111)
        self.label_67.setObjectName(u"label_67")
        self.label_67.setFont(font8)
        self.label_67.setStyleSheet(u"color: gray;")

        self.verticalLayout_36.addWidget(self.label_67)


        self.verticalLayout_35.addLayout(self.verticalLayout_36)


        self.gridLayout_156.addWidget(self.frame_111, 1, 1, 1, 1)

        self.frame_112 = QFrame(self.cap1_27)
        self.frame_112.setObjectName(u"frame_112")
        self.frame_112.setMaximumSize(QSize(80, 16777215))
        self.frame_112.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_112.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_50 = QGridLayout(self.frame_112)
        self.gridLayout_50.setObjectName(u"gridLayout_50")
        self.label_68 = QLabel(self.frame_112)
        self.label_68.setObjectName(u"label_68")
        self.label_68.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_68.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_50.addWidget(self.label_68, 0, 1, 1, 1)


        self.gridLayout_156.addWidget(self.frame_112, 1, 0, 1, 1)


        self.horizontal1_7.addWidget(self.cap1_27)


        self.gridLayout_34.addLayout(self.horizontal1_7, 5, 0, 1, 1)

        self.horizontal1_4 = QHBoxLayout()
        self.horizontal1_4.setObjectName(u"horizontal1_4")
        self.cap1_14 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_14.setObjectName(u"cap1_14")
        self.cap1_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_14.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_142 = QGridLayout(self.cap1_14)
        self.gridLayout_142.setObjectName(u"gridLayout_142")
        self.frame_83 = QFrame(self.cap1_14)
        self.frame_83.setObjectName(u"frame_83")
        self.frame_83.setMaximumSize(QSize(80, 16777215))
        self.frame_83.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_83.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_36 = QGridLayout(self.frame_83)
        self.gridLayout_36.setObjectName(u"gridLayout_36")
        self.label_14 = QLabel(self.frame_83)
        self.label_14.setObjectName(u"label_14")
        self.label_14.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_14.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_36.addWidget(self.label_14, 0, 1, 1, 1)


        self.gridLayout_142.addWidget(self.frame_83, 1, 0, 1, 1)

        self.frame_84 = QFrame(self.cap1_14)
        self.frame_84.setObjectName(u"frame_84")
        self.frame_84.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_84.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_5 = QVBoxLayout(self.frame_84)
        self.verticalLayout_5.setObjectName(u"verticalLayout_5")
        self.verticalLayout_6 = QVBoxLayout()
        self.verticalLayout_6.setObjectName(u"verticalLayout_6")
        self.label_15 = QLabel(self.frame_84)
        self.label_15.setObjectName(u"label_15")

        self.verticalLayout_6.addWidget(self.label_15)

        self.label_16 = QLabel(self.frame_84)
        self.label_16.setObjectName(u"label_16")
        self.label_16.setFont(font8)
        self.label_16.setStyleSheet(u"color: gray;")

        self.verticalLayout_6.addWidget(self.label_16)


        self.verticalLayout_5.addLayout(self.verticalLayout_6)


        self.gridLayout_142.addWidget(self.frame_84, 1, 1, 1, 1)


        self.horizontal1_4.addWidget(self.cap1_14)

        self.cap1_17 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_17.setObjectName(u"cap1_17")
        self.cap1_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_145 = QGridLayout(self.cap1_17)
        self.gridLayout_145.setObjectName(u"gridLayout_145")
        self.frame_89 = QFrame(self.cap1_17)
        self.frame_89.setObjectName(u"frame_89")
        self.frame_89.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_89.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_13 = QVBoxLayout(self.frame_89)
        self.verticalLayout_13.setObjectName(u"verticalLayout_13")
        self.verticalLayout_14 = QVBoxLayout()
        self.verticalLayout_14.setObjectName(u"verticalLayout_14")
        self.label_23 = QLabel(self.frame_89)
        self.label_23.setObjectName(u"label_23")

        self.verticalLayout_14.addWidget(self.label_23)

        self.label_24 = QLabel(self.frame_89)
        self.label_24.setObjectName(u"label_24")
        self.label_24.setFont(font8)
        self.label_24.setStyleSheet(u"color: gray;")

        self.verticalLayout_14.addWidget(self.label_24)


        self.verticalLayout_13.addLayout(self.verticalLayout_14)


        self.gridLayout_145.addWidget(self.frame_89, 1, 1, 1, 1)

        self.frame_90 = QFrame(self.cap1_17)
        self.frame_90.setObjectName(u"frame_90")
        self.frame_90.setMaximumSize(QSize(80, 16777215))
        self.frame_90.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_90.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_39 = QGridLayout(self.frame_90)
        self.gridLayout_39.setObjectName(u"gridLayout_39")
        self.label_25 = QLabel(self.frame_90)
        self.label_25.setObjectName(u"label_25")
        self.label_25.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_25.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_39.addWidget(self.label_25, 0, 1, 1, 1)


        self.gridLayout_145.addWidget(self.frame_90, 1, 0, 1, 1)


        self.horizontal1_4.addWidget(self.cap1_17)

        self.cap1_18 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_18.setObjectName(u"cap1_18")
        self.cap1_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_146 = QGridLayout(self.cap1_18)
        self.gridLayout_146.setObjectName(u"gridLayout_146")
        self.frame_91 = QFrame(self.cap1_18)
        self.frame_91.setObjectName(u"frame_91")
        self.frame_91.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_91.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_15 = QVBoxLayout(self.frame_91)
        self.verticalLayout_15.setObjectName(u"verticalLayout_15")
        self.verticalLayout_16 = QVBoxLayout()
        self.verticalLayout_16.setObjectName(u"verticalLayout_16")
        self.label_26 = QLabel(self.frame_91)
        self.label_26.setObjectName(u"label_26")

        self.verticalLayout_16.addWidget(self.label_26)

        self.label_27 = QLabel(self.frame_91)
        self.label_27.setObjectName(u"label_27")
        self.label_27.setFont(font8)
        self.label_27.setStyleSheet(u"color: gray;")

        self.verticalLayout_16.addWidget(self.label_27)


        self.verticalLayout_15.addLayout(self.verticalLayout_16)


        self.gridLayout_146.addWidget(self.frame_91, 1, 1, 1, 1)

        self.frame_92 = QFrame(self.cap1_18)
        self.frame_92.setObjectName(u"frame_92")
        self.frame_92.setMaximumSize(QSize(80, 16777215))
        self.frame_92.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_92.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_40 = QGridLayout(self.frame_92)
        self.gridLayout_40.setObjectName(u"gridLayout_40")
        self.label_28 = QLabel(self.frame_92)
        self.label_28.setObjectName(u"label_28")
        self.label_28.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_28.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_40.addWidget(self.label_28, 0, 1, 1, 1)


        self.gridLayout_146.addWidget(self.frame_92, 1, 0, 1, 1)


        self.horizontal1_4.addWidget(self.cap1_18)


        self.gridLayout_34.addLayout(self.horizontal1_4, 2, 0, 1, 1)

        self.horizontal1_5 = QHBoxLayout()
        self.horizontal1_5.setObjectName(u"horizontal1_5")
        self.cap1_19 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_19.setObjectName(u"cap1_19")
        self.cap1_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_148 = QGridLayout(self.cap1_19)
        self.gridLayout_148.setObjectName(u"gridLayout_148")
        self.frame_95 = QFrame(self.cap1_19)
        self.frame_95.setObjectName(u"frame_95")
        self.frame_95.setMaximumSize(QSize(80, 16777215))
        self.frame_95.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_95.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_42 = QGridLayout(self.frame_95)
        self.gridLayout_42.setObjectName(u"gridLayout_42")
        self.label_32 = QLabel(self.frame_95)
        self.label_32.setObjectName(u"label_32")
        self.label_32.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_32.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_42.addWidget(self.label_32, 0, 1, 1, 1)


        self.gridLayout_148.addWidget(self.frame_95, 1, 0, 1, 1)

        self.frame_96 = QFrame(self.cap1_19)
        self.frame_96.setObjectName(u"frame_96")
        self.frame_96.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_96.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_19 = QVBoxLayout(self.frame_96)
        self.verticalLayout_19.setObjectName(u"verticalLayout_19")
        self.verticalLayout_20 = QVBoxLayout()
        self.verticalLayout_20.setObjectName(u"verticalLayout_20")
        self.label_33 = QLabel(self.frame_96)
        self.label_33.setObjectName(u"label_33")

        self.verticalLayout_20.addWidget(self.label_33)

        self.label_34 = QLabel(self.frame_96)
        self.label_34.setObjectName(u"label_34")
        self.label_34.setFont(font8)
        self.label_34.setStyleSheet(u"color: gray;")

        self.verticalLayout_20.addWidget(self.label_34)


        self.verticalLayout_19.addLayout(self.verticalLayout_20)


        self.gridLayout_148.addWidget(self.frame_96, 1, 1, 1, 1)


        self.horizontal1_5.addWidget(self.cap1_19)

        self.cap1_20 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_20.setObjectName(u"cap1_20")
        self.cap1_20.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_20.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_149 = QGridLayout(self.cap1_20)
        self.gridLayout_149.setObjectName(u"gridLayout_149")
        self.frame_97 = QFrame(self.cap1_20)
        self.frame_97.setObjectName(u"frame_97")
        self.frame_97.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_97.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_21 = QVBoxLayout(self.frame_97)
        self.verticalLayout_21.setObjectName(u"verticalLayout_21")
        self.verticalLayout_22 = QVBoxLayout()
        self.verticalLayout_22.setObjectName(u"verticalLayout_22")
        self.label_35 = QLabel(self.frame_97)
        self.label_35.setObjectName(u"label_35")

        self.verticalLayout_22.addWidget(self.label_35)

        self.label_43 = QLabel(self.frame_97)
        self.label_43.setObjectName(u"label_43")
        self.label_43.setFont(font8)
        self.label_43.setStyleSheet(u"color: gray;")

        self.verticalLayout_22.addWidget(self.label_43)


        self.verticalLayout_21.addLayout(self.verticalLayout_22)


        self.gridLayout_149.addWidget(self.frame_97, 1, 1, 1, 1)

        self.frame_98 = QFrame(self.cap1_20)
        self.frame_98.setObjectName(u"frame_98")
        self.frame_98.setMaximumSize(QSize(80, 16777215))
        self.frame_98.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_98.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_43 = QGridLayout(self.frame_98)
        self.gridLayout_43.setObjectName(u"gridLayout_43")
        self.label_44 = QLabel(self.frame_98)
        self.label_44.setObjectName(u"label_44")
        self.label_44.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_44.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_43.addWidget(self.label_44, 0, 1, 1, 1)


        self.gridLayout_149.addWidget(self.frame_98, 1, 0, 1, 1)


        self.horizontal1_5.addWidget(self.cap1_20)

        self.cap1_21 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_21.setObjectName(u"cap1_21")
        self.cap1_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_150 = QGridLayout(self.cap1_21)
        self.gridLayout_150.setObjectName(u"gridLayout_150")
        self.frame_99 = QFrame(self.cap1_21)
        self.frame_99.setObjectName(u"frame_99")
        self.frame_99.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_99.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_23 = QVBoxLayout(self.frame_99)
        self.verticalLayout_23.setObjectName(u"verticalLayout_23")
        self.verticalLayout_24 = QVBoxLayout()
        self.verticalLayout_24.setObjectName(u"verticalLayout_24")
        self.label_45 = QLabel(self.frame_99)
        self.label_45.setObjectName(u"label_45")

        self.verticalLayout_24.addWidget(self.label_45)

        self.label_46 = QLabel(self.frame_99)
        self.label_46.setObjectName(u"label_46")
        self.label_46.setFont(font8)
        self.label_46.setStyleSheet(u"color: gray;")

        self.verticalLayout_24.addWidget(self.label_46)


        self.verticalLayout_23.addLayout(self.verticalLayout_24)


        self.gridLayout_150.addWidget(self.frame_99, 1, 1, 1, 1)

        self.frame_100 = QFrame(self.cap1_21)
        self.frame_100.setObjectName(u"frame_100")
        self.frame_100.setMaximumSize(QSize(80, 16777215))
        self.frame_100.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_100.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_44 = QGridLayout(self.frame_100)
        self.gridLayout_44.setObjectName(u"gridLayout_44")
        self.label_47 = QLabel(self.frame_100)
        self.label_47.setObjectName(u"label_47")
        self.label_47.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_47.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_44.addWidget(self.label_47, 0, 1, 1, 1)


        self.gridLayout_150.addWidget(self.frame_100, 1, 0, 1, 1)


        self.horizontal1_5.addWidget(self.cap1_21)


        self.gridLayout_34.addLayout(self.horizontal1_5, 3, 0, 1, 1)

        self.horizontal1_3 = QHBoxLayout()
        self.horizontal1_3.setObjectName(u"horizontal1_3")
        self.cap1_13 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_13.setObjectName(u"cap1_13")
        self.cap1_13.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_13.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_141 = QGridLayout(self.cap1_13)
        self.gridLayout_141.setObjectName(u"gridLayout_141")
        self.frame_81 = QFrame(self.cap1_13)
        self.frame_81.setObjectName(u"frame_81")
        self.frame_81.setMaximumSize(QSize(80, 16777215))
        self.frame_81.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_81.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_35 = QGridLayout(self.frame_81)
        self.gridLayout_35.setObjectName(u"gridLayout_35")
        self.label_11 = QLabel(self.frame_81)
        self.label_11.setObjectName(u"label_11")
        self.label_11.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_11.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_35.addWidget(self.label_11, 0, 1, 1, 1)


        self.gridLayout_141.addWidget(self.frame_81, 1, 0, 1, 1)

        self.frame_82 = QFrame(self.cap1_13)
        self.frame_82.setObjectName(u"frame_82")
        self.frame_82.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_82.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_4 = QVBoxLayout(self.frame_82)
        self.verticalLayout_4.setObjectName(u"verticalLayout_4")
        self.verticalLayout = QVBoxLayout()
        self.verticalLayout.setObjectName(u"verticalLayout")
        self.label_12 = QLabel(self.frame_82)
        self.label_12.setObjectName(u"label_12")

        self.verticalLayout.addWidget(self.label_12)

        self.label_13 = QLabel(self.frame_82)
        self.label_13.setObjectName(u"label_13")
        self.label_13.setFont(font8)
        self.label_13.setStyleSheet(u"color: gray;")

        self.verticalLayout.addWidget(self.label_13)


        self.verticalLayout_4.addLayout(self.verticalLayout)


        self.gridLayout_141.addWidget(self.frame_82, 1, 1, 1, 1)


        self.horizontal1_3.addWidget(self.cap1_13)

        self.cap1_16 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_16.setObjectName(u"cap1_16")
        self.cap1_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_144 = QGridLayout(self.cap1_16)
        self.gridLayout_144.setObjectName(u"gridLayout_144")
        self.frame_87 = QFrame(self.cap1_16)
        self.frame_87.setObjectName(u"frame_87")
        self.frame_87.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_87.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_11 = QVBoxLayout(self.frame_87)
        self.verticalLayout_11.setObjectName(u"verticalLayout_11")
        self.verticalLayout_12 = QVBoxLayout()
        self.verticalLayout_12.setObjectName(u"verticalLayout_12")
        self.label_20 = QLabel(self.frame_87)
        self.label_20.setObjectName(u"label_20")

        self.verticalLayout_12.addWidget(self.label_20)

        self.label_21 = QLabel(self.frame_87)
        self.label_21.setObjectName(u"label_21")
        self.label_21.setFont(font8)
        self.label_21.setStyleSheet(u"color: gray;")

        self.verticalLayout_12.addWidget(self.label_21)


        self.verticalLayout_11.addLayout(self.verticalLayout_12)


        self.gridLayout_144.addWidget(self.frame_87, 1, 1, 1, 1)

        self.frame_88 = QFrame(self.cap1_16)
        self.frame_88.setObjectName(u"frame_88")
        self.frame_88.setMaximumSize(QSize(80, 16777215))
        self.frame_88.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_88.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_38 = QGridLayout(self.frame_88)
        self.gridLayout_38.setObjectName(u"gridLayout_38")
        self.label_22 = QLabel(self.frame_88)
        self.label_22.setObjectName(u"label_22")
        self.label_22.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_22.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_38.addWidget(self.label_22, 0, 1, 1, 1)


        self.gridLayout_144.addWidget(self.frame_88, 1, 0, 1, 1)


        self.horizontal1_3.addWidget(self.cap1_16)

        self.cap1_15 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_15.setObjectName(u"cap1_15")
        self.cap1_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_15.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_143 = QGridLayout(self.cap1_15)
        self.gridLayout_143.setObjectName(u"gridLayout_143")
        self.frame_85 = QFrame(self.cap1_15)
        self.frame_85.setObjectName(u"frame_85")
        self.frame_85.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_85.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_9 = QVBoxLayout(self.frame_85)
        self.verticalLayout_9.setObjectName(u"verticalLayout_9")
        self.verticalLayout_10 = QVBoxLayout()
        self.verticalLayout_10.setObjectName(u"verticalLayout_10")
        self.label_17 = QLabel(self.frame_85)
        self.label_17.setObjectName(u"label_17")

        self.verticalLayout_10.addWidget(self.label_17)

        self.label_18 = QLabel(self.frame_85)
        self.label_18.setObjectName(u"label_18")
        self.label_18.setFont(font8)
        self.label_18.setStyleSheet(u"color: gray;")

        self.verticalLayout_10.addWidget(self.label_18)


        self.verticalLayout_9.addLayout(self.verticalLayout_10)


        self.gridLayout_143.addWidget(self.frame_85, 1, 1, 1, 1)

        self.frame_86 = QFrame(self.cap1_15)
        self.frame_86.setObjectName(u"frame_86")
        self.frame_86.setMaximumSize(QSize(80, 16777215))
        self.frame_86.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_86.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_37 = QGridLayout(self.frame_86)
        self.gridLayout_37.setObjectName(u"gridLayout_37")
        self.label_19 = QLabel(self.frame_86)
        self.label_19.setObjectName(u"label_19")
        self.label_19.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_19.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_37.addWidget(self.label_19, 0, 1, 1, 1)


        self.gridLayout_143.addWidget(self.frame_86, 1, 0, 1, 1)


        self.horizontal1_3.addWidget(self.cap1_15)


        self.gridLayout_34.addLayout(self.horizontal1_3, 0, 0, 1, 1)

        self.horizontal1_6 = QHBoxLayout()
        self.horizontal1_6.setObjectName(u"horizontal1_6")
        self.cap1_22 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_22.setObjectName(u"cap1_22")
        self.cap1_22.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_22.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_151 = QGridLayout(self.cap1_22)
        self.gridLayout_151.setObjectName(u"gridLayout_151")
        self.frame_101 = QFrame(self.cap1_22)
        self.frame_101.setObjectName(u"frame_101")
        self.frame_101.setMaximumSize(QSize(80, 16777215))
        self.frame_101.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_101.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_45 = QGridLayout(self.frame_101)
        self.gridLayout_45.setObjectName(u"gridLayout_45")
        self.label_48 = QLabel(self.frame_101)
        self.label_48.setObjectName(u"label_48")
        self.label_48.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_48.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_45.addWidget(self.label_48, 0, 1, 1, 1)


        self.gridLayout_151.addWidget(self.frame_101, 1, 0, 1, 1)

        self.frame_102 = QFrame(self.cap1_22)
        self.frame_102.setObjectName(u"frame_102")
        self.frame_102.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_102.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_25 = QVBoxLayout(self.frame_102)
        self.verticalLayout_25.setObjectName(u"verticalLayout_25")
        self.verticalLayout_26 = QVBoxLayout()
        self.verticalLayout_26.setObjectName(u"verticalLayout_26")
        self.label_52 = QLabel(self.frame_102)
        self.label_52.setObjectName(u"label_52")

        self.verticalLayout_26.addWidget(self.label_52)

        self.label_53 = QLabel(self.frame_102)
        self.label_53.setObjectName(u"label_53")
        self.label_53.setFont(font8)
        self.label_53.setStyleSheet(u"color: gray;")

        self.verticalLayout_26.addWidget(self.label_53)


        self.verticalLayout_25.addLayout(self.verticalLayout_26)


        self.gridLayout_151.addWidget(self.frame_102, 1, 1, 1, 1)


        self.horizontal1_6.addWidget(self.cap1_22)

        self.cap1_23 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_23.setObjectName(u"cap1_23")
        self.cap1_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_23.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_152 = QGridLayout(self.cap1_23)
        self.gridLayout_152.setObjectName(u"gridLayout_152")
        self.frame_103 = QFrame(self.cap1_23)
        self.frame_103.setObjectName(u"frame_103")
        self.frame_103.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_103.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_27 = QVBoxLayout(self.frame_103)
        self.verticalLayout_27.setObjectName(u"verticalLayout_27")
        self.verticalLayout_28 = QVBoxLayout()
        self.verticalLayout_28.setObjectName(u"verticalLayout_28")
        self.label_54 = QLabel(self.frame_103)
        self.label_54.setObjectName(u"label_54")

        self.verticalLayout_28.addWidget(self.label_54)

        self.label_55 = QLabel(self.frame_103)
        self.label_55.setObjectName(u"label_55")
        self.label_55.setFont(font8)
        self.label_55.setStyleSheet(u"color: gray;")

        self.verticalLayout_28.addWidget(self.label_55)


        self.verticalLayout_27.addLayout(self.verticalLayout_28)


        self.gridLayout_152.addWidget(self.frame_103, 1, 1, 1, 1)

        self.frame_104 = QFrame(self.cap1_23)
        self.frame_104.setObjectName(u"frame_104")
        self.frame_104.setMaximumSize(QSize(80, 16777215))
        self.frame_104.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_104.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_46 = QGridLayout(self.frame_104)
        self.gridLayout_46.setObjectName(u"gridLayout_46")
        self.label_56 = QLabel(self.frame_104)
        self.label_56.setObjectName(u"label_56")
        self.label_56.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_56.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_46.addWidget(self.label_56, 0, 1, 1, 1)


        self.gridLayout_152.addWidget(self.frame_104, 1, 0, 1, 1)


        self.horizontal1_6.addWidget(self.cap1_23)

        self.cap1_24 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_24.setObjectName(u"cap1_24")
        self.cap1_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_24.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_153 = QGridLayout(self.cap1_24)
        self.gridLayout_153.setObjectName(u"gridLayout_153")
        self.frame_105 = QFrame(self.cap1_24)
        self.frame_105.setObjectName(u"frame_105")
        self.frame_105.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_105.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_29 = QVBoxLayout(self.frame_105)
        self.verticalLayout_29.setObjectName(u"verticalLayout_29")
        self.verticalLayout_30 = QVBoxLayout()
        self.verticalLayout_30.setObjectName(u"verticalLayout_30")
        self.label_57 = QLabel(self.frame_105)
        self.label_57.setObjectName(u"label_57")

        self.verticalLayout_30.addWidget(self.label_57)

        self.label_58 = QLabel(self.frame_105)
        self.label_58.setObjectName(u"label_58")
        self.label_58.setFont(font8)
        self.label_58.setStyleSheet(u"color: gray;")

        self.verticalLayout_30.addWidget(self.label_58)


        self.verticalLayout_29.addLayout(self.verticalLayout_30)


        self.gridLayout_153.addWidget(self.frame_105, 1, 1, 1, 1)

        self.frame_106 = QFrame(self.cap1_24)
        self.frame_106.setObjectName(u"frame_106")
        self.frame_106.setMaximumSize(QSize(80, 16777215))
        self.frame_106.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_106.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_47 = QGridLayout(self.frame_106)
        self.gridLayout_47.setObjectName(u"gridLayout_47")
        self.label_59 = QLabel(self.frame_106)
        self.label_59.setObjectName(u"label_59")
        self.label_59.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_59.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_47.addWidget(self.label_59, 0, 1, 1, 1)


        self.gridLayout_153.addWidget(self.frame_106, 1, 0, 1, 1)


        self.horizontal1_6.addWidget(self.cap1_24)


        self.gridLayout_34.addLayout(self.horizontal1_6, 1, 0, 1, 1)

        self.horizontal1_8 = QHBoxLayout()
        self.horizontal1_8.setObjectName(u"horizontal1_8")
        self.cap1_28 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_28.setObjectName(u"cap1_28")
        self.cap1_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_28.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_157 = QGridLayout(self.cap1_28)
        self.gridLayout_157.setObjectName(u"gridLayout_157")
        self.frame_113 = QFrame(self.cap1_28)
        self.frame_113.setObjectName(u"frame_113")
        self.frame_113.setMaximumSize(QSize(80, 16777215))
        self.frame_113.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_113.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_51 = QGridLayout(self.frame_113)
        self.gridLayout_51.setObjectName(u"gridLayout_51")
        self.label_69 = QLabel(self.frame_113)
        self.label_69.setObjectName(u"label_69")
        self.label_69.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_69.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_51.addWidget(self.label_69, 0, 1, 1, 1)


        self.gridLayout_157.addWidget(self.frame_113, 1, 0, 1, 1)

        self.frame_114 = QFrame(self.cap1_28)
        self.frame_114.setObjectName(u"frame_114")
        self.frame_114.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_114.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_37 = QVBoxLayout(self.frame_114)
        self.verticalLayout_37.setObjectName(u"verticalLayout_37")
        self.verticalLayout_38 = QVBoxLayout()
        self.verticalLayout_38.setObjectName(u"verticalLayout_38")
        self.label_70 = QLabel(self.frame_114)
        self.label_70.setObjectName(u"label_70")

        self.verticalLayout_38.addWidget(self.label_70)

        self.label_71 = QLabel(self.frame_114)
        self.label_71.setObjectName(u"label_71")
        self.label_71.setFont(font8)
        self.label_71.setStyleSheet(u"color: gray;")

        self.verticalLayout_38.addWidget(self.label_71)


        self.verticalLayout_37.addLayout(self.verticalLayout_38)


        self.gridLayout_157.addWidget(self.frame_114, 1, 1, 1, 1)


        self.horizontal1_8.addWidget(self.cap1_28)

        self.cap1_29 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_29.setObjectName(u"cap1_29")
        self.cap1_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_29.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_158 = QGridLayout(self.cap1_29)
        self.gridLayout_158.setObjectName(u"gridLayout_158")
        self.frame_115 = QFrame(self.cap1_29)
        self.frame_115.setObjectName(u"frame_115")
        self.frame_115.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_115.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_39 = QVBoxLayout(self.frame_115)
        self.verticalLayout_39.setObjectName(u"verticalLayout_39")
        self.verticalLayout_40 = QVBoxLayout()
        self.verticalLayout_40.setObjectName(u"verticalLayout_40")
        self.label_72 = QLabel(self.frame_115)
        self.label_72.setObjectName(u"label_72")

        self.verticalLayout_40.addWidget(self.label_72)

        self.label_73 = QLabel(self.frame_115)
        self.label_73.setObjectName(u"label_73")
        self.label_73.setFont(font8)
        self.label_73.setStyleSheet(u"color: gray;")

        self.verticalLayout_40.addWidget(self.label_73)


        self.verticalLayout_39.addLayout(self.verticalLayout_40)


        self.gridLayout_158.addWidget(self.frame_115, 1, 1, 1, 1)

        self.frame_116 = QFrame(self.cap1_29)
        self.frame_116.setObjectName(u"frame_116")
        self.frame_116.setMaximumSize(QSize(80, 16777215))
        self.frame_116.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_116.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_52 = QGridLayout(self.frame_116)
        self.gridLayout_52.setObjectName(u"gridLayout_52")
        self.label_74 = QLabel(self.frame_116)
        self.label_74.setObjectName(u"label_74")
        self.label_74.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_74.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_52.addWidget(self.label_74, 0, 1, 1, 1)


        self.gridLayout_158.addWidget(self.frame_116, 1, 0, 1, 1)


        self.horizontal1_8.addWidget(self.cap1_29)

        self.cap1_30 = QFrame(self.scrollAreaWidgetContents_2)
        self.cap1_30.setObjectName(u"cap1_30")
        self.cap1_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.cap1_30.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_159 = QGridLayout(self.cap1_30)
        self.gridLayout_159.setObjectName(u"gridLayout_159")
        self.frame_117 = QFrame(self.cap1_30)
        self.frame_117.setObjectName(u"frame_117")
        self.frame_117.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_117.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_41 = QVBoxLayout(self.frame_117)
        self.verticalLayout_41.setObjectName(u"verticalLayout_41")
        self.verticalLayout_42 = QVBoxLayout()
        self.verticalLayout_42.setObjectName(u"verticalLayout_42")
        self.label_75 = QLabel(self.frame_117)
        self.label_75.setObjectName(u"label_75")

        self.verticalLayout_42.addWidget(self.label_75)

        self.label_76 = QLabel(self.frame_117)
        self.label_76.setObjectName(u"label_76")
        self.label_76.setFont(font8)
        self.label_76.setStyleSheet(u"color: gray;")

        self.verticalLayout_42.addWidget(self.label_76)


        self.verticalLayout_41.addLayout(self.verticalLayout_42)


        self.gridLayout_159.addWidget(self.frame_117, 1, 1, 1, 1)

        self.frame_118 = QFrame(self.cap1_30)
        self.frame_118.setObjectName(u"frame_118")
        self.frame_118.setMaximumSize(QSize(80, 16777215))
        self.frame_118.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_118.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_53 = QGridLayout(self.frame_118)
        self.gridLayout_53.setObjectName(u"gridLayout_53")
        self.label_77 = QLabel(self.frame_118)
        self.label_77.setObjectName(u"label_77")
        self.label_77.setPixmap(QPixmap(u"icons/pngwing.com (1).png"))
        self.label_77.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_53.addWidget(self.label_77, 0, 1, 1, 1)


        self.gridLayout_159.addWidget(self.frame_118, 1, 0, 1, 1)


        self.horizontal1_8.addWidget(self.cap1_30)


        self.gridLayout_34.addLayout(self.horizontal1_8, 4, 0, 1, 1)

        self.scrollArea.setWidget(self.scrollAreaWidgetContents_2)

        self.verticalLayout_8.addWidget(self.scrollArea)

        self.verticalLayout_7 = QVBoxLayout()
        self.verticalLayout_7.setObjectName(u"verticalLayout_7")

        self.verticalLayout_8.addLayout(self.verticalLayout_7)


        self.gridLayout_125.addWidget(self.frame_53, 1, 0, 1, 1)

        self.frame_54 = QFrame(self.rrhh)
        self.frame_54.setObjectName(u"frame_54")
        self.frame_54.setMaximumSize(QSize(16777215, 100))
        self.frame_54.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_54.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_31 = QGridLayout(self.frame_54)
        self.gridLayout_31.setObjectName(u"gridLayout_31")
        self.horizontalLayout_8 = QHBoxLayout()
        self.horizontalLayout_8.setObjectName(u"horizontalLayout_8")
        self.label_10 = QLabel(self.frame_54)
        self.label_10.setObjectName(u"label_10")
        self.label_10.setFont(font5)

        self.horizontalLayout_8.addWidget(self.label_10)

        self.lineEdit_6 = QLineEdit(self.frame_54)
        self.lineEdit_6.setObjectName(u"lineEdit_6")
        self.lineEdit_6.setMaximumSize(QSize(150, 16777215))

        self.horizontalLayout_8.addWidget(self.lineEdit_6)

        self.boton_actualizacion = QPushButton(self.frame_54)
        self.boton_actualizacion.setObjectName(u"boton_actualizacion")
        self.boton_actualizacion.setMinimumSize(QSize(30, 30))
        self.boton_actualizacion.setFont(font)
        self.boton_actualizacion.setStyleSheet(u"background-color: #434343;\n"
"color: white;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")
        icon14 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.AddressBookNew))
        self.boton_actualizacion.setIcon(icon14)

        self.horizontalLayout_8.addWidget(self.boton_actualizacion)

        self.crear_informe_3 = QPushButton(self.frame_54)
        self.crear_informe_3.setObjectName(u"crear_informe_3")
        self.crear_informe_3.setMinimumSize(QSize(30, 30))
        self.crear_informe_3.setFont(font)
        self.crear_informe_3.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_8.addWidget(self.crear_informe_3)


        self.gridLayout_31.addLayout(self.horizontalLayout_8, 0, 0, 1, 1)


        self.gridLayout_125.addWidget(self.frame_54, 0, 0, 1, 1)


        self.gridLayout_123.addLayout(self.gridLayout_125, 2, 0, 1, 1)


        self.gridLayout_124.addLayout(self.gridLayout_123, 0, 0, 1, 1)

        self.tabWidget.addTab(self.rrhh, "")
        self.marketing = QWidget()
        self.marketing.setObjectName(u"marketing")
        self.gridLayout_54 = QGridLayout(self.marketing)
        self.gridLayout_54.setObjectName(u"gridLayout_54")
        self.GRID_4 = QGridLayout()
        self.GRID_4.setObjectName(u"GRID_4")
        self.frame_14 = QFrame(self.marketing)
        self.frame_14.setObjectName(u"frame_14")
        self.frame_14.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_14.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_2 = QFormLayout(self.frame_14)
        self.formLayout_2.setObjectName(u"formLayout_2")
        self.gridLayout_55 = QGridLayout()
        self.gridLayout_55.setObjectName(u"gridLayout_55")
        self.frame_16 = QFrame(self.frame_14)
        self.frame_16.setObjectName(u"frame_16")
        self.frame_16.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_16.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_57 = QGridLayout(self.frame_16)
        self.gridLayout_57.setObjectName(u"gridLayout_57")
        self.horizontalLayout_9 = QHBoxLayout()
        self.horizontalLayout_9.setObjectName(u"horizontalLayout_9")
        self.frame_grafico_1 = QFrame(self.frame_16)
        self.frame_grafico_1.setObjectName(u"frame_grafico_1")
        self.frame_grafico_1.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_1.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_60 = QGridLayout(self.frame_grafico_1)
        self.gridLayout_60.setObjectName(u"gridLayout_60")

        self.horizontalLayout_9.addWidget(self.frame_grafico_1)

        self.frame_17 = QFrame(self.frame_16)
        self.frame_17.setObjectName(u"frame_17")
        self.frame_17.setMaximumSize(QSize(200, 16777215))
        self.frame_17.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_17.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_58 = QGridLayout(self.frame_17)
        self.gridLayout_58.setObjectName(u"gridLayout_58")
        self.gridLayout_59 = QGridLayout()
        self.gridLayout_59.setObjectName(u"gridLayout_59")
        self.label_79 = QLabel(self.frame_17)
        self.label_79.setObjectName(u"label_79")
        self.label_79.setFont(font5)
        self.label_79.setAlignment(Qt.AlignmentFlag.AlignLeading|Qt.AlignmentFlag.AlignLeft|Qt.AlignmentFlag.AlignTop)

        self.gridLayout_59.addWidget(self.label_79, 0, 0, 1, 1)

        self.label_80 = QLabel(self.frame_17)
        self.label_80.setObjectName(u"label_80")
        font9 = QFont()
        font9.setPointSize(14)
        font9.setBold(False)
        self.label_80.setFont(font9)
        self.label_80.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_59.addWidget(self.label_80, 1, 0, 1, 1)

        self.label_78 = QLabel(self.frame_17)
        self.label_78.setObjectName(u"label_78")
        self.label_78.setFont(font4)
        self.label_78.setStyleSheet(u"color: green;")
        self.label_78.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_59.addWidget(self.label_78, 2, 0, 1, 1)


        self.gridLayout_58.addLayout(self.gridLayout_59, 0, 0, 1, 1)


        self.horizontalLayout_9.addWidget(self.frame_17)

        self.frame_grafico_2 = QFrame(self.frame_16)
        self.frame_grafico_2.setObjectName(u"frame_grafico_2")
        self.frame_grafico_2.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_2.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_62 = QGridLayout(self.frame_grafico_2)
        self.gridLayout_62.setObjectName(u"gridLayout_62")

        self.horizontalLayout_9.addWidget(self.frame_grafico_2)

        self.horizontalLayout_9.setStretch(0, 1)
        self.horizontalLayout_9.setStretch(1, 1)
        self.horizontalLayout_9.setStretch(2, 1)

        self.gridLayout_57.addLayout(self.horizontalLayout_9, 1, 0, 1, 1)


        self.gridLayout_55.addWidget(self.frame_16, 0, 0, 1, 1)


        self.formLayout_2.setLayout(0, QFormLayout.FieldRole, self.gridLayout_55)


        self.GRID_4.addWidget(self.frame_14, 1, 0, 1, 1)

        self.frame_18 = QFrame(self.marketing)
        self.frame_18.setObjectName(u"frame_18")
        self.frame_18.setMaximumSize(QSize(16777215, 100))
        self.frame_18.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_18.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_63 = QGridLayout(self.frame_18)
        self.gridLayout_63.setObjectName(u"gridLayout_63")
        self.horizontalLayout_10 = QHBoxLayout()
        self.horizontalLayout_10.setObjectName(u"horizontalLayout_10")
        self.label_81 = QLabel(self.frame_18)
        self.label_81.setObjectName(u"label_81")

        self.horizontalLayout_10.addWidget(self.label_81)

        self.crear_auto = QPushButton(self.frame_18)
        self.crear_auto.setObjectName(u"crear_auto")
        self.crear_auto.setMinimumSize(QSize(30, 30))
        self.crear_auto.setMaximumSize(QSize(200, 16777215))
        self.crear_auto.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_10.addWidget(self.crear_auto)

        self.crear_informe_7 = QPushButton(self.frame_18)
        self.crear_informe_7.setObjectName(u"crear_informe_7")
        self.crear_informe_7.setMinimumSize(QSize(30, 30))
        self.crear_informe_7.setMaximumSize(QSize(170, 16777215))
        self.crear_informe_7.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_10.addWidget(self.crear_informe_7)


        self.gridLayout_63.addLayout(self.horizontalLayout_10, 0, 0, 1, 1)


        self.GRID_4.addWidget(self.frame_18, 0, 0, 1, 1)


        self.gridLayout_54.addLayout(self.GRID_4, 0, 0, 1, 1)

        self.tabWidget.addTab(self.marketing, "")
        self.innovation = QWidget()
        self.innovation.setObjectName(u"innovation")
        self.gridLayout_70 = QGridLayout(self.innovation)
        self.gridLayout_70.setObjectName(u"gridLayout_70")
        self.GRID_5 = QGridLayout()
        self.GRID_5.setObjectName(u"GRID_5")
        self.frame_15 = QFrame(self.innovation)
        self.frame_15.setObjectName(u"frame_15")
        self.frame_15.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_15.setFrameShadow(QFrame.Shadow.Raised)
        self.formLayout_3 = QFormLayout(self.frame_15)
        self.formLayout_3.setObjectName(u"formLayout_3")
        self.gridLayout_56 = QGridLayout()
        self.gridLayout_56.setObjectName(u"gridLayout_56")
        self.frame_19 = QFrame(self.frame_15)
        self.frame_19.setObjectName(u"frame_19")
        self.frame_19.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_19.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_64 = QGridLayout(self.frame_19)
        self.gridLayout_64.setObjectName(u"gridLayout_64")
        self.scrollArea_2 = QScrollArea(self.frame_19)
        self.scrollArea_2.setObjectName(u"scrollArea_2")
        self.scrollArea_2.setWidgetResizable(True)
        self.scrollAreaWidgetContents_3 = QWidget()
        self.scrollAreaWidgetContents_3.setObjectName(u"scrollAreaWidgetContents_3")
        self.scrollAreaWidgetContents_3.setGeometry(QRect(0, 0, 833, 1029))
        self.gridLayout_68 = QGridLayout(self.scrollAreaWidgetContents_3)
        self.gridLayout_68.setObjectName(u"gridLayout_68")
        self.horizontalLayout_11 = QHBoxLayout()
        self.horizontalLayout_11.setObjectName(u"horizontalLayout_11")
        self.frame_grafico_3 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_grafico_3.setObjectName(u"frame_grafico_3")
        self.frame_grafico_3.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_3.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_65 = QGridLayout(self.frame_grafico_3)
        self.gridLayout_65.setObjectName(u"gridLayout_65")
        self.verticalLayout_43 = QVBoxLayout()
        self.verticalLayout_43.setObjectName(u"verticalLayout_43")
        self.label_82 = QLabel(self.frame_grafico_3)
        self.label_82.setObjectName(u"label_82")
        self.label_82.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_43.addWidget(self.label_82)

        self.frame_70 = QFrame(self.frame_grafico_3)
        self.frame_70.setObjectName(u"frame_70")
        self.frame_70.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_70.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_41 = QHBoxLayout(self.frame_70)
        self.horizontalLayout_41.setObjectName(u"horizontalLayout_41")
        self.horizontalLayout_42 = QHBoxLayout()
        self.horizontalLayout_42.setObjectName(u"horizontalLayout_42")
        self.frame_71 = QFrame(self.frame_70)
        self.frame_71.setObjectName(u"frame_71")
        self.frame_71.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_71.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_98 = QVBoxLayout(self.frame_71)
        self.verticalLayout_98.setObjectName(u"verticalLayout_98")
        self.verticalLayout_99 = QVBoxLayout()
        self.verticalLayout_99.setObjectName(u"verticalLayout_99")
        self.label_112 = QLabel(self.frame_71)
        self.label_112.setObjectName(u"label_112")

        self.verticalLayout_99.addWidget(self.label_112)

        self.label_113 = QLabel(self.frame_71)
        self.label_113.setObjectName(u"label_113")
        font10 = QFont()
        font10.setPointSize(7)
        font10.setBold(False)
        self.label_113.setFont(font10)

        self.verticalLayout_99.addWidget(self.label_113)

        self.progressBar_16 = QProgressBar(self.frame_71)
        self.progressBar_16.setObjectName(u"progressBar_16")
        self.progressBar_16.setValue(90)

        self.verticalLayout_99.addWidget(self.progressBar_16)


        self.verticalLayout_98.addLayout(self.verticalLayout_99)


        self.horizontalLayout_42.addWidget(self.frame_71)

        self.frame_72 = QFrame(self.frame_70)
        self.frame_72.setObjectName(u"frame_72")
        self.frame_72.setMaximumSize(QSize(100, 16777215))
        self.frame_72.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_72.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_100 = QVBoxLayout(self.frame_72)
        self.verticalLayout_100.setObjectName(u"verticalLayout_100")
        self.verticalLayout_101 = QVBoxLayout()
        self.verticalLayout_101.setObjectName(u"verticalLayout_101")
        self.pushButton_29 = QPushButton(self.frame_72)
        self.pushButton_29.setObjectName(u"pushButton_29")
        icon15 = QIcon(QIcon.fromTheme(QIcon.ThemeIcon.EditDelete))
        self.pushButton_29.setIcon(icon15)

        self.verticalLayout_101.addWidget(self.pushButton_29)


        self.verticalLayout_100.addLayout(self.verticalLayout_101)


        self.horizontalLayout_42.addWidget(self.frame_72)


        self.horizontalLayout_41.addLayout(self.horizontalLayout_42)


        self.verticalLayout_43.addWidget(self.frame_70)

        self.frame_67 = QFrame(self.frame_grafico_3)
        self.frame_67.setObjectName(u"frame_67")
        self.frame_67.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_67.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_39 = QHBoxLayout(self.frame_67)
        self.horizontalLayout_39.setObjectName(u"horizontalLayout_39")
        self.horizontalLayout_40 = QHBoxLayout()
        self.horizontalLayout_40.setObjectName(u"horizontalLayout_40")
        self.frame_68 = QFrame(self.frame_67)
        self.frame_68.setObjectName(u"frame_68")
        self.frame_68.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_68.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_94 = QVBoxLayout(self.frame_68)
        self.verticalLayout_94.setObjectName(u"verticalLayout_94")
        self.verticalLayout_95 = QVBoxLayout()
        self.verticalLayout_95.setObjectName(u"verticalLayout_95")
        self.label_110 = QLabel(self.frame_68)
        self.label_110.setObjectName(u"label_110")

        self.verticalLayout_95.addWidget(self.label_110)

        self.label_111 = QLabel(self.frame_68)
        self.label_111.setObjectName(u"label_111")
        self.label_111.setFont(font10)

        self.verticalLayout_95.addWidget(self.label_111)

        self.progressBar_15 = QProgressBar(self.frame_68)
        self.progressBar_15.setObjectName(u"progressBar_15")
        self.progressBar_15.setValue(30)

        self.verticalLayout_95.addWidget(self.progressBar_15)


        self.verticalLayout_94.addLayout(self.verticalLayout_95)


        self.horizontalLayout_40.addWidget(self.frame_68)

        self.frame_69 = QFrame(self.frame_67)
        self.frame_69.setObjectName(u"frame_69")
        self.frame_69.setMaximumSize(QSize(100, 16777215))
        self.frame_69.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_69.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_96 = QVBoxLayout(self.frame_69)
        self.verticalLayout_96.setObjectName(u"verticalLayout_96")
        self.verticalLayout_97 = QVBoxLayout()
        self.verticalLayout_97.setObjectName(u"verticalLayout_97")
        self.pushButton_28 = QPushButton(self.frame_69)
        self.pushButton_28.setObjectName(u"pushButton_28")
        self.pushButton_28.setIcon(icon15)

        self.verticalLayout_97.addWidget(self.pushButton_28)


        self.verticalLayout_96.addLayout(self.verticalLayout_97)


        self.horizontalLayout_40.addWidget(self.frame_69)


        self.horizontalLayout_39.addLayout(self.horizontalLayout_40)


        self.verticalLayout_43.addWidget(self.frame_67)

        self.frame_64 = QFrame(self.frame_grafico_3)
        self.frame_64.setObjectName(u"frame_64")
        self.frame_64.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_64.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_37 = QHBoxLayout(self.frame_64)
        self.horizontalLayout_37.setObjectName(u"horizontalLayout_37")
        self.horizontalLayout_38 = QHBoxLayout()
        self.horizontalLayout_38.setObjectName(u"horizontalLayout_38")
        self.frame_65 = QFrame(self.frame_64)
        self.frame_65.setObjectName(u"frame_65")
        self.frame_65.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_65.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_90 = QVBoxLayout(self.frame_65)
        self.verticalLayout_90.setObjectName(u"verticalLayout_90")
        self.verticalLayout_91 = QVBoxLayout()
        self.verticalLayout_91.setObjectName(u"verticalLayout_91")
        self.label_108 = QLabel(self.frame_65)
        self.label_108.setObjectName(u"label_108")

        self.verticalLayout_91.addWidget(self.label_108)

        self.label_109 = QLabel(self.frame_65)
        self.label_109.setObjectName(u"label_109")
        self.label_109.setFont(font10)

        self.verticalLayout_91.addWidget(self.label_109)

        self.progressBar_14 = QProgressBar(self.frame_65)
        self.progressBar_14.setObjectName(u"progressBar_14")
        self.progressBar_14.setValue(24)

        self.verticalLayout_91.addWidget(self.progressBar_14)


        self.verticalLayout_90.addLayout(self.verticalLayout_91)


        self.horizontalLayout_38.addWidget(self.frame_65)

        self.frame_66 = QFrame(self.frame_64)
        self.frame_66.setObjectName(u"frame_66")
        self.frame_66.setMaximumSize(QSize(100, 16777215))
        self.frame_66.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_66.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_92 = QVBoxLayout(self.frame_66)
        self.verticalLayout_92.setObjectName(u"verticalLayout_92")
        self.verticalLayout_93 = QVBoxLayout()
        self.verticalLayout_93.setObjectName(u"verticalLayout_93")
        self.pushButton_27 = QPushButton(self.frame_66)
        self.pushButton_27.setObjectName(u"pushButton_27")
        self.pushButton_27.setIcon(icon15)

        self.verticalLayout_93.addWidget(self.pushButton_27)


        self.verticalLayout_92.addLayout(self.verticalLayout_93)


        self.horizontalLayout_38.addWidget(self.frame_66)


        self.horizontalLayout_37.addLayout(self.horizontalLayout_38)


        self.verticalLayout_43.addWidget(self.frame_64)

        self.frame_29 = QFrame(self.frame_grafico_3)
        self.frame_29.setObjectName(u"frame_29")
        self.frame_29.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_29.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_17 = QHBoxLayout(self.frame_29)
        self.horizontalLayout_17.setObjectName(u"horizontalLayout_17")
        self.horizontalLayout_18 = QHBoxLayout()
        self.horizontalLayout_18.setObjectName(u"horizontalLayout_18")
        self.frame_30 = QFrame(self.frame_29)
        self.frame_30.setObjectName(u"frame_30")
        self.frame_30.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_30.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_52 = QVBoxLayout(self.frame_30)
        self.verticalLayout_52.setObjectName(u"verticalLayout_52")
        self.verticalLayout_53 = QVBoxLayout()
        self.verticalLayout_53.setObjectName(u"verticalLayout_53")
        self.label_88 = QLabel(self.frame_30)
        self.label_88.setObjectName(u"label_88")

        self.verticalLayout_53.addWidget(self.label_88)

        self.label_89 = QLabel(self.frame_30)
        self.label_89.setObjectName(u"label_89")
        self.label_89.setFont(font10)

        self.verticalLayout_53.addWidget(self.label_89)

        self.progressBar_4 = QProgressBar(self.frame_30)
        self.progressBar_4.setObjectName(u"progressBar_4")
        self.progressBar_4.setValue(24)

        self.verticalLayout_53.addWidget(self.progressBar_4)


        self.verticalLayout_52.addLayout(self.verticalLayout_53)


        self.horizontalLayout_18.addWidget(self.frame_30)

        self.frame_31 = QFrame(self.frame_29)
        self.frame_31.setObjectName(u"frame_31")
        self.frame_31.setMaximumSize(QSize(100, 16777215))
        self.frame_31.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_31.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_54 = QVBoxLayout(self.frame_31)
        self.verticalLayout_54.setObjectName(u"verticalLayout_54")
        self.verticalLayout_55 = QVBoxLayout()
        self.verticalLayout_55.setObjectName(u"verticalLayout_55")
        self.pushButton_18 = QPushButton(self.frame_31)
        self.pushButton_18.setObjectName(u"pushButton_18")
        self.pushButton_18.setIcon(icon15)

        self.verticalLayout_55.addWidget(self.pushButton_18)


        self.verticalLayout_54.addLayout(self.verticalLayout_55)


        self.horizontalLayout_18.addWidget(self.frame_31)


        self.horizontalLayout_17.addLayout(self.horizontalLayout_18)


        self.verticalLayout_43.addWidget(self.frame_29)

        self.frame_26 = QFrame(self.frame_grafico_3)
        self.frame_26.setObjectName(u"frame_26")
        self.frame_26.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_26.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_15 = QHBoxLayout(self.frame_26)
        self.horizontalLayout_15.setObjectName(u"horizontalLayout_15")
        self.horizontalLayout_16 = QHBoxLayout()
        self.horizontalLayout_16.setObjectName(u"horizontalLayout_16")
        self.frame_27 = QFrame(self.frame_26)
        self.frame_27.setObjectName(u"frame_27")
        self.frame_27.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_27.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_48 = QVBoxLayout(self.frame_27)
        self.verticalLayout_48.setObjectName(u"verticalLayout_48")
        self.verticalLayout_49 = QVBoxLayout()
        self.verticalLayout_49.setObjectName(u"verticalLayout_49")
        self.label_86 = QLabel(self.frame_27)
        self.label_86.setObjectName(u"label_86")

        self.verticalLayout_49.addWidget(self.label_86)

        self.label_87 = QLabel(self.frame_27)
        self.label_87.setObjectName(u"label_87")
        self.label_87.setFont(font10)

        self.verticalLayout_49.addWidget(self.label_87)

        self.progressBar_3 = QProgressBar(self.frame_27)
        self.progressBar_3.setObjectName(u"progressBar_3")
        self.progressBar_3.setValue(11)

        self.verticalLayout_49.addWidget(self.progressBar_3)


        self.verticalLayout_48.addLayout(self.verticalLayout_49)


        self.horizontalLayout_16.addWidget(self.frame_27)

        self.frame_28 = QFrame(self.frame_26)
        self.frame_28.setObjectName(u"frame_28")
        self.frame_28.setMaximumSize(QSize(100, 16777215))
        self.frame_28.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_28.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_50 = QVBoxLayout(self.frame_28)
        self.verticalLayout_50.setObjectName(u"verticalLayout_50")
        self.verticalLayout_51 = QVBoxLayout()
        self.verticalLayout_51.setObjectName(u"verticalLayout_51")
        self.pushButton_17 = QPushButton(self.frame_28)
        self.pushButton_17.setObjectName(u"pushButton_17")
        self.pushButton_17.setIcon(icon15)

        self.verticalLayout_51.addWidget(self.pushButton_17)


        self.verticalLayout_50.addLayout(self.verticalLayout_51)


        self.horizontalLayout_16.addWidget(self.frame_28)


        self.horizontalLayout_15.addLayout(self.horizontalLayout_16)


        self.verticalLayout_43.addWidget(self.frame_26)

        self.frame_23 = QFrame(self.frame_grafico_3)
        self.frame_23.setObjectName(u"frame_23")
        self.frame_23.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_23.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_14 = QHBoxLayout(self.frame_23)
        self.horizontalLayout_14.setObjectName(u"horizontalLayout_14")
        self.horizontalLayout_13 = QHBoxLayout()
        self.horizontalLayout_13.setObjectName(u"horizontalLayout_13")
        self.frame_24 = QFrame(self.frame_23)
        self.frame_24.setObjectName(u"frame_24")
        self.frame_24.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_24.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_47 = QVBoxLayout(self.frame_24)
        self.verticalLayout_47.setObjectName(u"verticalLayout_47")
        self.verticalLayout_46 = QVBoxLayout()
        self.verticalLayout_46.setObjectName(u"verticalLayout_46")
        self.label_83 = QLabel(self.frame_24)
        self.label_83.setObjectName(u"label_83")

        self.verticalLayout_46.addWidget(self.label_83)

        self.label_84 = QLabel(self.frame_24)
        self.label_84.setObjectName(u"label_84")
        self.label_84.setFont(font10)

        self.verticalLayout_46.addWidget(self.label_84)

        self.progressBar_2 = QProgressBar(self.frame_24)
        self.progressBar_2.setObjectName(u"progressBar_2")
        self.progressBar_2.setValue(24)

        self.verticalLayout_46.addWidget(self.progressBar_2)


        self.verticalLayout_47.addLayout(self.verticalLayout_46)


        self.horizontalLayout_13.addWidget(self.frame_24)

        self.frame_25 = QFrame(self.frame_23)
        self.frame_25.setObjectName(u"frame_25")
        self.frame_25.setMaximumSize(QSize(100, 16777215))
        self.frame_25.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_25.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_45 = QVBoxLayout(self.frame_25)
        self.verticalLayout_45.setObjectName(u"verticalLayout_45")
        self.verticalLayout_44 = QVBoxLayout()
        self.verticalLayout_44.setObjectName(u"verticalLayout_44")
        self.pushButton_16 = QPushButton(self.frame_25)
        self.pushButton_16.setObjectName(u"pushButton_16")
        self.pushButton_16.setIcon(icon15)

        self.verticalLayout_44.addWidget(self.pushButton_16)


        self.verticalLayout_45.addLayout(self.verticalLayout_44)


        self.horizontalLayout_13.addWidget(self.frame_25)


        self.horizontalLayout_14.addLayout(self.horizontalLayout_13)


        self.verticalLayout_43.addWidget(self.frame_23)


        self.gridLayout_65.addLayout(self.verticalLayout_43, 0, 0, 1, 1)

        self.frame_58 = QFrame(self.frame_grafico_3)
        self.frame_58.setObjectName(u"frame_58")
        self.frame_58.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_58.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_33 = QHBoxLayout(self.frame_58)
        self.horizontalLayout_33.setObjectName(u"horizontalLayout_33")
        self.horizontalLayout_34 = QHBoxLayout()
        self.horizontalLayout_34.setObjectName(u"horizontalLayout_34")
        self.frame_59 = QFrame(self.frame_58)
        self.frame_59.setObjectName(u"frame_59")
        self.frame_59.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_59.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_82 = QVBoxLayout(self.frame_59)
        self.verticalLayout_82.setObjectName(u"verticalLayout_82")
        self.verticalLayout_83 = QVBoxLayout()
        self.verticalLayout_83.setObjectName(u"verticalLayout_83")
        self.label_104 = QLabel(self.frame_59)
        self.label_104.setObjectName(u"label_104")

        self.verticalLayout_83.addWidget(self.label_104)

        self.label_105 = QLabel(self.frame_59)
        self.label_105.setObjectName(u"label_105")
        self.label_105.setFont(font10)

        self.verticalLayout_83.addWidget(self.label_105)

        self.progressBar_12 = QProgressBar(self.frame_59)
        self.progressBar_12.setObjectName(u"progressBar_12")
        self.progressBar_12.setValue(50)

        self.verticalLayout_83.addWidget(self.progressBar_12)


        self.verticalLayout_82.addLayout(self.verticalLayout_83)


        self.horizontalLayout_34.addWidget(self.frame_59)

        self.frame_60 = QFrame(self.frame_58)
        self.frame_60.setObjectName(u"frame_60")
        self.frame_60.setMaximumSize(QSize(100, 16777215))
        self.frame_60.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_60.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_84 = QVBoxLayout(self.frame_60)
        self.verticalLayout_84.setObjectName(u"verticalLayout_84")
        self.verticalLayout_85 = QVBoxLayout()
        self.verticalLayout_85.setObjectName(u"verticalLayout_85")
        self.pushButton_25 = QPushButton(self.frame_60)
        self.pushButton_25.setObjectName(u"pushButton_25")
        self.pushButton_25.setIcon(icon15)

        self.verticalLayout_85.addWidget(self.pushButton_25)


        self.verticalLayout_84.addLayout(self.verticalLayout_85)


        self.horizontalLayout_34.addWidget(self.frame_60)


        self.horizontalLayout_33.addLayout(self.horizontalLayout_34)


        self.gridLayout_65.addWidget(self.frame_58, 1, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_grafico_3)

        self.frame_grafico_4 = QFrame(self.scrollAreaWidgetContents_3)
        self.frame_grafico_4.setObjectName(u"frame_grafico_4")
        self.frame_grafico_4.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_grafico_4.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_66 = QGridLayout(self.frame_grafico_4)
        self.gridLayout_66.setObjectName(u"gridLayout_66")
        self.verticalLayout_56 = QVBoxLayout()
        self.verticalLayout_56.setObjectName(u"verticalLayout_56")
        self.label_90 = QLabel(self.frame_grafico_4)
        self.label_90.setObjectName(u"label_90")
        self.label_90.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.verticalLayout_56.addWidget(self.label_90)

        self.frame_79 = QFrame(self.frame_grafico_4)
        self.frame_79.setObjectName(u"frame_79")
        self.frame_79.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_79.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_47 = QHBoxLayout(self.frame_79)
        self.horizontalLayout_47.setObjectName(u"horizontalLayout_47")
        self.horizontalLayout_48 = QHBoxLayout()
        self.horizontalLayout_48.setObjectName(u"horizontalLayout_48")
        self.frame_80 = QFrame(self.frame_79)
        self.frame_80.setObjectName(u"frame_80")
        self.frame_80.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_80.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_110 = QVBoxLayout(self.frame_80)
        self.verticalLayout_110.setObjectName(u"verticalLayout_110")
        self.verticalLayout_111 = QVBoxLayout()
        self.verticalLayout_111.setObjectName(u"verticalLayout_111")
        self.label_118 = QLabel(self.frame_80)
        self.label_118.setObjectName(u"label_118")

        self.verticalLayout_111.addWidget(self.label_118)

        self.label_119 = QLabel(self.frame_80)
        self.label_119.setObjectName(u"label_119")
        self.label_119.setFont(font10)

        self.verticalLayout_111.addWidget(self.label_119)

        self.progressBar_19 = QProgressBar(self.frame_80)
        self.progressBar_19.setObjectName(u"progressBar_19")
        self.progressBar_19.setValue(2)

        self.verticalLayout_111.addWidget(self.progressBar_19)


        self.verticalLayout_110.addLayout(self.verticalLayout_111)


        self.horizontalLayout_48.addWidget(self.frame_80)

        self.frame_119 = QFrame(self.frame_79)
        self.frame_119.setObjectName(u"frame_119")
        self.frame_119.setMaximumSize(QSize(100, 16777215))
        self.frame_119.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_119.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_112 = QVBoxLayout(self.frame_119)
        self.verticalLayout_112.setObjectName(u"verticalLayout_112")
        self.verticalLayout_113 = QVBoxLayout()
        self.verticalLayout_113.setObjectName(u"verticalLayout_113")
        self.pushButton_32 = QPushButton(self.frame_119)
        self.pushButton_32.setObjectName(u"pushButton_32")
        self.pushButton_32.setIcon(icon15)

        self.verticalLayout_113.addWidget(self.pushButton_32)


        self.verticalLayout_112.addLayout(self.verticalLayout_113)


        self.horizontalLayout_48.addWidget(self.frame_119)


        self.horizontalLayout_47.addLayout(self.horizontalLayout_48)


        self.verticalLayout_56.addWidget(self.frame_79)

        self.frame_76 = QFrame(self.frame_grafico_4)
        self.frame_76.setObjectName(u"frame_76")
        self.frame_76.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_76.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_45 = QHBoxLayout(self.frame_76)
        self.horizontalLayout_45.setObjectName(u"horizontalLayout_45")
        self.horizontalLayout_46 = QHBoxLayout()
        self.horizontalLayout_46.setObjectName(u"horizontalLayout_46")
        self.frame_77 = QFrame(self.frame_76)
        self.frame_77.setObjectName(u"frame_77")
        self.frame_77.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_77.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_106 = QVBoxLayout(self.frame_77)
        self.verticalLayout_106.setObjectName(u"verticalLayout_106")
        self.verticalLayout_107 = QVBoxLayout()
        self.verticalLayout_107.setObjectName(u"verticalLayout_107")
        self.label_116 = QLabel(self.frame_77)
        self.label_116.setObjectName(u"label_116")

        self.verticalLayout_107.addWidget(self.label_116)

        self.label_117 = QLabel(self.frame_77)
        self.label_117.setObjectName(u"label_117")
        self.label_117.setFont(font10)

        self.verticalLayout_107.addWidget(self.label_117)

        self.progressBar_18 = QProgressBar(self.frame_77)
        self.progressBar_18.setObjectName(u"progressBar_18")
        self.progressBar_18.setValue(100)

        self.verticalLayout_107.addWidget(self.progressBar_18)


        self.verticalLayout_106.addLayout(self.verticalLayout_107)


        self.horizontalLayout_46.addWidget(self.frame_77)

        self.frame_78 = QFrame(self.frame_76)
        self.frame_78.setObjectName(u"frame_78")
        self.frame_78.setMaximumSize(QSize(100, 16777215))
        self.frame_78.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_78.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_108 = QVBoxLayout(self.frame_78)
        self.verticalLayout_108.setObjectName(u"verticalLayout_108")
        self.verticalLayout_109 = QVBoxLayout()
        self.verticalLayout_109.setObjectName(u"verticalLayout_109")
        self.pushButton_31 = QPushButton(self.frame_78)
        self.pushButton_31.setObjectName(u"pushButton_31")
        self.pushButton_31.setIcon(icon15)

        self.verticalLayout_109.addWidget(self.pushButton_31)


        self.verticalLayout_108.addLayout(self.verticalLayout_109)


        self.horizontalLayout_46.addWidget(self.frame_78)


        self.horizontalLayout_45.addLayout(self.horizontalLayout_46)


        self.verticalLayout_56.addWidget(self.frame_76)

        self.frame_73 = QFrame(self.frame_grafico_4)
        self.frame_73.setObjectName(u"frame_73")
        self.frame_73.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_73.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_43 = QHBoxLayout(self.frame_73)
        self.horizontalLayout_43.setObjectName(u"horizontalLayout_43")
        self.horizontalLayout_44 = QHBoxLayout()
        self.horizontalLayout_44.setObjectName(u"horizontalLayout_44")
        self.frame_74 = QFrame(self.frame_73)
        self.frame_74.setObjectName(u"frame_74")
        self.frame_74.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_74.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_102 = QVBoxLayout(self.frame_74)
        self.verticalLayout_102.setObjectName(u"verticalLayout_102")
        self.verticalLayout_103 = QVBoxLayout()
        self.verticalLayout_103.setObjectName(u"verticalLayout_103")
        self.label_114 = QLabel(self.frame_74)
        self.label_114.setObjectName(u"label_114")

        self.verticalLayout_103.addWidget(self.label_114)

        self.label_115 = QLabel(self.frame_74)
        self.label_115.setObjectName(u"label_115")
        self.label_115.setFont(font10)

        self.verticalLayout_103.addWidget(self.label_115)

        self.progressBar_17 = QProgressBar(self.frame_74)
        self.progressBar_17.setObjectName(u"progressBar_17")
        self.progressBar_17.setValue(50)

        self.verticalLayout_103.addWidget(self.progressBar_17)


        self.verticalLayout_102.addLayout(self.verticalLayout_103)


        self.horizontalLayout_44.addWidget(self.frame_74)

        self.frame_75 = QFrame(self.frame_73)
        self.frame_75.setObjectName(u"frame_75")
        self.frame_75.setMaximumSize(QSize(100, 16777215))
        self.frame_75.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_75.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_104 = QVBoxLayout(self.frame_75)
        self.verticalLayout_104.setObjectName(u"verticalLayout_104")
        self.verticalLayout_105 = QVBoxLayout()
        self.verticalLayout_105.setObjectName(u"verticalLayout_105")
        self.pushButton_30 = QPushButton(self.frame_75)
        self.pushButton_30.setObjectName(u"pushButton_30")
        self.pushButton_30.setIcon(icon15)

        self.verticalLayout_105.addWidget(self.pushButton_30)


        self.verticalLayout_104.addLayout(self.verticalLayout_105)


        self.horizontalLayout_44.addWidget(self.frame_75)


        self.horizontalLayout_43.addLayout(self.horizontalLayout_44)


        self.verticalLayout_56.addWidget(self.frame_73)

        self.frame_32 = QFrame(self.frame_grafico_4)
        self.frame_32.setObjectName(u"frame_32")
        self.frame_32.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_32.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_19 = QHBoxLayout(self.frame_32)
        self.horizontalLayout_19.setObjectName(u"horizontalLayout_19")
        self.horizontalLayout_20 = QHBoxLayout()
        self.horizontalLayout_20.setObjectName(u"horizontalLayout_20")
        self.frame_33 = QFrame(self.frame_32)
        self.frame_33.setObjectName(u"frame_33")
        self.frame_33.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_33.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_57 = QVBoxLayout(self.frame_33)
        self.verticalLayout_57.setObjectName(u"verticalLayout_57")
        self.verticalLayout_58 = QVBoxLayout()
        self.verticalLayout_58.setObjectName(u"verticalLayout_58")
        self.label_91 = QLabel(self.frame_33)
        self.label_91.setObjectName(u"label_91")

        self.verticalLayout_58.addWidget(self.label_91)

        self.label_92 = QLabel(self.frame_33)
        self.label_92.setObjectName(u"label_92")
        self.label_92.setFont(font10)

        self.verticalLayout_58.addWidget(self.label_92)

        self.progressBar_5 = QProgressBar(self.frame_33)
        self.progressBar_5.setObjectName(u"progressBar_5")
        self.progressBar_5.setValue(24)

        self.verticalLayout_58.addWidget(self.progressBar_5)


        self.verticalLayout_57.addLayout(self.verticalLayout_58)


        self.horizontalLayout_20.addWidget(self.frame_33)

        self.frame_34 = QFrame(self.frame_32)
        self.frame_34.setObjectName(u"frame_34")
        self.frame_34.setMaximumSize(QSize(100, 16777215))
        self.frame_34.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_34.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_59 = QVBoxLayout(self.frame_34)
        self.verticalLayout_59.setObjectName(u"verticalLayout_59")
        self.verticalLayout_60 = QVBoxLayout()
        self.verticalLayout_60.setObjectName(u"verticalLayout_60")
        self.pushButton_19 = QPushButton(self.frame_34)
        self.pushButton_19.setObjectName(u"pushButton_19")
        self.pushButton_19.setIcon(icon15)

        self.verticalLayout_60.addWidget(self.pushButton_19)


        self.verticalLayout_59.addLayout(self.verticalLayout_60)


        self.horizontalLayout_20.addWidget(self.frame_34)


        self.horizontalLayout_19.addLayout(self.horizontalLayout_20)


        self.verticalLayout_56.addWidget(self.frame_32)

        self.frame_35 = QFrame(self.frame_grafico_4)
        self.frame_35.setObjectName(u"frame_35")
        self.frame_35.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_35.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_21 = QHBoxLayout(self.frame_35)
        self.horizontalLayout_21.setObjectName(u"horizontalLayout_21")
        self.horizontalLayout_24 = QHBoxLayout()
        self.horizontalLayout_24.setObjectName(u"horizontalLayout_24")
        self.frame_36 = QFrame(self.frame_35)
        self.frame_36.setObjectName(u"frame_36")
        self.frame_36.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_36.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_61 = QVBoxLayout(self.frame_36)
        self.verticalLayout_61.setObjectName(u"verticalLayout_61")
        self.verticalLayout_62 = QVBoxLayout()
        self.verticalLayout_62.setObjectName(u"verticalLayout_62")
        self.label_93 = QLabel(self.frame_36)
        self.label_93.setObjectName(u"label_93")

        self.verticalLayout_62.addWidget(self.label_93)

        self.label_94 = QLabel(self.frame_36)
        self.label_94.setObjectName(u"label_94")
        self.label_94.setFont(font10)

        self.verticalLayout_62.addWidget(self.label_94)

        self.progressBar_6 = QProgressBar(self.frame_36)
        self.progressBar_6.setObjectName(u"progressBar_6")
        self.progressBar_6.setValue(24)

        self.verticalLayout_62.addWidget(self.progressBar_6)


        self.verticalLayout_61.addLayout(self.verticalLayout_62)


        self.horizontalLayout_24.addWidget(self.frame_36)

        self.frame_37 = QFrame(self.frame_35)
        self.frame_37.setObjectName(u"frame_37")
        self.frame_37.setMaximumSize(QSize(100, 16777215))
        self.frame_37.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_37.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_63 = QVBoxLayout(self.frame_37)
        self.verticalLayout_63.setObjectName(u"verticalLayout_63")
        self.verticalLayout_64 = QVBoxLayout()
        self.verticalLayout_64.setObjectName(u"verticalLayout_64")
        self.pushButton_20 = QPushButton(self.frame_37)
        self.pushButton_20.setObjectName(u"pushButton_20")
        self.pushButton_20.setIcon(icon15)

        self.verticalLayout_64.addWidget(self.pushButton_20)


        self.verticalLayout_63.addLayout(self.verticalLayout_64)


        self.horizontalLayout_24.addWidget(self.frame_37)


        self.horizontalLayout_21.addLayout(self.horizontalLayout_24)


        self.verticalLayout_56.addWidget(self.frame_35)

        self.frame_38 = QFrame(self.frame_grafico_4)
        self.frame_38.setObjectName(u"frame_38")
        self.frame_38.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_38.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_25 = QHBoxLayout(self.frame_38)
        self.horizontalLayout_25.setObjectName(u"horizontalLayout_25")
        self.horizontalLayout_26 = QHBoxLayout()
        self.horizontalLayout_26.setObjectName(u"horizontalLayout_26")
        self.frame_39 = QFrame(self.frame_38)
        self.frame_39.setObjectName(u"frame_39")
        self.frame_39.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_39.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_65 = QVBoxLayout(self.frame_39)
        self.verticalLayout_65.setObjectName(u"verticalLayout_65")
        self.verticalLayout_66 = QVBoxLayout()
        self.verticalLayout_66.setObjectName(u"verticalLayout_66")
        self.label_95 = QLabel(self.frame_39)
        self.label_95.setObjectName(u"label_95")

        self.verticalLayout_66.addWidget(self.label_95)

        self.label_96 = QLabel(self.frame_39)
        self.label_96.setObjectName(u"label_96")
        self.label_96.setFont(font10)

        self.verticalLayout_66.addWidget(self.label_96)

        self.progressBar_8 = QProgressBar(self.frame_39)
        self.progressBar_8.setObjectName(u"progressBar_8")
        self.progressBar_8.setValue(50)

        self.verticalLayout_66.addWidget(self.progressBar_8)


        self.verticalLayout_65.addLayout(self.verticalLayout_66)


        self.horizontalLayout_26.addWidget(self.frame_39)

        self.frame_41 = QFrame(self.frame_38)
        self.frame_41.setObjectName(u"frame_41")
        self.frame_41.setMaximumSize(QSize(100, 16777215))
        self.frame_41.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_41.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_67 = QVBoxLayout(self.frame_41)
        self.verticalLayout_67.setObjectName(u"verticalLayout_67")
        self.verticalLayout_68 = QVBoxLayout()
        self.verticalLayout_68.setObjectName(u"verticalLayout_68")
        self.pushButton_21 = QPushButton(self.frame_41)
        self.pushButton_21.setObjectName(u"pushButton_21")
        self.pushButton_21.setIcon(icon15)

        self.verticalLayout_68.addWidget(self.pushButton_21)


        self.verticalLayout_67.addLayout(self.verticalLayout_68)


        self.horizontalLayout_26.addWidget(self.frame_41)


        self.horizontalLayout_25.addLayout(self.horizontalLayout_26)


        self.verticalLayout_56.addWidget(self.frame_38)


        self.gridLayout_66.addLayout(self.verticalLayout_56, 0, 0, 1, 1)

        self.frame_61 = QFrame(self.frame_grafico_4)
        self.frame_61.setObjectName(u"frame_61")
        self.frame_61.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_61.setFrameShadow(QFrame.Shadow.Raised)
        self.horizontalLayout_35 = QHBoxLayout(self.frame_61)
        self.horizontalLayout_35.setObjectName(u"horizontalLayout_35")
        self.horizontalLayout_36 = QHBoxLayout()
        self.horizontalLayout_36.setObjectName(u"horizontalLayout_36")
        self.frame_62 = QFrame(self.frame_61)
        self.frame_62.setObjectName(u"frame_62")
        self.frame_62.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_62.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_86 = QVBoxLayout(self.frame_62)
        self.verticalLayout_86.setObjectName(u"verticalLayout_86")
        self.verticalLayout_87 = QVBoxLayout()
        self.verticalLayout_87.setObjectName(u"verticalLayout_87")
        self.label_106 = QLabel(self.frame_62)
        self.label_106.setObjectName(u"label_106")

        self.verticalLayout_87.addWidget(self.label_106)

        self.label_107 = QLabel(self.frame_62)
        self.label_107.setObjectName(u"label_107")
        self.label_107.setFont(font10)

        self.verticalLayout_87.addWidget(self.label_107)

        self.progressBar_13 = QProgressBar(self.frame_62)
        self.progressBar_13.setObjectName(u"progressBar_13")
        self.progressBar_13.setValue(24)

        self.verticalLayout_87.addWidget(self.progressBar_13)


        self.verticalLayout_86.addLayout(self.verticalLayout_87)


        self.horizontalLayout_36.addWidget(self.frame_62)

        self.frame_63 = QFrame(self.frame_61)
        self.frame_63.setObjectName(u"frame_63")
        self.frame_63.setMaximumSize(QSize(100, 16777215))
        self.frame_63.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_63.setFrameShadow(QFrame.Shadow.Raised)
        self.verticalLayout_88 = QVBoxLayout(self.frame_63)
        self.verticalLayout_88.setObjectName(u"verticalLayout_88")
        self.verticalLayout_89 = QVBoxLayout()
        self.verticalLayout_89.setObjectName(u"verticalLayout_89")
        self.pushButton_26 = QPushButton(self.frame_63)
        self.pushButton_26.setObjectName(u"pushButton_26")
        self.pushButton_26.setIcon(icon15)

        self.verticalLayout_89.addWidget(self.pushButton_26)


        self.verticalLayout_88.addLayout(self.verticalLayout_89)


        self.horizontalLayout_36.addWidget(self.frame_63)


        self.horizontalLayout_35.addLayout(self.horizontalLayout_36)


        self.gridLayout_66.addWidget(self.frame_61, 1, 0, 1, 1)


        self.horizontalLayout_11.addWidget(self.frame_grafico_4)

        self.horizontalLayout_11.setStretch(0, 1)
        self.horizontalLayout_11.setStretch(1, 1)

        self.gridLayout_68.addLayout(self.horizontalLayout_11, 0, 0, 1, 1)

        self.scrollArea_2.setWidget(self.scrollAreaWidgetContents_3)

        self.gridLayout_64.addWidget(self.scrollArea_2, 0, 0, 1, 1)


        self.gridLayout_56.addWidget(self.frame_19, 0, 0, 1, 1)


        self.formLayout_3.setLayout(0, QFormLayout.FieldRole, self.gridLayout_56)


        self.GRID_5.addWidget(self.frame_15, 1, 0, 1, 1)

        self.frame_21 = QFrame(self.innovation)
        self.frame_21.setObjectName(u"frame_21")
        self.frame_21.setMaximumSize(QSize(16777215, 100))
        self.frame_21.setFrameShape(QFrame.Shape.StyledPanel)
        self.frame_21.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_69 = QGridLayout(self.frame_21)
        self.gridLayout_69.setObjectName(u"gridLayout_69")
        self.horizontalLayout_12 = QHBoxLayout()
        self.horizontalLayout_12.setObjectName(u"horizontalLayout_12")
        self.label_85 = QLabel(self.frame_21)
        self.label_85.setObjectName(u"label_85")

        self.horizontalLayout_12.addWidget(self.label_85)

        self.crear_proyecto = QPushButton(self.frame_21)
        self.crear_proyecto.setObjectName(u"crear_proyecto")
        self.crear_proyecto.setMinimumSize(QSize(30, 30))
        self.crear_proyecto.setMaximumSize(QSize(170, 16777215))
        self.crear_proyecto.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_12.addWidget(self.crear_proyecto)

        self.crear_informe_5 = QPushButton(self.frame_21)
        self.crear_informe_5.setObjectName(u"crear_informe_5")
        self.crear_informe_5.setMinimumSize(QSize(30, 30))
        self.crear_informe_5.setMaximumSize(QSize(170, 16777215))
        self.crear_informe_5.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);\n"
"")

        self.horizontalLayout_12.addWidget(self.crear_informe_5)


        self.gridLayout_69.addLayout(self.horizontalLayout_12, 0, 0, 1, 1)


        self.GRID_5.addWidget(self.frame_21, 0, 0, 1, 1)


        self.gridLayout_70.addLayout(self.GRID_5, 0, 0, 1, 1)

        self.tabWidget.addTab(self.innovation, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.main_body.addWidget(self.contenido, 1, 1, 1, 1)

        self.main_body.setRowStretch(0, 1)

        self.gridLayout_2.addLayout(self.main_body, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(9)


        QMetaObject.connectSlotsByName(MainWindow)
    # setupUi

    def retranslateUi(self, MainWindow):
        MainWindow.setWindowTitle(QCoreApplication.translate("MainWindow", u"MainWindow", None))
        self.pushButton_3.setText("")
        self.pushButton_7.setText("")
        self.pushButton_6.setText("")
        self.pushButton_5.setText("")
        self.pushButton_4.setText("")
        self.pushButton_2.setText("")
        self.pushButton.setText("")
        self.label.setText(QCoreApplication.translate("MainWindow", u"LOGO", None))
        self.comboBox.setItemText(0, QCoreApplication.translate("MainWindow", u"NAVAS S.A", None))
        self.comboBox.setItemText(1, QCoreApplication.translate("MainWindow", u"Empresa 1", None))
        self.comboBox.setItemText(2, QCoreApplication.translate("MainWindow", u"Empresa 2", None))

        self.pushButton_9.setText("")
        self.pushButton_10.setText("")
        self.pushButton_8.setText("")
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Identificaci\u00f3n:", None))
        self.pass_label.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a:", None))
        self.Tit.setText(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"Usuario:", None))
        self.entry_button.setText(QCoreApplication.translate("MainWindow", u"Identificar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("MainWindow", u"Login", None))
        self.descargar_documentacion.setText(QCoreApplication.translate("MainWindow", u"Instrucciones de ingreso datos", None))
        self.boton_subir_archivo.setText(QCoreApplication.translate("MainWindow", u"Subir Archivo (.csv - .txt)", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.enter_data), QCoreApplication.translate("MainWindow", u"Enter_Data", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Ingresos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hoy:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"22.000\u20ac", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Home), QCoreApplication.translate("MainWindow", u"Home", None))
        ___qtablewidgetitem = self.tableWidget.horizontalHeaderItem(0)
        ___qtablewidgetitem.setText(QCoreApplication.translate("MainWindow", u"Id", None));
        ___qtablewidgetitem1 = self.tableWidget.horizontalHeaderItem(1)
        ___qtablewidgetitem1.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem2 = self.tableWidget.horizontalHeaderItem(2)
        ___qtablewidgetitem2.setText(QCoreApplication.translate("MainWindow", u"Ubicaci\u00f3n", None));
        ___qtablewidgetitem3 = self.tableWidget.horizontalHeaderItem(3)
        ___qtablewidgetitem3.setText(QCoreApplication.translate("MainWindow", u"Stock", None));
        ___qtablewidgetitem4 = self.tableWidget.horizontalHeaderItem(4)
        ___qtablewidgetitem4.setText(QCoreApplication.translate("MainWindow", u"Peso", None));

        __sortingEnabled = self.tableWidget.isSortingEnabled()
        self.tableWidget.setSortingEnabled(False)
        ___qtablewidgetitem5 = self.tableWidget.item(0, 0)
        ___qtablewidgetitem5.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem6 = self.tableWidget.item(0, 1)
        ___qtablewidgetitem6.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem7 = self.tableWidget.item(0, 2)
        ___qtablewidgetitem7.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem8 = self.tableWidget.item(0, 3)
        ___qtablewidgetitem8.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem9 = self.tableWidget.item(0, 4)
        ___qtablewidgetitem9.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem10 = self.tableWidget.item(0, 5)
        ___qtablewidgetitem10.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem11 = self.tableWidget.item(0, 6)
        ___qtablewidgetitem11.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem12 = self.tableWidget.item(1, 0)
        ___qtablewidgetitem12.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem13 = self.tableWidget.item(1, 1)
        ___qtablewidgetitem13.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem14 = self.tableWidget.item(1, 2)
        ___qtablewidgetitem14.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem15 = self.tableWidget.item(1, 3)
        ___qtablewidgetitem15.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem16 = self.tableWidget.item(1, 4)
        ___qtablewidgetitem16.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem17 = self.tableWidget.item(1, 5)
        ___qtablewidgetitem17.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem18 = self.tableWidget.item(1, 6)
        ___qtablewidgetitem18.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem19 = self.tableWidget.item(2, 0)
        ___qtablewidgetitem19.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem20 = self.tableWidget.item(2, 1)
        ___qtablewidgetitem20.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem21 = self.tableWidget.item(2, 2)
        ___qtablewidgetitem21.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem22 = self.tableWidget.item(2, 3)
        ___qtablewidgetitem22.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem23 = self.tableWidget.item(2, 4)
        ___qtablewidgetitem23.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem24 = self.tableWidget.item(2, 5)
        ___qtablewidgetitem24.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem25 = self.tableWidget.item(2, 6)
        ___qtablewidgetitem25.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem26 = self.tableWidget.item(3, 0)
        ___qtablewidgetitem26.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem27 = self.tableWidget.item(3, 1)
        ___qtablewidgetitem27.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem28 = self.tableWidget.item(3, 2)
        ___qtablewidgetitem28.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem29 = self.tableWidget.item(3, 3)
        ___qtablewidgetitem29.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem30 = self.tableWidget.item(3, 4)
        ___qtablewidgetitem30.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem31 = self.tableWidget.item(3, 5)
        ___qtablewidgetitem31.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem32 = self.tableWidget.item(3, 6)
        ___qtablewidgetitem32.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem33 = self.tableWidget.item(4, 0)
        ___qtablewidgetitem33.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem34 = self.tableWidget.item(4, 1)
        ___qtablewidgetitem34.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem35 = self.tableWidget.item(4, 2)
        ___qtablewidgetitem35.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem36 = self.tableWidget.item(4, 3)
        ___qtablewidgetitem36.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem37 = self.tableWidget.item(4, 4)
        ___qtablewidgetitem37.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem38 = self.tableWidget.item(4, 5)
        ___qtablewidgetitem38.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem39 = self.tableWidget.item(4, 6)
        ___qtablewidgetitem39.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem40 = self.tableWidget.item(5, 0)
        ___qtablewidgetitem40.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem41 = self.tableWidget.item(5, 1)
        ___qtablewidgetitem41.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem42 = self.tableWidget.item(5, 2)
        ___qtablewidgetitem42.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem43 = self.tableWidget.item(5, 3)
        ___qtablewidgetitem43.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem44 = self.tableWidget.item(5, 4)
        ___qtablewidgetitem44.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem45 = self.tableWidget.item(5, 5)
        ___qtablewidgetitem45.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem46 = self.tableWidget.item(5, 6)
        ___qtablewidgetitem46.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem47 = self.tableWidget.item(6, 0)
        ___qtablewidgetitem47.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem48 = self.tableWidget.item(6, 1)
        ___qtablewidgetitem48.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem49 = self.tableWidget.item(6, 2)
        ___qtablewidgetitem49.setText(QCoreApplication.translate("MainWindow", u"1.3.4", None));
        ___qtablewidgetitem50 = self.tableWidget.item(6, 3)
        ___qtablewidgetitem50.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem51 = self.tableWidget.item(6, 4)
        ___qtablewidgetitem51.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem52 = self.tableWidget.item(6, 5)
        ___qtablewidgetitem52.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem53 = self.tableWidget.item(6, 6)
        ___qtablewidgetitem53.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem54 = self.tableWidget.item(7, 0)
        ___qtablewidgetitem54.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem55 = self.tableWidget.item(7, 1)
        ___qtablewidgetitem55.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem56 = self.tableWidget.item(7, 2)
        ___qtablewidgetitem56.setText(QCoreApplication.translate("MainWindow", u"1.3.4", None));
        ___qtablewidgetitem57 = self.tableWidget.item(7, 3)
        ___qtablewidgetitem57.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem58 = self.tableWidget.item(7, 4)
        ___qtablewidgetitem58.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem59 = self.tableWidget.item(7, 5)
        ___qtablewidgetitem59.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem60 = self.tableWidget.item(7, 6)
        ___qtablewidgetitem60.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem61 = self.tableWidget.item(8, 0)
        ___qtablewidgetitem61.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem62 = self.tableWidget.item(8, 1)
        ___qtablewidgetitem62.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem63 = self.tableWidget.item(8, 2)
        ___qtablewidgetitem63.setText(QCoreApplication.translate("MainWindow", u"1.3.9", None));
        ___qtablewidgetitem64 = self.tableWidget.item(8, 3)
        ___qtablewidgetitem64.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem65 = self.tableWidget.item(8, 4)
        ___qtablewidgetitem65.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem66 = self.tableWidget.item(8, 5)
        ___qtablewidgetitem66.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem67 = self.tableWidget.item(8, 6)
        ___qtablewidgetitem67.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem68 = self.tableWidget.item(9, 0)
        ___qtablewidgetitem68.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem69 = self.tableWidget.item(9, 1)
        ___qtablewidgetitem69.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem70 = self.tableWidget.item(9, 2)
        ___qtablewidgetitem70.setText(QCoreApplication.translate("MainWindow", u"1.3.9", None));
        ___qtablewidgetitem71 = self.tableWidget.item(9, 3)
        ___qtablewidgetitem71.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem72 = self.tableWidget.item(9, 4)
        ___qtablewidgetitem72.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem73 = self.tableWidget.item(9, 5)
        ___qtablewidgetitem73.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem74 = self.tableWidget.item(9, 6)
        ___qtablewidgetitem74.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem75 = self.tableWidget.item(10, 0)
        ___qtablewidgetitem75.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem76 = self.tableWidget.item(10, 1)
        ___qtablewidgetitem76.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem77 = self.tableWidget.item(10, 2)
        ___qtablewidgetitem77.setText(QCoreApplication.translate("MainWindow", u"1.3.9", None));
        ___qtablewidgetitem78 = self.tableWidget.item(10, 3)
        ___qtablewidgetitem78.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem79 = self.tableWidget.item(10, 4)
        ___qtablewidgetitem79.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem80 = self.tableWidget.item(10, 5)
        ___qtablewidgetitem80.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem81 = self.tableWidget.item(10, 6)
        ___qtablewidgetitem81.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem82 = self.tableWidget.item(11, 0)
        ___qtablewidgetitem82.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem83 = self.tableWidget.item(11, 1)
        ___qtablewidgetitem83.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem84 = self.tableWidget.item(11, 2)
        ___qtablewidgetitem84.setText(QCoreApplication.translate("MainWindow", u"1.3.9", None));
        ___qtablewidgetitem85 = self.tableWidget.item(11, 3)
        ___qtablewidgetitem85.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem86 = self.tableWidget.item(11, 4)
        ___qtablewidgetitem86.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem87 = self.tableWidget.item(11, 5)
        ___qtablewidgetitem87.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem88 = self.tableWidget.item(11, 6)
        ___qtablewidgetitem88.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem89 = self.tableWidget.item(12, 0)
        ___qtablewidgetitem89.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem90 = self.tableWidget.item(12, 1)
        ___qtablewidgetitem90.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem91 = self.tableWidget.item(12, 2)
        ___qtablewidgetitem91.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem92 = self.tableWidget.item(12, 3)
        ___qtablewidgetitem92.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem93 = self.tableWidget.item(12, 4)
        ___qtablewidgetitem93.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem94 = self.tableWidget.item(12, 5)
        ___qtablewidgetitem94.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem95 = self.tableWidget.item(12, 6)
        ___qtablewidgetitem95.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem96 = self.tableWidget.item(13, 0)
        ___qtablewidgetitem96.setText(QCoreApplication.translate("MainWindow", u"14", None));
        ___qtablewidgetitem97 = self.tableWidget.item(13, 1)
        ___qtablewidgetitem97.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem98 = self.tableWidget.item(13, 2)
        ___qtablewidgetitem98.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem99 = self.tableWidget.item(13, 3)
        ___qtablewidgetitem99.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem100 = self.tableWidget.item(13, 4)
        ___qtablewidgetitem100.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem101 = self.tableWidget.item(13, 5)
        ___qtablewidgetitem101.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem102 = self.tableWidget.item(13, 6)
        ___qtablewidgetitem102.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem103 = self.tableWidget.item(14, 0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"15", None));
        ___qtablewidgetitem104 = self.tableWidget.item(14, 1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem105 = self.tableWidget.item(14, 2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem106 = self.tableWidget.item(14, 3)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem107 = self.tableWidget.item(14, 4)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem108 = self.tableWidget.item(14, 5)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem109 = self.tableWidget.item(14, 6)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem110 = self.tableWidget.item(15, 0)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"16", None));
        ___qtablewidgetitem111 = self.tableWidget.item(15, 1)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem112 = self.tableWidget.item(15, 2)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem113 = self.tableWidget.item(15, 3)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem114 = self.tableWidget.item(15, 4)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem115 = self.tableWidget.item(15, 5)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem116 = self.tableWidget.item(15, 6)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem117 = self.tableWidget.item(16, 0)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"17", None));
        ___qtablewidgetitem118 = self.tableWidget.item(16, 1)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem119 = self.tableWidget.item(16, 2)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem120 = self.tableWidget.item(16, 3)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem121 = self.tableWidget.item(16, 4)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem122 = self.tableWidget.item(16, 5)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem123 = self.tableWidget.item(16, 6)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem124 = self.tableWidget.item(17, 0)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"18", None));
        ___qtablewidgetitem125 = self.tableWidget.item(17, 1)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem126 = self.tableWidget.item(17, 2)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem127 = self.tableWidget.item(17, 3)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem128 = self.tableWidget.item(17, 4)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem129 = self.tableWidget.item(17, 5)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem130 = self.tableWidget.item(17, 6)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem131 = self.tableWidget.item(18, 0)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"19", None));
        ___qtablewidgetitem132 = self.tableWidget.item(18, 1)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem133 = self.tableWidget.item(18, 2)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem134 = self.tableWidget.item(18, 3)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem135 = self.tableWidget.item(18, 4)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem136 = self.tableWidget.item(18, 5)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem137 = self.tableWidget.item(18, 6)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        ___qtablewidgetitem138 = self.tableWidget.item(19, 0)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"20", None));
        ___qtablewidgetitem139 = self.tableWidget.item(19, 1)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem140 = self.tableWidget.item(19, 2)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"1.3.2", None));
        ___qtablewidgetitem141 = self.tableWidget.item(19, 3)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"50", None));
        ___qtablewidgetitem142 = self.tableWidget.item(19, 4)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"10kg", None));
        ___qtablewidgetitem143 = self.tableWidget.item(19, 5)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"Automatizar", None));
        ___qtablewidgetitem144 = self.tableWidget.item(19, 6)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"Ordenar", None));
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.boton_filtrar.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.crear_suministro.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.crear_informe.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory), QCoreApplication.translate("MainWindow", u"Inventory", None))
        ___qtablewidgetitem145 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"N\u00ba Orden", None));
        ___qtablewidgetitem146 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem147 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"Fecha Orden", None));
        ___qtablewidgetitem148 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem149 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"Precio/u", None));
        ___qtablewidgetitem150 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"Unidad", None));
        ___qtablewidgetitem151 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem152 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"Estado", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem153 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem154 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem155 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem156 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem157 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem158 = self.tableWidget_2.item(0, 5)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem159 = self.tableWidget_2.item(0, 6)
        ___qtablewidgetitem159.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem160 = self.tableWidget_2.item(0, 7)
        ___qtablewidgetitem160.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem161 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem161.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem162 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem162.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem163 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem163.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem164 = self.tableWidget_2.item(1, 3)
        ___qtablewidgetitem164.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem165 = self.tableWidget_2.item(1, 4)
        ___qtablewidgetitem165.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem166 = self.tableWidget_2.item(1, 5)
        ___qtablewidgetitem166.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem167 = self.tableWidget_2.item(1, 6)
        ___qtablewidgetitem167.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem168 = self.tableWidget_2.item(1, 7)
        ___qtablewidgetitem168.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem169 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem169.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem170 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem170.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem171 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem171.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem172 = self.tableWidget_2.item(2, 3)
        ___qtablewidgetitem172.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem173 = self.tableWidget_2.item(2, 4)
        ___qtablewidgetitem173.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem174 = self.tableWidget_2.item(2, 5)
        ___qtablewidgetitem174.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem175 = self.tableWidget_2.item(2, 6)
        ___qtablewidgetitem175.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem176 = self.tableWidget_2.item(2, 7)
        ___qtablewidgetitem176.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem177 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem177.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem178 = self.tableWidget_2.item(3, 1)
        ___qtablewidgetitem178.setText(QCoreApplication.translate("MainWindow", u"Proveedor C", None));
        ___qtablewidgetitem179 = self.tableWidget_2.item(3, 2)
        ___qtablewidgetitem179.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem180 = self.tableWidget_2.item(3, 3)
        ___qtablewidgetitem180.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem181 = self.tableWidget_2.item(3, 4)
        ___qtablewidgetitem181.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem182 = self.tableWidget_2.item(3, 5)
        ___qtablewidgetitem182.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem183 = self.tableWidget_2.item(3, 6)
        ___qtablewidgetitem183.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem184 = self.tableWidget_2.item(3, 7)
        ___qtablewidgetitem184.setText(QCoreApplication.translate("MainWindow", u"En tr\u00e1nsito", None));
        ___qtablewidgetitem185 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem185.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem186 = self.tableWidget_2.item(4, 1)
        ___qtablewidgetitem186.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem187 = self.tableWidget_2.item(4, 2)
        ___qtablewidgetitem187.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem188 = self.tableWidget_2.item(4, 3)
        ___qtablewidgetitem188.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem189 = self.tableWidget_2.item(4, 4)
        ___qtablewidgetitem189.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem190 = self.tableWidget_2.item(4, 5)
        ___qtablewidgetitem190.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem191 = self.tableWidget_2.item(4, 6)
        ___qtablewidgetitem191.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem192 = self.tableWidget_2.item(4, 7)
        ___qtablewidgetitem192.setText(QCoreApplication.translate("MainWindow", u"En tr\u00e1nsito", None));
        ___qtablewidgetitem193 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem193.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem194 = self.tableWidget_2.item(5, 1)
        ___qtablewidgetitem194.setText(QCoreApplication.translate("MainWindow", u"Proveedor B", None));
        ___qtablewidgetitem195 = self.tableWidget_2.item(5, 2)
        ___qtablewidgetitem195.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem196 = self.tableWidget_2.item(5, 3)
        ___qtablewidgetitem196.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem197 = self.tableWidget_2.item(5, 4)
        ___qtablewidgetitem197.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem198 = self.tableWidget_2.item(5, 5)
        ___qtablewidgetitem198.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem199 = self.tableWidget_2.item(5, 6)
        ___qtablewidgetitem199.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem200 = self.tableWidget_2.item(5, 7)
        ___qtablewidgetitem200.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_8.setText(QCoreApplication.translate("MainWindow", u"-5080\u20ac", None))
        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gastos por mes:", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Buscador", None))
        self.boton_filtrar_2.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.crear_recordatorio.setText(QCoreApplication.translate("MainWindow", u"Crear recordatorio", None))
        self.crear_informe_2.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Buys), QCoreApplication.translate("MainWindow", u"Buys", None))
        ___qtablewidgetitem201 = self.tableWidget_3.horizontalHeaderItem(0)
        ___qtablewidgetitem201.setText(QCoreApplication.translate("MainWindow", u"ID", None));
        ___qtablewidgetitem202 = self.tableWidget_3.horizontalHeaderItem(1)
        ___qtablewidgetitem202.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem203 = self.tableWidget_3.horizontalHeaderItem(2)
        ___qtablewidgetitem203.setText(QCoreApplication.translate("MainWindow", u"Comprador", None));
        ___qtablewidgetitem204 = self.tableWidget_3.horizontalHeaderItem(3)
        ___qtablewidgetitem204.setText(QCoreApplication.translate("MainWindow", u"Fecha", None));
        ___qtablewidgetitem205 = self.tableWidget_3.horizontalHeaderItem(4)
        ___qtablewidgetitem205.setText(QCoreApplication.translate("MainWindow", u"Actividad", None));
        ___qtablewidgetitem206 = self.tableWidget_3.horizontalHeaderItem(5)
        ___qtablewidgetitem206.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem207 = self.tableWidget_3.horizontalHeaderItem(6)
        ___qtablewidgetitem207.setText(QCoreApplication.translate("MainWindow", u"Estado", None));

        __sortingEnabled2 = self.tableWidget_3.isSortingEnabled()
        self.tableWidget_3.setSortingEnabled(False)
        ___qtablewidgetitem208 = self.tableWidget_3.item(0, 0)
        ___qtablewidgetitem208.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem209 = self.tableWidget_3.item(0, 1)
        ___qtablewidgetitem209.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem210 = self.tableWidget_3.item(0, 2)
        ___qtablewidgetitem210.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem211 = self.tableWidget_3.item(0, 3)
        ___qtablewidgetitem211.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem212 = self.tableWidget_3.item(0, 4)
        ___qtablewidgetitem212.setText(QCoreApplication.translate("MainWindow", u"LLamada", None));
        ___qtablewidgetitem213 = self.tableWidget_3.item(0, 5)
        ___qtablewidgetitem213.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem214 = self.tableWidget_3.item(0, 6)
        ___qtablewidgetitem214.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem215 = self.tableWidget_3.item(1, 0)
        ___qtablewidgetitem215.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem216 = self.tableWidget_3.item(1, 1)
        ___qtablewidgetitem216.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem217 = self.tableWidget_3.item(1, 2)
        ___qtablewidgetitem217.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem218 = self.tableWidget_3.item(1, 3)
        ___qtablewidgetitem218.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem219 = self.tableWidget_3.item(1, 4)
        ___qtablewidgetitem219.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None));
        ___qtablewidgetitem220 = self.tableWidget_3.item(1, 5)
        ___qtablewidgetitem220.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem221 = self.tableWidget_3.item(1, 6)
        ___qtablewidgetitem221.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem222 = self.tableWidget_3.item(2, 0)
        ___qtablewidgetitem222.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem223 = self.tableWidget_3.item(2, 1)
        ___qtablewidgetitem223.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem224 = self.tableWidget_3.item(2, 2)
        ___qtablewidgetitem224.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem225 = self.tableWidget_3.item(2, 3)
        ___qtablewidgetitem225.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem226 = self.tableWidget_3.item(2, 4)
        ___qtablewidgetitem226.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        ___qtablewidgetitem227 = self.tableWidget_3.item(2, 5)
        ___qtablewidgetitem227.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem228 = self.tableWidget_3.item(2, 6)
        ___qtablewidgetitem228.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem229 = self.tableWidget_3.item(3, 0)
        ___qtablewidgetitem229.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem230 = self.tableWidget_3.item(3, 1)
        ___qtablewidgetitem230.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem231 = self.tableWidget_3.item(3, 2)
        ___qtablewidgetitem231.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem232 = self.tableWidget_3.item(3, 3)
        ___qtablewidgetitem232.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem233 = self.tableWidget_3.item(3, 4)
        ___qtablewidgetitem233.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None));
        ___qtablewidgetitem234 = self.tableWidget_3.item(3, 5)
        ___qtablewidgetitem234.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem235 = self.tableWidget_3.item(3, 6)
        ___qtablewidgetitem235.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem236 = self.tableWidget_3.item(4, 0)
        ___qtablewidgetitem236.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem237 = self.tableWidget_3.item(4, 1)
        ___qtablewidgetitem237.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem238 = self.tableWidget_3.item(4, 2)
        ___qtablewidgetitem238.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem239 = self.tableWidget_3.item(4, 3)
        ___qtablewidgetitem239.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem240 = self.tableWidget_3.item(4, 4)
        ___qtablewidgetitem240.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None));
        ___qtablewidgetitem241 = self.tableWidget_3.item(4, 5)
        ___qtablewidgetitem241.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem242 = self.tableWidget_3.item(4, 6)
        ___qtablewidgetitem242.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem243 = self.tableWidget_3.item(5, 0)
        ___qtablewidgetitem243.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem244 = self.tableWidget_3.item(5, 1)
        ___qtablewidgetitem244.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem245 = self.tableWidget_3.item(5, 2)
        ___qtablewidgetitem245.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem246 = self.tableWidget_3.item(5, 3)
        ___qtablewidgetitem246.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem247 = self.tableWidget_3.item(5, 4)
        ___qtablewidgetitem247.setText(QCoreApplication.translate("MainWindow", u"Confirmar", None));
        ___qtablewidgetitem248 = self.tableWidget_3.item(5, 5)
        ___qtablewidgetitem248.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem249 = self.tableWidget_3.item(5, 6)
        ___qtablewidgetitem249.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem250 = self.tableWidget_3.item(6, 0)
        ___qtablewidgetitem250.setText(QCoreApplication.translate("MainWindow", u"7", None));
        ___qtablewidgetitem251 = self.tableWidget_3.item(6, 1)
        ___qtablewidgetitem251.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem252 = self.tableWidget_3.item(6, 2)
        ___qtablewidgetitem252.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem253 = self.tableWidget_3.item(6, 3)
        ___qtablewidgetitem253.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem254 = self.tableWidget_3.item(6, 4)
        ___qtablewidgetitem254.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        ___qtablewidgetitem255 = self.tableWidget_3.item(6, 5)
        ___qtablewidgetitem255.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem256 = self.tableWidget_3.item(6, 6)
        ___qtablewidgetitem256.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem257 = self.tableWidget_3.item(7, 0)
        ___qtablewidgetitem257.setText(QCoreApplication.translate("MainWindow", u"8", None));
        ___qtablewidgetitem258 = self.tableWidget_3.item(7, 1)
        ___qtablewidgetitem258.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem259 = self.tableWidget_3.item(7, 2)
        ___qtablewidgetitem259.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem260 = self.tableWidget_3.item(7, 3)
        ___qtablewidgetitem260.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem261 = self.tableWidget_3.item(7, 4)
        ___qtablewidgetitem261.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        ___qtablewidgetitem262 = self.tableWidget_3.item(7, 5)
        ___qtablewidgetitem262.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem263 = self.tableWidget_3.item(7, 6)
        ___qtablewidgetitem263.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem264 = self.tableWidget_3.item(8, 0)
        ___qtablewidgetitem264.setText(QCoreApplication.translate("MainWindow", u"9", None));
        ___qtablewidgetitem265 = self.tableWidget_3.item(8, 1)
        ___qtablewidgetitem265.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem266 = self.tableWidget_3.item(8, 2)
        ___qtablewidgetitem266.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem267 = self.tableWidget_3.item(8, 3)
        ___qtablewidgetitem267.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem268 = self.tableWidget_3.item(8, 4)
        ___qtablewidgetitem268.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        ___qtablewidgetitem269 = self.tableWidget_3.item(8, 5)
        ___qtablewidgetitem269.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem270 = self.tableWidget_3.item(8, 6)
        ___qtablewidgetitem270.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem271 = self.tableWidget_3.item(9, 0)
        ___qtablewidgetitem271.setText(QCoreApplication.translate("MainWindow", u"10", None));
        ___qtablewidgetitem272 = self.tableWidget_3.item(9, 1)
        ___qtablewidgetitem272.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem273 = self.tableWidget_3.item(9, 2)
        ___qtablewidgetitem273.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem274 = self.tableWidget_3.item(9, 3)
        ___qtablewidgetitem274.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem275 = self.tableWidget_3.item(9, 4)
        ___qtablewidgetitem275.setText(QCoreApplication.translate("MainWindow", u"LLamada", None));
        ___qtablewidgetitem276 = self.tableWidget_3.item(9, 5)
        ___qtablewidgetitem276.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem277 = self.tableWidget_3.item(9, 6)
        ___qtablewidgetitem277.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem278 = self.tableWidget_3.item(10, 0)
        ___qtablewidgetitem278.setText(QCoreApplication.translate("MainWindow", u"11", None));
        ___qtablewidgetitem279 = self.tableWidget_3.item(10, 1)
        ___qtablewidgetitem279.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem280 = self.tableWidget_3.item(10, 2)
        ___qtablewidgetitem280.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem281 = self.tableWidget_3.item(10, 3)
        ___qtablewidgetitem281.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem282 = self.tableWidget_3.item(10, 4)
        ___qtablewidgetitem282.setText(QCoreApplication.translate("MainWindow", u"LLamada", None));
        ___qtablewidgetitem283 = self.tableWidget_3.item(10, 5)
        ___qtablewidgetitem283.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem284 = self.tableWidget_3.item(10, 6)
        ___qtablewidgetitem284.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem285 = self.tableWidget_3.item(11, 0)
        ___qtablewidgetitem285.setText(QCoreApplication.translate("MainWindow", u"12", None));
        ___qtablewidgetitem286 = self.tableWidget_3.item(11, 1)
        ___qtablewidgetitem286.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem287 = self.tableWidget_3.item(11, 2)
        ___qtablewidgetitem287.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem288 = self.tableWidget_3.item(11, 3)
        ___qtablewidgetitem288.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem289 = self.tableWidget_3.item(11, 4)
        ___qtablewidgetitem289.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        ___qtablewidgetitem290 = self.tableWidget_3.item(11, 5)
        ___qtablewidgetitem290.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem291 = self.tableWidget_3.item(11, 6)
        ___qtablewidgetitem291.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        ___qtablewidgetitem292 = self.tableWidget_3.item(12, 0)
        ___qtablewidgetitem292.setText(QCoreApplication.translate("MainWindow", u"13", None));
        ___qtablewidgetitem293 = self.tableWidget_3.item(12, 1)
        ___qtablewidgetitem293.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem294 = self.tableWidget_3.item(12, 2)
        ___qtablewidgetitem294.setText(QCoreApplication.translate("MainWindow", u"Azure", None));
        ___qtablewidgetitem295 = self.tableWidget_3.item(12, 3)
        ___qtablewidgetitem295.setText(QCoreApplication.translate("MainWindow", u"En 2 dias", None));
        ___qtablewidgetitem296 = self.tableWidget_3.item(12, 4)
        ___qtablewidgetitem296.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        ___qtablewidgetitem297 = self.tableWidget_3.item(12, 5)
        ___qtablewidgetitem297.setText(QCoreApplication.translate("MainWindow", u"215\u20ac", None));
        ___qtablewidgetitem298 = self.tableWidget_3.item(12, 6)
        ___qtablewidgetitem298.setText(QCoreApplication.translate("MainWindow", u"Orden compra", None));
        self.tableWidget_3.setSortingEnabled(__sortingEnabled2)

        self.label_9.setText(QCoreApplication.translate("MainWindow", u"Ventas", None))
        self.lineEdit_5.setText(QCoreApplication.translate("MainWindow", u"Buscador", None))
        self.pushButton_15.setText(QCoreApplication.translate("MainWindow", u"Total: 12.000\u20ac", None))
        self.pushButton_14.setText(QCoreApplication.translate("MainWindow", u"Pendientes: 6", None))
        self.pushButton_13.setText(QCoreApplication.translate("MainWindow", u"Ventas por cliente: 1.23", None))
        self.pushButton_12.setText(QCoreApplication.translate("MainWindow", u"Producto m\u00e1s vendido: ID: 5", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.sales), QCoreApplication.translate("MainWindow", u"Sales", None))
        ___qtablewidgetitem299 = self.tableWidget_12.horizontalHeaderItem(0)
        ___qtablewidgetitem299.setText(QCoreApplication.translate("MainWindow", u"N\u00ba Orden", None));
        ___qtablewidgetitem300 = self.tableWidget_12.horizontalHeaderItem(1)
        ___qtablewidgetitem300.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem301 = self.tableWidget_12.horizontalHeaderItem(2)
        ___qtablewidgetitem301.setText(QCoreApplication.translate("MainWindow", u"Fecha Orden", None));
        ___qtablewidgetitem302 = self.tableWidget_12.horizontalHeaderItem(3)
        ___qtablewidgetitem302.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem303 = self.tableWidget_12.horizontalHeaderItem(4)
        ___qtablewidgetitem303.setText(QCoreApplication.translate("MainWindow", u"Precio/u", None));
        ___qtablewidgetitem304 = self.tableWidget_12.horizontalHeaderItem(5)
        ___qtablewidgetitem304.setText(QCoreApplication.translate("MainWindow", u"Unidad", None));
        ___qtablewidgetitem305 = self.tableWidget_12.horizontalHeaderItem(6)
        ___qtablewidgetitem305.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem306 = self.tableWidget_12.horizontalHeaderItem(7)
        ___qtablewidgetitem306.setText(QCoreApplication.translate("MainWindow", u"Estado", None));

        __sortingEnabled3 = self.tableWidget_12.isSortingEnabled()
        self.tableWidget_12.setSortingEnabled(False)
        ___qtablewidgetitem307 = self.tableWidget_12.item(0, 0)
        ___qtablewidgetitem307.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem308 = self.tableWidget_12.item(0, 1)
        ___qtablewidgetitem308.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem309 = self.tableWidget_12.item(0, 2)
        ___qtablewidgetitem309.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem310 = self.tableWidget_12.item(0, 3)
        ___qtablewidgetitem310.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem311 = self.tableWidget_12.item(0, 4)
        ___qtablewidgetitem311.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem312 = self.tableWidget_12.item(0, 5)
        ___qtablewidgetitem312.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem313 = self.tableWidget_12.item(0, 6)
        ___qtablewidgetitem313.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem314 = self.tableWidget_12.item(0, 7)
        ___qtablewidgetitem314.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem315 = self.tableWidget_12.item(1, 0)
        ___qtablewidgetitem315.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem316 = self.tableWidget_12.item(1, 1)
        ___qtablewidgetitem316.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem317 = self.tableWidget_12.item(1, 2)
        ___qtablewidgetitem317.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem318 = self.tableWidget_12.item(1, 3)
        ___qtablewidgetitem318.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem319 = self.tableWidget_12.item(1, 4)
        ___qtablewidgetitem319.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem320 = self.tableWidget_12.item(1, 5)
        ___qtablewidgetitem320.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem321 = self.tableWidget_12.item(1, 6)
        ___qtablewidgetitem321.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem322 = self.tableWidget_12.item(1, 7)
        ___qtablewidgetitem322.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem323 = self.tableWidget_12.item(2, 0)
        ___qtablewidgetitem323.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem324 = self.tableWidget_12.item(2, 1)
        ___qtablewidgetitem324.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem325 = self.tableWidget_12.item(2, 2)
        ___qtablewidgetitem325.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem326 = self.tableWidget_12.item(2, 3)
        ___qtablewidgetitem326.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem327 = self.tableWidget_12.item(2, 4)
        ___qtablewidgetitem327.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem328 = self.tableWidget_12.item(2, 5)
        ___qtablewidgetitem328.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem329 = self.tableWidget_12.item(2, 6)
        ___qtablewidgetitem329.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem330 = self.tableWidget_12.item(2, 7)
        ___qtablewidgetitem330.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem331 = self.tableWidget_12.item(3, 0)
        ___qtablewidgetitem331.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem332 = self.tableWidget_12.item(3, 1)
        ___qtablewidgetitem332.setText(QCoreApplication.translate("MainWindow", u"Proveedor C", None));
        ___qtablewidgetitem333 = self.tableWidget_12.item(3, 2)
        ___qtablewidgetitem333.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem334 = self.tableWidget_12.item(3, 3)
        ___qtablewidgetitem334.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem335 = self.tableWidget_12.item(3, 4)
        ___qtablewidgetitem335.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem336 = self.tableWidget_12.item(3, 5)
        ___qtablewidgetitem336.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem337 = self.tableWidget_12.item(3, 6)
        ___qtablewidgetitem337.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem338 = self.tableWidget_12.item(3, 7)
        ___qtablewidgetitem338.setText(QCoreApplication.translate("MainWindow", u"En tr\u00e1nsito", None));
        ___qtablewidgetitem339 = self.tableWidget_12.item(4, 0)
        ___qtablewidgetitem339.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem340 = self.tableWidget_12.item(4, 1)
        ___qtablewidgetitem340.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem341 = self.tableWidget_12.item(4, 2)
        ___qtablewidgetitem341.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem342 = self.tableWidget_12.item(4, 3)
        ___qtablewidgetitem342.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem343 = self.tableWidget_12.item(4, 4)
        ___qtablewidgetitem343.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem344 = self.tableWidget_12.item(4, 5)
        ___qtablewidgetitem344.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem345 = self.tableWidget_12.item(4, 6)
        ___qtablewidgetitem345.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem346 = self.tableWidget_12.item(4, 7)
        ___qtablewidgetitem346.setText(QCoreApplication.translate("MainWindow", u"En tr\u00e1nsito", None));
        ___qtablewidgetitem347 = self.tableWidget_12.item(5, 0)
        ___qtablewidgetitem347.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem348 = self.tableWidget_12.item(5, 1)
        ___qtablewidgetitem348.setText(QCoreApplication.translate("MainWindow", u"Proveedor B", None));
        ___qtablewidgetitem349 = self.tableWidget_12.item(5, 2)
        ___qtablewidgetitem349.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem350 = self.tableWidget_12.item(5, 3)
        ___qtablewidgetitem350.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem351 = self.tableWidget_12.item(5, 4)
        ___qtablewidgetitem351.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem352 = self.tableWidget_12.item(5, 5)
        ___qtablewidgetitem352.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem353 = self.tableWidget_12.item(5, 6)
        ___qtablewidgetitem353.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem354 = self.tableWidget_12.item(5, 7)
        ___qtablewidgetitem354.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        self.tableWidget_12.setSortingEnabled(__sortingEnabled3)

        self.label_36.setText(QCoreApplication.translate("MainWindow", u"-5080\u20ac", None))
        self.label_37.setText(QCoreApplication.translate("MainWindow", u"Gastos por mes:", None))
        self.label_38.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.label_42.setText(QCoreApplication.translate("MainWindow", u"Total:", None))
        self.label_41.setText(QCoreApplication.translate("MainWindow", u"Gastos por mes:", None))
        self.label_49.setText(QCoreApplication.translate("MainWindow", u"-5080\u20ac", None))
        self.label_50.setText(QCoreApplication.translate("MainWindow", u"Ingresos:", None))
        self.label_40.setText(QCoreApplication.translate("MainWindow", u"+5.720", None))
        self.label_51.setText(QCoreApplication.translate("MainWindow", u"10.800\u20ac", None))
        self.label_39.setText(QCoreApplication.translate("MainWindow", u"Finanzas", None))
        self.boton_filtrar_3.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.crear_recordatorio_4.setText(QCoreApplication.translate("MainWindow", u"Crear recordatorio", None))
        self.crear_informe_4.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.finance), QCoreApplication.translate("MainWindow", u"finance", None))
        self.label_60.setText("")
        self.label_61.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_62.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_63.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_64.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_65.setText("")
        self.label_66.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_67.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_68.setText("")
        self.label_14.setText("")
        self.label_15.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_16.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_23.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_24.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_25.setText("")
        self.label_26.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_27.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_28.setText("")
        self.label_32.setText("")
        self.label_33.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_34.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_35.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_43.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_44.setText("")
        self.label_45.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_46.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_47.setText("")
        self.label_11.setText("")
        self.label_12.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_13.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_20.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_21.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_22.setText("")
        self.label_17.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_18.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_19.setText("")
        self.label_48.setText("")
        self.label_52.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_53.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_54.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_55.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_56.setText("")
        self.label_57.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_58.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_59.setText("")
        self.label_69.setText("")
        self.label_70.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_71.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_72.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_73.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_74.setText("")
        self.label_75.setText(QCoreApplication.translate("MainWindow", u"Nombre", None))
        self.label_76.setText(QCoreApplication.translate("MainWindow", u"Profesi\u00f3n", None))
        self.label_77.setText("")
        self.label_10.setText(QCoreApplication.translate("MainWindow", u"Recursos Humanos", None))
        self.lineEdit_6.setText(QCoreApplication.translate("MainWindow", u"Buscador", None))
        self.boton_actualizacion.setText(QCoreApplication.translate("MainWindow", u"Vista Avanzada", None))
        self.crear_informe_3.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.rrhh), QCoreApplication.translate("MainWindow", u"RRHH", None))
        self.label_79.setText(QCoreApplication.translate("MainWindow", u"Marketing Electr\u00f3nico", None))
        self.label_80.setText(QCoreApplication.translate("MainWindow", u"Recibidos", None))
        self.label_78.setText(QCoreApplication.translate("MainWindow", u"5", None))
        self.label_81.setText(QCoreApplication.translate("MainWindow", u"Marketing Electr\u00f3nico", None))
        self.crear_auto.setText(QCoreApplication.translate("MainWindow", u"Crear Automatizaci\u00f3n", None))
        self.crear_informe_7.setText(QCoreApplication.translate("MainWindow", u"Crear Informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.marketing), QCoreApplication.translate("MainWindow", u"Marketing", None))
        self.label_82.setText(QCoreApplication.translate("MainWindow", u"Proyectos", None))
        self.label_112.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_113.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_29.setText("")
        self.label_110.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_111.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_28.setText("")
        self.label_108.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_109.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_27.setText("")
        self.label_88.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_89.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_18.setText("")
        self.label_86.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_87.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_17.setText("")
        self.label_83.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_84.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_16.setText("")
        self.label_104.setText(QCoreApplication.translate("MainWindow", u"Nombre Proyecto", None))
        self.label_105.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_25.setText("")
        self.label_90.setText(QCoreApplication.translate("MainWindow", u"Informes", None))
        self.label_118.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_119.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_32.setText("")
        self.label_116.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_117.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_31.setText("")
        self.label_114.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_115.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_30.setText("")
        self.label_91.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_92.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_19.setText("")
        self.label_93.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_94.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_20.setText("")
        self.label_95.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_96.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_21.setText("")
        self.label_106.setText(QCoreApplication.translate("MainWindow", u"Nombre Informe", None))
        self.label_107.setText(QCoreApplication.translate("MainWindow", u"Departamento", None))
        self.pushButton_26.setText("")
        self.label_85.setText(QCoreApplication.translate("MainWindow", u"Innovaci\u00f3n", None))
        self.crear_proyecto.setText(QCoreApplication.translate("MainWindow", u"Crear Proyecto", None))
        self.crear_informe_5.setText(QCoreApplication.translate("MainWindow", u"Crear Informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.innovation), QCoreApplication.translate("MainWindow", u"Innovation", None))
    # retranslateUi

