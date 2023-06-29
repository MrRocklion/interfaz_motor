import sys
from PyQt5 import QtWidgets, uic
import sys


fusible_1 = True
fusible_2 = True
fusible_3 = True
fusible_4 = True
fusible_5 = True
fusible_6 = True

def handleBtn1():
    global fusible_1
    fusible_1 = not fusible_1
    if fusible_1:
        window.lab1.setText("ON")
        window.lab1.setStyleSheet("color: green")
    else:
        window.lab1.setText("OFF")
        window.lab1.setStyleSheet("color: red")

def handleBtn2():

    global fusible_2
    fusible_2 = not fusible_2
    if fusible_2:
        window.lab2.setText("ON")
        window.lab2.setStyleSheet("color: green")
    else:
        window.lab2.setText("OFF")
        window.lab2.setStyleSheet("color: red")


def handleBtn3():

    global fusible_3
    fusible_3 = not fusible_3
    if fusible_3:
        window.lab3.setText("ON")
        window.lab3.setStyleSheet("color: green")
    else:
        window.lab3.setText("OFF")
        window.lab3.setStyleSheet("color: red")


def handleBtn4():

    global fusible_4
    fusible_4 = not fusible_4
    if fusible_4:
        window.lab4.setText("ON")
        window.lab4.setStyleSheet("color: green")
    else:
        window.lab4.setText("OFF")
        window.lab4.setStyleSheet("color: red")


def handleBtn5():

    global fusible_5
    fusible_5 = not fusible_5
    if fusible_5:
        window.lab5.setText("ON")
        window.lab5.setStyleSheet("color: green")
    else:
        window.lab5.setText("OFF")
        window.lab5.setStyleSheet("color: red")

def handleBtn6():
   
    global fusible_6
    fusible_6 = not fusible_6
    if fusible_6:
        window.lab6.setText("ON")
        window.lab6.setStyleSheet("color: green")
    else:
        window.lab6.setText("OFF")
        window.lab6.setStyleSheet("color: red")



class Ui(QtWidgets.QMainWindow):
    def __init__(self):
        super(Ui, self).__init__() # Call the inherited classes __init__ method
        uic.loadUi('mainwindow.ui', self) #
        self.show() # Show the GUI
app = QtWidgets.QApplication(sys.argv)
window = Ui()
window.btn1.clicked.connect(lambda:handleBtn1() )
window.btn2.clicked.connect(lambda:handleBtn2() )
window.btn3.clicked.connect(lambda:handleBtn3() )
window.btn4.clicked.connect(lambda:handleBtn4() )
window.btn5.clicked.connect(lambda:handleBtn5() )
window.btn6.clicked.connect(lambda:handleBtn6() )
app.exec_()