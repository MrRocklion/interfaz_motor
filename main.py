import sys
from PyQt5 import QtWidgets, uic
import RPi.GPIO as GPIO
import sys

GPIO.setmode(GPIO.BOARD)
#configuracion GPIO
pin_1 = 8
pin_2 = 10
pin_3 = 12
pin_4 = 11
pin_5 = 13
pin_6 = 15

GPIO.setup(pin_1,GPIO.OUT)
GPIO.setup(pin_2,GPIO.OUT)
GPIO.setup(pin_3,GPIO.OUT)
GPIO.setup(pin_4,GPIO.OUT)
GPIO.setup(pin_5,GPIO.OUT)
GPIO.setup(pin_6,GPIO.OUT)


fusible_1 = True
fusible_2 = True
fusible_3 = True
fusible_4 = True
fusible_5 = True
fusible_6 = True

GPIO.output(pin_1, True)
GPIO.output(pin_2, True)
GPIO.output(pin_3, True)
GPIO.output(pin_4, True)
GPIO.output(pin_5, True)
GPIO.output(pin_6, True)

def handleBtn1():
    global fusible_1
    fusible_1 = not fusible_1
    if fusible_1:
        window.lab1.setText("ON")
        window.lab1.setStyleSheet("color: green")
        GPIO.output(pin_1, True)
    else:
        window.lab1.setText("OFF")
        window.lab1.setStyleSheet("color: red")
        GPIO.output(pin_1, False)

def handleBtn2():

    global fusible_2
    fusible_2 = not fusible_2
    if fusible_2:
        window.lab2.setText("ON")
        window.lab2.setStyleSheet("color: green")
        GPIO.output(pin_2, True)
    else:
        window.lab2.setText("OFF")
        window.lab2.setStyleSheet("color: red")
        GPIO.output(pin_2, False)


def handleBtn3():

    global fusible_3
    fusible_3 = not fusible_3
    if fusible_3:
        window.lab3.setText("ON")
        window.lab3.setStyleSheet("color: green")
        GPIO.output(pin_3, True)
    else:
        window.lab3.setText("OFF")
        window.lab3.setStyleSheet("color: red")
        GPIO.output(pin_3, False)


def handleBtn4():

    global fusible_4
    fusible_4 = not fusible_4
    if fusible_4:
        window.lab4.setText("ON")
        window.lab4.setStyleSheet("color: green")
        GPIO.output(pin_4, True)
    else:
        window.lab4.setText("OFF")
        window.lab4.setStyleSheet("color: red")
        GPIO.output(pin_4, False)


def handleBtn5():

    global fusible_5
    fusible_5 = not fusible_5
    if fusible_5:
        window.lab5.setText("ON")
        window.lab5.setStyleSheet("color: green")
        GPIO.output(pin_5, True)
    else:
        window.lab5.setText("OFF")
        window.lab5.setStyleSheet("color: red")
        GPIO.output(pin_5, False)

def handleBtn6():
   
    global fusible_6
    fusible_6 = not fusible_6
    if fusible_6:
        window.lab6.setText("ON")
        window.lab6.setStyleSheet("color: green")
        GPIO.output(pin_6, True)
    else:
        window.lab6.setText("OFF")
        window.lab6.setStyleSheet("color: red")
        GPIO.output(pin_6, False)



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
app.exec_()