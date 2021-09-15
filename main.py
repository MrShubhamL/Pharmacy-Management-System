from PyQt5.QtCore import *
from PyQt5.QtGui import *
from PyQt5.QtWidgets import *
import sys
import sqlite3
from tkinter import*
from tkinter import ttk
from PyQt5.uic import loadUi, loadUiType

from PyQt5 import QtWidgets, QtCore, QtGui, uic
from PyQt5.QtCore import Qt
from shutil import copyfile
from xlwt import Workbook
from PIL import Image
from PIL import Image
from shutil import copyfile
from xlwt import Workbook
# con = sqlite3.connect("database/Library.db")
# cur = con.cursor()
import Masters,toolmenu,Owner_login

class MainApp(QMainWindow,Tk):
    def __init__(self):
        # super(MainApp,self).__init__()
        QMainWindow.__init__(self)
        self.initUI()
        self.setWindowIcon(QtGui.QIcon('icon.ico'))
        self.setWindowTitle("Medivision")
        self.showFullScreen()
        self.setGeometry(0, 0, 1366, 768)
        self.setCentralWidget(self.mdi)
        self.show()


    def initUI(self):
        self.mdi = QMdiArea()
        self.toolBar()
        self.mainMenu()
        # self.tabWidget()
        # self.widgets()
        # self.layouts()
        # self.displayProducts()
        # self.displayMembers()


    def toolBar(self):
        self.tb = self.addToolBar("Tool Bar")
        self.tb.setToolButtonStyle(Qt.ToolButtonTextUnderIcon)
        self.addActions

        # Tool Bar Buttons
        self.sales = QAction(QIcon('src/icons/sales.png'), "F5-Sales", self)
        self.sales.setFont(QFont("Liberation Mono", 12))
        self.sales.triggered.connect(self.Sales)
        self.tb.addAction(self.sales)
        self.tb.addSeparator()

        self.purchase = QAction(QIcon('src/icons/purchase.png'), "F6-Purchase", self)
        # self.addMember.triggered.connect(self.add_member)
        self.purchase.setFont(QFont("Liberation Mono",12))
        self.purchase.triggered.connect(self.Purchase)
        self.tb.addAction(self.purchase)
        self.tb.addSeparator()

        self.S_return = QAction(QIcon('src/icons/S_return.png'), "F7-Sales Return", self)
        self.S_return.setFont(QFont("Liberation Mono", 12))
        # self.sellProduct.triggered.connect(self.sell_product)
        self.tb.addAction(self.S_return)
        self.tb.addSeparator()

        self.P_return = QAction(QIcon('src/icons/P_return.png'), "F8-Pur. Return", self)
        self.P_return.setFont(QFont("Liberation Mono", 12))
        # self.returnProduct.triggered.connect(self.return_product)
        self.tb.addAction(self.P_return)
        self.tb.addSeparator()

        self.receipts = QAction(QIcon('src/icons/receipt.png'), "F9-Receipts", self)
        self.receipts.setFont(QFont("Arial", 12))
        # self.refreshTb.triggered.connect(self.refresh_all_tables)
        self.tb.addAction(self.receipts)
        self.tb.addSeparator()

        self.payment = QAction(QIcon('src/icons/payment.png'), "F11-Payments", self)
        self.payment.setFont(QFont("Arial", 12))
        # self.refreshTb.triggered.connect(self.refresh_all_tables)
        self.tb.addAction(self.payment)
        self.tb.addSeparator()

        self.ledger = QAction(QIcon('src/icons/ledger.png'), "F12-Ledger", self)
        self.ledger.setFont(QFont("Arial", 12))
        # self.refreshTb.triggered.connect(self.refresh_all_tables)
        self.tb.addAction(self.ledger)
        self.tb.addSeparator()

        self.product_detalis = QAction(QIcon('src/icons/purchase.png'), "Products Details", self)
        self.product_detalis.setFont(QFont("Arial", 12))
        self.product_detalis.triggered.connect(self.Product_Details)
        self.tb.addAction(self.product_detalis)
        self.tb.addSeparator()



    def actionBar(self):
        self.actionbar = self.statusBar()


