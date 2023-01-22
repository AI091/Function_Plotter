from PySide2.QtWidgets import (
    QWidget,
    QVBoxLayout,
    QLabel,
    QLineEdit,
    QPushButton,
    QHBoxLayout,
)

from PySide2.QtCore import Qt
from helper import parse_input


class FunctionInput(QWidget):
    def __init__(self) -> None:
        super().__init__()

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
        self.min_x_input = QLineEdit()

        self.max_x_label = QLabel("Max X")
        self.max_x_input = QLineEdit()

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
