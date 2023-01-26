import sys
from PySide2.QtWidgets import QMainWindow, QApplication
from matplotlib.backends.backend_qt5agg import (
    FigureCanvasQTAgg as FigureCanvas,
    NavigationToolbar2QT as NavigationToolbar,
)


from PySide2.QtWidgets import (
    QApplication,
    QWidget,
    QMainWindow,
    QVBoxLayout,
    QMessageBox,
)

from custom_errors import (
    UnsupportedOperand,
    minMaxError,
    EmptyInput,
    IncorrectVariable,
    DivisionByZero,
)
from function_input import FunctionInput

from helper import parse_input
from canvas import PlotCanvas
from helper import CORRECT_INPUT_PROMPT


class MainWindow(QMainWindow):
    """
    Main window of the application

    ...

    Attributes
    ----------
    input_function : FunctionInput
        input widget for the function
    plot_button : QPushButton
        button to plot the function when pressed
    canvas : PlotCanvas
        matplotlib canvas to plot the function
    tool_bar : NavigationToolbar
        matplotlib toolbar to add zooming and panning functionality
    last_alert : str
        holds the last alert message if any

    Methods
    -------
    alert(message):
        shows a warning message box with the given message
    plot():
        plots the function on the canvas
    """

    def __init__(self):
        super().__init__()
        self.setWindowTitle("Plotter")

        self.input_function = FunctionInput()
        self.input_function.plot_button.clicked.connect(self.plot)

        self.canvas = PlotCanvas(self, width=5, height=4, dpi=100)
        self.tool_bar = NavigationToolbar(self.canvas, self)

        layout = QVBoxLayout()
        layout.addWidget(self.input_function)
        layout.addWidget(self.tool_bar)
        layout.addWidget(self.canvas)
        widget = QWidget()
        widget.setLayout(layout)
        self.setCentralWidget(widget)

        self.last_alert = None

    def alert(self, message):
        self.last_alert = message
        alert = QMessageBox.warning(
            self, "Error", message, buttons=QMessageBox.Ok, defaultButton=QMessageBox.Ok
        )

    def plot(self):
        try:
            function = parse_input(self.input_function.input_dialog.text())
            self.canvas.plot(
                function,
                self.input_function.input_dialog.text(),
                self.input_function.min_x_input.value(),
                self.input_function.max_x_input.value(),
            )

        except minMaxError as e:
            self.alert(str(e))
            return

        except UnsupportedOperand as e:
            self.alert(str(e))
            return

        except SyntaxError:
            self.alert("Invalid mathermatical expression\n" + CORRECT_INPUT_PROMPT)
            return

        except ZeroDivisionError:
            self.alert("Cant divide by Zero")
            return

        except Exception as error:
            self.alert(str(error))
            return


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    app.exec_()