# ============== Main Menu Bar =======================
    def mainMenu(self):
        self.menubar = self.menuBar()      
          
        masters_bar = self.menubar.addMenu("Masters")
        transaction_bar = self.menubar.addMenu("Transactions")
        Acc_bar = self.menubar.addMenu("Acoount Reports")
        report_bar = self.menubar.addMenu("Reports")
        m_report_bar = self.menubar.addMenu("Management Reports")
        o_s_bar = self.menubar.addMenu("Owner Security")
        utilities_bar = self.menubar.addMenu("Utilities")
        downloads_bar = self.menubar.addMenu("Downloads")
        windowa_bar = self.menubar.addMenu("Windows")
        exit_bar = self.menubar.addMenu("Exit")

        # Sub menu items
# ============================= Masters Bar ======================================
        GST_Category = QAction("GST Category Master", self)
        GST_Category.triggered.connect(self.Masters1)
        masters_bar.addAction(GST_Category)

        Category_Master = QAction("Category Master", self)
        Category_Master.triggered.connect(self.Masters2)
        masters_bar.addAction(Category_Master)

        HSN_Master = QAction("HSN Master", self)
        HSN_Master.triggered.connect(self.Masters3)
        masters_bar.addAction(HSN_Master)


        P_Master = QAction("Product Master", self)
        P_Master.triggered.connect(self.Masters4)
        masters_bar.addAction(P_Master)

        Phy_Master = QAction("Physical Stock", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(Phy_Master)

        SalesMan_Master = QAction("SalesMan Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(SalesMan_Master)

        Dr_Master = QAction("Doctor Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(Dr_Master)

        F_Master = QAction("Family Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(F_Master)

        Patient_Master = QAction("Patient Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(Patient_Master)

        group_master = QAction("Group Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(group_master)

        ledger_master = QAction("Ledger Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(ledger_master)

        cash_pending = QAction("Cash Pending Ledger", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(cash_pending)

        reminder = QAction("Reminder", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(reminder)

        N_Master = QAction("Narration Master", self)
        # exit_file.triggered.connect(self.exit_programm_func)
        masters_bar.addAction(N_Master)
# ============================= Masters Bar END ======================================


      



       ####################### # Transaction Bar # ##########################
        OrderMenu = transaction_bar.addMenu("Orders")
        OrderMenu.addAction("Order 1...")
        OrderMenu.addAction("Order 2...")
        # check_statistic.triggered.connect(self.check_staticctics)

        purchase_inward = QAction("Purchase Inward", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(purchase_inward)

        self.purchase_bill = QAction("Purchase Bill", self)
        self.purchase_bill.setShortcut("F6")
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(self.purchase_bill)

        self.Sales_bill = QAction("Sales Bill", self)
        self.Sales_bill.setShortcut("F5")
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(self.Sales_bill)

        purchase_return = transaction_bar.addMenu("Purchase Return")
        purchase_return.addAction("Purchase 1...")
        purchase_return.addAction("Purchase 2...")
        # # clear_items_table.triggered.connect(self.clear_all_items)

        self.sales_return = QAction("Sales Return", self)
        self.sales_return.setShortcut("F7")
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(self.sales_return)

        vouchers = QAction("Vouchers", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(vouchers)

        cash_collection = QAction("Cash Collection", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(cash_collection)

        self.receipts = QAction("Receipts", self)
        self.receipts.setShortcut("F9")
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(self.receipts)

        self.payments = QAction("Payments", self)
        self.payments.setShortcut("F11")
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(self.payments)

        stock_adjustment = QAction("Stock Adjustments", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(stock_adjustment)

        bill_proforma = QAction("Bill Proforma", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(bill_proforma)

        bank_reconciliation = QAction("Bank Reconciliation", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        transaction_bar.addAction(bank_reconciliation)
       ####################### # Transaction Bar End # ##########################

       ####################### # Accounts Report Bar # ##########################

        self.Ledger_Menu = QAction("Ledger", self)
        self.Ledger_Menu.setShortcut("F12")
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(self.Ledger_Menu)

        Cash_Pending_Menu = QAction("Cash Pending Ledger Report", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(Cash_Pending_Menu)

        group_summery_Menu = QAction("Group Summary", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(group_summery_Menu)

        trail_balance = QAction("Trial Balance", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(trail_balance)

        P_L_Account = QAction("Profite and Loss Account", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(P_L_Account)

        Balance_Sheet_Menu = QAction("Balance Sheet", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(Balance_Sheet_Menu)

        Acc_bar.addSeparator()

        register_printing = Acc_bar.addMenu("Register Printing")
        register_printing.addAction("Print 1...")
        register_printing.addAction("Print 2...")

        Acc_bar.addSeparator()

        cash_book = QAction("Cash Book", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(cash_book)

        daily_cash_tally = QAction("Daily Cash Tally", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(daily_cash_tally)

        Acc_bar.addSeparator()

        profit_summary = QAction("Profite Summary", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(profit_summary)

        business_glance = QAction("Business at a Glance", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(business_glance)

        sales_purchase = QAction("Sales Purchase Summery", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(sales_purchase)


        LBT_register = QAction("LBT Purchase Register", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(LBT_register)


        LBT_register = QAction("LBT Purchase Register", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(LBT_register)

        Acc_bar.addSeparator()


        value_added_report = QAction("Value Added Tax Report", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(value_added_report)


        j1_j2_report = QAction("J1/J2 Report", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(j1_j2_report)


        Annexures = QAction("Vat Annexures", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(Annexures)


        GSTR_3B = QAction("Data For GSTR 3B", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(GSTR_3B)


        GSTR_1 = QAction("Data For GSTR 1", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(GSTR_1)


        GSTR_2 = QAction("Data For GSTR 2", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(GSTR_2)


        trans_1 = QAction("Data For Trans 1", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(trans_1)


        GST_Day_Books = QAction("GST Day Books", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        Acc_bar.addAction(GST_Day_Books)
       ####################### # Accounts Report Bar END # ##########################


       ####################### # Reports Bar # ##########################

        sales_reports = QAction("Sales Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(sales_reports)

        purchase_reports = QAction("Purchase Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(purchase_reports)

        returns_reports = QAction("Sales Return Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(returns_reports)

        purchase_returns_reports = QAction("Purchase Return Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(purchase_returns_reports)

        purchase_inward_reports = QAction("Purchase Inward Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(purchase_inward_reports)

        wise_stock_reports = QAction("Preparation Wise Stock Details Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(wise_stock_reports)

        stock_details_reports = QAction("Stock Details", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(stock_details_reports)

        stock_statement_reports = QAction("Stock Statement", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(stock_statement_reports)

        expiry_reports = QAction("Expiry Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(expiry_reports)

        Drug_type_reports = QAction("Drug Type Wise Reports", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        report_bar.addAction(Drug_type_reports)
       ####################### # Reports Bar END # ##########################

       ####################### # Management Reports Bar # ##########################

        product_card = QAction("Product Card", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(product_card)
   
        Points_Ledger = QAction("Points Ledger", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(Points_Ledger)
   
        producr_ledger = QAction("Product Monthly Ledger", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(producr_ledger)
   
        substitute = QAction("Substitute", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(substitute)
   
        order_sales = QAction("Order Based on Sales", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(order_sales)
   
        saftey_stock = QAction("Order Based on Safety Stock", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(saftey_stock)
   
        DayReport = QAction("Day Report", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(DayReport)
   
        DayReport = QAction("Purchase Rate Variation", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(DayReport)
   
        DayReport = QAction("Non Moving Stock", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        m_report_bar.addAction(DayReport)
       ####################### # Management Reports Bar END # ##########################

       ####################### # Owner Security Bar # ##########################

        logins_create = QAction("Create Logins", self)
        # logins_create.triggered.connect(self.Owner_login)
        o_s_bar.addAction(logins_create)

        rights_login = QAction("Logins Rights", self)
        rights_login.triggered.connect(self.Owner_login)
        o_s_bar.addAction(rights_login)
       ####################### # Owner Security Bar End # ##########################

       ####################### # Utilities Bar # ##########################

        backup_database = QAction("Backup Database", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(backup_database)

        utilities_bar.addSeparator()

        hospital_dashboard = QAction("Hospital Dashboard", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(hospital_dashboard)

        Control_is_Here = QAction("Control Is Here", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(Control_is_Here)

        most_billing_products  = QAction("Most Billing Products", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(most_billing_products)

        stationary_utility = QAction("Bill Stationary Setting Utility", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(stationary_utility)

        utilities_bar.addSeparator()

        Day_end_process = QAction("Day End Process", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(Day_end_process)

        reverce_day_end_process = QAction("Reverce Day End Process", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(reverce_day_end_process)

        utilities_bar.addSeparator()

        medivision_data_transfer = QAction("Medivision Data Transfer", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(medivision_data_transfer)

        Products_master = QAction("Products Master Edition Utility", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(Products_master)

        physical_stock_edition = QAction("Physical Stock Edition Utility", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(physical_stock_edition)

        Product_card_and_P_Stock = QAction("Physical Card and Phisical Stock Tally", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(Product_card_and_P_Stock)

        storage_transfer = QAction("Storage Transfer", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(storage_transfer)

        Update_GST = QAction("Update GST", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(Update_GST)

        utilities_bar.addSeparator()

        tally_transfer = QAction("Tally Transfer", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        utilities_bar.addAction(tally_transfer)

        utilities_bar.addSeparator()

        SMS_Module = utilities_bar.addMenu("SMS Module")
        SMS_Module.addAction("Module 1...")
        SMS_Module.addAction("Module 2...")

        utilities_bar.addSeparator()

        iLogic_Utility = utilities_bar.addMenu("iLogic Utility")
        iLogic_Utility.addAction("logic utility 1...")
        iLogic_Utility.addAction("logic utility 2...")

       ####################### # Utilities Bar END # ##########################

       ####################### # Download Bar  # ##########################

        Download_wholesaler_database = QAction("Download Wholesaler Databse", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        downloads_bar.addAction(Download_wholesaler_database)
       
        Download_Product_bank = QAction("Download Product Bank", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        downloads_bar.addAction(Download_Product_bank)
       
        Map_productMaster = QAction("Map ProductMaster with Product Bank", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        downloads_bar.addAction(Map_productMaster)
       
        Download_Medisoft_New_Version = QAction("Download Medisoft New Version", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        downloads_bar.addAction(Download_Medisoft_New_Version)
       
        Download_Ammyy_Admin = QAction("Download Ammyy Admin", self)
        # clear_items_table.triggered.connect(self.clear_all_items)
        downloads_bar.addAction(Download_Ammyy_Admin)

       ####################### # Download Bar  # ##########################


        # # Help_bar
        # about_prg = QAction("About", self)
        # # about_prg.triggered.connect(self.about_programm)
        # help_bar.addAction(about_prg)


    
        exit_window = QAction("Exit", self)
        exit_window.setIcon(QIcon("src/icons/cancel.png"))
        exit_window.triggered.connect(self.exit)
        exit_bar.addAction(exit_window)

    def exit(self):
        sys.exit(MainApp)


    #   ======================= ToolBar Operations ========================


    def Sales(self):
        self.saleswindow = toolmenu.Sales()
        self.mdi.addSubWindow(self.saleswindow)
        self.saleswindow.show()



    def Purchase(self):
        self.purchasewindow = toolmenu.Purchase()
        self.mdi.addSubWindow(self.purchasewindow)
        self.purchasewindow.show()



    def Product_Details(self):
        self.Productwindow = toolmenu.Product_Details()
        self.mdi.addSubWindow(self.Productwindow)
        self.Productwindow.show()



    #   ======================= Master Menubar Operations ========================


    def Masters1(self):
        self.master_window = Masters.GST_Category_Master()
        self.mdi.addSubWindow(self.master_window)
        self.master_window.show()


    def Masters2(self):
        self.master_window = Masters.Category_Master()
        self.mdi.addSubWindow(self.master_window)
        self.master_window.show()


    def Masters3(self):
        self.master_window = Masters.HSN_Master()
        self.mdi.addSubWindow(self.master_window)
        self.master_window.show()


    def Masters4(self):
        self.master_window = Masters.Product_Master()
        self.mdi.addSubWindow(self.master_window)
        self.master_window.show()


    #   ======================= Owner_Login Operations ========================


    def Owner_login(self):
        self.owner_rights = Owner_login.Owner_login()
        self.mdi.addSubWindow(self.owner_rights)
        self.owner_rights.show()













def main():
    app = QApplication(sys.argv)
    window = MainApp()
    window.show()
    sys.exit(app.exec_())
    # app.exec_()


if __name__ == '__main__':
    main()
    
    