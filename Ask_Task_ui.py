# Form implementation generated from reading ui file '/Users/andrejlazarev/Desktop/PYthon/Ask_Task.ui'
#
# Created by: PyQt6 UI code generator 6.5.0
#
# WARNING: Any manual changes made to this file will be lost when pyuic6 is
# run again.  Do not edit this file unless you know what you are doing.


from PyQt6 import QtCore, QtGui, QtWidgets


class Ui_MainWindow(object):
    def setupUi(self, MainWindow):
        MainWindow.setObjectName("MainWindow")
        MainWindow.resize(800, 913)
        self.centralwidget = QtWidgets.QWidget(parent=MainWindow)
        self.centralwidget.setObjectName("centralwidget")
        self.stackedWidget = QtWidgets.QStackedWidget(parent=self.centralwidget)
        self.stackedWidget.setGeometry(QtCore.QRect(0, 0, 800, 913))
        self.stackedWidget.setObjectName("stackedWidget")
        self.page = QtWidgets.QWidget()
        self.page.setObjectName("page")
        self.label = QtWidgets.QLabel(parent=self.page)
        self.label.setGeometry(QtCore.QRect(0, 0, 800, 913))
        self.label.setText("")
        self.label.setPixmap(QtGui.QPixmap("/Users/andrejlazarev/Desktop/PYthon/1.png"))
        self.label.setObjectName("label")
        self.Registration_Page_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.Registration_Page_pushButton.setGeometry(QtCore.QRect(90, 620, 641, 91))
        self.Registration_Page_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.Registration_Page_pushButton.setText("")
        self.Registration_Page_pushButton.setObjectName("Registration_Page_pushButton")
        self.Entry_Page_pushButton = QtWidgets.QPushButton(parent=self.page)
        self.Entry_Page_pushButton.setGeometry(QtCore.QRect(90, 760, 641, 91))
        self.Entry_Page_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.Entry_Page_pushButton.setText("")
        self.Entry_Page_pushButton.setObjectName("Entry_Page_pushButton")
        self.stackedWidget.addWidget(self.page)
        self.page_2 = QtWidgets.QWidget()
        self.page_2.setObjectName("page_2")
        self.label_2 = QtWidgets.QLabel(parent=self.page_2)
        self.label_2.setGeometry(QtCore.QRect(0, 0, 800, 913))
        self.label_2.setText("")
        self.label_2.setPixmap(QtGui.QPixmap("/Users/andrejlazarev/Desktop/PYthon/2.png"))
        self.label_2.setObjectName("label_2")
        self.Registration_Login_lineEdit = QtWidgets.QLineEdit(parent=self.page_2)
        self.Registration_Login_lineEdit.setGeometry(QtCore.QRect(350, 380, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Registration_Login_lineEdit.setFont(font)
        self.Registration_Login_lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.Registration_Login_lineEdit.setText("")
        self.Registration_Login_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Registration_Login_lineEdit.setObjectName("Registration_Login_lineEdit")
        self.Registration_Password_lineEdit = QtWidgets.QLineEdit(parent=self.page_2)
        self.Registration_Password_lineEdit.setGeometry(QtCore.QRect(460, 530, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Registration_Password_lineEdit.setFont(font)
        self.Registration_Password_lineEdit.setAccessibleName("")
        self.Registration_Password_lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color:white;")
        self.Registration_Password_lineEdit.setText("")
        self.Registration_Password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Registration_Password_lineEdit.setObjectName("Registration_Password_lineEdit")
        self.Registration_pushButton = QtWidgets.QPushButton(parent=self.page_2)
        self.Registration_pushButton.setGeometry(QtCore.QRect(60, 700, 681, 71))
        self.Registration_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.Registration_pushButton.setText("")
        self.Registration_pushButton.setObjectName("Registration_pushButton")
        self.stackedWidget.addWidget(self.page_2)
        self.page_3 = QtWidgets.QWidget()
        self.page_3.setObjectName("page_3")
        self.label_3 = QtWidgets.QLabel(parent=self.page_3)
        self.label_3.setGeometry(QtCore.QRect(0, 0, 800, 913))
        self.label_3.setText("")
        self.label_3.setPixmap(QtGui.QPixmap("/Users/andrejlazarev/Desktop/PYthon/3.png"))
        self.label_3.setObjectName("label_3")
        self.Entry_Login_lineEdit = QtWidgets.QLineEdit(parent=self.page_3)
        self.Entry_Login_lineEdit.setGeometry(QtCore.QRect(350, 380, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Entry_Login_lineEdit.setFont(font)
        self.Entry_Login_lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color: white;")
        self.Entry_Login_lineEdit.setText("")
        self.Entry_Login_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignLeading|QtCore.Qt.AlignmentFlag.AlignLeft|QtCore.Qt.AlignmentFlag.AlignVCenter)
        self.Entry_Login_lineEdit.setObjectName("Entry_Login_lineEdit")
        self.Entry_pushButton = QtWidgets.QPushButton(parent=self.page_3)
        self.Entry_pushButton.setGeometry(QtCore.QRect(290, 690, 221, 61))
        self.Entry_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.Entry_pushButton.setText("")
        self.Entry_pushButton.setObjectName("Entry_pushButton")
        self.Entry_Password_lineEdit = QtWidgets.QLineEdit(parent=self.page_3)
        self.Entry_Password_lineEdit.setGeometry(QtCore.QRect(460, 530, 271, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Entry_Password_lineEdit.setFont(font)
        self.Entry_Password_lineEdit.setAccessibleName("")
        self.Entry_Password_lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"color:white;")
        self.Entry_Password_lineEdit.setText("")
        self.Entry_Password_lineEdit.setEchoMode(QtWidgets.QLineEdit.EchoMode.Password)
        self.Entry_Password_lineEdit.setObjectName("Entry_Password_lineEdit")
        self.stackedWidget.addWidget(self.page_3)
        self.page_4 = QtWidgets.QWidget()
        self.page_4.setObjectName("page_4")
        self.label_4 = QtWidgets.QLabel(parent=self.page_4)
        self.label_4.setGeometry(QtCore.QRect(0, 0, 800, 913))
        self.label_4.setText("")
        self.label_4.setPixmap(QtGui.QPixmap("/Users/andrejlazarev/Desktop/PYthon/4.png"))
        self.label_4.setObjectName("label_4")
        self.Name_Task_lineEdit = QtWidgets.QLineEdit(parent=self.page_4)
        self.Name_Task_lineEdit.setGeometry(QtCore.QRect(350, 240, 381, 41))
        font = QtGui.QFont()
        font.setPointSize(10)
        self.Name_Task_lineEdit.setFont(font)
        self.Name_Task_lineEdit.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"")
        self.Name_Task_lineEdit.setText("")
        self.Name_Task_lineEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.Name_Task_lineEdit.setObjectName("Name_Task_lineEdit")
        self.dateEdit = QtWidgets.QDateEdit(parent=self.page_4)
        self.dateEdit.setGeometry(QtCore.QRect(270, 330, 261, 31))
        self.dateEdit.setAlignment(QtCore.Qt.AlignmentFlag.AlignCenter)
        self.dateEdit.setDate(QtCore.QDate(2023, 1, 1))
        self.dateEdit.setObjectName("dateEdit")
        self.Add_Task_pushButton = QtWidgets.QPushButton(parent=self.page_4)
        self.Add_Task_pushButton.setGeometry(QtCore.QRect(160, 400, 321, 51))
        self.Add_Task_pushButton.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;")
        self.Add_Task_pushButton.setText("")
        self.Add_Task_pushButton.setObjectName("Add_Task_pushButton")
        self.listWidget = QtWidgets.QListWidget(parent=self.page_4)
        self.listWidget.setGeometry(QtCore.QRect(95, 515, 611, 303))
        font = QtGui.QFont()
        font.setPointSize(14)
        self.listWidget.setFont(font)
        self.listWidget.setStyleSheet("background-color: rgba(0,0,0,0);\n"
"border: none;\n"
"color:white;")
        self.listWidget.setDragEnabled(True)
        self.listWidget.setObjectName("listWidget")
        self.ONE_DAY_pushButton = QtWidgets.QPushButton(parent=self.page_4)
        self.ONE_DAY_pushButton.setGeometry(QtCore.QRect(120, 470, 93, 28))
        self.ONE_DAY_pushButton.setStyleSheet("\n"
"")
        self.ONE_DAY_pushButton.setObjectName("ONE_DAY_pushButton")
        self.ALL_pushButton = QtWidgets.QPushButton(parent=self.page_4)
        self.ALL_pushButton.setGeometry(QtCore.QRect(590, 470, 93, 28))
        self.ALL_pushButton.setObjectName("ALL_pushButton")
        self.WEEK_pushButton = QtWidgets.QPushButton(parent=self.page_4)
        self.WEEK_pushButton.setGeometry(QtCore.QRect(270, 470, 93, 28))
        self.WEEK_pushButton.setObjectName("WEEK_pushButton")
        self.MONTH_pushButton = QtWidgets.QPushButton(parent=self.page_4)
        self.MONTH_pushButton.setGeometry(QtCore.QRect(440, 470, 93, 28))
        self.MONTH_pushButton.setObjectName("MONTH_pushButton")
        self.label_4.raise_()
        self.dateEdit.raise_()
        self.Name_Task_lineEdit.raise_()
        self.Add_Task_pushButton.raise_()
        self.listWidget.raise_()
        self.ONE_DAY_pushButton.raise_()
        self.ALL_pushButton.raise_()
        self.WEEK_pushButton.raise_()
        self.MONTH_pushButton.raise_()
        self.stackedWidget.addWidget(self.page_4)
        MainWindow.setCentralWidget(self.centralwidget)

        self.retranslateUi(MainWindow)
        QtCore.QMetaObject.connectSlotsByName(MainWindow)

    def retranslateUi(self, MainWindow):
        _translate = QtCore.QCoreApplication.translate
        MainWindow.setWindowTitle(_translate("MainWindow", "MainWindow"))
        self.ONE_DAY_pushButton.setText(_translate("MainWindow", "1 день"))
        self.ALL_pushButton.setText(_translate("MainWindow", "все"))
        self.WEEK_pushButton.setText(_translate("MainWindow", "неделя"))
        self.MONTH_pushButton.setText(_translate("MainWindow", "месяц"))
