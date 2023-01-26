import matplotlib
import numpy as np
import matplotlib.pyplot as plt

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure
from config import NUMBER_OF_POINTS, EPSILON
from custom_errors import minMaxError


class PlotCanvas(FigureCanvas):
    """
    Class to represent the FigureCanvas widget

    ...

    Attributes
    ----------
    axes : AxesSubplot
        subplot of the figure
    figure : Figure
        matplotlib figure to plot on

    Methods:
    --------
    plot(parsed_function, function, min, max):
        plots the function on the canvas

    """

    def __init__(self, parent=None, width=5, height=4, dpi=100):
        fig = Figure(figsize=(width, height), dpi=dpi)
        self.axes = fig.add_subplot(111)
        super().__init__(fig)

    def plot(
        self,
        parsed_function,
        function,
        min,
        max,
    ):
        """
        checks if the min and max values are valid and plots the function on the canvas

        Parameters
        ----------
            parsed_function : str
                parsed function to be plotted
            function : str
                function name to be visualized on the canvas
            min : float
                minimum value of the x-axis
            max : float
                maximum value of the x-axis

        """

        if min >= max:
            raise minMaxError("min must be less than max")

        self.axes.clear()
        if min < 0 and max > 0:
            x_values = np.concatenate(
                (
                    np.linspace(min, 0 - EPSILON, NUMBER_OF_POINTS // 2),
                    np.linspace(0 + EPSILON, max, NUMBER_OF_POINTS // 2),
                )
            )
        else:
            x_values = np.linspace(min, max, NUMBER_OF_POINTS)

        y_values = np.array([eval(parsed_function) for x in x_values])
        self.axes.plot(x_values, y_values, "r")
        self.axes.set_title(f"F(x) = {function}")
        self.axes.set_xlabel("x")
        self.axes.set_ylabel("F(x)")
        self.draw()
