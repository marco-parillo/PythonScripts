'''
Prints a local csv file.
'''

import sys
import csv
# from PySide6 import QtCore, QtWidgets, QtGui
from PySide6 import QtCore, QtWidgets # , QtGui not needed?

class MyWidget(QtWidgets.QWidget):
    '''
    extends QWidget and includes a QPushButton and QLabel.
    When you click the button, the magic function is called.
    '''
    def __init__(self):
        super().__init__()

        self.button = QtWidgets.QPushButton("Next Record!")
        self.text = QtWidgets.QLabel("Start of File",
                                     alignment=QtCore.Qt.AlignCenter)

        self.layout = QtWidgets.QVBoxLayout()
        self.layout.addWidget(self.text)
        self.layout.addWidget(self.button)
        self.setLayout(self.layout)

        self.button.clicked.connect(self.magic)

    @QtCore.Slot()
    def magic(self):
        '''
        The MyWidget class has the magic member function that
        reads the csv file.
        '''
        try:
            with open('employee_file.csv', mode='r', encoding='utf-8') as employee_file:
                csv_data = csv.reader (employee_file)
                csv_list = list(csv_data) # actually a list of lists
                self.text.setText(str(csv_list[0]))
        except TypeError:
            self.text.setText("Type Error")
        except OSError:
            self.text.setText("OS Error")
        except:
            self.text.setText("Some other file opening exception")


if __name__ == "__main__":
    app = QtWidgets.QApplication([])

    widget = MyWidget()
    widget.resize(800, 600)
    widget.show()

    sys.exit(app.exec_())
