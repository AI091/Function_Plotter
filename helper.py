from custom_errors import (
    UnsupportedOperand,
    IncorrectVariable,
    DivisionByZero,
    EmptyInput,
)

CORRECT_INPUT_PROMPT = 'Please enter a valid function of "x". \nsupported operands are  + - / * ^ \nex: x^2 + 2*x + 1'
allowed_operands = {"+", "-", " ", "/", "*", "^", "(", ")"}


def check_operands(user_input):
    """
    Checks if the operands are valid "in the allowed set of operands" and raises an error if not

    Parameters
    ----------
    user_input : str
        user input to be checked

    """
    if user_input == "":
        raise EmptyInput(CORRECT_INPUT_PROMPT)

    user_input = user_input.replace(" ", "")

    for operand in user_input:
        if operand != "x" and not operand.isdigit() and operand not in allowed_operands:
            raise UnsupportedOperand(
                f"Operand {operand} is not allowed\n{CORRECT_INPUT_PROMPT}"
            )


def parse_input(user_input):
    """
    Parses the user input to be evaluated by the function plotter and returns the parsed input

    Parameters
    ----------
    user_input : str
        user input to be parsed

    Returns
    -------
    str
        parsed user input

    """
    user_input = user_input.replace(" ", "")
    check_operands(user_input)
    return "".join([operand if operand != "^" else "**" for operand in user_input])
