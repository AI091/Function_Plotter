"""
The module defines custom errors to be raised in the function plotter.
"""


class UnsupportedOperand(Exception):
    """Raised when the input contains an unsupported operand"""

    pass


class IncorrectVariable(Exception):
    """Raised when the input contains an unsupported variable"""

    pass


class DivisionByZero(Exception):
    """Raised when the input contains a division by zero"""

    pass


class EmptyInput(Exception):
    """Raised when the input is empty"""

    pass


class minMaxError(Exception):
    """Raised when the input contains a division by zero"""

    pass
