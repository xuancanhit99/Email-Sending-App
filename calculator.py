import sys
import re
import ast
import operator as op
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt

# Supported operators for mathematical expressions
operators = {ast.Add: op.add, ast.Sub: op.sub, ast.Mult: op.mul, ast.Div: op.truediv, ast.USub: op.neg}


def evaluate_expression(node):
    # Evaluate the expression based on the type of the node
    if isinstance(node, ast.Constant):  # If the node is a number, return the number
        return node.value
    elif isinstance(node, ast.BinOp):  # If the node is a binary operation, perform the operation
        return operators[type(node.op)](evaluate_expression(node.left), evaluate_expression(node.right))
    elif isinstance(node, ast.UnaryOp):  # If the node is a unary operation, perform the operation
        return operators[type(node.op)](evaluate_expression(node.operand))
    else:
        raise TypeError(node)


class CalculatorApp(QMainWindow):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Smart Calculator")
        self.resize(400, 300)

        self.main_widget = QWidget(self)
        self.setCentralWidget(self.main_widget)

        self.layout = QVBoxLayout(self.main_widget)

        self.input = QLineEdit()  # Input field for entering the expression
        self.input.setAlignment(Qt.AlignRight)
        self.layout.addWidget(self.input)

        # Create a horizontal layout for the result title and display
        self.result_layout = QHBoxLayout()

        self.result_title = QLabel("Result:")  # Label for the result
        self.result_layout.addWidget(self.result_title)

        self.display = QLineEdit()  # Display field for showing the result
        self.display.setReadOnly(True)
        self.display.setAlignment(Qt.AlignRight)
        self.result_layout.addWidget(self.display)

        # Add the horizontal layout to the main layout
        self.layout.addLayout(self.result_layout)

        self.button = QPushButton("Calculate")  # Button for performing the calculation
        self.button.clicked.connect(self.calculate)
        self.layout.addWidget(self.button)

    def calculate(self):
        # Calculate the result of the expression entered in the input field
        expression = self.input.text()
        # Sanitize the expression to ensure safety before evaluation
        expression = re.sub(r'[^\d\+\-\*\/\(\) ]', '', expression)
        try:
            tree = ast.parse(expression, mode='eval')
            result = evaluate_expression(tree.body)
            self.display.setText(str(result))
        except Exception as e:
            self.display.setText("Error: " + str(e))  # Display the error message if there is an error


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
