from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
# import mysql.connector
import sqlite3
from tkinter import*
from tkinter import ttk
from PyQt5.uic import loadUi, loadUiType
from PyQt5.QtCore import Qt
from PyQt5.QtCore import QDate, QTime, QDateTime, Qt


pi,_ = loadUiType('ToolBar\Purchase.ui')
class Purchase(QMainWindow,pi):
    count = 0
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Purchase")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.Show_Combobox()
        self.Purchase_Bill_No()
        self.show()

    def Show_Combobox(self):
        self.comboBox_4.addItems(["A", "B"])
        now = QDate.currentDate()
        self.comboBox.addItem(now.toString(Qt.ISODate))
        self.comboBox_2.addItem(now.toString(Qt.ISODate))
        self.comboBox_3.addItems(["Online Mode", "Cash"])
        self.comboBox_5.addItems(["NIL", "5%","12%","18%","28%"])

        # For Product_Details....................

       

    def Purchase_Bill_No(self):
        self.lineEdit.setSizeIncrement(10,10)
        



    

ui,_ = loadUiType('ToolBar\Sales.ui')
class Sales(QMainWindow,ui):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.Handel_Buttons()
        self.Box()
        self.show()



    def Handel_Buttons(self):
        self.lineEdit.textChanged.connect(self.Login)
    
    def Box(self):
        username = self.lineEdit.text()

        if username == "":
            self.groupBox.setEnabled(False) 




    def Login(self):
        # self.db = mysql.connector.connect(host="localhost",username="root",password="Shubham@lohar952",database="medisoft")
        # self.cur = self.db.cursor()

        password = self.lineEdit.text()
        

        # sql = "SELECT password FROM login_rights"  
        self.cur.execute("SELECT * FROM login_rights")
        my_data = self.cur.fetchall()

        for row in my_data  :
            if password == (row[0]):
                print('user match')
                self.statusBar().showMessage('You Are Successfull Login')
                self.label_10.setText("Admin")
                self.groupBox.setEnabled(True)
                
            else:
                # self.statusBar().showMessage('Invalid Username Or Password')
                self.groupBox.setEnabled(False)
                self.label_10.setText("Invalid Password ")



        
