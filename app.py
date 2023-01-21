import sys
import random
import matplotlib

matplotlib.use("Qt5Agg")

from PySide2.QtWidgets import QMainWindow, QApplication
from PySide2.QtCore import QTimer

from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QMessageBox,
)

from PySide2.QtCore import Qt

from custom_errors import UnsupportedOperand

# Only needed for access to command line arguments
import sys


class FunctionInput(QWidget):
    def gotFocus(self) -> bool:
        print('eee')
        return super().hasFocus()
    def __init__(self) -> None:
        super().__init__()

        layout = QVBoxLayout()
        
        self.label = QLabel("Enter your function:")
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        input_layout = QHBoxLayout()
        self.input_dialog = QLineEdit()
        self.input_dialog.setStyleSheet(":focus{border: 2px solid #333; }*{padding: 5px;}")
        self.plot_button = QPushButton("Plot")
        self.plot_button.setStyleSheet(
            ":hover{background-color: #030303; color: #fff;}*{height:21px;background-color: #333; color: #fff;}"
        )


        self.min_x_label = QLabel("Min X")
        self.min_x_input = QLineEdit() 

        self.max_x_label = QLabel("Max X")
        self.max_x_input = QLineEdit()
        # self.max_x_input.setFocusPolicy(self.func)


        min_max_layout = QVBoxLayout() 
        
        min_max_layout.addWidget(self.min_x_label)
        min_max_layout.addWidget(self.min_x_input)
        min_max_layout.addWidget(self.max_x_label)
        min_max_layout.addWidget(self.max_x_input)


        min_max = QWidget() 
        min_max.setLayout(min_max_layout)


        input_layout.addWidget(self.input_dialog)
        input_layout.addWidget(self.plot_button)
        input = QWidget()
        input.setLayout(input_layout)

        layout.addWidget(input)
        layout.addWidget(min_max)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)

    def func(self): 
        print("hhh") 



class MplCanvas(FigureCanvas):
    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

    def plot(self, function, min=-10, max=10):
        self.axes.clear()
        x_values = [i for i in range(min, max + 1)]
        y_values = [eval(function) for x in x_values]

        self.axes.plot(x_values, y_values, "r")
        self.draw()


class MainWindow(QMainWindow):
    allowed_operands = set(["+", "-", " ", "/", "*", "^"])

    def __init__(self):
        super().__init__()

        self.input_function = FunctionInput()
        self.canvas = MplCanvas(self, width=5, height=4, dpi=100)
        layout = QVBoxLayout()
        layout.addWidget(self.input_function)
        layout.addWidget(self.canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.input_function.plot_button.clicked.connect(self.plot)

    def check_operands(self, user_input):
        for operand in user_input:
            if (
                not operand == "x"
                and not operand.isdigit()
                and operand not in self.allowed_operands
            ):
                raise UnsupportedOperand(f"{operand} is not allowed")

    def parse_input(self, user_input):
        self.check_operands(user_input)
        return "".join([operand if operand != "^" else "**" for operand in user_input])

    def alert(self, message):
        alert = QMessageBox.warning(
            self, "Error", message, buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok
        )

    def plot(self):
        try:
            function = self.parse_input(self.input_function.input_dialog.text())
            self.canvas.plot(function=function)
        except UnsupportedOperand as e:
            self.alert(str(e))
            print(e)
            return
        except Exception as e:
            self.alert("Invalid input")
            print(e)
            return



app = QApplication(sys.argv)

window = MainWindow()
window.show()

app.exec_()
