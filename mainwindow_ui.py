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
    QMainWindow, QProgressBar, QPushButton, QSizePolicy,
    QTabWidget, QTableWidget, QTableWidgetItem, QVBoxLayout,
    QWidget)

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
        font1.setFamilies([u"Verdana"])
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
        font2.setFamilies([u"Verdana"])
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
        self.Inventario = QWidget()
        self.Inventario.setObjectName(u"Inventario")
        self.gridLayout_9 = QGridLayout(self.Inventario)
        self.gridLayout_9.setObjectName(u"gridLayout_9")
        self.GRID = QGridLayout()
        self.GRID.setObjectName(u"GRID")
        self.frame_3 = QFrame(self.Inventario)
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

        self.graphic = QFrame(self.Inventario)
        self.graphic.setObjectName(u"graphic")
        self.graphic.setFrameShape(QFrame.Shape.StyledPanel)
        self.graphic.setFrameShadow(QFrame.Shadow.Raised)
        self.gridLayout_14 = QGridLayout(self.graphic)
        self.gridLayout_14.setObjectName(u"gridLayout_14")
        self.grid_graphic = QGridLayout()
        self.grid_graphic.setObjectName(u"grid_graphic")

        self.gridLayout_14.addLayout(self.grid_graphic, 0, 0, 1, 1)


        self.GRID.addWidget(self.graphic, 1, 1, 1, 1)

        self.frame_4 = QFrame(self.Inventario)
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

        self.tabWidget.addTab(self.Inventario, "")
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
        self.tableWidget = QTableWidget(self.frame_2)
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
        if (self.tableWidget.rowCount() < 14):
            self.tableWidget.setRowCount(14)
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
        icon9 = QIcon()
        icon9.addFile(u"icons/icons8-automation-32.png", QSize(), QIcon.Mode.Normal, QIcon.State.Off)
        __qtablewidgetitem12 = QTableWidgetItem()
        __qtablewidgetitem12.setIcon(icon9);
        self.tableWidget.setItem(0, 5, __qtablewidgetitem12)
        icon10 = QIcon(QIcon.fromTheme(u"accessories-calculator"))
        __qtablewidgetitem13 = QTableWidgetItem()
        __qtablewidgetitem13.setIcon(icon10);
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
        __qtablewidgetitem19 = QTableWidgetItem()
        self.tableWidget.setItem(1, 5, __qtablewidgetitem19)
        __qtablewidgetitem20 = QTableWidgetItem()
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
        self.tableWidget.setItem(2, 5, __qtablewidgetitem26)
        __qtablewidgetitem27 = QTableWidgetItem()
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
        self.tableWidget.setItem(3, 5, __qtablewidgetitem33)
        __qtablewidgetitem34 = QTableWidgetItem()
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
        self.tableWidget.setItem(4, 5, __qtablewidgetitem40)
        __qtablewidgetitem41 = QTableWidgetItem()
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
        self.tableWidget.setItem(5, 5, __qtablewidgetitem47)
        __qtablewidgetitem48 = QTableWidgetItem()
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
        self.tableWidget.setItem(6, 5, __qtablewidgetitem54)
        __qtablewidgetitem55 = QTableWidgetItem()
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
        self.tableWidget.setItem(7, 5, __qtablewidgetitem61)
        __qtablewidgetitem62 = QTableWidgetItem()
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
        self.tableWidget.setItem(8, 5, __qtablewidgetitem68)
        __qtablewidgetitem69 = QTableWidgetItem()
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
        self.tableWidget.setItem(9, 5, __qtablewidgetitem75)
        __qtablewidgetitem76 = QTableWidgetItem()
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
        self.tableWidget.setItem(10, 5, __qtablewidgetitem82)
        __qtablewidgetitem83 = QTableWidgetItem()
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
        self.tableWidget.setItem(11, 5, __qtablewidgetitem89)
        __qtablewidgetitem90 = QTableWidgetItem()
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
        self.tableWidget.setItem(12, 5, __qtablewidgetitem96)
        __qtablewidgetitem97 = QTableWidgetItem()
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
        self.tableWidget.setItem(13, 5, __qtablewidgetitem103)
        __qtablewidgetitem104 = QTableWidgetItem()
        self.tableWidget.setItem(13, 6, __qtablewidgetitem104)
        self.tableWidget.setObjectName(u"tableWidget")
        self.tableWidget.setLayoutDirection(Qt.LayoutDirection.LeftToRight)
        self.tableWidget.setSizeAdjustPolicy(QAbstractScrollArea.SizeAdjustPolicy.AdjustIgnored)
        self.tableWidget.setEditTriggers(QAbstractItemView.EditTrigger.NoEditTriggers)
        self.tableWidget.setAlternatingRowColors(True)
        self.tableWidget.setIconSize(QSize(0, 0))
        self.tableWidget.setGridStyle(Qt.PenStyle.DashLine)
        self.tableWidget.setRowCount(14)
        self.tableWidget.setColumnCount(7)
        self.tableWidget.horizontalHeader().setVisible(True)
        self.tableWidget.horizontalHeader().setCascadingSectionResizes(False)
        self.tableWidget.horizontalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.horizontalHeader().setStretchLastSection(True)
        self.tableWidget.verticalHeader().setVisible(False)
        self.tableWidget.verticalHeader().setCascadingSectionResizes(False)
        self.tableWidget.verticalHeader().setProperty(u"showSortIndicator", False)
        self.tableWidget.verticalHeader().setStretchLastSection(False)

        self.gridLayout_18.addWidget(self.tableWidget, 0, 0, 1, 1)


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
        self.boton_filtrar.setMaximumSize(QSize(100, 16777215))
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
        self.crear_suministro.setMaximumSize(QSize(100, 16777215))
        font4 = QFont()
        font4.setBold(False)
        self.crear_suministro.setFont(font4)
        self.crear_suministro.setStyleSheet(u"background-color: #d9d9d9;\n"
"color: black;\n"
"border: 1px solid black;\n"
"border-radius: 15px;\n"
"padding:5px;\n"
"box-shadow: 5px 5px 15px rgba(0, 0, 0, 0.3);")

        self.horizontalLayout_3.addWidget(self.crear_suministro)

        self.crear_informe = QPushButton(self.frame_5)
        self.crear_informe.setObjectName(u"crear_informe")
        self.crear_informe.setMaximumSize(QSize(110, 16777215))
        self.crear_informe.setFont(font4)
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

        self.horizontalLayout_4.addWidget(self.label_5)

        self.lineEdit_4 = QLineEdit(self.frame_7)
        self.lineEdit_4.setObjectName(u"lineEdit_4")
        self.lineEdit_4.setMaximumSize(QSize(200, 100))

        self.horizontalLayout_4.addWidget(self.lineEdit_4)

        self.boton_filtrar_2 = QPushButton(self.frame_7)
        self.boton_filtrar_2.setObjectName(u"boton_filtrar_2")
        self.boton_filtrar_2.setMaximumSize(QSize(100, 16777215))
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
        self.crear_recordatorio.setMaximumSize(QSize(150, 16777215))
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
        self.crear_informe_2.setMaximumSize(QSize(150, 16777215))
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
        __qtablewidgetitem105 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(0, __qtablewidgetitem105)
        __qtablewidgetitem106 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(1, __qtablewidgetitem106)
        __qtablewidgetitem107 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(2, __qtablewidgetitem107)
        __qtablewidgetitem108 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(3, __qtablewidgetitem108)
        __qtablewidgetitem109 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(4, __qtablewidgetitem109)
        __qtablewidgetitem110 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(5, __qtablewidgetitem110)
        __qtablewidgetitem111 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(6, __qtablewidgetitem111)
        __qtablewidgetitem112 = QTableWidgetItem()
        self.tableWidget_2.setHorizontalHeaderItem(7, __qtablewidgetitem112)
        if (self.tableWidget_2.rowCount() < 6):
            self.tableWidget_2.setRowCount(6)
        __qtablewidgetitem113 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 0, __qtablewidgetitem113)
        __qtablewidgetitem114 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 1, __qtablewidgetitem114)
        __qtablewidgetitem115 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 2, __qtablewidgetitem115)
        __qtablewidgetitem116 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 3, __qtablewidgetitem116)
        __qtablewidgetitem117 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 4, __qtablewidgetitem117)
        __qtablewidgetitem118 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 5, __qtablewidgetitem118)
        __qtablewidgetitem119 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 6, __qtablewidgetitem119)
        __qtablewidgetitem120 = QTableWidgetItem()
        self.tableWidget_2.setItem(0, 7, __qtablewidgetitem120)
        __qtablewidgetitem121 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 0, __qtablewidgetitem121)
        __qtablewidgetitem122 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 1, __qtablewidgetitem122)
        __qtablewidgetitem123 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 2, __qtablewidgetitem123)
        __qtablewidgetitem124 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 3, __qtablewidgetitem124)
        __qtablewidgetitem125 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 4, __qtablewidgetitem125)
        __qtablewidgetitem126 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 5, __qtablewidgetitem126)
        __qtablewidgetitem127 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 6, __qtablewidgetitem127)
        __qtablewidgetitem128 = QTableWidgetItem()
        self.tableWidget_2.setItem(1, 7, __qtablewidgetitem128)
        __qtablewidgetitem129 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 0, __qtablewidgetitem129)
        __qtablewidgetitem130 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 1, __qtablewidgetitem130)
        __qtablewidgetitem131 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 2, __qtablewidgetitem131)
        __qtablewidgetitem132 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 3, __qtablewidgetitem132)
        __qtablewidgetitem133 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 4, __qtablewidgetitem133)
        __qtablewidgetitem134 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 5, __qtablewidgetitem134)
        __qtablewidgetitem135 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 6, __qtablewidgetitem135)
        __qtablewidgetitem136 = QTableWidgetItem()
        self.tableWidget_2.setItem(2, 7, __qtablewidgetitem136)
        __qtablewidgetitem137 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 0, __qtablewidgetitem137)
        __qtablewidgetitem138 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 1, __qtablewidgetitem138)
        __qtablewidgetitem139 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 2, __qtablewidgetitem139)
        __qtablewidgetitem140 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 3, __qtablewidgetitem140)
        __qtablewidgetitem141 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 4, __qtablewidgetitem141)
        __qtablewidgetitem142 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 5, __qtablewidgetitem142)
        __qtablewidgetitem143 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 6, __qtablewidgetitem143)
        __qtablewidgetitem144 = QTableWidgetItem()
        self.tableWidget_2.setItem(3, 7, __qtablewidgetitem144)
        __qtablewidgetitem145 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 0, __qtablewidgetitem145)
        __qtablewidgetitem146 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 1, __qtablewidgetitem146)
        __qtablewidgetitem147 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 2, __qtablewidgetitem147)
        __qtablewidgetitem148 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 3, __qtablewidgetitem148)
        __qtablewidgetitem149 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 4, __qtablewidgetitem149)
        __qtablewidgetitem150 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 5, __qtablewidgetitem150)
        __qtablewidgetitem151 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 6, __qtablewidgetitem151)
        __qtablewidgetitem152 = QTableWidgetItem()
        self.tableWidget_2.setItem(4, 7, __qtablewidgetitem152)
        __qtablewidgetitem153 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 0, __qtablewidgetitem153)
        __qtablewidgetitem154 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 1, __qtablewidgetitem154)
        __qtablewidgetitem155 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 2, __qtablewidgetitem155)
        __qtablewidgetitem156 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 3, __qtablewidgetitem156)
        __qtablewidgetitem157 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 4, __qtablewidgetitem157)
        __qtablewidgetitem158 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 5, __qtablewidgetitem158)
        __qtablewidgetitem159 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 6, __qtablewidgetitem159)
        __qtablewidgetitem160 = QTableWidgetItem()
        self.tableWidget_2.setItem(5, 7, __qtablewidgetitem160)
        self.tableWidget_2.setObjectName(u"tableWidget_2")
        self.tableWidget_2.setRowCount(6)
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
        self.progressBar = QProgressBar(self.frame_10)
        self.progressBar.setObjectName(u"progressBar")
        self.progressBar.setValue(24)

        self.gridLayout_22.addWidget(self.progressBar, 3, 0, 1, 1)

        self.label_6 = QLabel(self.frame_10)
        self.label_6.setObjectName(u"label_6")
        font5 = QFont()
        font5.setPointSize(11)
        font5.setBold(True)
        self.label_6.setFont(font5)

        self.gridLayout_22.addWidget(self.label_6, 0, 0, 1, 1)

        self.label_8 = QLabel(self.frame_10)
        self.label_8.setObjectName(u"label_8")
        font6 = QFont()
        font6.setPointSize(10)
        font6.setBold(True)
        self.label_8.setFont(font6)
        self.label_8.setStyleSheet(u"color: red;")
        self.label_8.setAlignment(Qt.AlignmentFlag.AlignCenter)

        self.gridLayout_22.addWidget(self.label_8, 2, 0, 1, 1)

        self.label_7 = QLabel(self.frame_10)
        self.label_7.setObjectName(u"label_7")
        font7 = QFont()
        font7.setPointSize(12)
        font7.setBold(True)
        self.label_7.setFont(font7)
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

        self.gridLayout_27.addLayout(self.GRID_3, 0, 0, 1, 1)


        self.horizontalLayout_5.addWidget(self.frame_lineal)


        self.gridLayout_24.addLayout(self.horizontalLayout_5, 1, 0, 1, 1)


        self.gridLayout_16.addWidget(self.frame_9, 0, 0, 1, 1)


        self.formLayout.setLayout(0, QFormLayout.FieldRole, self.gridLayout_16)


        self.GRID_2.addWidget(self.frame_6, 1, 0, 1, 1)


        self.gridLayout_20.addLayout(self.GRID_2, 0, 0, 1, 1)

        self.tabWidget.addTab(self.Buys, "")
        self.tab_4 = QWidget()
        self.tab_4.setObjectName(u"tab_4")
        self.tabWidget.addTab(self.tab_4, "")
        self.tab_5 = QWidget()
        self.tab_5.setObjectName(u"tab_5")
        self.tabWidget.addTab(self.tab_5, "")
        self.tab_6 = QWidget()
        self.tab_6.setObjectName(u"tab_6")
        self.tabWidget.addTab(self.tab_6, "")
        self.tab_7 = QWidget()
        self.tab_7.setObjectName(u"tab_7")
        self.tabWidget.addTab(self.tab_7, "")
        self.tab_2 = QWidget()
        self.tab_2.setObjectName(u"tab_2")
        self.tabWidget.addTab(self.tab_2, "")

        self.gridLayout_4.addWidget(self.tabWidget, 0, 1, 1, 1)


        self.gridLayout_7.addLayout(self.gridLayout_4, 1, 0, 1, 1)


        self.main_body.addWidget(self.contenido, 1, 1, 1, 1)

        self.main_body.setRowStretch(0, 1)

        self.gridLayout_2.addLayout(self.main_body, 0, 2, 1, 1)

        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)

        self.tabWidget.setCurrentIndex(3)


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
        self.id_label.setText(QCoreApplication.translate("MainWindow", u"Identificaci\u00f3n", None))
        self.pass_label.setText(QCoreApplication.translate("MainWindow", u"Contrase\u00f1a", None))
        self.Tit.setText(QCoreApplication.translate("MainWindow", u"Inicio de sesi\u00f3n", None))
        self.user_label.setText(QCoreApplication.translate("MainWindow", u"Usuario", None))
        self.entry_button.setText(QCoreApplication.translate("MainWindow", u"Identificar", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.login), QCoreApplication.translate("MainWindow", u"Login", None))
        self.pushButton_11.setText(QCoreApplication.translate("MainWindow", u"Ingresos", None))
        self.label_2.setText(QCoreApplication.translate("MainWindow", u"Hoy:", None))
        self.label_3.setText(QCoreApplication.translate("MainWindow", u"22.000\u20ac", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventario), QCoreApplication.translate("MainWindow", u"Home", None))
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
        self.tableWidget.setSortingEnabled(__sortingEnabled)

        self.label_4.setText(QCoreApplication.translate("MainWindow", u"Inventario", None))
        self.boton_filtrar.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.crear_suministro.setText(QCoreApplication.translate("MainWindow", u"Nuevo", None))
        self.crear_informe.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Inventory), QCoreApplication.translate("MainWindow", u"Inventory", None))
        self.label_5.setText(QCoreApplication.translate("MainWindow", u"Compras", None))
        self.lineEdit_4.setText(QCoreApplication.translate("MainWindow", u"Buscador", None))
        self.boton_filtrar_2.setText(QCoreApplication.translate("MainWindow", u"Filtrar", None))
        self.crear_recordatorio.setText(QCoreApplication.translate("MainWindow", u"Crear recordatorio", None))
        self.crear_informe_2.setText(QCoreApplication.translate("MainWindow", u"Crear informe", None))
        ___qtablewidgetitem103 = self.tableWidget_2.horizontalHeaderItem(0)
        ___qtablewidgetitem103.setText(QCoreApplication.translate("MainWindow", u"N\u00ba Orden", None));
        ___qtablewidgetitem104 = self.tableWidget_2.horizontalHeaderItem(1)
        ___qtablewidgetitem104.setText(QCoreApplication.translate("MainWindow", u"Proveedor", None));
        ___qtablewidgetitem105 = self.tableWidget_2.horizontalHeaderItem(2)
        ___qtablewidgetitem105.setText(QCoreApplication.translate("MainWindow", u"Fecha Orden", None));
        ___qtablewidgetitem106 = self.tableWidget_2.horizontalHeaderItem(3)
        ___qtablewidgetitem106.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem107 = self.tableWidget_2.horizontalHeaderItem(4)
        ___qtablewidgetitem107.setText(QCoreApplication.translate("MainWindow", u"Precio/u", None));
        ___qtablewidgetitem108 = self.tableWidget_2.horizontalHeaderItem(5)
        ___qtablewidgetitem108.setText(QCoreApplication.translate("MainWindow", u"Unidad", None));
        ___qtablewidgetitem109 = self.tableWidget_2.horizontalHeaderItem(6)
        ___qtablewidgetitem109.setText(QCoreApplication.translate("MainWindow", u"Total", None));
        ___qtablewidgetitem110 = self.tableWidget_2.horizontalHeaderItem(7)
        ___qtablewidgetitem110.setText(QCoreApplication.translate("MainWindow", u"Estado", None));

        __sortingEnabled1 = self.tableWidget_2.isSortingEnabled()
        self.tableWidget_2.setSortingEnabled(False)
        ___qtablewidgetitem111 = self.tableWidget_2.item(0, 0)
        ___qtablewidgetitem111.setText(QCoreApplication.translate("MainWindow", u"1", None));
        ___qtablewidgetitem112 = self.tableWidget_2.item(0, 1)
        ___qtablewidgetitem112.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem113 = self.tableWidget_2.item(0, 2)
        ___qtablewidgetitem113.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem114 = self.tableWidget_2.item(0, 3)
        ___qtablewidgetitem114.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem115 = self.tableWidget_2.item(0, 4)
        ___qtablewidgetitem115.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem116 = self.tableWidget_2.item(0, 5)
        ___qtablewidgetitem116.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem117 = self.tableWidget_2.item(0, 6)
        ___qtablewidgetitem117.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem118 = self.tableWidget_2.item(0, 7)
        ___qtablewidgetitem118.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem119 = self.tableWidget_2.item(1, 0)
        ___qtablewidgetitem119.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem120 = self.tableWidget_2.item(1, 1)
        ___qtablewidgetitem120.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem121 = self.tableWidget_2.item(1, 2)
        ___qtablewidgetitem121.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem122 = self.tableWidget_2.item(1, 3)
        ___qtablewidgetitem122.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem123 = self.tableWidget_2.item(1, 4)
        ___qtablewidgetitem123.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem124 = self.tableWidget_2.item(1, 5)
        ___qtablewidgetitem124.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem125 = self.tableWidget_2.item(1, 6)
        ___qtablewidgetitem125.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem126 = self.tableWidget_2.item(1, 7)
        ___qtablewidgetitem126.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem127 = self.tableWidget_2.item(2, 0)
        ___qtablewidgetitem127.setText(QCoreApplication.translate("MainWindow", u"3", None));
        ___qtablewidgetitem128 = self.tableWidget_2.item(2, 1)
        ___qtablewidgetitem128.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem129 = self.tableWidget_2.item(2, 2)
        ___qtablewidgetitem129.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem130 = self.tableWidget_2.item(2, 3)
        ___qtablewidgetitem130.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem131 = self.tableWidget_2.item(2, 4)
        ___qtablewidgetitem131.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem132 = self.tableWidget_2.item(2, 5)
        ___qtablewidgetitem132.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem133 = self.tableWidget_2.item(2, 6)
        ___qtablewidgetitem133.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem134 = self.tableWidget_2.item(2, 7)
        ___qtablewidgetitem134.setText(QCoreApplication.translate("MainWindow", u"Entregado", None));
        ___qtablewidgetitem135 = self.tableWidget_2.item(3, 0)
        ___qtablewidgetitem135.setText(QCoreApplication.translate("MainWindow", u"4", None));
        ___qtablewidgetitem136 = self.tableWidget_2.item(3, 1)
        ___qtablewidgetitem136.setText(QCoreApplication.translate("MainWindow", u"Proveedor C", None));
        ___qtablewidgetitem137 = self.tableWidget_2.item(3, 2)
        ___qtablewidgetitem137.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem138 = self.tableWidget_2.item(3, 3)
        ___qtablewidgetitem138.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem139 = self.tableWidget_2.item(3, 4)
        ___qtablewidgetitem139.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem140 = self.tableWidget_2.item(3, 5)
        ___qtablewidgetitem140.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem141 = self.tableWidget_2.item(3, 6)
        ___qtablewidgetitem141.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem142 = self.tableWidget_2.item(3, 7)
        ___qtablewidgetitem142.setText(QCoreApplication.translate("MainWindow", u"En tr\u00e1nsito", None));
        ___qtablewidgetitem143 = self.tableWidget_2.item(4, 0)
        ___qtablewidgetitem143.setText(QCoreApplication.translate("MainWindow", u"5", None));
        ___qtablewidgetitem144 = self.tableWidget_2.item(4, 1)
        ___qtablewidgetitem144.setText(QCoreApplication.translate("MainWindow", u"Proveedor A", None));
        ___qtablewidgetitem145 = self.tableWidget_2.item(4, 2)
        ___qtablewidgetitem145.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem146 = self.tableWidget_2.item(4, 3)
        ___qtablewidgetitem146.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem147 = self.tableWidget_2.item(4, 4)
        ___qtablewidgetitem147.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem148 = self.tableWidget_2.item(4, 5)
        ___qtablewidgetitem148.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem149 = self.tableWidget_2.item(4, 6)
        ___qtablewidgetitem149.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem150 = self.tableWidget_2.item(4, 7)
        ___qtablewidgetitem150.setText(QCoreApplication.translate("MainWindow", u"En tr\u00e1nsito", None));
        ___qtablewidgetitem151 = self.tableWidget_2.item(5, 0)
        ___qtablewidgetitem151.setText(QCoreApplication.translate("MainWindow", u"6", None));
        ___qtablewidgetitem152 = self.tableWidget_2.item(5, 1)
        ___qtablewidgetitem152.setText(QCoreApplication.translate("MainWindow", u"Proveedor B", None));
        ___qtablewidgetitem153 = self.tableWidget_2.item(5, 2)
        ___qtablewidgetitem153.setText(QCoreApplication.translate("MainWindow", u"2024-09-01", None));
        ___qtablewidgetitem154 = self.tableWidget_2.item(5, 3)
        ___qtablewidgetitem154.setText(QCoreApplication.translate("MainWindow", u"Producto", None));
        ___qtablewidgetitem155 = self.tableWidget_2.item(5, 4)
        ___qtablewidgetitem155.setText(QCoreApplication.translate("MainWindow", u"5\u20ac", None));
        ___qtablewidgetitem156 = self.tableWidget_2.item(5, 5)
        ___qtablewidgetitem156.setText(QCoreApplication.translate("MainWindow", u"2", None));
        ___qtablewidgetitem157 = self.tableWidget_2.item(5, 6)
        ___qtablewidgetitem157.setText(QCoreApplication.translate("MainWindow", u"10\u20ac", None));
        ___qtablewidgetitem158 = self.tableWidget_2.item(5, 7)
        ___qtablewidgetitem158.setText(QCoreApplication.translate("MainWindow", u"Pendiente", None));
        self.tableWidget_2.setSortingEnabled(__sortingEnabled1)

        self.label_6.setText(QCoreApplication.translate("MainWindow", u"Gastos por mes:", None))
        self.label_8.setText(QCoreApplication.translate("MainWindow", u"-5080\u20ac", None))
        self.label_7.setText(QCoreApplication.translate("MainWindow", u"Total", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.Buys), QCoreApplication.translate("MainWindow", u"Buys", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_4), QCoreApplication.translate("MainWindow", u"Sales", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_5), QCoreApplication.translate("MainWindow", u"finance", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_6), QCoreApplication.translate("MainWindow", u"RRHH", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_7), QCoreApplication.translate("MainWindow", u"Marketing", None))
        self.tabWidget.setTabText(self.tabWidget.indexOf(self.tab_2), QCoreApplication.translate("MainWindow", u"Innovation", None))
    # retranslateUi

