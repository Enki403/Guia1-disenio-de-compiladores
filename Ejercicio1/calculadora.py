from math import sqrt
from PyQt5.QtGui import QIcon
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QLineEdit, QPushButton, QApplication, QStyleFactory

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # titulo
        self.setWindowTitle('Calculadora (Ejercicio 1)')
        # layout
        self.setLayout(QVBoxLayout())
        self.keypad()

        self.operands = []
        self.answer = []
        self.calculated = False

        # setting fixed size
        self.setFixedSize(541,212)
        self.setWindowIcon(QIcon('icons/calc_icon.png'))

        # enable/disable debug mode
        self.debug_mode = False
    
        self.show()

    def keypad(self):
        container = QWidget()
        # grid layout
        container.setLayout(QGridLayout())

        # botones
        self.result = QLineEdit()
        self.result.setReadOnly(True)
        btn_eq = QPushButton('=', clicked = self.f_result)
        btn_ac = QPushButton('AC', clicked = self.clear)
        btn_0 = QPushButton('0', clicked = lambda:self.num_press('0'))
        btn_1 = QPushButton('1', clicked = lambda:self.num_press('1'))
        btn_2 = QPushButton('2', clicked = lambda:self.num_press('2'))
        btn_3 = QPushButton('3', clicked = lambda:self.num_press('3'))
        btn_4 = QPushButton('4', clicked = lambda:self.num_press('4'))
        btn_5 = QPushButton('5', clicked = lambda:self.num_press('5'))
        btn_6 = QPushButton('6', clicked = lambda:self.num_press('6'))
        btn_7 = QPushButton('7', clicked = lambda:self.num_press('7'))
        btn_8 = QPushButton('8', clicked = lambda:self.num_press('8'))
        btn_9 = QPushButton('9', clicked = lambda:self.num_press('9'))
        btn_add = QPushButton('+', clicked = lambda:self.op_press('+'))
        btn_sub = QPushButton('-', clicked = lambda:self.op_press('-'))
        btn_mult = QPushButton('*', clicked = lambda:self.op_press('*'))
        btn_div = QPushButton('/', clicked = lambda:self.op_press('/'))
        btn_dot = QPushButton('.', clicked = lambda:self.num_press('.'))
        btn_sqrt = QPushButton('√', clicked = lambda:self.op_press('sqrt('))
        btn_open_p = QPushButton('(', clicked = lambda:self.op_press('('))
        btn_close_p = QPushButton(')', clicked = lambda:self.op_press(')'))

        # agregar botones al layout
        container.layout().addWidget(self.result, 0, 0, 1, 5)

        container.layout().addWidget(btn_7,2,0)
        container.layout().addWidget(btn_8,2,1)
        container.layout().addWidget(btn_9,2,2)
        container.layout().addWidget(btn_sqrt,2,3)
        container.layout().addWidget(btn_ac,2,4)

        container.layout().addWidget(btn_4,3,0)
        container.layout().addWidget(btn_5,3,1)
        container.layout().addWidget(btn_6,3,2)
        container.layout().addWidget(btn_add,3,3)
        container.layout().addWidget(btn_mult,3,4)

        container.layout().addWidget(btn_1,4,0)
        container.layout().addWidget(btn_2,4,1)
        container.layout().addWidget(btn_3,4,2)
        container.layout().addWidget(btn_sub,4,3)
        container.layout().addWidget(btn_div,4,4)

        container.layout().addWidget(btn_dot,5,0)
        container.layout().addWidget(btn_0,5,1)
        container.layout().addWidget(btn_open_p,5,2)
        container.layout().addWidget(btn_close_p,5,3)
        container.layout().addWidget(btn_eq, 5,4)

        self.layout().addWidget(container)
   
    def num_press(self, key):
        if self.calculated:
            self.clear()
            self.calculated = False

        self.operands.append(key)
        result_string = ''.join(self.operands)
        if self.answer:
            self.result.setText(''.join(self.answer) + result_string)
        else:
            self.result.setText(result_string)

        if self.debug_mode: self.debug()

    def op_press(self, key):

        temp_string = ''.join(self.operands).rstrip('.')
        if temp_string != "":
            self.answer.append(temp_string)
        self.answer.append(key)
        self.operands = []
        self.result.setText(''.join(self.answer))
        
        if self.debug_mode: self.debug()

    def f_result(self):
        final_string = ''.join(self.answer) + ''.join(self.operands)
        try:
            final_result = eval(final_string)
        except SyntaxError as e:
            if "'(' was never closed" in e.msg:
                self.num_press(')')
                self.f_result()
            else:
                self.result.setText('Error de sintaxis...')
        except ZeroDivisionError:
             self.result.setText("No se puede dividir entre 0")
        except:
                self.result.setText('Error de sintaxis...')

        else:
            final_string += ' = '
            final_string += str(final_result)
            self.result.setText(final_string)
        self.calculated = True

        if self.debug_mode: self.debug()


    def clear(self):
        self.operands = []
        self.answer = []
        self.result.clear()
        
        if self.debug_mode: self.debug()

    def debug(self):
        print('==============================')
        print('buffer -> ',self.operands)
        print('cache -> ', self.answer)
        print('==============================')

app = QApplication([])
mw = MainWindow()
app.setStyle(QStyleFactory.create('Fusion'))
app.exec_()