ti,_ = loadUiType('ToolBar\Product_Details.ui')
class Product_Details(QMainWindow,ti):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("Transactions")
        self.setWindowIcon(QIcon('src/icons/power_module.png'))
        self.setGeometry(500,500,1366,768)
        self.setupUi(self)
        self.Show_Combobox1()
        self.Show_All_Products()
        self.Show_All_Opening_Quantity()
        self.HandelButtons()
        self.Show_Combobox()
        self.show()

    def Show_Combobox1(self):
        self.comboBox_3.addItems(["Manage Batch wise Inventory","Manage Batch wise Inventory & Expire Date","Primary"])
    
    def HandelButtons(self):
        self.pushButton_9.clicked.connect(self.AddMedicine)
        self.pushButton.clicked.connect(self.Search_Medicine)
        self.pushButton_10.clicked.connect(self.clear)



    def AddMedicine(self):
        # self.db = mysql.connector.connect(host="localhost",username="root",password="Shubham@lohar952",database="medisoft")
        # self.cur = self.db.cursor()

        Name = self.lineEdit_3.text()
        Packing = self.lineEdit_6.text()
        Alias = self.lineEdit_2.text()
        Barcode = self.lineEdit_7.text()
        Under_Group = self.comboBox_3.currentText()
        Unit = self.lineEdit_8.text()
        Code = self.lineEdit_4.text()
        HSN_No = self.lineEdit_5.text()
        Rack_No = self.lineEdit_9.text()
        Batch_No = self.lineEdit_16.text()
        Batch_Date = self.lineEdit_21.text()
        Quantity = self.lineEdit_17.text()
        Expire_Date = self.lineEdit_22.text()
        Location = self.lineEdit_18.text()
        Supplier = self.lineEdit_19.text()


        Landing_Cost = self.lineEdit_20.text()
        Selling_Rate = self.lineEdit_10.text()
        Profit = self.lineEdit_11.text()

        Tax_Include = self.checkBox.setChecked(True)
       

        Tax = self.comboBox.currentText()
        Discond = self.lineEdit_12.text()
        Discond_Per = self.lineEdit_13.text()
        Category = self.comboBox_2.currentText()
        Mfg_By = self.lineEdit_14.text()


        my_data = (Name,Packing,Alias,Barcode,Under_Group,Unit,Code,HSN_No,Rack_No,Batch_No,Batch_Date,Quantity,Expire_Date,Selling_Rate,Profit,Tax_Include,Tax,Discond,Discond_Per,Category,Mfg_By,Landing_Cost,Location,Supplier)
        my_query = "INSERT INTO product_details VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s,%s)"

        self.cur.execute(my_query,my_data)

        buttonReplay = QMessageBox.information(self,"Success","Data Successfully Added!")

        self.db.commit()
        self.statusBar().showMessage('New User Added')
        self.Show_All_Products()
        self.Show_All_Opening_Quantity()
        self.db.close()



    def Show_All_Products(self):
        # self.db = mysql.connector.connect(host="localhost",username="root",password="Shubham@lohar952",database="medisoft")
        # self.cur = self.db.cursor()


        self.cur.execute(''' SELECT Name,Code,Barcode,Under_Group,Batch_No,Batch_Date,Quantity,Landing_Cost,Selling_Rate,Location,Supplier FROM product_details''')
        data = self.cur.fetchall()

        self.tableWidget.setRowCount(0)
        self.tableWidget.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget.rowCount()
            self.tableWidget.insertRow(row_position)

        self.db.commit()
        self.db.close()


    def Show_All_Opening_Quantity(self):
        # self.db = mysql.connector.connect(host="localhost",username="root",password="Shubham@lohar952",database="medisoft")
        # self.cur = self.db.cursor()


        self.cur.execute(''' SELECT Batch_No,Batch_Date,Quantity,Landing_Cost,Selling_Rate,Location,Supplier FROM product_details''')
        data = self.cur.fetchall()

        self.tableWidget_2.setRowCount(0)
        self.tableWidget_2.insertRow(0)

        for row, form in enumerate(data):
            for column, item in enumerate(form):
                self.tableWidget_2.setItem(row, column, QTableWidgetItem(str(item)))
                column += 1

            row_position = self.tableWidget_2.rowCount()
            self.tableWidget_2.insertRow(row_position)

        self.db.commit()
        self.db.close()


    def Search_Medicine(self):

        # self.db = mysql.connector.connect(host="localhost",username="root",password="Shubham@lohar952",database="medisoft")
        # self.cur = self.db.cursor()


        book_title = self.lineEdit_3.text()

        if book_title == "":
            buttonReply = QMessageBox.information(self,"Empty","Please Enter The Name of Medicine")
        else: 
            sql = ''' SELECT * FROM product_details WHERE Name=%s'''
            self.cur.execute(sql ,[(book_title)])

            data = self.cur.fetchone()

            try:   
                print(data)
                self.lineEdit_3.setText(data[0])
                self.lineEdit_6.setText(data[1])
                self.lineEdit_2.setText(data[2])
                self.lineEdit_7.setText(data[3])
                self.comboBox_3.setCurrentText(data[4])
                self.lineEdit_8.setText(data[5])

                self.lineEdit_4.setText(data[6])
                self.lineEdit_5.setText(data[7])
                self.lineEdit_9.setText(data[8])
                self.lineEdit_16.setText(data[9])

                self.lineEdit_21.setText(data[10])

                self.lineEdit_17.setText(data[11])

                self.lineEdit_22.setText(data[12])

                self.lineEdit_18.setText(data[13])
                self.lineEdit_19.setText(data[14])

                self.lineEdit_20.setText((data[15]))

                self.lineEdit_10.setText(data[16])
                self.lineEdit_11.setText(data[17])

                # self.checkBox.setChecked(data[18])


                self.comboBox.setCurrentText(data[19])
                self.lineEdit_12.setText(data[20])
                self.lineEdit_13.setText(data[21])
                self.comboBox_2.setCurrentText(data[22])
                self.lineEdit_14.setText(str(data[23]))
            except:
                buttonReply = QMessageBox.information(self,"Sorry","No such book in our Library please check book name")

        self.db.commit()
        self.statusBar().showMessage('Data Fatched')
        self.db.close()

    def Show_Combobox(self):
        self.comboBox.addItems(["NIL", "5%","12%","18%","28%"])
        self.comboBox_2.addItems(["Tablet", "Liquid","Capsule","Tube","Cosmatics"])

        


    def clear(self):
        self.lineEdit_3.setText("")
        self.lineEdit_6.setText("")
        self.lineEdit_2.setText("")
        self.lineEdit_7.setText("")
        self.comboBox_3.setCurrentText("")
        self.lineEdit_8.setText("")

        self.lineEdit_4.setText("")
        self.lineEdit_5.setText("")
        self.lineEdit_9.setText("")
        self.lineEdit_16.setText("")

        self.lineEdit_21.setText("")

        self.lineEdit_17.setText("")

        self.lineEdit_22.setText("")

        self.lineEdit_18.setText("")
        self.lineEdit_19.setText("")

        self.lineEdit_20.setText("")

        self.lineEdit_10.setText("")
        self.lineEdit_11.setText("")

        # self.checkBox.setChecked(data[18])


        self.comboBox.setCurrentText("")
        self.lineEdit_12.setText("")
        self.lineEdit_13.setText("")
        self.comboBox_2.setCurrentText("")
        self.lineEdit_14.setText("")
      