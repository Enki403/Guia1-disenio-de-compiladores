from PyQt5.QtGui import QIcon
from PyQt5.QtCore import Qt
from PyQt5.QtWidgets import QWidget, QVBoxLayout, QGridLayout, QPlainTextEdit, QPushButton, QApplication, QStyleFactory, QLabel, QFileDialog
import re
import pandas as pd

class MainWindow(QWidget):
    def __init__(self):
        super().__init__()
        # titulo
        self.setWindowTitle('Analizador (Ejercicio 3)')

        # setting fixed size & icon
        self.setFixedSize(1400,496)
        self.setWindowIcon(QIcon('icons/pat_icon.png'))

        # layout
        self.setLayout(QVBoxLayout())

        # enable/disable debug mode
        self.debug_mode = False

        self.file_name = ''
        self.file_content = ''

        # regex
        self.regex_first = r"\d+"
        self.regex_second = r"[\d]+[\w]+"
        self.regex_third = r"\w*([aeiou])\w*\1\w*\1\w*"
        self.regex_fourth = r"[$-/:-?{-~!\"^_`\[\]]"
        
        self.results()
    
        self.show()

    def file_loader(self):
        container = QWidget()
        # grid layout
        container.setLayout(QGridLayout())

        # buttons
        self.btn_open_file = QPushButton('Abrir...', clicked = self.open_file_dialog)
        self.search_pattern = QPushButton('Coincidir', clicked = self.find_instances)
        self.clear = QPushButton('Borrar contenedores', clicked = self.f_clear)

        container.layout().addWidget(self.btn_open_file, 0,0)
        container.layout().addWidget(self.search_pattern, 0,1)
        container.layout().addWidget(self.clear, 0,2)

        self.layout().addWidget(container)
    
    def results(self):
        self.file_loader()
        container = QWidget()
        # grid layout
        container.setLayout(QGridLayout())

        # text box
        self.first = QPlainTextEdit(self)
        self.second = QPlainTextEdit(self)
        self.third = QPlainTextEdit(self)
        self.fourth = QPlainTextEdit(self)

        self.first.setReadOnly(True)
        self.second.setReadOnly(True)
        self.third.setReadOnly(True)
        self.fourth.setReadOnly(True)

        # labels
        first_label = QLabel("&Coincidencia(s) de r\'{}\': ".format(self.regex_first),self)
        second_label = QLabel("&Coincidencia(s) de r\'{}\': ".format(self.regex_second),self)
        third_label = QLabel("&Coincidencia(s) de r\'{}\': ".format(self.regex_third),self)
        fourth_label = QLabel("&Coincidencia(s) de r\'{}\': ".format(self.regex_fourth),self)


        # binding
        first_label.setBuddy(self.first)
        second_label.setBuddy(self.second)
        third_label.setBuddy(self.third)
        fourth_label.setBuddy(self.fourth)

        container.layout().addWidget(self.first, 1, 0)
        container.layout().addWidget(first_label, 0, 0)
        container.layout().addWidget(self.second, 1, 1)
        container.layout().addWidget(second_label, 0, 1)
        container.layout().addWidget(self.third, 1, 2)
        container.layout().addWidget(third_label, 0, 2)
        container.layout().addWidget(self.fourth, 1, 3)
        container.layout().addWidget(fourth_label, 0, 3)

        self.layout().addWidget(container)
    
    def quantity(self, q1, q2, q3, q4):
        self.quantity_container = QWidget()
        # grid layout
        self.quantity_container.setLayout(QGridLayout())


        # labels        
        first_label = QLabel("&Coincidencia(s): {}".format(len(q1)),self)
        second_label = QLabel("&Coincidencia(s): {}".format(len(q2)),self)
        third_label = QLabel("&Coincidencia(s): {}".format(len(q3)),self)
        fourth_label = QLabel("&Coincidencia(s): {}".format(len(q4)),self)

        # binding
        first_label.setBuddy(self.first)
        second_label.setBuddy(self.second)
        third_label.setBuddy(self.third)
        fourth_label.setBuddy(self.fourth)

        self.quantity_container.layout().addWidget(first_label, 0, 0)
        self.quantity_container.layout().addWidget(second_label, 0, 1)
        self.quantity_container.layout().addWidget(third_label, 0, 2)
        self.quantity_container.layout().addWidget(fourth_label, 0, 3)

        self.quantity_container.layout().addWidget(QPushButton('Exportar', clicked = self.export_file), 1, 1, 1, 2)

        self.layout().addWidget(self.quantity_container)

    def hide_quantity(self):
        try:
            self.quantity_container.hide()
        except:
            pass
    
    def hide_msg(self):
        try:
            self.exp_msg .hide()
        except:
            pass

    def exported_msg(self, p):
        self.exp_msg = QWidget()
        # grid layout
        self.exp_msg.setLayout(QGridLayout())
        if p == 2:
            msg = QLabel("Nada que exportar.",self)
            msg.setStyleSheet("font-weight:700;color:red;")
        else:
            msg = QLabel("Exportado con exito.",self)
            msg.setStyleSheet("font-weight:700;color:green;")
        msg.setAlignment(Qt.AlignCenter)
        self.exp_msg.layout().addWidget(msg, 0, 1, 1, 2)
        self.layout().addWidget(self.exp_msg)


    def find_instances(self):
        self.f_clear()

        self.q1 = re.findall(self.regex_first, self.file_content)
        self.q2 = re.findall(self.regex_second, self.file_content, re.IGNORECASE)
        self.q3 = re.findall(self.regex_third, self.file_content, re.IGNORECASE)
        self.q4 = re.findall(self.regex_fourth, self.file_content, re.IGNORECASE)

        self.quantity(self.q1, self.q2, self.q3, self.q4)

        if self.debug_mode:
            print("first array: ", self.q1)
            print("second array: ", self.q2)
            print("third array: ", self.q3)
            print("fourth array: ", self.q4)

        for coincidence1 in self.q1:
            self.first.insertPlainText(coincidence1+'\n')

        for coincidence2 in self.q2:
            self.second.insertPlainText(coincidence2+'\n')

        for coincidence3 in self.q3:
            self.third.insertPlainText(coincidence3+'\n')
        
        for coincidence3 in self.q4:
            self.fourth.insertPlainText(coincidence3+'\n')

    def f_clear(self):
        self.hide_quantity()
        self.hide_msg()
        self.first.clear()
        self.second.clear()
        self.third.clear()
        self.fourth.clear()
    
    def open_file_dialog(self):
        options = QFileDialog.Options()
        self.file_name, file_type = QFileDialog.getOpenFileName(self,"QFileDialog.getOpenFileName()","","Text Files (*.txt);;All Files (*)", options=options)
        if self.file_name:
            try:
                self.setWindowTitle('Analizador (Ejercicio 3) -  {}'.format(self.file_name.split('/')[-1]))
                file = open(self.file_name, 'r')
                self.file_content = file.read()
                file.close()
            except:
                self.setWindowTitle('Analizador (Ejercicio 3) -  *** Tipo de Archivo No Valido***'.format(self.file_name.split('/')[-1]))

    def export_file(self):
        self.hide_msg()

        # transformer
        data = [len(self.q1), len(self.q2), len(self.q3), len(self.q4)]
        max_v = data.index(max(data))

        self.q1.extend(["" for i in range(max(data) - len(self.q1))])
        self.q2.extend(["" for i in range(max(data) - len(self.q2))])
        self.q3.extend(["" for i in range(max(data) - len(self.q3))])
        self.q4.extend(["" for i in range(max(data) - len(self.q4))])

        
        df = pd.DataFrame({
             "Patron 1 (r\"{}\")".format(self.regex_first): self.q1,
             "Patron 2 (r\"{}\")".format(self.regex_second): self.q2,
             "Patron 3 (r\"{}\")".format(self.regex_third): self.q3,
             "Patron 4 (r\"{}\")".format(self.regex_fourth): self.q4
        })
        
        if (self.q1 == [] or self.q2 == [] or self.q3 == [] or self.q4 == []): 
            self.exported_msg(2)
            return

        writer = pd.ExcelWriter('Coincidencias en \'{}\'.xlsx'.format(self.file_name.split('/')[-1]), engine='xlsxwriter')
        df.to_excel(writer, sheet_name='Coincidencias', startrow=1, header=False, index=False)
        workbook = writer.book
        worksheet = writer.sheets['Coincidencias']
        (max_row, max_col) = df.shape
        column_settings = [{'header': column} for column in df.columns]
        worksheet.add_table(0, 0, max_row, max_col - 1, {'columns': column_settings})
        worksheet.set_column(0, max_col - 1, 39)
        writer.save()

        self.exported_msg(1)


app = QApplication([])
mw = MainWindow()
app.setStyle(QStyleFactory.create('Fusion'))
app.exec_()