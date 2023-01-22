from custom_errors import UnsupportedOperand

allowed_operands = set(["+", "-", " ", "/", "*", "^"])


def check_operands(user_input):
    for operand in user_input:
        if (
            not operand == "x"
            and not operand.isdigit()
            and operand not in allowed_operands
        ):
            raise UnsupportedOperand(f"{operand} is not allowed")


def parse_input(user_input):
    check_operands(user_input)
    return "".join([operand if operand != "^" else "**" for operand in user_input])
