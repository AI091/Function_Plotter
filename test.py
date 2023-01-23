from app import MainWindow
import PySide2.QtCore
from helper import CORRECT_INPUT_PROMPT
from time import sleep
import pytest


@pytest.fixture
def plotter(qtbot):
    return MainWindow()


def test_working_function(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "x^2")
    plotter.input_function.min_x_input.setValue(-10)
    plotter.input_function.max_x_input.setValue(10)
    qtbot.mouseClick(plotter.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)
    assert (
        plotter.last_alert is None
        and plotter.canvas.axes.title.get_text() == "F(x) = x^2"
    )


def test_no_input(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "")
    plotter.input_function.min_x_input.setValue(-10)
    plotter.input_function.max_x_input.setValue(10)
    qtbot.mouseClick(plotter.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)
    assert plotter.last_alert == CORRECT_INPUT_PROMPT


def test_wrong_input(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "y^2 + 2*x + 1")
    plotter.input_function.min_x_input.setValue(-10)
    plotter.input_function.max_x_input.setValue(10)
    qtbot.mouseClick(plotter.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)
    assert plotter.last_alert == f"Operand y is not allowed\n{CORRECT_INPUT_PROMPT}"


def test_wrong_matematical_expression(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "x + ")
    plotter.input_function.min_x_input.setValue(-10)
    plotter.input_function.max_x_input.setValue(10)
    qtbot.mouseClick(plotter.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)
    assert (
        plotter.last_alert
        == f"Invalid mathermatical expression\n{CORRECT_INPUT_PROMPT}"
    )


def test_wrong_min_max_range(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "x^2")
    plotter.input_function.min_x_input.setValue(10)
    plotter.input_function.max_x_input.setValue(-10)
    qtbot.mouseClick(plotter.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)
    assert plotter.last_alert == "min must be less than max"


def test_text_input_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "x+5")
    assert plotter.input_function.input_dialog.text() == "x+5"


def test_min_input_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    plotter.input_function.min_x_input.setValue(-10)
    assert plotter.input_function.min_x_input.value() == -10

def test_min_step_up_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    plotter.input_function.min_x_input.setValue(0)
    plotter.input_function.min_x_input.stepBy(1)
    assert plotter.input_function.min_x_input.value() == 0.1 

def test_min_step_down_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    plotter.input_function.min_x_input.setValue(0)
    plotter.input_function.min_x_input.stepBy(-1)
    assert plotter.input_function.min_x_input.value() == -0.1


def test_max_input_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    plotter.input_function.max_x_input.setValue(10)
    assert plotter.input_function.max_x_input.value() == 10

def test_max_step_up_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    plotter.input_function.max_x_input.setValue(0)
    plotter.input_function.max_x_input.stepBy(1)
    assert plotter.input_function.max_x_input.value() == 0.1

def test_max_step_down_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    plotter.input_function.max_x_input.setValue(0)
    plotter.input_function.max_x_input.stepBy(-1)
    assert plotter.input_function.max_x_input.value() == -0.1

def test_plot_button_working(qtbot, plotter):
    qtbot.addWidget(plotter)
    qtbot.keyClicks(plotter.input_function.input_dialog, "x^2")
    plotter.input_function.min_x_input.setValue(-10)
    plotter.input_function.max_x_input.setValue(10)
    qtbot.mouseClick(plotter.input_function.plot_button, PySide2.QtCore.Qt.LeftButton)
    assert plotter.input_function.plot_button.isEnabled() == True


def test_window_title(qtbot, plotter):
    qtbot.addWidget(plotter)
    assert plotter.windowTitle() == "Plotter"

