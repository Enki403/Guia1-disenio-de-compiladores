from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QApplication, QStyleFactory, QLabel
import re

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # titulo
        self.setWindowTitle('Conversor de Bases (Ejercicio 2)')

        # layout
        self.setLayout(QVBoxLayout())
        self.inputs()

        # setting fixed size & icon
        self.setFixedSize(485,200)
        self.setWindowIcon(QIcon('icons/conv_icon.png'))
    
        self.show()

    def inputs(self):
        container = QWidget()
        # grid layout
        container.setLayout(QGridLayout())

        #labels
        bin_label = QLabel("&Binario: ",self)
        oct_label = QLabel("&Octal: ",self)
        dec_label = QLabel("&Decimal: ",self)
        hex_label = QLabel("&Hexadecimal: ",self)

        # botones
        self.binary = QLineEdit()
        self.octal = QLineEdit()
        self.decimal = QLineEdit()
        self.hexadecimal = QLineEdit()


        self.btn_convert_bin = QPushButton('Convertir', clicked = lambda:self.convert_bin())
        self.btn_convert_oct = QPushButton('Convertir', clicked = lambda:self.convert_oct())
        self.btn_convert_dec = QPushButton('Convertir', clicked = lambda:self.convert_dec())
        self.btn_convert_hex = QPushButton('Convertir', clicked = lambda:self.convert_hex())

        # binding qlabel & qline
        bin_label.setBuddy(self.binary)
        oct_label.setBuddy(self.octal)
        dec_label.setBuddy(self.decimal)
        hex_label.setBuddy(self.hexadecimal)

        # agregar botones al layout
        container.layout().addWidget(self.binary, 0, 1, 1, 4)
        container.layout().addWidget(self.octal, 1, 1, 1, 4)
        container.layout().addWidget(self.decimal, 2, 1, 1, 4)
        container.layout().addWidget(self.hexadecimal, 3, 1, 1, 4)

        container.layout().addWidget(bin_label, 0, 0)
        container.layout().addWidget(oct_label, 1, 0)
        container.layout().addWidget(dec_label, 2, 0)
        container.layout().addWidget(hex_label, 3, 0)

        container.layout().addWidget(self.btn_convert_bin,0,5)
        container.layout().addWidget(self.btn_convert_oct,1,5)
        container.layout().addWidget(self.btn_convert_dec,2,5)
        container.layout().addWidget(self.btn_convert_hex,3,5)

        self.layout().addWidget(container)

    def convert_bin(self):
        if re.search("^[01]+$", self.binary.text()):
            self.octal.setText(str(oct(int(self.binary.text(), 2))[2:]))
            self.decimal.setText(str(int(self.binary.text(), 2)))
            self.hexadecimal.setText(str(hex(int(self.binary.text(), 2))[2:]))

    def convert_oct(self):
        if re.search("^[01234567]+$", self.octal.text()):
            self.binary.setText(str(bin(int(self.octal.text(), 8))[2:]))
            self.decimal.setText(str(int(self.octal.text(), 8)))
            self.hexadecimal.setText(str(hex(int(self.octal.text(), 8))[2:]))

    def convert_dec(self):
        if re.search("^\d+$", self.decimal.text()):
            self.binary.setText(str(bin(int(self.decimal.text()))[2:]))
            self.octal.setText(str(oct(int(self.decimal.text()))[2:]))
            self.hexadecimal.setText(str(hex(int(self.decimal.text()))[2:]))

    def convert_hex(self):
        if re.search("^[ABCDEFabcdef\d]+$", self.hexadecimal.text()):
            self.binary.setText(str(bin(int(self.hexadecimal.text(), 16))[2:]))
            self.octal.setText(str(oct(int(self.hexadecimal.text(), 16))[2:]))
            self.decimal.setText(str(int(self.hexadecimal.text(), 16)))


app = QApplication([])
mw = MainWindow()
app.setStyle(QStyleFactory.create('Fusion'))
app.exec_()