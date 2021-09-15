from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import MySQLdb
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


ui,_ = loadUiType('MenuBar\Master\GST_Category_Master.ui')
class GST_Category_Master(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.show()



pi,_ = loadUiType('MenuBar\Master\Category_Master.ui')
class Category_Master(QMainWindow,pi):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.show()

ci,_ = loadUiType('MenuBar\Master\HSN_Master.ui')
class HSN_Master(QMainWindow,ci):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.show()

di,_ = loadUiType('MenuBar\Master\Product_Master.ui')
class Product_Master(QMainWindow,di):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.show()
