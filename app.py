import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas


from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QMessageBox,
)

from custom_errors import UnsupportedOperand
from function_input import FunctionInput

from helper import parse_input  # Import the function from helper.py
from canvas import PlotCanvas


class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()

        self.input_function = FunctionInput()
        self.canvas = PlotCanvas(self, width=5, height=4, dpi=100)
        layout = QVBoxLayout()
        layout.addWidget(self.input_function)
        layout.addWidget(self.canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)
        self.input_function.plot_button.clicked.connect(self.plot)
        self.last_alert = None

    def alert(self, message):
        self.last_alert = message
        alert = QMessageBox.warning(
            self, "Error", message, buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok
        )

    def plot(self):
        try:
            function = parse_input(self.input_function.input_dialog.text())
            self.canvas.plot(function=function)

        except UnsupportedOperand as e:
            self.alert(str(e))
            return

        except Exception as e:
            print(e) ## This is for debugging purposes remove it in production
            self.alert("Invalid input")
            return


app = QApplication(sys.argv)
window = MainWindow()
window.show()
app.exec_()
