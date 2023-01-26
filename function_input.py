from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
    QDoubleSpinBox,
)

from PySide2.QtCore import Qt


class FunctionInput(QWidget):
    """
    A widget to get function input from the user 

    ...

    Attributes
    ----------
    label : QLabel
        label to show the user what to do
    input_dialog : QLineEdit
        input dialog to get the function from the user
    plot_button : QPushButton
        button to plot the function when pressed
    min_x_label : QLabel
        label to show the user what to do
    min_x_input : QDoubleSpinBox
        input dialog to get the minimum value of the x-axis from the user
    max_x_label : QLabel
        label to show the user what to do
    max_x_input : QDoubleSpinBox
        input dialog to get the maximum value of the x-axis from the user
    
    """
    def __init__(self) -> None:
        """
        Constructs all the necessary attributes for the FunctionInput object .
        """
        super().__init__()

        self.min_x = 1
        self.max_x = 10
        layout = QVBoxLayout()

        self.label = QLabel("Enter your function:")
        self.label.setAlignment(Qt.AlignCenter)

        layout.addWidget(self.label)

        input_layout = QHBoxLayout()
        self.input_dialog = QLineEdit()
        self.input_dialog.setStyleSheet(
            ":focus{border: 2px solid #333; }*{padding: 5px;}"
        )
        self.plot_button = QPushButton("Plot")
        self.plot_button.setStyleSheet(
            ":hover{background-color: #030303; color: #fff;}*{height:21px;background-color: #333; color: #fff;}"
        )

        self.min_x_label = QLabel("Min X")
        self.min_x_input = QDoubleSpinBox()
        self.min_x_input.setValue(1)
        self.min_x_input.setSingleStep(0.1)
        self.min_x_input.setMinimum(-1e10)
        self.min_x_input.setMaximum(1e10)

        self.max_x_label = QLabel("Max X")
        self.max_x_input = QDoubleSpinBox()
        self.max_x_input.setValue(10)
        self.max_x_input.setSingleStep(0.1)
        self.max_x_input.setMinimum(-1e10)
        self.max_x_input.setMaximum(1e10)

        min_max_layout = QHBoxLayout()
        min_max = QWidget()

        min_input = QWidget()
        min_input_layout = QHBoxLayout()
        min_input_layout.addWidget(self.min_x_label)
        min_input_layout.addWidget(self.min_x_input)
        min_input_layout.setAlignment(Qt.AlignLeft)
        min_input_layout.setSpacing(20)
        min_input.setLayout(min_input_layout)

        max_input = QWidget()
        max_input_layout = QHBoxLayout()
        max_input_layout.addWidget(self.max_x_label)
        max_input_layout.addWidget(self.max_x_input)
        max_input_layout.setAlignment(Qt.AlignRight)
        max_input_layout.setSpacing(20)
        max_input.setLayout(max_input_layout)

        min_max_layout.addWidget(min_input)
        min_max_layout.addWidget(max_input)

        min_max.setLayout(min_max_layout)

        input_layout.addWidget(self.input_dialog)
        input_layout.addWidget(self.plot_button)
        input_widget = QWidget()
        input_widget.setLayout(input_layout)

        layout.addWidget(input_widget)
        layout.addWidget(min_max)
        layout.setAlignment(Qt.AlignCenter)

        self.setLayout(layout)
