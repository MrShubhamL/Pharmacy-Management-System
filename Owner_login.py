from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
# import mysql.connector
import sqlite3
import tkinter
from tkinter import*
from tkinter import ttk
from PyQt5.uic import loadUi, loadUiType
import datetime
from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import Qt
from shutil import copyfile
from xlwt import Workbook
from PIL import Image
from PIL import Image
import re
import csv
import os
from shutil import copyfile
import xlwt
from xlwt import Workbook


ui,_ = loadUiType('MenuBar\Owner_Security\Owner_Security.ui')
class Owner_login(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.Handel_Buttons()
        self.show()


    def Handel_Buttons(self):
        self.pushButton.clicked.connect(self.AddUser)
        


    def AddUser(self):
        # self.db = mysql.connector.connect(host="localhost",username="root",password="Shubham@lohar952",database="medisoft")
        # self.cur = self.db.cursor()

        username = self.lineEdit.text()
        password = self.lineEdit_2.text()

        try:
            my_data = (username,password)
            my_query = "INSERT INTO login_rights VALUES (%s,%s)"
            self.cur.execute(my_query,my_data)
        except:
            ButtonReplay = QMessageBox.information(self,"Invalid","This is invalid username")

        self.db.commit()
        self.statusBar().showMessage('New User Added')
        self.db.close()


        