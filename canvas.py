import matplotlib

matplotlib.use("Qt5Agg")
from matplotlib.backends.backend_qt5agg import FigureCanvasQTAgg as FigureCanvas
from matplotlib.figure import Figure


class PlotCanvas(FigureCanvas):
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
