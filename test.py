from app import MainWindow
import PySide2.QtCore


def test_hello(qtbot):
    widget = MainWindow()
    qtbot.addWidget(widget)

    # click in the Greet button and make sure it updates the appropriate label
    qtbot.mouseClick(widget.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)

    assert widget.last_alert == "Invalid input"
