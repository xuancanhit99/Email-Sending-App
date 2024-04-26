import sys
import re
from PyQt5.QtWidgets import QMainWindow, QApplication, QWidget, QVBoxLayout, QHBoxLayout, QLineEdit, QPushButton, QLabel
from PyQt5.QtCore import Qt


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
        # Get the expression from input
        expression = self.input.text()
        # Sanitize the expression to ensure safety before evaluation
        expression = re.sub(r'[^\d\+\-\*\/\(\) ]', '', expression)
        try:
            # Evaluate the expression
            result = eval(expression)
        except Exception as e:
            result = str(e)
        # Display the result
        self.display.setText(str(result))


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CalculatorApp()
    window.show()
    sys.exit(app.exec_())
