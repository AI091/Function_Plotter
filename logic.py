from custom_errors import UnsupportedOperand
import matplotlib.pyplot as plt
import numpy as np

allowed_operands = set(["+", "-", " ", "/", "*", "^"])
functions_converter = {"sin": "np.sin", "cos": "np.cos", "tan": "np.tan" , "log": "np.log" }
# allowed_function = "TODO"
    

class FunctionPlotter:
    def prompt_input(self):
        user_input = input("enter your function:\n")
        self.check_operands(user_input)
        parsed_input = self.parse_input(user_input)
        return parsed_input

    def check_operands(self, user_input):
        for operand in user_input:
            if (
                not operand == "x"
                and not operand.isdigit()
                and operand not in allowed_operands
            ):
                raise UnsupportedOperand(f"{operand} is not allowed")


    def plot_function(self, min, max, func):
        x_values = np.linspace(min, max, num=200)
        y_values = np.array([])

        for x in x_values:
            y_values = np.append(y_values, eval(func))

        fig, ax = plt.subplots()
        ax.plot(x_values, y_values)
        plt.show()

    def parse_input(self, user_input):
        return "".join([operand if operand != "^" else "**" for operand in user_input])


x = 1
fc = FunctionPlotter()
func = fc.prompt_input()
print(func)
fc.plot_function(-10.0, 10.0, func)
