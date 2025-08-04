import sys
from PyQt5 import QtWidgets
from PyQt5.QtWidgets import QMessageBox
import home as ui 
import DatabaseHandler1 as db

class Control:
    def __init__(self):
    
        app = QtWidgets.QApplication(sys.argv)
        MainWindow = QtWidgets.QMainWindow()
        self.ui = ui.Ui_MainWindow()
        self.ui.setupUi(MainWindow)
        self.db = db.MyDB()

        # show search window
        self.ui.pushButton.clicked.connect(self.showsearch)
        # show add window
        self.ui.pushButton_2.clicked.connect(self.showadd)
        # show delete window
        self.ui.pushButton_3.clicked.connect(self.showdelete)
        # show update window
        self.ui.pushButton_4.clicked.connect(self.showupdate)
        # show all students
        self.ui.pushButton_13.clicked.connect(self.showstudents)
        #back to main window
        self.ui.pushButton_6.clicked.connect(self.backmain)
        self.ui.pushButton_8.clicked.connect(self.backmain)
        self.ui.pushButton_10.clicked.connect(self.backmain)
        self.ui.pushButton_12.clicked.connect(self.backmain)
        self.ui.pushButton_14.clicked.connect(self.backmain)

        
        # add
        self.ui.pushButton_7.clicked.connect(self.add)
        # search
        self.ui.pushButton_5.clicked.connect(self.search)
        # delete
        self.ui.pushButton_9.clicked.connect(self.delete)
        # update
        self.ui.pushButton_11.clicked.connect(self.update)

        MainWindow.show()
        sys.exit(app.exec_())

    def showsearch(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page)
    def showadd(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_2)   
    def showdelete(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_3)
    def showupdate(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_4)    
    def backmain(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.stackedWidgetPage1)

# view all student
        
    def showstudents(self):
        self.ui.stackedWidget.setCurrentWidget(self.ui.page_5)  
        data = self.db.showall()

        # Set row and column count
        self.ui.tableWidget_2.setRowCount(len(data))
        self.ui.tableWidget_2.setColumnCount(4)  
        # Add column headers (optional)
        self.ui.tableWidget_2.setHorizontalHeaderLabels(["Name", "Admission", "Email", "Phone"])

        # Populate table with data
        for row_num, row_data in enumerate(data):
            for col_num, item in enumerate(row_data):
                self.ui.tableWidget_2.setItem(row_num, col_num, QtWidgets.QTableWidgetItem(str(item)))

    
  

    def add(self):
        name = self.ui.lineEdit_4.text()
        admission = self.ui.lineEdit_5.text()
        email = self.ui.lineEdit_6.text()   
        phone = self.ui.lineEdit_7.text() 
        print(name, admission, email, phone)
        status = self.db.insertUser(name, admission, email, phone)
        if status == 1:
            QMessageBox.information(self.ui.stackedWidget, "student added",'student added') #print("Student added successfully.")
        elif status == 2:
            QMessageBox.information(self.ui.stackedWidget, "student already exists", 'already exists') #print("Student already exists.")
        else:
            QMessageBox.information(self.ui.stackedWidget, "an error occurred" , 'error') #print("An error occurred.")


    def search(self):
        admission = self.ui.lineEdit_2.text()
        print(admission)
        data = self.db.finduser(admission)

        if data:
            self.ui.tableWidget.setRowCount(2)
            self.ui.tableWidget.setColumnCount(3)
            self.ui.tableWidget.setItem(0,0,QtWidgets.QTableWidgetItem("Name"))
            self.ui.tableWidget.setItem(0,1,QtWidgets.QTableWidgetItem("Phone"))
            self.ui.tableWidget.setItem(0,2,QtWidgets.QTableWidgetItem("Email"))
            self.ui.tableWidget.setItem(1,0,QtWidgets.QTableWidgetItem(data[0]))
            self.ui.tableWidget.setItem(1,1,QtWidgets.QTableWidgetItem(data[1]))
            self.ui.tableWidget.setItem(1,2,QtWidgets.QTableWidgetItem(data[2]))
       
            
        else:
            QMessageBox.information(self.ui.page, "student not found", 'not found') #print("Student not found")    
            
                
    def delete(self):    
        admission = self.ui.lineEdit_9.text()   
        print(admission)
        status = self.db.deleteUser(admission)
        if status == 1:
            QMessageBox.information(self.ui.stackedWidget, "deleted successfully", 'done') #print("Deleted successfully")
        else:
            QMessageBox.information(self.ui.stackedWidget, "not found", 'not found') #print("Student not found")   


    def update(self):
        name = self.ui.lineEdit_10.text()
        admission = self.ui.lineEdit_11.text()
        email = self.ui.lineEdit_12.text()
        phone = self.ui.lineEdit_13.text()
        print(name, admission, email, phone)
        status = self.db.updateUser(name, admission, email, phone)
        if status == 1:
            QMessageBox.information(self.ui.stackedWidget, "student updated successfully", 'done') #print("Student updated successfully.")
        else:
            QMessageBox.information(self.ui.stackedWidget, "student not found", 'not found') #print("Student not found.") 
        

if __name__ == "__main__":
        Control()    
